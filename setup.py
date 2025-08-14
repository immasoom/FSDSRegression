# want to convert it in project then we need to use this setup.py

from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()      

        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
             requirements.remove(HYPHEN_E_DOT)

    return requirements

setup (
    name="RegressorProject",
    version='0.0.1',
    author="Masoom",
    author_email="masoom.haque@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)