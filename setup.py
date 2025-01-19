from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT="-e ."

def get_requirements(path:str)->List[str]:
    '''
    Returns list of requirements
    '''

    requirements = []
    with open(path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n" , "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


    return requirements

setup(
    name="mlp-project",
    author="Ankita Ayushi",
    author_email="ankita.btech21@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)