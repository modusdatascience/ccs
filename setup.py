from setuptools import setup, find_packages
import versioneer

setup(name='ccs',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='Matt Lewis',
      url='https://github.com/mattlewissf/ccs',
      package_data={'ccs': ['resources/*']},
      packages=find_packages(),
      requires=[]
     )