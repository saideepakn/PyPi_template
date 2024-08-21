import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "<YOUR REPO NAME>"
AUTHOR_USER_NAME = "<YOUR USERNAME>"
SRC_REPO = "<YOUR REPO NAME>"
AUTHOR_EMAIL = "<YOUR EMAIL ID>"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    authot_email = AUTHOR_EMAIL,
    description = "small python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url = {
        #"Documentation": "https://github.com/saideepakn/IPYNBrenderer/tree/master/docs",
        #"Source Code": "https://github.com/saideepakn/IPYNBrenderer",
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src"),

)
