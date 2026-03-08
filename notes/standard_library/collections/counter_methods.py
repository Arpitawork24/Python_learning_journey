from collections import Counter
ctr = Counter([1, 2, 4])

#  update(): Adds counts from another iterable or mapping
ctr.update([2, 2, 3, 3, 3, 1])
print(ctr)

# most_common(): Returns a list of the n most common elements and their counts from the most common to the least.
ctr = Counter([1, 4, 2, 3, 4, 2, 4])
common = ctr.most_common(2)
print(common)

#  add(): Increases the count of a single element by 1.

ctr = Counter([1, 2, 2])
ctr[2] += 1
ctr[3] += 1
print(ctr)