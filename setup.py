from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(

    name="mlops_project_1",
    version=0.1,
    author="Arka",
    packages=find_packages(),
    install_requires=requirements
)