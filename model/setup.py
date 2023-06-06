from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="easy_diffuser", 
    version="0.0.1",
    url="https://huggingface.co/leeyunjai/img2txt",
    packages=find_packages(),
    install_requires=requirements,
)