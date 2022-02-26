# library
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from matplotlib_venn import venn3, venn3_circles, venn3_unweighted


#  Venn Diagram 2 sets
#-----------------------------------------------------------------------------------------------
# Most basic version with just labels and set data, cirlce size depending on the magnitude of numebr of items within the circle.
subsets2=(30,10,5)
labels2=('A','B')
alpha=0.5
#1)
#venn2(subsets=(subsets2), set_labels=(labels2))

#2) Customizing the Venn Diagram
# Default colors are red,green but you can customise this - set_colors(). 
# alpha=x - controls the transpararencys
#venn2(subsets=(30,10,5), set_labels=('A','B'), set_colors=('purple','skyblue'), alpha=0.7)
 
#3) If you wish to not have the cicle sizes to be a magnitude of the set items
# venn2_unweighted(subsets=(30,10,5),set_labels=('A','B'),set_colors=('r','g'), alpha=0.5)

#4) Overlay an otulien fot he circle over the original for easier vewing.
#venn2(subsets=(30,10,5), set_labels=('A','B'),set_colors=('r','g'),alpha=0.5)

#  Solid circle
#venn2_circles(subsets=(30,10,5))

#  Dotted circle
#venn2_circles(subsets=subsets2, linestyle='dashed', linewidth=2, color='k')
#-----------------------------------------------------------------------------------------------

# Venn Diagram 3 sets
#-----------------------------------------------------------------------------------------------
# 1)
subsets3=(20,10,12,10,9,4,3)
labels3=('A','B','C')
# Basic - no customization and sizing
#1) 
#venn3(subsets=subsets3, set_labels=labels3, alpha=alpha)

#2) Customize the color of EACH area of the diagram with 'get_patch_by_id'
#v = venn3(subsets=subsets3, set_labels=labels3, alpha=alpha)
#v.get_patch_by_id('111').set_color('white')

#3) Change line widths for each circle,
#	set c=ven diagram
#	call each circle with c[0],c[1],c[2] and set line width
c = venn3_circles(subsets=subsets3, linestyle='dashed', linewidth=1, color='grey')
c[0].set_lw(5.0)
c[1].set_lw(8.0)
c[2].set_lw(2.0)
venn3(subsets=subsets3, set_labels=labels3, alpha=alpha)

#-----------------------------------------------------------------------------------------------


plt.title("Venn Diagram with Python")
plt.show()
