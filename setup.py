#!/usr/bin/env python
install_requires=['python-dateutil','numpy','xarray']
tests_require=['nose','coveralls']
# %%
from setuptools import find_packages
from numpy.distutils.core import setup,Extension

ext = [Extension(name='lowtran7',
                 sources=['lowtran7.f'],
                 f2py_options=['--quiet'])]

setup(name='lowtran',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D',
      description='Model of Earth atmosphere absorption and transmission vs. wavelength and location on Earth.',
      version='2.2.1',
      url='https://github.com/scivision/lowtran',
      classifiers=[
      'Intended Audience :: Science/Research',
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Topic :: Scientific/Engineering :: Atmospheric Science',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      ],
      ext_modules=ext,
      install_requires=install_requires,
      python_requires='>=3.5',
      extras_require={'plot':['matplotlib','seaborn'],
                      'tests':tests_require},
      tests_require=tests_require,
	  )
