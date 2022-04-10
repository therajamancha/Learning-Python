import marshal


marks = [98,99,75]
print(marks)
# print with index
print(marks[2])
# index from back
print(marks[-2]) 
# new list from existing
print(marks[0 : 2])
# for Loop
for mark in marks:
  print(mark)

# array list opertion in python
# add one more item in List
marks.append(84)
print(marks)

# add one more particuler index
marks.insert(2,98)
print(marks)
# find if any student get 100 marks 
print(100 in marks)
# print the lenght of array
print(len(marks))
