from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Education',
  'Operating System :: POSIX :: Linux',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
	name='drawVennDiagram',
	version='0.1.0',
	description='Non-interactive Venn Diagram outputer of 2/3 sets.',
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
