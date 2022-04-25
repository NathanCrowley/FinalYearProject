import upsetplot
from upsetplot import generate_counts
from upsetplot import plot
from matplotlib import pyplot

example = generate_counts()
#print(example)

plot(example)

pyplot.show()


