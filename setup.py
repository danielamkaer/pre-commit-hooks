from setuptools import find_packages
from setuptools import setup

setup(
    name='pre-commit-hooks',
    description='Some out-of-the-box hooks for pre-commit',
    url='https://github.com/danielamkaer/pre-commit-hooks',
    version='0.0.1',

    author='Daniel Amkaer Sorensen',
    author_email='daniel.amkaer@gmail.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'max_line_length = pre_commit_hooks.max_line_length:main',
        ],
    },
)
