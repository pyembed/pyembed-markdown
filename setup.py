from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['pyembed']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='pyembed-markdown',
    version='0.2.0',
    author='Matt Thomson',
    author_email='matt.thomson@cantab.net',
    url='https://github.com/pyembed/pyembed-markdown',
    description='Python Markdown extension for embedding content using OEmbed',
    long_description=open('README.rst').read() + '\n\n' +
        open('CHANGES.rst').read(),
    download_url='https://pypi.python.org/pypi/pyembed-markdown/',
    license=open('LICENSE.txt').read(),

    provides=['pyembed.markdown'],
    packages=['pyembed.markdown'],
    namespace_packages=['pyembed'],

    install_requires=[
        'pyembed',
        'markdown'
    ],
    tests_require=[
        'PyHamcrest',
        'mock',
        'pytest'
    ],

    cmdclass={'test': PyTest},

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Text Processing'
    ]
)
