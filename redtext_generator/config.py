"""
Configuration management for REDTEXT GoPhish integration.

Handles loading and saving GoPhish connection settings with three-layer
precedence: CLI args > environment variables > config file.
"""

import configparser
import os
from pathlib import Path


def get_config_path():
    """Return the path to the config file: ~/.config/redtext/config.ini"""
    return str(Path.home() / ".config" / "redtext" / "config.ini")


def save_gophish_config(api_url, api_key, verify_ssl=True):
    """Write GoPhish connection settings to the config file.

    Creates parent directories if they don't exist.

    Returns:
        str: The path to the written config file.
    """
    path = get_config_path()
    config_dir = os.path.dirname(path)
    os.makedirs(config_dir, exist_ok=True)

    # Restrict directory permissions (owner-only on Unix)
    try:
        os.chmod(config_dir, 0o700)
    except OSError:
        pass  # Windows doesn't support Unix permissions

    config = configparser.ConfigParser()
    config["gophish"] = {
        "api_url": api_url,
        "api_key": api_key,
        "verify_ssl": str(verify_ssl).lower(),
    }

    with open(path, "w", encoding="utf-8") as f:
        config.write(f)

    # Restrict file permissions — API key should not be world-readable
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass  # Windows doesn't support Unix permissions

    return path


def load_gophish_config(args=None):
    """Load GoPhish config with precedence: CLI args > env vars > config file.

    Args:
        args: argparse.Namespace with optional gophish_url, gophish_key,
              no_verify_ssl attributes.

    Returns:
        dict with keys: api_url, api_key, verify_ssl

    Raises:
        ValueError: If api_url or api_key cannot be resolved from any source.
    """
    result = {"api_url": None, "api_key": None, "verify_ssl": True}

    # Layer 1: Config file
    path = get_config_path()
    if os.path.isfile(path):
        config = configparser.ConfigParser()
        config.read(path, encoding="utf-8")
        if config.has_section("gophish"):
            result["api_url"] = config.get("gophish", "api_url", fallback=None)
            result["api_key"] = config.get("gophish", "api_key", fallback=None)
            result["verify_ssl"] = config.getboolean(
                "gophish", "verify_ssl", fallback=True
            )

    # Layer 2: Environment variables
    env_url = os.environ.get("REDTEXT_GOPHISH_URL")
    if env_url:
        result["api_url"] = env_url

    env_key = os.environ.get("REDTEXT_GOPHISH_KEY")
    if env_key:
        result["api_key"] = env_key

    env_ssl = os.environ.get("REDTEXT_GOPHISH_VERIFY_SSL")
    if env_ssl is not None:
        result["verify_ssl"] = env_ssl.lower() not in ("0", "false", "no")

    # Layer 3: CLI args
    if args is not None:
        cli_url = getattr(args, "gophish_url", None)
        if cli_url:
            result["api_url"] = cli_url

        cli_key = getattr(args, "gophish_key", None)
        if cli_key:
            result["api_key"] = cli_key

        if getattr(args, "no_verify_ssl", False):
            result["verify_ssl"] = False

    # Validate required fields
    missing = []
    if not result["api_url"]:
        missing.append("api_url")
    if not result["api_key"]:
        missing.append("api_key")

    if missing:
        raise ValueError(
            f"Missing GoPhish config: {', '.join(missing)}. "
            "Set via 'redtext-gen gophish setup', environment variables "
            "(REDTEXT_GOPHISH_URL, REDTEXT_GOPHISH_KEY), or CLI flags "
            "(--gophish-url, --gophish-key)."
        )

    return result
