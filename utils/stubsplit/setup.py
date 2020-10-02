import setuptools


setuptools.setup(
    entry_points = {
        'console_scripts': ['stubsplit=stubsplit.cli:main'],
    },
    setup_requires=['pbr'],
    tests_require=['pytest', 'PyHamcrest'], 
    install_requires=[
        'docopt',
    ],
    pbr=True
)

