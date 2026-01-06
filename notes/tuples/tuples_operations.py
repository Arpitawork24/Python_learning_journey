# to make changes in tuple(indirectly)-
# 1) change tuple into temp list
# 2) make necessary changes in the temp list
# 3) change temp list back to tuple
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

# we can directly concatenate two tuples without converting them to list -
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)