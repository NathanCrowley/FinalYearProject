from setuptools import find_packages, setup

VERSION = '0.1.0'
DESCRIPTION = 'python library example for learning how to create libs'

setup(
   name='mypythonlibNC',
   version=VERSION,
   author='Nathan Crowley',
   author_email='<crowley2305@gmail.com>',
   description=DESCRIPTION,
   packages=find_packages(include=['mypythonlib']),
   install_requirements=[],
   setup_requires=['pytest-runner'],
   tests_require=['pytest==4.4.1'],
   test_suite='tests',
   license='MIT',
   classifiers=[
	'Development Status :: 1 - Planning',
	'Intended Audience :: Developers',
	'Programming Language :: Python :: 3',
	'Operating System :: Unix',
	'Operating System :: MacOS :: MacOS X',
	'Operating System :: Microsoft :: Windows',
   ]
)

