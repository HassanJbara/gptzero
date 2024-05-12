from setuptools import setup, find_packages

setup(
    name="GPTZero", 
    version="1.0", 
    install_requires=open("requirements.txt", "r", encoding="utf-8").read().splitlines(),
    packages=find_packages(),
    include_package_data=True,
)
