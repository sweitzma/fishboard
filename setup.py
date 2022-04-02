from setuptools import setup, find_packages
from os import path
import re


__PATH__ = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(__PATH__, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def get_version():
    VERSIONFILE = path.join(__PATH__, 'fishboard', '__init__.py')
    with open(VERSIONFILE) as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  f.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find __version__ string in %s" % VERSIONFILE)

setup(
    name='fishboard',
    version=get_version(),
    license='MIT',
    description='Launch a simple http server for visualizing videos and images',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sweitzma/fishboard',
    keywords='http.server video image',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    ],
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3',
    entry_points={
        'console_scripts': ['fishboard=fishboard:main'],
    },
    include_package_data=True,
    zip_safe=False,
)
