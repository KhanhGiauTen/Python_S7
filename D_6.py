# 1. Create a tuple of numbers and print one item
numbers = (10, 20, 30, 40, 50)
print("One item from the tuple:", numbers[2])

# 2. Unpack a tuple into several variables
t = (1, 2, 3)
a, b, c = t
print("Unpacked values:", a, b, c)

# 3. Add an item to a tuple (tuples are immutable, so create a new one)
t = (1, 2, 3)
t = t + (4,)
print("Updated tuple:", t)

# 4. Find the index of an item in a tuple
t = (5, 10, 15, 20)
index = t.index(15)
print("Index of 15:", index)

# 5. Find the repeated items of a tuple
t = (1, 2, 3, 2, 4, 1, 5)
repeated = set([item for item in t if t.count(item) > 1])
print("Repeated items:", repeated)


# 1. Find max and min values
s = {4, 9, 1, 23, 7}
print("Max:", max(s))
print("Min:", min(s))

# 2. Check if a value is in a set
value = 10
print(f"{value} is in set? {value in s}")

# 3. Check if two sets have no common elements
a = {1, 2, 3}
b = {4, 5, 6}
print("Disjoint sets?", a.isdisjoint(b))

# 4. Unique words and frequency from a list of strings
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
unique_words = set(words)
frequency = {word: words.count(word) for word in unique_words}
print("Unique words:", unique_words)
print("Frequency:", frequency)

# 5. Find missing numbers in both directions between two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
missing_in_2 = set1 - set2
missing_in_1 = set2 - set1
print("Missing in set2:", missing_in_2)
print("Missing in set1:", missing_in_1)

# 1. Convert two lists into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print("Dictionary:", my_dict)

# 2. Merge two dictionaries
dict1 = {'x': 1, 'y': 2}
dict2 = {'z': 3}
merged = {**dict1, **dict2}
print("Merged dictionary:", merged)

# 3. Print value of key ‘history’
sample = {
    "name": "John",
    "subjects": {
        "math": 90,
        "history": 85
    }
}
print("History score:", sample["subjects"]["history"])

# 4. Initialize dictionary with default values
keys = ['id1', 'id2']
default_value = {'designation': 'Developer', 'salary': 8000}
new_dict = {key: default_value.copy() for key in keys}
print("Initialized dict:", new_dict)

# 5. Create dictionary by extracting keys
original = {'a': 1, 'b': 2, 'c': 3}
selected_keys = ['a', 'c']
extracted = {k: original[k] for k in selected_keys}
print("Extracted dict:", extracted)

# 6. Delete list of keys
keys_to_delete = ['b', 'c']
for key in keys_to_delete:
    original.pop(key, None)
print("After deletion:", original)

# 7. Check if a value exists
value_exists = 1 in original.values()
print("Value 1 exists?", value_exists)

# 8. Rename key
d = {'old_key': 10}
d['new_key'] = d.pop('old_key')
print("Renamed dict:", d)

# 9. Get key of minimum value
scores = {'a': 10, 'b': 5, 'c': 20}
min_key = min(scores, key=scores.get)
print("Key with min value:", min_key)

# 10. Change value of nested key
nested = {'emp1': {'name': 'John', 'salary': 5000}}
nested['emp1']['salary'] = 5500
print("Updated nested dict:", nested)

# 11. Count character frequency in a paragraph
paragraph = "hello world"
freq = {}
for ch in paragraph:
    if ch != ' ':
        freq[ch] = freq.get(ch, 0) + 1
print("Character frequency:", freq)

# 12. Dict of primes < N
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

N = 20
prime_dict = {i+1: p for i, p in enumerate([x for x in range(N) if is_prime(x)])}
print("Prime dictionary:", prime_dict)

# 13. Restructure company data
employees = {
    101: {"name": "Alice", "dept": "HR", "salary": 5000},
    102: {"name": "Bob", "dept": "IT", "salary": 6000},
    103: {"name": "Charlie", "dept": "HR", "salary": 5200},
    104: {"name": "David", "dept": "IT", "salary": 6100}
}

dept_employees = {}
for emp_id, info in employees.items():
    dept = info["dept"]
    if dept not in dept_employees:
        dept_employees[dept] = []
    dept_employees[dept].append({"name": info["name"], "salary": info["salary"]})

print("Department-wise employee data:")
for dept, emp_list in dept_employees.items():
    print(dept, ":", emp_list)

