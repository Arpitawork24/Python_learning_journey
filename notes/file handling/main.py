f = open("notes/file handling/myfile.txt", "r")
# print(f)
text = f.read()  #to read the file no arg given
print(text)
f.close() # necessary to save the file properly nd free system resources


f = open("notes/file handling/myfile2.txt", "a")  # a is for append => include the text at the ending of existing text nd   w is for write => clear full text nd then write  (creates new file if file doesnt exist) 

text = f.write("\nwelcome")  # to write or append 1 arg is given in write()
print(text)
f.close()

# x => creates new file nd if the file alrdy exists then it will give error

# f = open("notes/file handling/newfile.txt", "x")
# f.write("hello bro i am created using x mode")
# f.close()


# r = rt nd w = wt as t is the deafualt mode ; t mode is used tp handle text files thats default
# b=> binary mode ; used to handle binary files
f = open("notes/file handling/myfile.txt", "rb") # binary mode
# print(f)
text = f.read()  #to read the file no arg given
print(text)
f.close()
