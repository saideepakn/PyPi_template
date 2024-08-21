import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "IPYNBrenderer"
AUTHOR_USER_NAME = "saideepakn"
SRC_REPO = "IPYNBrenderer"
AUTHOR_EMAIL = "saideepaknamburu@gmail.com"

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
        #"Development Status :: 3 - Alpha",
        # "License :: OSI Approved :: MIT License",
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.7",
        # "Programming Language :: Python :: 3.8",
        # "Programming Language :: Python :: 3.9",
        # "Programming Language :: Python :: 3.10",
        # "Topic :: Software Development :: Libraries :: Python Modules",
        # "Topic :: Text Processing :: Markup :: Markdown",
        # "Intended Audience :: Developers",
        # "Operating System :: OS Independent",
        # "Natural Language
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src"),

)
