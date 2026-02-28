"""
QR code encoder.
Supports byte mode, ECC level L, versions 1-6 (up to ~134 bytes).
Produces scannable QR codes rendered as Unicode terminal art.

Reference: ISO/IEC 18004 (QR Code specification)
"""

# ═══════════════════════════════════════════════════════════════
#  CONSTANTS & TABLES
# ═══════════════════════════════════════════════════════════════

# Version info: (total codewords, ec codewords per block, num blocks) for ECC level L
_VERSION_TABLE = {
    1: (26, 7, 1),
    2: (44, 10, 1),
    3: (70, 15, 1),
    4: (100, 20, 1),
    5: (134, 26, 1),
    6: (172, 18, 2),
}

# Data capacity in bytes for each version at ECC level L
_CAPACITY = {
    1: 17,
    2: 32,
    3: 53,
    4: 78,
    5: 106,
    6: 134,
}

# Size of each version: 4*version + 17
_SIZE = {v: 4 * v + 17 for v in range(1, 7)}

# Alignment pattern positions (center coordinates) per version
_ALIGNMENT = {
    1: [],
    2: [6, 18],
    3: [6, 22],
    4: [6, 26],
    5: [6, 30],
    6: [6, 34],
}

# Format info bits for ECC level L (00) with each mask pattern (pre-computed with BCH)
_FORMAT_BITS = {
    0: 0x77C4,
    1: 0x72F3,
    2: 0x7DAA,
    3: 0x789D,
    4: 0x662F,
    5: 0x6318,
    6: 0x6C41,
    7: 0x6976,
}


# ═══════════════════════════════════════════════════════════════
#  GALOIS FIELD GF(256) ARITHMETIC
# ═══════════════════════════════════════════════════════════════

_GF_EXP = [0] * 512
_GF_LOG = [0] * 256

def _init_gf():
    """Initialize GF(256) log/exp tables with primitive polynomial 0x11D."""
    x = 1
    for i in range(255):
        _GF_EXP[i] = x
        _GF_LOG[x] = i
        x <<= 1
        if x >= 256:
            x ^= 0x11D
    for i in range(255, 512):
        _GF_EXP[i] = _GF_EXP[i - 255]

_init_gf()


def _gf_mul(a, b):
    if a == 0 or b == 0:
        return 0
    return _GF_EXP[_GF_LOG[a] + _GF_LOG[b]]


def _gf_poly_mul(p, q):
    """Multiply two polynomials in GF(256)."""
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] ^= _gf_mul(a, b)
    return r


def _gf_poly_div(dividend, divisor):
    """Divide polynomials in GF(256), return remainder."""
    result = list(dividend)
    for i in range(len(dividend) - len(divisor) + 1):
        coef = result[i]
        if coef != 0:
            for j in range(1, len(divisor)):
                if divisor[j] != 0:
                    result[i + j] ^= _gf_mul(divisor[j], coef)
    return result[-(len(divisor) - 1):]


def _rs_generator(n):
    """Build Reed-Solomon generator polynomial for n EC codewords."""
    g = [1]
    for i in range(n):
        g = _gf_poly_mul(g, [1, _GF_EXP[i]])
    return g


def _rs_encode(data, n_ec):
    """Compute n_ec Reed-Solomon error correction codewords for data."""
    gen = _rs_generator(n_ec)
    padded = data + [0] * n_ec
    remainder = _gf_poly_div(padded, gen)
    return remainder


# ═══════════════════════════════════════════════════════════════
#  DATA ENCODING (BYTE MODE)
# ═══════════════════════════════════════════════════════════════

