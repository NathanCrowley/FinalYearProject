# library
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles, venn3_unweighted
from sys import argv

def drawVenn2(subsets, labels, alpha, color=('r','g'), unweighted=0, *args):
	if unweighted == 0:
		venn2(subsets=subsets, set_labels=labels, alpha=alpha)
	else:
		venn2_unweighted(subsets=subsets, set_labels=labels, alpha=alpha)
	plt.title("Venn Diagram - 2 sets")
	plt.show()


def drawVenn3():
	pass
	
	
	

subsets2=(30,10,5)
labels2=('A','B')
alpha=0.5
drawVenn2(subsets2,labels2, alpha)
#drawVenn2(subsets2,labels2, alpha, unweighted=1)
