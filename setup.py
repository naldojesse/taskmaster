from setuptools import setup, find_packages

setup(
    name="taskmaster",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "networkx",
        # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "taskmaster=taskmaster.cli.cli:main",
        ],
    },
)
