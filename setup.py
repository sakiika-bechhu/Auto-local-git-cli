from setuptools import setup

setup(
    name='agit',
    version='0.1',
    py_modules=['agit'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        agit=agit:cmd
    ''',
)