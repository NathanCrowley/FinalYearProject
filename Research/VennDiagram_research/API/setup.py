from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Education',
  'Operating System :: POSIX :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
	name='DrawVennDiagram',
	version='0.3.0',
	description='Python API for visualisation of sets.',
	url='',
	author='Nathan Crowley',
	author_email='crowley2305@gmail.com',
	license='MIT',
	classifiers=classifiers,
	packages=find_packages(),
	install_requires=[
	'matplotlib','matplotlib_venn',
	],
)