def _encode_data(data_bytes, version):
    """Encode data in byte mode and pad to fill version capacity."""
    total_cw, ec_per_block, num_blocks = _VERSION_TABLE[version]
    data_cw = total_cw - ec_per_block * num_blocks

    bits = []
    # Mode indicator: 0100 (byte mode)
    bits.extend([0, 1, 0, 0])
    # Character count (8 bits for versions 1-9)
    count = len(data_bytes)
    for i in range(7, -1, -1):
        bits.append((count >> i) & 1)
    # Data
    for byte in data_bytes:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    # Terminator (up to 4 zeros)
    bits.extend([0] * min(4, data_cw * 8 - len(bits)))
    # Pad to byte boundary
    while len(bits) % 8 != 0:
        bits.append(0)
    # Convert to bytes
    codewords = []
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | bits[i + j]
        codewords.append(byte)
    # Pad with alternating 0xEC, 0x11
    pad = [0xEC, 0x11]
    pi = 0
    while len(codewords) < data_cw:
        codewords.append(pad[pi % 2])
        pi += 1

    return codewords[:data_cw]


def _make_blocks(data_cw, version):
    """Split data into blocks and compute EC codewords for each."""
    total_cw, ec_per_block, num_blocks = _VERSION_TABLE[version]
    data_per_block = len(data_cw) // num_blocks

    data_blocks = []
    ec_blocks = []
    offset = 0
    for _ in range(num_blocks):
        block = data_cw[offset:offset + data_per_block]
        data_blocks.append(block)
        ec_blocks.append(_rs_encode(block, ec_per_block))
        offset += data_per_block

    # Interleave data codewords
    result = []
    max_len = max(len(b) for b in data_blocks)
    for i in range(max_len):
        for block in data_blocks:
            if i < len(block):
                result.append(block[i])
    # Interleave EC codewords
    max_ec = max(len(b) for b in ec_blocks)
    for i in range(max_ec):
        for block in ec_blocks:
            if i < len(block):
                result.append(block[i])

    return result


# ═══════════════════════════════════════════════════════════════
#  MATRIX CONSTRUCTION
# ═══════════════════════════════════════════════════════════════

def _init_matrix(version):
    """Create empty QR matrix. None = unset, True = dark, False = light."""
    size = _SIZE[version]
    return [[None] * size for _ in range(size)]


def _place_finder(matrix, row, col):
    """Place a 7x7 finder pattern centered at (row+3, col+3)."""
    for r in range(7):
        for c in range(7):
            if (r in (0, 6) or c in (0, 6) or
                    (2 <= r <= 4 and 2 <= c <= 4)):
                matrix[row + r][col + c] = True
            else:
                matrix[row + r][col + c] = False


def _place_separators(matrix, size):
    """Place separator (white) lines around finder patterns."""
    for i in range(8):
        # Top-left
        if i < size:
            matrix[7][i] = False
            matrix[i][7] = False
        # Top-right
        if i < size:
            matrix[7][size - 8 + i] = False
            matrix[i][size - 8] = False
        # Bottom-left
        if i < size:
            matrix[size - 8][i] = False
            matrix[size - 8 + i][7] = False


def _place_alignment(matrix, version):
    """Place alignment patterns for the version."""
    positions = _ALIGNMENT[version]
    if len(positions) < 2:
        return
    centers = []
    for r in positions:
        for c in positions:
            centers.append((r, c))
    # Remove positions that overlap with finder patterns
    size = _SIZE[version]
    finders = {(3, 3), (3, size - 4), (size - 4, 3)}
    for cr, cc in centers:
        skip = False
        for fr, fc in finders:
            if abs(cr - fr) <= 5 and abs(cc - fc) <= 5:
                skip = True
                break
        if skip:
            continue
        for r in range(-2, 3):
            for c in range(-2, 3):
                if abs(r) == 2 or abs(c) == 2 or (r == 0 and c == 0):
                    matrix[cr + r][cc + c] = True
                else:
                    matrix[cr + r][cc + c] = False


def _place_timing(matrix, size):
    """Place timing patterns (alternating dark/light)."""
    for i in range(8, size - 8):
        val = (i % 2 == 0)
        if matrix[6][i] is None:
            matrix[6][i] = val
        if matrix[i][6] is None:
            matrix[i][6] = val


