"""Tests for the minimal QR code encoder."""

import unittest

from redtext_generator.qrencode import encode, render_ascii, _select_version, _CAPACITY, _SIZE


class TestSelectVersion(unittest.TestCase):
    def test_short_data_version_1(self):
        self.assertEqual(_select_version(10), 1)

    def test_medium_data_version_3(self):
        self.assertEqual(_select_version(40), 3)

    def test_max_capacity_version_6(self):
        self.assertEqual(_select_version(134), 6)

    def test_too_long_raises(self):
        with self.assertRaises(ValueError):
            _select_version(135)

    def test_boundary_values(self):
        for v, cap in _CAPACITY.items():
            self.assertEqual(_select_version(cap), v)


class TestEncode(unittest.TestCase):
    def test_returns_square_matrix(self):
        matrix = encode("test")
        self.assertEqual(len(matrix), len(matrix[0]))

    def test_matrix_contains_bools(self):
        matrix = encode("hello")
        for row in matrix:
            for cell in row:
                self.assertIsInstance(cell, bool)

    def test_known_dimensions_version_1(self):
        # "test" = 4 bytes -> version 1 (21x21) + 8 quiet zone = 29x29
        matrix = encode("test")
        self.assertEqual(len(matrix), _SIZE[1] + 8)

    def test_known_dimensions_version_2(self):
        # 20 bytes -> version 2 (25x25) + 8 quiet zone = 33x33
        matrix = encode("https://example.com/")
        self.assertEqual(len(matrix), _SIZE[2] + 8)

    def test_quiet_zone_top_row_white(self):
        matrix = encode("test")
        # Top 4 rows should be all white (quiet zone)
        for r in range(4):
            for c in range(len(matrix[0])):
                self.assertFalse(matrix[r][c], f"Quiet zone violated at ({r}, {c})")

    def test_quiet_zone_left_col_white(self):
        matrix = encode("test")
        for r in range(len(matrix)):
            for c in range(4):
                self.assertFalse(matrix[r][c], f"Quiet zone violated at ({r}, {c})")

    def test_finder_pattern_top_left(self):
        matrix = encode("test")
        # Top-left finder pattern starts at (4,4) after quiet zone
        # Top-left corner of finder should be dark
        self.assertTrue(matrix[4][4])
        # Inner white area
        self.assertFalse(matrix[5][5])
        # Center dark square
        self.assertTrue(matrix[6][6])

    def test_different_data_different_matrices(self):
        m1 = encode("hello")
        m2 = encode("world")
        self.assertNotEqual(m1, m2)

    def test_url_encoding(self):
        # Should not raise for typical phishing URLs
        matrix = encode("https://secure-portal.co/12345678")
        self.assertIsInstance(matrix, list)
        self.assertTrue(len(matrix) > 0)

    def test_max_length_data(self):
        # 134 bytes = max for version 6
        data = "x" * 134
        matrix = encode(data)
        self.assertEqual(len(matrix), _SIZE[6] + 8)


class TestRenderAscii(unittest.TestCase):
    def test_non_empty_output(self):
        matrix = encode("test")
        rendered = render_ascii(matrix)
        self.assertIsInstance(rendered, str)
        self.assertTrue(len(rendered) > 0)

    def test_contains_block_characters(self):
        matrix = encode("hello world")
        rendered = render_ascii(matrix)
        # Should contain at least some block characters
        block_chars = {"\u2588", "\u2580", "\u2584"}
        found = any(c in rendered for c in block_chars)
        self.assertTrue(found, "Rendered output should contain Unicode block characters")

    def test_compact_rows(self):
        matrix = encode("test")
        rendered = render_ascii(matrix)
        lines = rendered.split("\n")
        # Each text line represents 2 matrix rows, so line count ~= rows/2
        expected = (len(matrix) + 1) // 2
        self.assertEqual(len(lines), expected)

    def test_consistent_width(self):
        matrix = encode("test")
        rendered = render_ascii(matrix)
        lines = rendered.split("\n")
        widths = [len(line) for line in lines]
        self.assertEqual(len(set(widths)), 1, "All lines should have the same width")


if __name__ == "__main__":
    unittest.main()
