from test_features import drawVenn

# V1
set1 = set([1,2])
set2 = set([4,5])

# V2

v1 = drawVenn([set1,set2], ('A','B'))
#v2 = drawVenn((20,10,12,10,9,4,3), ('A','B','C'))


print("V1",v1)
#print("V2",v2)
