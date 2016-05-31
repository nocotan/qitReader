from setuptools import setup, find_packages

setup(name='qitreader',
      version='0.0.1',
      description='Qiita Reader in konsole',
      author='@nocotan',
      author_email='noconoco.lib@gmail.com',
      url='https://github.com/nocotan/qitReader',
      packages=find_packages(where='*'),
      entry_points="""
      [console_scripts]
      qitreader = qit_reader.qit_reader:qitReader.qit_reader
      """,)
