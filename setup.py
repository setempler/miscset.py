import setuptools


with open("miscset/version.py", "r") as fs:
    exec(fs.read())
with open("README.md", "r", encoding = "utf-8") as fs:
    long_description = fs.read()


setuptools.setup(
    name = "miscset",
    version = version_string_,
    author = "Sven Templer",
    author_email = "sven.templer@gmail.com",
    description = "Miscellaneous set of helpful methods.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/setempler/miscset.py",
    packages = setuptools.find_packages(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Shells",
        "Topic :: Utilities",
        "Topic :: Text Processing :: Markup :: HTML"
    ],
    install_requires = [
        "pyyaml"
    ],
    python_requires = ">=3.6",
)
