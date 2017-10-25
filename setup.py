from setuptools import setup

setup(name='modelbase',
      version='0.1',
      description='A package to build metabolic models',
      url='https://git.hhu.de/kinetic-models/modelbase',
      author='Oliver Ebenhoeh',
      author_email='oliver.ebenhoeh@hhu.de',
      license='GPL4',
      packages=['modelbase'],
      install_requires=[
          'numpy',
          'scipy',
          'numdifftools'
          'itertools',
          're',
          'pickle'
      ],
      zip_safe=False)