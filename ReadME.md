# Python API for visualisation of sets

#### Department of Computer Science BSc Computer Science University College Cork

#### Nathan John Crowley 118429092

#### Dr Rosane Minghim
:::

::: {.cell .markdown}
# Abstract

The project involves creating a Python API/ library to be used by
students or academic professionals with the aim of visualising sets,
using InteractiVenn's approach to Set Visualisation, to allow a greater
understanding of given sets, and their unions and intersections. The
Python API developed should allow users to input up to six sets of data
to be visualised as an interactive Venn Diagram with functionality that:

-   1\) Allow users to visualise the union and intersections of the
    given complex input sets.
-   2\) Allow users to hover over set unions and present the elements of
    a given set.

The developed Python API should take into account that the users may
have little or no technical skills, this should direct the design
towards being as easy as possible to use for the target audience. The
documentation of the Python API must have clear and concise information
on its functionality, along with concrete examples displaying to the
user the operations that can be performed. The project includes running
and evaluating the developed Python API by itself as well as against an
established API, UpSet -- Visualising Intersecting Sets, to highlight
the advantages and disadvantages of each API given a number of examples.
:::

::: {.cell .markdown}
# Import the API from PyPI
:::

::: {.cell .code execution_count="44" scrolled="true"}
``` {.python}
pip install DrawVennDiagram==0.3.0
```

::: {.output .stream .stdout}
    Collecting DrawVennDiagram==0.3.0
      Using cached DrawVennDiagram-0.3.0-py3-none-any.whl (3.5 kB)
    Requirement already satisfied: matplotlib-venn in /home/nathan/.local/lib/python3.8/site-packages (from DrawVennDiagram==0.3.0) (0.11.6)
    Requirement already satisfied: matplotlib in /home/nathan/.local/lib/python3.8/site-packages (from DrawVennDiagram==0.3.0) (3.4.3)
    Requirement already satisfied: scipy in /home/nathan/.local/lib/python3.8/site-packages (from matplotlib-venn->DrawVennDiagram==0.3.0) (1.7.1)
    Requirement already satisfied: numpy in /home/nathan/.local/lib/python3.8/site-packages (from matplotlib-venn->DrawVennDiagram==0.3.0) (1.21.2)
    Requirement already satisfied: pyparsing>=2.2.1 in /home/nathan/.local/lib/python3.8/site-packages (from matplotlib->DrawVennDiagram==0.3.0) (2.4.7)
    Requirement already satisfied: kiwisolver>=1.0.1 in /home/nathan/.local/lib/python3.8/site-packages (from matplotlib->DrawVennDiagram==0.3.0) (1.3.1)
    Requirement already satisfied: python-dateutil>=2.7 in /usr/lib/python3/dist-packages (from matplotlib->DrawVennDiagram==0.3.0) (2.7.3)
    Requirement already satisfied: cycler>=0.10 in /home/nathan/.local/lib/python3.8/site-packages (from matplotlib->DrawVennDiagram==0.3.0) (0.10.0)
    Requirement already satisfied: pillow>=6.2.0 in /usr/lib/python3/dist-packages (from matplotlib->DrawVennDiagram==0.3.0) (7.0.0)
    Requirement already satisfied: six in /usr/lib/python3/dist-packages (from cycler>=0.10->matplotlib->DrawVennDiagram==0.3.0) (1.14.0)
    Installing collected packages: DrawVennDiagram
      Attempting uninstall: DrawVennDiagram
        Found existing installation: DrawVennDiagram 0.5.0
        Uninstalling DrawVennDiagram-0.5.0:
          Successfully uninstalled DrawVennDiagram-0.5.0
    Successfully installed DrawVennDiagram-0.3.0
    Note: you may need to restart the kernel to use updated packages.
:::
:::

::: {.cell .code execution_count="45"}
``` {.python}
from DrawVennDiagram import *
```
:::

::: {.cell .markdown}
# Read in the data file

