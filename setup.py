from setuptools import setup
from pathlib import Path

VERSION = '1.1.5'
DESCRIPTION = 'A discord.py extension for command localization.'

# Setting up
setup(
    name="discord-localization",
    version=VERSION,
    author="Pearoo",
    author_email="<contact@pearoo.dev>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=Path("README.md").read_text(),
    packages=["discord.ext.localization"],
    install_requires=["discord.py"],
    keywords=['discord.py', 'i18n', 'translation', 'localisation', 'localization'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Source": "https://github.com/rnxm/discord-localization"
    }
)
# command: python setup.py sdist bdist_wheel
