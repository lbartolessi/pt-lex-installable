from setuptools import setup, find_packages

setup(
    name='pt_lex',
    version='0.1.0',
    packages=find_packages(),
    description='A Python library for Portuguese lexical analysis, adapted for installation.',
    author='Original Author: msamribeiro, Packager: <Tu Nombre o Nick>',
    url='<URL de tu fork en GitHub>',
    # Lista de dependencias que pt-lex necesita para funcionar
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    # Esto es importante para que pueda encontrar los archivos de datos que incluye
    include_package_data=True,
    package_data={
        '': ['*.csv', '*.p'],
    },
)
