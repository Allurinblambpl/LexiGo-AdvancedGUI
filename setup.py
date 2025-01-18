from setuptools import setup, find_packages

setup(
    name="LexiGo-GUI",
    version="1.0.0",
    packages=find_packages(),  # Wyszuka wszystkie pakiety w folderze
    install_requires=[
        "customtkinter",  # Dodajemy zależność od customtkinter
    ],
    author="Alluringlambpl",
    author_email="fboost247@gmail.com",
    description="A modern GUI application built using customtkinter.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Allurinblambpl/LexiGo-AdvancedGUI",  # Adres repozytorium na GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
