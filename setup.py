from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'bip85-cli',
    version = '0.0.1',
    author = 'Valerio Vaccaro',
    author_email = 'valerio.vaccaro@gmail.com',
    license = 'MIT',
    description = 'Bip85 lib and cli written in python able to derive mnemonics from your master mnemonic.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/valerio-vaccaro/bip85-utils',
    py_modules = ['bip85lib', 'bip85_cli'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        bip85-cli=bip85_cli:main
    '''
)
