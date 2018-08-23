#!/usr/env/bin/ python3
from setuptools import setup, Extension

setup(name="andrnx",
      version="0.1",
      description="Package to convert from GNSS logger to Rinex files",
      author='Miquel Garcia',
      author_email='info@rokubun.cat',
      url='https://www.rokubun.cat',
      packages=['andrnx'],
      test_suite="andrnx.test",
      scripts=['bin/gnsslogger_to_rnx'])

