from setuptools import find_packages, setup
from typing import List
HYPEN_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements


setup(
    name="ml_project",
    version='0.0.1',
    author="onkar",
    author_email="onkarkandar157@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)