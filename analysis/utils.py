from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, Template


def get_template(template_folder: str, template_name: str) -> Template:
    """Recupera uma instancia de Template (jinja2) através dos
    nomes fornecidos.
    :param template_folder: Nome da paste que contem os templates;
    :param template_name: Nome do template a ser recuperado;
    :author: Brian Duarte
    """
    template_dir = get_root_dir().joinpath("templates", template_folder)

    jinja_env = Environment(loader=FileSystemLoader(template_dir))
    return jinja_env.get_template(template_name)


def concat_name_with_timestamp(name: str) -> str:
    """Concatena  o nome fornecido com um timestamp que é gerado
    usando o padrão: "yyyy-mm-dd HH-mm-ss".
    :param name: Nome a ser concatenado;
    :return: filename_2024-04-13 15-28-32;
    :author: Brian Duarte
    """
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    return f"{name}_{timestamp}"


def get_csv_path(filename: str) -> Path:
    """Recupera uma instancia de Path (pathlib) como o path para o arquivo
    csv cujo o nome foi fornecido.
    :param name: Nome do arquivo a ser recuperado;
    :return: Instancia da Path com o path do arquivo solicitado;
    :author: Brian Duarte
    """
    return get_root_dir().joinpath("assets", f"{filename}.csv")


def get_root_dir() -> Path:
    return Path(__file__).parent.parent
