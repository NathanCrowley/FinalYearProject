# Python API for visualisation of sets
#### Department of Computer Science BSc Computer Science University College Cork
#### Nathan John Crowley 118429092
####  Dr Rosane Minghim

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


## How to use:
### Import the API from PyPI.
	- pip install DrawVennDiagram==0.3.0.
	- from DrawVennDiagram import *
### Read in the data file 
	file = "test_model.ivenn"
	data = read_data(file)

	labels = data[0]
	mapped_values = data[1]
	values = data[2]

	print("Labels:",labels,"\n")
	print("Origninal Values:",values,"\n")
	print("Mapped Values:",mapped_values,"\n")
- **Labels**: The set names read in from the input data.
- **Original Values**: These are the original raw set values taken from the input data.
- **Mapped Values**: The API required integer values as inputs to the system. Therefore I created an in-built function in the API that will take the biological and map each raw value to a unique integer value.

### How to interact with Python API
- **Step 1**: Create Python set objects with mapped values as inputs.
- **Step 2**: Create a Sets tuple, which contains the Python set objects created in **Step 1**.
- **Step 3**: State the labels you wish to display.
- **Step 4**: Create a "drawVenn" object, giving the sets tuple from **Step2** and labels from **Step3** as input parameters.
- **Step 5**: Print the "drawVenn" object using the overridden String method of the API.
	####Step 1: Create Python set objects with mapped values as inputs.
	set1 = set(mapped_values[0])
	set2 = set(mapped_values[1])

	####Step 2: Create a Sets tuple, which contains the Python set objects created in **Step 1**.
	sets = (set1,set2)

	####Step 3: State the labels you wish to display.
	l2 = labels[0:2]

	####Step 4: Create a "drawVenn" object, giving the sets tuple from **Step2** and labels from **Step3** as input parameters.
	v = drawVenn(sets,l2)

		
# Project Strucutre
### README.md
- Markdown file to describe essential details of the project.
### setup.py
- Python file to help build the library.
### Test directory
- Directory containing Python test files to test the functionality of the library.
### MANIFEST.in
- File to add & remove files to and from the source distribution.
### LICENSES.txt
- Text file of the License for the library.
