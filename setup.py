from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='agit',
    version='0.1.1',
    py_modules=['agit'],
    install_requires=[
        'Click',
    ],
    license='MIT',
    author='Kei',
    author_email='nwcntyrcrm@gmail.com',
    long_description=long_description,  # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown',
    entry_points='''
        [console_scripts]
        agit=agit:cmd
    ''',
    url='https://github.com/sakiika-bechhu/Auto-local-git-cli',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    description='Command line interface for setting git local user and email according to repository',

)
