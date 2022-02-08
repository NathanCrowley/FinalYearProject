from test_features import drawVenn

# V1
v1_set1 = set([1,2,3])
v1_set2 = set([3,4,5])

# V2
v2_set1 = set([1,11,5])
v2_set2 = set([2,22,5])
v2_set3 = set([3,33,5])

## Only really have once instance of the venn diagram at a time

'''
Expect a 2 set Venn Diagram - weighted
>> v1 = drawVenn([v1_set1,v1_set2], ('A','B'))
'''

'''
Excpet a 2 set Venn Diagram - unweighted
>> v1 = drawVenn([v1_set1,v1_set2], ('A','B'), True)
'''

'''
Expect a 3 set VD - weighted
>> v1 = drawVenn([v2_set1,v2_set2,v2_set3],('A','B','C'))
'''

'''
Expect a 3 set VD - unweighted
v1 = drawVenn([v2_set1,v2_set2,v2_set3],('A','B','C'),True)
'''

#------------------------------------------------------------------
v1 = drawVenn([v1_set1,v1_set2], ('A','B'))
print()

