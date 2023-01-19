s = 0
for cont in range(1,501,2):
    if cont % 3 == 0:
        s += cont
        print(cont)
print(s)