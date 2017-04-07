from setuptools import setup, find_packages

setup(name='ccs',
      version='0.1',
      author='Matt Lewis',
      url='https://github.com/mattlewissf/ccs',
      package_data={'ccs': ['resources/*']},
      packages=find_packages(),
      requires=[]
     )