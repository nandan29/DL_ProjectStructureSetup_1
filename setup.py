import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

#version on which u r working , since working on initial version ,so 0.0.0 .when another version so 0.0.1 and so on.
__version__ = "0.0.0"

REPO_NAME = "DL_ProjectStructureSetup_1"
AUTHOR_USER_NAME = "nandan29"
SRC_REPO = "deepClassifier"
AUTHOR_EMAIL = "shubham.datascience29@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },

    #src to be identified as package directory as inside src folder deepClassifier is present as package (as it contains __init__.py file)
    package_dir={"": "src"},
    #src directory to be considered for identifying the packages ...
    packages=setuptools.find_packages(where="src"))