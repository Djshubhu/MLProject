from setuptools import find_packages,setup
from typing import List

HYPE_E_DOT="-e ."

def get_requiremts(File_path:str)->List[str]:
    requirements=[]
    with open(File_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPE_E_DOT is requirements:
            requirements.remove(HYPE_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='SP',
    author_email='sp9371414223@gmail.com',
    packages=find_packages(),
    install_require=get_requiremts('requirement.txt')
)