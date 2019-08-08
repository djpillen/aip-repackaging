from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

requirements.append("DAPPr=0.0.1")
requirements.append("bhlaspaceapiclient=0.0.1")

setup(
    name='aip-repackaging',
    version='0.0.1',
    url='https://github.com/djpillen/aip-repackaging',
    author='Dallas Pillen',
    packages=find_packages(),
    scripts=['aip_repackager.py'],
    description='Bentley Historical Library scripts to repackage Archivematica AIPs',
    dependency_links=[
                    'git+https://github.com/bentley-historical-library/DAPPr.git@master#egg=DAPPr-0.0.1',
                    'git+https://github.com/bentley-historical-library/bhlaspaceapiclient.git@master#egg=bhlaspaceapiclient-0.0.1'
                    ],
    install_requires=requirements
)