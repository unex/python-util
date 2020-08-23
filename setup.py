from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="derw",
    author="notderw",
    version="0.0.2",
    description="Misc tools for other stuff",
    url="https://github.com/notderw/python-util",
    install_requires=requirements,
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6.0'
)
