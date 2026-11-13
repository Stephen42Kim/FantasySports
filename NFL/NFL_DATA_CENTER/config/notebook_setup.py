
from pathlib import Path
import sys
import logging
import os

import pandas as pd
import numpy as np
import polars as pl
import duckdb

# Project root is the folder above config/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Main project directories
CONFIG_DIR = PROJECT_ROOT / "config"
SRC_DIR = PROJECT_ROOT / "src"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"
EXPORTS_DIR = DATA_DIR / "exports"
LOGS_DIR = DATA_DIR / "logs"

DATABASE_DIR = PROJECT_ROOT / "database"
REPORTS_DIR = PROJECT_ROOT / "reports"

DB_PATH = DATABASE_DIR / "nfl_warehouse.duckdb"

# Ensure folders exist
for directory in [
    RAW_DIR,
    BRONZE_DIR,
    SILVER_DIR,
    GOLD_DIR,
    EXPORTS_DIR,
    LOGS_DIR,
    DATABASE_DIR,
    REPORTS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

# Make project imports available
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Pandas display configuration
pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 100)
pd.set_option("display.width", 180)

# Logging
LOG_PATH = LOGS_DIR / "project.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("nfl_project")

print("NFL project configuration loaded.")
print(f"Project root: {PROJECT_ROOT}")
print(f"Database: {DB_PATH}")
print(f"Python: {sys.executable}")
