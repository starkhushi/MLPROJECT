from setuptools import setup, find_packages
from typing import List

Hyphen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)

    return requirements


setup(
name='ml_project',
version='0.0.1',
author='starkhushi',
author_email='khushi.2226cseml1010@kiet.edu',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)