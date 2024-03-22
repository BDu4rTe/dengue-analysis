import pandas as pd
import logging

logger = logging.getLogger(__file__)


class DataAnalysis:
    def __init__(path: str, self) -> None:
        self.path = path

    def csv_converter(self) -> pd.DataFrame:
        return pd.read_csv(self.path)

    def clear_age_field() -> pd.DataFrame: ...
