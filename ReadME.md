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

## Testing API
    - tests found in TestAPI folder.

	
# Abstract
The project involves creating a Python API/ library to be used by students or academic
professionals with the aim of visualising sets, using InteractiVenn’s approach to Set
Visualisation, to allow a greater understanding of given sets, and their unions and
intersections. The Python API developed should allow users to input up to six sets of data to
be visualised as an interactive Venn Diagram with functionality that:
- 1) Allow users to visualise the union and intersections of the given complex input sets.
- 2) Allow users to hover over set unions and present the elements of a given set.

The developed Python API should take into account that the users may have little or no
technical skills, this should direct the design towards being as easy as possible to use for the
target audience. The documentation of the Python API must have clear and concise
information on its functionality, along with concrete examples displaying to the user the
operations that can be performed.
The project includes running and evaluating the developed Python API by itself as well as
against an established API, UpSet – Visualising Intersecting Sets, to highlight the advantages
and disadvantages of each API given a number of examples.
