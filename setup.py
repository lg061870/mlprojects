from setuptools import find_packages, setup
from typing import  List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    ''' return list of requirements'''
    requirements = []

    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [reg.replace("\n", "") for reg in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = 'mlproject',
    version='0.0.1',
    author='Guillermo Jimenez',
    author_email='lg061870@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)