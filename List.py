#q1
fruits = ("apple", "banana", "cherry", "date")
print(fruits[0])
print(fruits[3])

#q2
num_tuple = (1, 2, 3, 4, 5)
a, b, *rest = num_tuple
print(a)
print(b)
print(rest)

#q3
fruits[1] = "blueberry"
# the code above will raise an error because tuples are immutable

#q4
colors = {"red", "green", "blue", "yellow"}
colors.add("purple")

#q5
primary_colors = {"red", "green", "blue"}
intersection_set = colors & primary_colors #intersection
union_set = colors ^ primary_colors #union
difference_set = colors - primary_colors #difference
print(intersection_set)
print(union_set)
print(difference_set)

#q6
print({"green"}.issubset(primary_colors))
print({"orange"}.issuperset(primary_colors))


#q7
dict = {"Alice": 25, "Bob": 27, "Charlie": 30, "Diana": 33}
print(dict["Bob"])

#q8
dict["Eve"] = 88
dict["Alice"] = 95
del dict["Charlie"]
print(dict)

#q9
for name, grade in dict.items():
    print(f"Student: {name}, Grade: {grade}")
