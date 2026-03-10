from collections import OrderedDict

od1 = OrderedDict([("a",1),("b",2)])
od2 = OrderedDict([("b",2),("a",1)])

print(od1 == od2) 
#this will give output as false 
# if it would have been normal dict then it would have given true as in normal dict this order doesnt matter!!