from setuptools import setup, find_packages
hyper_e_dot = "e ."
def read_file(filepath):
    
    with open(filepath,'r') as fileObject:
        
        requirements = fileObject.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if hyper_e_dot in requirements:
            requirements.remove(hyper_e_dot)
            
setup(
    name = "Flight Price Prediction",
    author="Aziz Ashfak",
    author_email="azizashfak@gmail.com",
    packages= find_packages(),
    install_requires = read_file("requirements.txt")
)