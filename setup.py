from setuptools import setup

setup(
    name='RaphaelSphere',
    version='0.1.0',
    py_modules=['sphere'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        sphere=sphere:cli
    '''
)