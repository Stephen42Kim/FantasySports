
from pathlib import Path
import pandas as pd
import polars as pl
import duckdb


def inspect_dataset(data, name="Dataset"):
    """Display basic information about a Pandas or Polars dataset."""

    print(f"\n{name}")
    print("=" * 60)

    if isinstance(data, pd.DataFrame):
        print("Type: Pandas DataFrame")
        print("Shape:", data.shape)
        display(data.head())
        display(data.dtypes.to_frame("dtype"))

    elif isinstance(data, pl.DataFrame):
        print("Type: Polars DataFrame")
        print("Shape:", data.shape)
        display(data.head())
        print(data.schema)

    else:
        raise TypeError("Expected a Pandas or Polars DataFrame.")


def save_parquet(data, path):
    """Save Pandas or Polars data to a Parquet file."""

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if isinstance(data, pd.DataFrame):
        data.to_parquet(path, index=False)

    elif isinstance(data, pl.DataFrame):
        data.write_parquet(path)

    else:
        raise TypeError("Expected a Pandas or Polars DataFrame.")

    print(f"Saved: {path}")


def get_duckdb_connection(db_path):
    """Create a DuckDB connection."""

    db_path = str(db_path)
    return duckdb.connect(db_path)


def check_duplicates(data, columns):
    """Report duplicate records for a specified key."""

    if isinstance(data, pd.DataFrame):
        count = data.duplicated(subset=columns).sum()

    elif isinstance(data, pl.DataFrame):
        count = (
            data.group_by(columns)
            .len()
            .filter(pl.col("len") > 1)
            .height
        )

    else:
        raise TypeError("Expected a Pandas or Polars DataFrame.")

    print(f"Duplicate records by {columns}: {count}")
    return count


def validate_required_columns(data, required_columns):
    """Check whether all required columns are present."""

    actual_columns = set(data.columns)
    missing = set(required_columns) - actual_columns

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    print("Required columns validated.")


def season_summary(data, season_column="season"):
    """Count records by season."""

    if isinstance(data, pd.DataFrame):
        return data.groupby(season_column).size().reset_index(name="rows")

    if isinstance(data, pl.DataFrame):
        return (
            data.group_by(season_column)
            .len()
            .sort(season_column)
        )

    raise TypeError("Expected a Pandas or Polars DataFrame.")