def _reserve_format(matrix, size):
    """Reserve format info areas (set to False temporarily)."""
    # Around top-left finder
    for i in range(9):
        if matrix[8][i] is None:
            matrix[8][i] = False
        if matrix[i][8] is None:
            matrix[i][8] = False
    # Around top-right finder
    for i in range(8):
        if matrix[8][size - 1 - i] is None:
            matrix[8][size - 1 - i] = False
    # Around bottom-left finder
    for i in range(7):
        if matrix[size - 1 - i][8] is None:
            matrix[size - 1 - i][8] = False
    # Dark module
    matrix[size - 8][8] = True


def _place_data(matrix, codewords, size):
    """Place data bits in the matrix using the upward/downward zigzag pattern."""
    bits = []
    for cw in codewords:
        for i in range(7, -1, -1):
            bits.append((cw >> i) & 1)

    bit_idx = 0
    # Columns go right to left in pairs, skipping column 6 (timing)
    col = size - 1
    going_up = True

    while col >= 0:
        if col == 6:
            col -= 1
            continue

        rows = range(size - 1, -1, -1) if going_up else range(size)
        for row in rows:
            for dc in (0, -1):
                c = col + dc
                if c < 0 or c >= size:
                    continue
                if matrix[row][c] is None:
                    if bit_idx < len(bits):
                        matrix[row][c] = bool(bits[bit_idx])
                        bit_idx += 1
                    else:
                        matrix[row][c] = False

        going_up = not going_up
        col -= 2


# ═══════════════════════════════════════════════════════════════
#  MASKING
# ═══════════════════════════════════════════════════════════════

