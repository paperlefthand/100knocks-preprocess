import polars as pl
from pathlib import Path

DATA_FOLDER = Path(__file__).parents[1] / "data"


def load_data():
    return (
        pl.read_parquet(DATA_FOLDER / "category.parquet"),
        pl.read_parquet(DATA_FOLDER / "customer.parquet"),
        pl.read_parquet(DATA_FOLDER / "geocode.parquet"),
        pl.read_parquet(DATA_FOLDER / "product.parquet"),
        pl.read_parquet(DATA_FOLDER / "receipt.parquet"),
        pl.read_parquet(DATA_FOLDER / "store.parquet"),
    )
