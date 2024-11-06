tuples = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ("", ""), ()]
tup = []
for i in tuples:
    if i:
        tup.append(i)

print(tup)
