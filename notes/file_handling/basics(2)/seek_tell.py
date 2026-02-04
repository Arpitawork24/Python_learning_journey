with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(7)  # this means that letters upto 7th index will only print

with open('sample.txt', 'r') as f:
    f.seek(2)  # this means that cursor is at index 2
    print(f.read())
    print(f.tell())  # tells the position of the cursor i.e. at 7 rn (bcz of truncate)