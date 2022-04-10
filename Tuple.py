# [] List , () Tuple , {} Sets

# tuple is inmutable const data in it 
# can't perform any method to update
marks = (98,95,84,98,56,95) # parenthisis is not requird for tupels

# how many times 98 visible in tuple
print(marks.count(98))

# get first index of 95 in tuple
print(marks.index(95))

# Sets in python (unorder) 
#  set is only store uiniq value
allMarks = {98,94,97,95,76,86,76}
print(allMarks)
#  sets dont know which item is i which index

for mark in allMarks:
  print(mark)

# dictonary like object in javascript
newMark = {
  # keys & value
  "Maths" : 89,
  "Sci" : 97,
  "Soc" : 98
}
# print entire Dictionary
print(newMark)
# print value by key
print("Maths Mark",newMark["Maths"])
# add one more
newMark["Art"] = 78
print(newMark)
# rechaking got update in marks
newMark["Sci"] = 94
print(newMark)

