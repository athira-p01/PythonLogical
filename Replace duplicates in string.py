text = "Gfg is best. Gfg also has Classes now. Classes help understand better."
words = text.split()
result = []
new = {}
for i in words:
    if i in new:
        if i == "Gfg":
            result.append("It")
        else:
            result.append("They")
    else:
        result.append(i)
        new[i] = True

output = ' '.join(result)
print(output)
