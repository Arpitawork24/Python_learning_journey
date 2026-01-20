# enumerate is a built in function used to loop over sequencesnd get the index value of each element 

marks = [22,45,36,97,2,82]
# syntax -
# for index, value in sequence (list,tuple, string)     ---dont do--> for value, index in seq
for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("topper")