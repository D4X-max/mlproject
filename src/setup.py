from setuptools import setup, find_packages

setup(
    name='mlprojects',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        # Add other project dependencies here
    ],
    author='Your Name',
    description='Machine Learning Project'
)