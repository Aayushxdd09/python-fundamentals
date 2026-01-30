marks = {
"Harry": 92,
"Shubham": 67,
"Aryan": 33
}

print(marks)
print(marks.items())
print(marks.keys())
print(marks.values())


marks.update({"Harry": 95, "Manav": 77})
print(marks)


### IMP NOTE - Works same but "get" gives none if not in the dict and second one gives error
print(marks.get("Harry2"))
print(marks["Harry2"])


