s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1 - s2)
print(s2 - s1)

print(s2.issubset(s1))
print({1,45}.issubset(s1))
