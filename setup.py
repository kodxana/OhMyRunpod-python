from setuptools import setup, find_packages
import os
import sys

RUNPOD_ENV_VARS = (
    'RUNPOD_POD_ID',
    'RUNPOD_PUBLIC_IP',
    'RUNPOD_TCP_PORT_22',
    'RUNPOD_DC_ID',
)
LOCAL_INSTALL_OVERRIDE = 'OHMYRUNPOD_ALLOW_LOCAL_INSTALL'

def is_runpod_environment():
    return any(os.environ.get(var) for var in RUNPOD_ENV_VARS)

def local_install_override_enabled():
    return os.environ.get(LOCAL_INSTALL_OVERRIDE, '').lower() in {'1', 'true', 'yes', 'on'}

if 'egg_info' not in sys.argv and not is_runpod_environment() and not local_install_override_enabled():
    raise SystemExit(
        'OhMyRunpod is intended to be installed only inside Runpod pods. '
        f'If you are developing or testing locally, set {LOCAL_INSTALL_OVERRIDE}=1 to bypass this guard.'
    )

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='OhMyRunpod',
    version='0.6.3',
    author='Madiator2011',
    author_email='admin@madiator.com',
    url='https://github.com/kodxana/OhMyRunpod-python',
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'rich>=13.0.0',
    ],
    project_urls={
        'Source': 'https://github.com/kodxana/OhMyRunPod-python',
        'Bug Reports': 'https://github.com/kodxana/OhMyRunPod-python/issues',
    },
    entry_points={
        'console_scripts': [
            'OhMyRunpod=OhMyRunpod.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
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
