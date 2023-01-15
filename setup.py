import pathlib

from setuptools import find_packages, setup
import setuptools_scm


def get_version(rel_path: str):
    file_path = pathlib.Path(__file__).parent.absolute() / rel_path
    for line in file_path.read_text().splitlines():
        if line.strip().lower().startswith("__version__"):
            return line.split('=')[1]
    raise RuntimeError("Unable to find version string.")


if __name__ == "__main__":
    #print(get_version("src/showme/version.py"))
    try:
        setup()
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
