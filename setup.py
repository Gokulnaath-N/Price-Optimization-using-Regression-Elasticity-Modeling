from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='demandex',
    version='0.0.1',
    author='Gokulnaath_N',
    author_email='gokulnaathn64@gmail.com',
    description='Demandex — ML-Powered Price Optimization & Elasticity Modeling System',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    python_requires='>=3.11',
)