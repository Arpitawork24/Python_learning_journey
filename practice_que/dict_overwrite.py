# Find the output of the following program:

d = dict()
for i in range (3):
	for j in range(2):
		d[i] = j
print(d)

# Dictionary keys are unique
# Assigning d[i] = j again replaces the old value
# Inner loops last value of j survives

# 1st loop will give 3 values to i 0, 1 and 2. In the empty dictionary, valued are added and overwrited in j loop, 
# for eg. D[0] = [0] becomes D[0] = 1, due to overwriting.