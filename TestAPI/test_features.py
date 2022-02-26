# library
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles, venn3_unweighted

#Titles
'''title = "Venn Diagram"'''
weighted_title = "- weighted "
unweighted_title = "- unweighted "
three_sets_title = " - 3 sets "
two_sets_title = " - 2 sets "
#Colours
default_two_set_colours = ("")

'''
8/2/22 - trying to get the colour setter and label settter working
		- make it interactvie
		- post it to pyPI
'''

## How to use ****** currently only 2 set venn diagram ****---------------------
'''
- create a drawVenn object with 'subsets' and 'labels' as attributes.
- you can show the venn diagram with the print(object) fucntion.
- the api will know if its a 2 or 3 set diagram based on the labels inputted.
'''
## ------------------------------------------------------------------------------

class drawVenn:
	def __init__(self,subsets,labels,unweighted=False):
		self.subsets = subsets
		self.labels = labels
		self.number_of_sets = len(labels)
		self.unweighted = unweighted
		self.title = "Venn Diagram"
		if self.number_of_sets == 3: # 3 set Venn diagram
			if self.unweighted == False:
				venn3(subsets=self.subsets, set_labels=self.labels) 
			elif self.unweighted == True:
				venn3_unweighted(subsets=self.subsets, set_labels=self.labels)
		elif self.number_of_sets == 2: # 2 set Venn diagram
			if self.unweighted == False:
				venn2(subsets=self.subsets, set_labels=self.labels)
			elif self.unweighted == True:
				venn2_unweighted(subsets=self.subsets, set_labels=self.labels)
		
		
	def __str__(self):
		title = self.title
		if self.number_of_sets == 3:		# 3 set Venn diagram
			title += three_sets_title
			if self.unweighted == False:
				title += weighted_title
			else:
				title += unweighted_title
		else:								# 2 set Venn diagram
			title += two_sets_title
			if self.unweighted == True:
				title += weighted_title
			else:
				title += unweighted_title
		plt.title(title)
		plt.show()
		
	# Getters and setters
	def set_labels(self, labels):
		self.labels = labels
		
	def set_circles_design(self):
		pass
#-------------------------------------------------------------------------------------------------------------------------------------------------	

