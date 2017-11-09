from setuptools import setup

requirements = list()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='shopcart',
    packages=['shopcart'],
    version='',
    description='',
    include_package_data=True,
    author='Herald Yu',
    author_email='yuhr123@gmail.com',
    url='',
    license='MIT',
    install_requires=requirements,
)
