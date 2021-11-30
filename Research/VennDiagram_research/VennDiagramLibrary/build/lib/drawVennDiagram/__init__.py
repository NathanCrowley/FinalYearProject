# library
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles, venn3_unweighted
from sys import argv

default_alpha=0.5
# 2 sets 
default_labels2=('A','B')
default_color2=('r','g')
default_unweighted2=0
# 3 sets
default_labels3=('A','B','C')
default_color3=('r','g','b')
default_unweighted3=0


def drawVenn2(subsets, labels=default_labels2, alpha=default_alpha, color=default_color2, unweighted=default_unweighted2):
	if unweighted == 0:
		venn2(subsets=subsets, set_labels=labels, alpha=alpha)
	else:
		venn2_unweighted(subsets=subsets, set_labels=labels, alpha=alpha)
	plt.title("Venn Diagram - 2 sets")
	plt.show()


def drawVenn3(subsets, labels=default_labels3, alpha=default_alpha, color=default_color3, unweighted=default_unweighted3):
	if unweighted == 0:
		venn3(subsets=subsets, set_labels=labels, alpha=alpha)
	else:
		venn3_unweighted(subsets=subsets, set_labels=labels, alpha=alpha)
	plt.title("Venn Diagram - 3 sets")
	plt.show()

