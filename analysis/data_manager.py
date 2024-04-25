import pandas as pd
from pathlib import Path
from abc import ABC, abstractmethod
from utils import get_csv_path, concat_name_with_timestamp
import logging

logger = logging.getLogger(__file__)


class DataManager(ABC):
    @abstractmethod
    def rename_columns(self) -> None:
        """Método para renomear todas as colunas do DataFrame [pandas]"""

    def csv_converter(self, path: Path) -> pd.DataFrame:
        """Método para converter um arquivo csv em uma DataFrame [pandas]"""
        self.df = pd.read_csv(path)
        self.exclude_empty_columns()
        return self.df

    def exclude_empty_columns(self) -> None:
        """Método para excluir todas as colunas vazias do DataFrame [pandas]"""
        self.df = self.df.dropna(axis=1, how="all")

    def generate_new_csv(self, filename: str) -> None:
        """Método para gerar um novo arquivo csv a partir do DataFrame [pandas]
        da classe e o nome do arquivo fornecido.
        :param filename: Nome do arquivo csv que sera gerado.
        """
        name: str = concat_name_with_timestamp(filename)
        self.df.to_csv(get_csv_path(name), index=False)
        logger.info(f"New csv file saved with name: {name}")
