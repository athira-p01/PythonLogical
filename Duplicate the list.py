lis = [1,2,2,3,3,4,5,5]
set1 = set(lis)
if len(lis) == len(set1):
   print("No duplicates in the list")
else:
   print("Duplicates in the list")



lis = [1,2,2,3,3,4,5,5,5]
set2 = set()
l2 = set()
for i in lis:
   if i in set2:
      l2.add(i)
   else:
      set2.add(i)
print(l2)

