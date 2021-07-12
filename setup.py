from setuptools import find_packages, setup

setup(
    name='py3cw',
    version='0.0.22',

    description='3commas Python wrapper',

    url='https://github.com/bogdanteodoru/py3cw',

    author='Bogdan Teodoru',
    author_email='me@bogdanteodoru.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable'
    ],

    keywords='api 3commas trading crypto bitcoin altcoin',

    packages=find_packages(exclude=['tests']),

    install_requires=[
        'requests',
    ],
)
