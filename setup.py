from setuptools import setup, find_packages

setup(
    name="gitsy",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gitsy=cli:main',
        ],
    },
    author="Diti jain and Dev mehta",
    author_email="ditijainj@gmail.com",
    description="A simple version control system implemented in Python",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/diti-jain/gitsy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)