from setuptools import setup, find_packages
from setuptools import setup


VERSION = '1.0.0'
DESCRIPTION = 'A fancy cool font generator that helps create stylish text font styles '


# Setting up
setup(
    name="fancytexts",
    version=VERSION,
    author="sahansandaruwan",
    author_email="<sahansandaruwanbandara64@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'fancytext', 'sahansandaruwan',],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)