-   **Labels**: The set names read in from the input data.
-   **Original Values**: These are the original raw set values taken
    from the input data.
-   **Mapped Values**: The API required integer values as inputs to the
    system. Therefore I created an in-built function in the API that
    will take the biological and map each raw value to a unique integer
    value.
:::

::: {.cell .code execution_count="46"}
``` {.python}
# State input file
file = "test_model.ivenn"

# Read in data using API's in-built "read_data(file)"
data = read_data(file)

# Set input data to variables
labels = data[0]
mapped_values = data[1]
values = data[2]

print("Labels:",labels,"\n")
print("Origninal Values:",values,"\n")
print("Mapped Values:",mapped_values,"\n")
```

::: {.output .stream .stdout}
    Labels: ['name1', 'nAme 2', 'Na_Me3', 'Na_Me4', 'Na_Me', 'Na_Me'] 

    Origninal Values: [['e1', 'w2', 'f3', 'e', '3', '4'], ['e122', 'w23', 'f3', 'e', '3', '4', '5', '6', '7', 'g', 'r', 't', 'y', 'd'], ['e1', 'w2', 'f3', 'e', '3', '4', 'w', 'q', 'a', 's', 'd', 'f', 'g', 'h', 'r', 't'], ['4', 'w', 'q', 'a', 's', 'd', 'f', 'g', 'h', 'r', 't', 'm', 'b', 'v', '65', '34', '23'], ['44', 'w4', 'q4', 'a4', 's4', 'd4', 'f4', 'g4', 'h4', 'r4', 't4', 'g', 'm', 'b', 'v', '653', '343', '23'], ['43', 'w3', 'q3', 'a3', 's3', 'd3', 'f3', 'g3', 'h3', 'r3', 't3', 'g', 'm3', 'b3', 'v', '65', '34', '23']] 

    Mapped Values: [[22, 49, 25, 21, 2, 5], [23, 50, 25, 21, 2, 5, 8, 9, 12, 27, 38, 44, 53, 18], [22, 49, 25, 21, 2, 5, 48, 35, 13, 41, 18, 24, 27, 30, 38, 44]] 
:::
:::

::: {.cell .markdown}
# Test Biological data in API

-   Test the input file, \"test_model.ivenn\" using the Python API
    created.
:::

::: {.cell .markdown}
# How to interact with Python API

-   **Step 1**: Create Python set objects with mapped values as inputs.
-   **Step 2**: Create a Sets tuple, which contains the Python set
    objects created in **Step 1**.
-   **Step 3**: State the labels you wish to display.
-   **Step 4**: Create a \"drawVenn\" object, giving the sets tuple from
    **Step2** and labels from **Step3** as input parameters.
-   **Step 5**: Print the \"drawVenn\" object using the overridden
    String method of the API.
:::

::: {.cell .markdown}
## 2 Set Venn Diagram using API {#2-set-venn-diagram-using-api}

-   The API will automatically create a 2-set Venn diagram from the set
    and label tuples given to the drawVenn object.
    -   The API will generate a 2-set or 3-set diagram automatically
        based on the number if set labels inputs.
:::

::: {.cell .code execution_count="47"}
``` {.python}
#Step 1: Create Python set objects with mapped values as inputs.
set1 = set(mapped_values[0])
set2 = set(mapped_values[1])

#Step 2: Create a Sets tuple, which contains the Python set objects created in **Step 1**.
sets = (set1,set2)

#Step 3: State the labels you wish to display.
l2 = labels[0:2]

#Step 4: Create a "drawVenn" object, giving the sets tuple from **Step2** and labels from **Step3** as input parameters.
v = drawVenn(sets,l2)
```

::: {.output .display_data}
![](vertopal_a357c2d1603c4108bda7a3b8a17db2b2/864b8bc441616da09479b2388eef461834735cbd.png)
:::
:::

::: {.cell .markdown}
# 3 Set Venn Diagram using API {#3-set-venn-diagram-using-api}

