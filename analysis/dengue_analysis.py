from pathlib import Path
import pandas as pd
from rich.console import Console
from data_manager import DataManager
from enums.dengue_columns import DengueColumns
from enums.regions import Regions

console = Console()


class DengueAnalysis(DataManager):

    def __init__(self, path: Path) -> None:
        self.main_df = self.csv_converter(path)
        self.zona_sul = self.__set_zone(Regions.SUL)
        self.zona_sudoeste = self.__set_zone(Regions.SUDOESTE)
        self.zona_sudeste = self.__set_zone(Regions.SUDESTE)
        self.zona_norte = self.__set_zone(Regions.NORTE)
        self.zona_nordeste = self.__set_zone(Regions.NORDESTE)
        self.zona_leste = self.__set_zone(Regions.LESTE)
        self.zona_oeste = self.__set_zone(Regions.OESTE)
        self.zona_centro = self.__set_zone(Regions.CENTRO)

    def rename_columns(self) -> None:
        """Método para renomear o header de todas as
        colunas do DataFrame.
        """
        self.main_df.columns = [
            column_enum.value for column_enum in DengueColumns
        ]

    def __set_zone(self, region: Regions) -> pd.DataFrame:
        """Método para separar a região fornecida do DataFrame
        principal e configurar um DataFrame para exclusivo para a mesma.
        :param region: Região que sera separada do data frame original.
        """
        return self.main_df[
            self.main_df[DengueColumns.REGIAO.value] == region.value
        ]

    def get_lowest_know_symptom(self, zone: pd.DataFrame) -> None: ...
