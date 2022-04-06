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
#Labels
default_labels=["A","B","C","D","E","F"]

## How to use ****** currently only 2 set venn diagram ****---------------------
'''
- create a drawVenn object with 'subsets' and 'labels' as attributes.
- you can show the venn diagram with the print(object) fucntion.
- the api will know if its a 2 or 3 set diagram based on the labels inputted.
'''
## ------------------------------------------------------------------------------

class drawVenn:
    def __init__(self,subsets,labels,unweighted=False,colors=('r','g')):
        self.subsets = subsets
        self.labels = labels
        self.number_of_sets = len(labels)
        self.unweighted = unweighted
        self.title = "Venn Diagram"
        self.set_colors = colors
        if self.number_of_sets == 3: # 3 set Venn diagram
            if self.unweighted == False:
                venn3(self.subsets,self.labels) 
            elif self.unweighted == True:
                venn3_unweighted(self.subsets,self.labels)
        elif self.number_of_sets == 2: # 2 set Venn diagram
            if self.unweighted == False:
                venn2(self.subsets,self.labels,set_colors=colors)
            elif self.unweighted == True:
                venn2_unweighted(self.subsets,self.labels,set_colors=colors)

    def __str__(self):
        title = self.title
        if self.number_of_sets == 3:       # 3 set Venn diagram
            title += three_sets_title
            if self.unweighted == False:
                title += weighted_title
            else:
                title += unweighted_title
        else:                              # 2 set Venn diagram
            title += two_sets_title
            if self.unweighted == True:
                title += weighted_title
            else:
                title += unweighted_title
        plt.title(title)
        plt.show()

    # Getters and setters
    def set_solid_circles(self):
        venn2_circles(self.subsets)
        
    def set_dashed_circles(self):
        venn2_circles(self.subsets,linestyle='dashed')

    def set_labels(self,labels):
        self.labels = labels  
    def get_labels(self):
        return self.labels
    
    def get_sets_values(self):
        return self.subsets
    def set_sets_values(self,sets):
        self.subsets = sets
#-------------------------------------------------------------------------------------------------------------------------------------------------	

