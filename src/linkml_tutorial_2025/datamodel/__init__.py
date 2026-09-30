"""Data model package for linkml-tutorial-2025."""

from pathlib import Path
from .linkml_tutorial_2025 import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "linkml_tutorial_2025.yaml"
