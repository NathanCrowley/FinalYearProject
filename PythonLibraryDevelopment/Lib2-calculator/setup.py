from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
	name='nathansBasicCalculator',
	version='0.0.1',
	description='Very basic calculator',
	url='',
	author='Nathan Crowley',
	author_email='crowley2305@gmail.com',
	license='MIT',
	classifiers=classifiers,
	packages=find_packages(),
	initial_requirements=['']
)
