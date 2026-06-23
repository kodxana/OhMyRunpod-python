from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='OhMyRunpod',
    version='0.6.5',
    author='Madiator2011',
    author_email='admin@madiator.com',
    url='https://github.com/kodxana/OhMyRunpod-python',
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL-3.0-only',
    install_requires=[
        'rich>=13.0.0',
    ],
    project_urls={
        'Source': 'https://github.com/kodxana/OhMyRunpod-python',
        'Bug Reports': 'https://github.com/kodxana/OhMyRunpod-python/issues',
    },
    entry_points={
        'console_scripts': [
            'OhMyRunpod=OhMyRunpod.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
)
