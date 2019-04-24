from setuptools import setup, find_packages

setup(
    name="attack_explorer",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['attack_explorer=attack_cli.navigator:execute']
    },
)