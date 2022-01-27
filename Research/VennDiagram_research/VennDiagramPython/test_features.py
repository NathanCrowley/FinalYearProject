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

## How to use ****** currently only 2 set venn diagram ****---------------------
'''
- create a drawVenn object with 'subsets' and 'labels' as attributes.
- you can show the venn diagram with the print(object) fucntion.
- the api will know if its a 2 or 3 set diagram based on the labels inputted.
'''
## ------------------------------------------------------------------------------
'''
My notes:
	- for some reason the if statements are all running and the plt.show() shows all the venn diagrams and so they overlap and look terrible.
'''

class drawVenn:
	def __init__(self,subsets,labels):
		self.subsets = subsets
		self.labels = labels
		self.number_of_sets = len(labels)
		self.unweighted = True
		self.title = "Venn Diagram"
		if self.number_of_sets == 3: # 3 set Venn diagram
			if self.unweighted == False:
				self.venn_diagram_3 = venn3(subsets=self.subsets, set_labels=self.labels) 
			elif self.unweighted == True:
				self.venn_diagram_3_unweighted = venn3_unweighted(subsets=self.subsets, set_labels=self.labels)
		else: # 2 set Venn diagram
			if self.unweighted == 0:
				self.venn_diagram_2 = venn2(subsets=self.subsets, set_labels=self.labels)
			elif self.unweighted == 1:
				self.venn_diagram_2_unweighted = venn2_unweighted(subsets=self.subsets, set_labels=self.labels)
		
		
	def __str__(self):
		title = self.title
		if self.number_of_sets == 3:		# 3 set Venn diagram
			title += three_sets_title
			if self.unweighted == False:
				title += weighted_title
			else:
				title += unweighted_title
		else:					# 2 set Venn diagram
			title += two_sets_title
			if self.unweighted == True:
				title += weighted_title
			else:
				title += unweighted_title
		plt.title(title)
		plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------------------	

'''class drawVenn:
	def __init__(self, subsets, labels):
		self.subsets = subsets
		self.labels = labels
		self.number_of_sets = len(labels)
		# use the length of the labes to know if its a 2 or 3 set ven diagram
	
	def __str__(self):
		if self.number_of_sets == 3:
			venn3_unweighted(subsets=self.subsets, set_labels=self.labels)
			plt.title("Three set Venn Diagram")
		else:
			venn2_unweighted(subsets=self.subsets, set_labels=self.labels)
			plt.title("Two set Venn Diagram")
		plt.show()
		
	# Getters and setters
	def set_color():
		pass
		
	def set_labels():
		pass
		
	def set_circles_design():
		pass'''
		
		

#--------------Test the Class---------------------------


#-------------------------------------------------------

