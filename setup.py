from setuptools import setup

setup(
    name='blakpip',
    version='0.1',
    py_modules=['blakpip', 'blakpip_core'],
    entry_points={
        'console_scripts': ['blakpip=blakpip:main'],
    },
)
