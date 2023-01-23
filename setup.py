import pathlib

from setuptools import find_packages, setup
import setuptools_scm
setup()

#
# def myversion():
#     from setuptools_scm.version import SEMVER_MINOR, guess_next_simple_semver, release_branch_semver_version
#
#     def my_release_branch_semver_version(version):
#         v = release_branch_semver_version(version)
#         if v == version.format_next_version(guess_next_simple_semver, retain=SEMVER_MINOR):
#             return version.format_next_version(guess_next_simple_semver, fmt="{guessed}", retain=SEMVER_MINOR)
#         return v
#
#     return {
#         'version_scheme': my_release_branch_semver_version,
#         'local_scheme': 'no-local-version',
#     }
#
#
# setup(use_scm_version=myversion)
#
# if __name__ == "__main__":
#     print(myversion())

#
# def get_version(rel_path: str):
#     file_path = pathlib.Path(__file__).parent.absolute() / rel_path
#     for line in file_path.read_text().splitlines():
#         if line.strip().lower().startswith("__version__"):
#             return line.split('=')[1]
#     raise RuntimeError("Unable to find version string.")
#
#
# if __name__ == "__main__":
#     #print(get_version("src/showme/version.py"))
#     try:
#         setup()
#     except:  # noqa
#         print(
#             "\n\nAn error occurred while building the project, "
#             "please ensure you have the most updated version of setuptools, "
#             "setuptools_scm and wheel with:\n"
#             "   pip install -U setuptools setuptools_scm wheel\n\n"
#         )
#         raise
