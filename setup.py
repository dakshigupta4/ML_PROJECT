from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:    #-e->editable mode, .->this folder.
            requirements.remove('-e .')
    return requirements
# In this setup file, we are using setuptools to package our project.
setup(
    name='ml_project',
    version='0.1.0',
    author='Dakshi Gupta',
    author_email='dakshigupta4@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)