-   The API will automatically create a 3-set Venn diagram from the set
    and label tuples given to the drawVenn object.
    -   The API will generate a 2-set or 3-set diagram automatically
        based on the number if set labels inputs.
:::

::: {.cell .code execution_count="48"}
``` {.python}
#Step 1: Create Python set objects with mapped values as inputs.
set1 = set(mapped_values[0])
set2 = set(mapped_values[1])
set3 = set(mapped_values[2])

#Step 2: Create a Sets tuple, which contains the Python set objects created in **Step 1**.
sets = (set1,set2,set3)

#Step 3: State the labels you wish to display.
l3 = labels[0:3]

#Step 4: Create a "drawVenn" object, giving the sets tuple from **Step2** and labels from **Step3** as input parameters.
v2 = drawVenn(sets,l3,True)
```

::: {.output .display_data}
![](vertopal_a357c2d1603c4108bda7a3b8a17db2b2/8f5786c069c7970dad879876c2490a1098bdbe1f.png)
:::
:::

::: {.cell .markdown}
# 2 Set - Weighted vs Unweighted {#2-set---weighted-vs-unweighted}
:::

::: {.cell .markdown}
## Weighted

-   A weighted set has size correlated to the magnitude of the set
    value.
:::

::: {.cell .code execution_count="49"}
``` {.python}
set1 = set(mapped_values[0])
set2 = set(mapped_values[1])

sets = (set1,set2)
l2 = labels[0:2]

vw = drawVenn(sets,l2)
```

::: {.output .display_data}
![](vertopal_a357c2d1603c4108bda7a3b8a17db2b2/864b8bc441616da09479b2388eef461834735cbd.png)
:::
:::

::: {.cell .markdown}
## Unweighted

-   Set the third argument of the drawVenn object to True to produce
    unweighted diagram.
    -   The API will automatically recalibrate the outputted diagram.
-   Unweighted just allows all sets to be equal size, regarless of the
    values in the sets.
:::

::: {.cell .code execution_count="50"}
``` {.python}
set1 = set(mapped_values[0])
set2 = set(mapped_values[1])

sets = (set1,set2)
l2 = labels[0:2]

vuw = drawVenn(sets,l2,True)
```

::: {.output .display_data}
![](vertopal_a357c2d1603c4108bda7a3b8a17db2b2/c5f703748e3cc61eec50c061b4bee0e583ae45a0.png)
:::
:::

::: {.cell .markdown}
# Modify the Venn Diagram set colours

-   Set colours can be manually selected before the drawVenn object is
    created.
-   The drawVenn API will default the set colours to red,green,blue.
:::

::: {.cell .code execution_count="51"}
``` {.python}
set1 = set(mapped_values[0])
set2 = set(mapped_values[1])

sets = (set1,set2)
l2 = labels[0:2]

colours = ('purple','skyblue')

vp = drawVenn(sets,l2,colors=colours)
```

::: {.output .display_data}
![](vertopal_a357c2d1603c4108bda7a3b8a17db2b2/a8d36e9981839bbc043065070d497e8852462959.png)
:::
:::

::: {.cell .markdown}
# Modify the Circle border

-   Solid circle border can be created using the set_solid_circles()
    method.
-   Dashed circle borders can be added using the set_dashed_circles()
    method.
:::

::: {.cell .code execution_count="52"}
``` {.python}
set1 = set(mapped_values[0])
set2 = set(mapped_values[1])

sets = (set1,set2)
l2 = labels[0:2]

drawVenn(sets,l2)
v.set_solid_circles()
```

::: {.output .display_data}
![](vertopal_a357c2d1603c4108bda7a3b8a17db2b2/a503aab7c0b7a144fd339856abf99e456677d34d.png)
:::
:::

::: {.cell .code execution_count="53"}
``` {.python}
set1 = set(mapped_values[0])
set2 = set(mapped_values[1])

sets = (set1,set2)
l2 = labels[0:2]

drawVenn(sets,l2)
v.set_dashed_circles()
```

