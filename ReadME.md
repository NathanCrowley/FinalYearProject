# FYP : InteractiVenn as an API
Users can create, view and interact with Venn Diagrams of up to 6 sets, using a simple Python API.

## How to install the Python API
- Linux:
	- install the package with command line: <pip install drawVennDiagram==0.1.0>
	
## How to use the Python API
- Linux:
	- create a python file
	- inside the python file call the package: <from drawVennDiagram import *>
	- draw a 2 set VennDiagram:
		- create a tuple of elements	(30,10,5)
		- create a tuple of labels	('A',B')
		- call the function 		<drawVenn2(subsets,lables,alpha)>
	- draw a 3 set VennDiagram:
		- create a tuple of elements	(20,10,12,10,9,4,3)
		- create a tuple of labels	('A',B','C')
		- call the function 		<drawVenn3(subsets,lables,alpha)>


## Python virtual enviroment created
- open  :	source venv/bin/activate
- close :	deactivate


