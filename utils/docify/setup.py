import setuptools


setuptools.setup(
    entry_points = {
        'console_scripts': ['docify=docify.cli:main'],
    },
    setup_requires=['pbr'],
    tests_require=['pytest', 'PyHamcrest'], 
    install_requires=[
        'docopt',
    ],
    pbr=True
)