::: {.output .display_data}
![](vertopal_a357c2d1603c4108bda7a3b8a17db2b2/7493a406c2ef19fc95c1d874f419523cce6f3d78.png)
:::
:::

::: {.cell .markdown}
# Work in progress

-   Increase the limited input set sizes from current 3 sets to maximum
    of 6 sets.
-   Add interactivity that allows the user to hover over certain sets
    and allow users to click a set and return the set values.
:::

::: {.cell .markdown}
# Four set
:::

::: {.cell .code execution_count="63"}
``` {.python}
## import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

fig,ax = plt.subplots()
alpha = 0.4

                # (x,y),width,height,angle
#ellipse = Ellipse((0, 0), 5, 2, angle=40, alpha=0.5)

#top right
ellipse = Ellipse((0, 0.5), 4, 2, angle=60, alpha=alpha)
#bottom right
ellipse2 = Ellipse((0.5, -0.5), 4, 2, angle=60, alpha=alpha)
#top left
ellipse3 = Ellipse((-0.3, 0.2), 4, 2, angle=120, alpha=alpha)
#bottom left
ellipse4 = Ellipse((-0.8,-0.5), 4, 2, angle=120, alpha=alpha)


dotxy=0.1
angle=180
color="red"

A = Ellipse((-1.5,0),dotxy,dotxy,angle=180,color="red")
B = Ellipse((1.3,0),dotxy,dotxy,angle=180,color="red")
C = Ellipse((-1.1,1.4),dotxy,dotxy,angle=180,color="red")
D = Ellipse((0.8,1.5),dotxy,dotxy,angle=180,color="red")
AC = Ellipse((-1.3,0.7),0.1,0.1,angle=180,color="red")
CD = Ellipse((-0.2,1),0.1,0.1,angle=180,color="red")
ACD = Ellipse((-0.8,0),0.1,0.1,angle=180,color="red")
BD = Ellipse((0.9,0.6),0.1,0.1,angle=180,color="red")
BCD = Ellipse((0.4,0),0.1,0.1,angle=180,color="red")
ABCD = Ellipse((-0.2,-0.6),0.1,0.1,angle=180,color="red")
AD = Ellipse((-1.1,-0.86),0.1,0.1,angle=180,color="red")
BC = Ellipse((0.7,-1.1),0.1,0.1,angle=180,color="red")
ABD = Ellipse((-0.65,-1.1),0.1,0.1,angle=180,color="red")
ABC = Ellipse((0.2,-1.2),0.1,0.1,angle=180,color="red")
AB = Ellipse((-0.2,-2),0.1,0.1,angle=180,color="red")

areas = [A,B,C,D,AC,CD,ACD,BD,BCD,ABCD,AD,BC,ABD,ABC,AB]


ellipses = [ellipse,ellipse2,ellipse3,ellipse4]
for e in ellipses:
    ax.add_artist(e)
    
#for a in areas:
#ax.add_artist(a)
    
plt.text(-1.6,0,"A")
plt.text(1.3,0,"B")
plt.text(-1.1,1.4,"C")
plt.text(0.8,1.5,"D")
plt.text(-1.3,0.7,"AC")
plt.text(-0.2,1,"CD")
plt.text(-0.8,0,"ACD")
plt.text("BD")
plt.text("BCD")
plt.text("ABCD")
plt.text("AD")
plt.text("BC")
plt.text("ABD")
plt.text("ABC")
plt.text("AB")



ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
```

::: {.output .execute_result execution_count="63"}
    (-3.0, 3.0)
:::

::: {.output .display_data}
![](vertopal_a357c2d1603c4108bda7a3b8a17db2b2/4c683a8b44feb8612fc64aa233952571e8a66f94.png)
:::
:::

::: {.cell .markdown}
# Interactive
:::

::: {.cell .code}
``` {.python}
```
:::

::: {.cell .code}
``` {.python}
```
:::
