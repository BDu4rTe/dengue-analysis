from pathlib import Path
from jinja2 import Environment, FileSystemLoader, Template


def get_template(template_folder: str) -> Template:
    template_dir = get_root_dir().joinpath("templates", template_folder)

    jinja_env = Environment(loader=FileSystemLoader(template_dir))
    return jinja_env.get_template("index.html")


def get_csv_path(filename: str) -> Path:
    return get_root_dir().joinpath("assets", f"{filename}.csv")


def get_root_dir() -> Path:
    return Path(__file__).parent
