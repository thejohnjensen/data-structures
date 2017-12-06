"""The setup for mailroom project in python."""
from setuptools import setup

setup(
    name="data-structures",
    description="Data structures written in python",
    version=0.1,
    author="Zach Taylor & John Jensen",
    author_email="zacharymtaylor3@gmail.com & jensen.john.r@gmail.com",
    license='MIT',
    py_modules=['src/linked_list', 'src/binheap', 'src/bst', 'src/deque',
                'src/doubly_linked_list', 'src/graph', 'src/hash_table',
                'src/priorityq', 'src/que_', 'src/stack', 'src/trie'],
    install_requires=['ipython'],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={
        'console_scripts': []
    }
)
