from setuptools import setup,find_packages
from typing import List,Any

def get_requirements() -> List[Any]:
    """

    Returns:
        List[Any]: _description_
    """
    requirement_list :List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #Read the lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                #strip whitespace and new line characters
                requirement = line.strip()
                #Ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_list
print(get_requirements())

setup(
    name = "AI-TRAVEL-PLANNER",
    version = '0.0.1',
    author='Keerthi Vardhan Naidu',
    author_email="nettemkeerthivardhannaidu@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
        

                    
                    