def _mask_fn(pattern, row, col):
    """Return True if module should be flipped for given mask pattern."""
    if pattern == 0: return (row + col) % 2 == 0
    if pattern == 1: return row % 2 == 0
    if pattern == 2: return col % 3 == 0
    if pattern == 3: return (row + col) % 3 == 0
    if pattern == 4: return (row // 2 + col // 3) % 2 == 0
    if pattern == 5: return (row * col) % 2 + (row * col) % 3 == 0
    if pattern == 6: return ((row * col) % 2 + (row * col) % 3) % 2 == 0
    if pattern == 7: return ((row + col) % 2 + (row * col) % 3) % 2 == 0
    return False


def _is_data_module(matrix_template, row, col):
    """Check if a position is a data module (was None in the template)."""
    return matrix_template[row][col] is None


def _apply_mask(matrix, matrix_template, pattern, size):
    """Apply mask pattern to data modules only."""
    for r in range(size):
        for c in range(size):
            if _is_data_module(matrix_template, r, c):
                if _mask_fn(pattern, r, c):
                    matrix[r][c] = not matrix[r][c]


def _penalty_score(matrix, size):
    """Calculate mask penalty score (simplified — rules 1 and 2)."""
    score = 0
    # Rule 1: runs of same color (rows and cols)
    for r in range(size):
        run = 1
        for c in range(1, size):
            if matrix[r][c] == matrix[r][c - 1]:
                run += 1
            else:
                if run >= 5:
                    score += run - 2
                run = 1
        if run >= 5:
            score += run - 2
    for c in range(size):
        run = 1
        for r in range(1, size):
            if matrix[r][c] == matrix[r - 1][c]:
                run += 1
            else:
                if run >= 5:
                    score += run - 2
                run = 1
        if run >= 5:
            score += run - 2
    # Rule 2: 2x2 blocks of same color
    for r in range(size - 1):
        for c in range(size - 1):
            v = matrix[r][c]
            if v == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
                score += 3
    return score


def _write_format_info(matrix, pattern, size):
    """Write format info bits for ECC level L and given mask pattern."""
    bits = _FORMAT_BITS[pattern]
    # Positions around top-left finder
    positions_a = [
        (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5),
        (8, 7), (8, 8), (7, 8), (5, 8), (4, 8), (3, 8),
        (2, 8), (1, 8), (0, 8),
    ]
    # Positions: bottom-left then top-right
    positions_b = [
        (size - 1, 8), (size - 2, 8), (size - 3, 8), (size - 4, 8),
        (size - 5, 8), (size - 6, 8), (size - 7, 8),
        (8, size - 8), (8, size - 7), (8, size - 6), (8, size - 5),
        (8, size - 4), (8, size - 3), (8, size - 2), (8, size - 1),
    ]
    for i, (r, c) in enumerate(positions_a):
        matrix[r][c] = bool((bits >> (14 - i)) & 1)
    for i, (r, c) in enumerate(positions_b):
        matrix[r][c] = bool((bits >> (14 - i)) & 1)


# ═══════════════════════════════════════════════════════════════
#  PUBLIC API
# ═══════════════════════════════════════════════════════════════

def _select_version(data_len):
    """Pick the smallest version that fits the data."""
    for v in range(1, 7):
        if data_len <= _CAPACITY[v]:
            return v
    raise ValueError(f"Data too long ({data_len} bytes). Maximum is {_CAPACITY[6]} bytes for version 6.")


def encode(data):
    """
    Encode a string as a QR code.

    Args:
        data: The string to encode (typically a URL).

    Returns:
        A 2D list of bools (True = dark module, False = light module),
        including a 4-module quiet zone border.
    """
    data_bytes = data.encode("utf-8")
    version = _select_version(len(data_bytes))
    size = _SIZE[version]

    # Encode data into codewords with EC
    data_cw = _encode_data(data_bytes, version)
    all_cw = _make_blocks(data_cw, version)

    # Build template (to track which modules are data vs function)
    template = _init_matrix(version)
    _place_finder(template, 0, 0)
    _place_finder(template, 0, size - 7)
    _place_finder(template, size - 7, 0)
    _place_separators(template, size)
    _place_alignment(template, version)
    _place_timing(template, size)
    _reserve_format(template, size)

    # Try all 8 mask patterns, pick the one with lowest penalty
    best_matrix = None
    best_score = float("inf")
    best_mask = 0

    for pattern in range(8):
        # Build fresh matrix
        m = _init_matrix(version)
        _place_finder(m, 0, 0)
        _place_finder(m, 0, size - 7)
        _place_finder(m, size - 7, 0)
        _place_separators(m, size)
        _place_alignment(m, version)
        _place_timing(m, size)
        _reserve_format(m, size)
        _place_data(m, all_cw, size)
        _apply_mask(m, template, pattern, size)
        _write_format_info(m, pattern, size)

        score = _penalty_score(m, size)
        if score < best_score:
            best_score = score
            best_matrix = m
            best_mask = pattern

    # Add quiet zone (4 modules of white on all sides)
    qz = 4
    final_size = size + 2 * qz
    final = [[False] * final_size for _ in range(final_size)]
    for r in range(size):
        for c in range(size):
            final[r + qz][c + qz] = best_matrix[r][c]

    return final


def render_ascii(matrix):
    """
    Render a QR matrix as a compact Unicode string.

    Uses half-block characters so each text row represents 2 QR module rows:
    - '█' (full block)  = top dark, bottom dark
    - '▀' (upper half)  = top dark, bottom light
    - '▄' (lower half)  = top light, bottom dark
    - ' ' (space)       = top light, bottom light
    """
    rows = len(matrix)
    lines = []
    for r in range(0, rows, 2):
        line = []
        for c in range(len(matrix[0])):
            top = matrix[r][c]
            bot = matrix[r + 1][c] if r + 1 < rows else False
            if top and bot:
                line.append("\u2588")      # █
            elif top and not bot:
                line.append("\u2580")      # ▀
            elif not top and bot:
                line.append("\u2584")      # ▄
            else:
                line.append(" ")
        lines.append("".join(line))
    return "\n".join(lines)
