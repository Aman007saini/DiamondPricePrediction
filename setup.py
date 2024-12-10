from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'    #another method to link requirements.txt to setup.py using command pip install -r requirements.txt
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Aman',
    author_email='amanashu72@gmail.com',
    install_requires= get_requirements('requirements.txt'),
    packages= find_packages()
)