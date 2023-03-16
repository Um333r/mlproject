from setuptools import find_packages,setup
from typing import list

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    ''''
     this function will return the list of requirement
    ''''
     requirements=[]
     with open(file_path)as file_obj:
          requirements=file_obj.readlines()
          requirements=[req.replace("\n","")for req in requirements]
          
          if HYPEN_E_DOT in requirements:
              requirements.remove(HYPEN_E_DOT)
              
     return requirements
              
  
  
setup(
name='mlproject',
version='0.0.1',
author='Umar',
author_email='mohum3r@gmail.comm',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)