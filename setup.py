from setuptools import setup

setup(
    name='psn-sales',
    version='1.0',
    py_modules=['psn-sales'],
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        psn-sales=psn_sales:cli
    '''
)
