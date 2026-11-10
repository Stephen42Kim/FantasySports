
# ==========================================
# NFL DATA WAREHOUSE - SHARED NOTEBOOK SETUP
# ==========================================

import os
import sys
import warnings
from pathlib import Path
from datetime import datetime

# Core data libraries
import numpy as np
import pandas as pd
import polars as pl

# Database
import duckdb

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Utilities
from tqdm.auto import tqdm

# ==========================================
# PROJECT PATHS
# ==========================================

PROJECT_ROOT = Path(
    r"C:\Desktop\Sports\FantasySports\NFL\NFL_Data_Warehouse"
)

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"
EXPORT_DIR = DATA_DIR / "exports"

DATABASE_DIR = PROJECT_ROOT / "database"
REPORTS_DIR = PROJECT_ROOT / "reports"

# Create directories if missing
for folder in [
    RAW_DIR,
    BRONZE_DIR,
    SILVER_DIR,
    GOLD_DIR,
    EXPORT_DIR,
    DATABASE_DIR,
    REPORTS_DIR
]:
    folder.mkdir(parents=True, exist_ok=True)

# ==========================================
# DATABASE
# ==========================================

DB_PATH = DATABASE_DIR / "nfl_warehouse.duckdb"

# ==========================================
# DISPLAY SETTINGS
# ==========================================

pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 100)
pd.set_option("display.width", 180)

warnings.filterwarnings("ignore", category=FutureWarning)

# ==========================================
# PROJECT STATUS
# ==========================================

print("NFL DATA WAREHOUSE SETUP COMPLETE")
print("----------------------------------")
print("Python:", sys.executable)
print("Project:", PROJECT_ROOT)
print("Database:", DB_PATH)
print("Pandas:", pd.__version__)
print("Polars:", pl.__version__)
print("DuckDB:", duckdb.__version__)
