import os
import sys
from pathlib import Path
import tomlkit
from tomlkit.toml_document import TOMLDocument


def read(pyproject_path: Path) -> TOMLDocument:
    with pyproject_path.open("r", encoding="utf-8") as t:
        return tomlkit.parse(t.read())


def get_path(working_dir=os.getcwd()):
    if 'ipykernel' in sys.modules:
        return Path(os.environ['PROJECT_ROOT']).joinpath("pyproject.toml")
    else:
        return Path(working_dir).joinpath("pyproject.toml")
