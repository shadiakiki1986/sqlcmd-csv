from setuptools import setup, find_packages

setup(
    name='sqlcmd_csv',
    version="0.0.1,
    author="Shadi Akiki",
    url='https://github.com/shadiakiki1986/ms-sqlcmd-csv',
    description="convert microsoft's sqlcmd output to valid csv",    
    packages=find_packages(),
    install_requires=[
      "pandas",
      "click",
    ],
)
