from setuptools import setup

setup(
    name='psn-sale',
    version='0.1dev',
    py_modules=['psn-sale'],
    install_requires=[
        'bs4',
        'click',
        'requests',
        'tabulate'
    ],
    entry_points='''
        [console_scripts]
        psn-sale=psn_sale:cli
    '''
)
