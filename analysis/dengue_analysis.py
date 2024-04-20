from pathlib import Path
import pandas as pd
from rich.console import Console
from data_manager import DataManager
from enums.dengue_columns import DengueColumns

console = Console()


class DengueAnalysis(DataManager):

    def __init__(self, path: Path) -> None:
        self.df = self.csv_converter(path)

    @property
    def df(self):
        return self.__df

    @df.setter
    def df(self, data_frame: pd.DataFrame) -> None:
        self.__df = data_frame

    @property
    def zona_sul(self) -> pd.DataFrame:
        return self.__zona_sul

    @zona_sul.setter
    def zona_zul(self, data_frame: pd.DataFrame) -> None:
        self.__zona_sul = data_frame

    @property
    def zona_sudeste(self) -> pd.DataFrame:
        return self.__zona_sudeste

    @zona_sudeste.setter
    def zona_sudeste(self, data_frame: pd.DataFrame) -> None:
        self.__zona_sudeste = data_frame

    @property
    def zona_sudoeste(self) -> pd.DataFrame:
        return self.__zona_sudoeste

    @zona_sudoeste.setter
    def zona_sudoeste(self, data_frame: pd.DataFrame) -> None:
        self.__zona_sudoeste = data_frame

    @property
    def zona_oeste(self) -> pd.DataFrame:
        return self.__zona_oeste

    @zona_oeste.setter
    def zona_oeste(self, data_frame: pd.DataFrame) -> None:
        self.__zona_oeste = data_frame

    @property
    def zona_leste(self) -> pd.DataFrame:
        return self.__zona_leste

    @zona_leste.setter
    def zona_leste(self, data_frame) -> None:
        self.__zona_leste = data_frame

    @property
    def zona_nordeste(self) -> pd.DataFrame:
        return self.__zona_nordeste

    @zona_nordeste.setter
    def zona_nordeste(self, data_frame: pd.DataFrame) -> None:
        self.__zona_nordeste = data_frame

    def rename_columns(self) -> None:
        self.df.columns = [column_enum.value for column_enum in DengueColumns]
