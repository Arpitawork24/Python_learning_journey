# Taking input and initializing dictionary
keys = input().split()
values = map(int, input().split())
my_dict = dict(zip(keys, values))
k, v = input().split()

# Insert k,v in my_dict
my_dict[k]=int(v)
# Print Inserted if inserted successfuly
print("Inserted")

# Delete entry with key d from my_dict
# Print Deleted if deleted successfuly else print -1
d = input()
if d in my_dict:
    del my_dict[d]
    print ("Deleted")
else :
    print (-1)

# Print marks of given key p if key present, else print -1
p = input()
if p in my_dict:
    print(f"Marks of {p} is {my_dict[p]}")
else :
    print(-1)
