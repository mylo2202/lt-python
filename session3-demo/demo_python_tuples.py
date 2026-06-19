# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
#   kernelspec:
#     display_name: Python 3
#     name: python3
# ---

# %% [markdown] id="5ZiY4EZEmg_k"
# # Tuples in Python Presentation

# %% [markdown] id="j_iz78VsmlqE"
# ## Examples

# %% [markdown] id="OZau9OwgkE1G"
# ### Introduction to Tuples
#
# Tuples are sequences that function much like lists, with elements indexed starting at zero.

# %% id="-gT-4BVwj2fA"
# Declaring tuples with parentheses
names = ('Glenn', 'Sally', 'Joseph')
print(names[2]) # Output: Joseph

# %% id="4cSxwkJSkUCW"
# Declaring tuples with integers
numbers = (1, 9, 2)
print(max(numbers)) # Output: 9

# %% id="GRmvGARPkVs7"
# Tuples are iterable just like lists
for val in numbers:
    print(val)

# %% [markdown] id="Nn2_H52-kZvT"
# ### Properties of Tuples
#
# The defining characteristic of a tuple is that it is immutable. Unlike lists, you cannot alter a tuple's contents once created, and they have far fewer built-in methods, making them more memory-efficient.

# %% id="vvFFE_WMkh0A"
# Immutability demo
x = [4, 5, 6]
x[2] = 7 # Works for lists
print(x)

y = (5, 4, 3)
# y[2] = 0 # This would cause a Traceback: 'tuple' object does not support item assignment

# %% id="SedItdTAkwAb"
# Comparison of available methods
l = list()
print(dir(l)) # Shows many methods: append, sort, reverse, etc.

t = tuple()
print(dir(t)) # Only shows: count, index

# %% [markdown] id="nVwLETmqkzmJ"
# ### Tuple Unpacking, Assignment and Comparison
#
# Tuples can be used on the left-hand side of an assignment statement to "unpack" values into multiple variables at once. Tuples are also comparable, which is useful for sorting, it compares the first item, then the second, and so on.

# %% id="fk7SkKQZk4Nt"
# Tuple unpacking
(x, y) = (4, 'fred')
print(y) # Output: 'fred'

# Parentheses can often be omitted
a, b = (99, 98)
print(a) # Output: 99

# %% id="MFVCPtPKZ31G"
a,b,c = 99, 98, 100
print(a, b, c)
print(a)

# %% id="ZIQrRD34asAJ"
(5,1 ,2) < (5, 1, 2, 0)

# %% id="1cpMU_QdlAuG"
# Tuple comparison
print((0, 1, 2) < (5, 1, 2))      # True
print(('Jones', 'Sally') < ('Jones', 'Sam')) # True

# %% [markdown] id="1dTqIFCclDjI"
# ### Tuples in Dictionaries and Data Manipulation
#
# Use the `items()` method to get a list of tuples from a dictionary. You can also sort data by values instead of keys.

# %% id="hvNUIUGwlUC-"
# Converting a dictionary to a list of tuples
d = {'a': 10, 'b': 1, 'c': 22}
tups = d.items()
print(tups) # Output: [('a', 10), ('b', 1), ('c', 22)]

# Sorting a dictionary by key
for k, v in sorted(d.items()):
    print(k, v)

# Sorting by VALUE instead of key
# We create a list of (value, key) tuples
tmp = list()
for k, v in d.items():
    tmp.append((v, k))

# Now we can sort by the value (the first element in our new tuples)
tmp.sort(reverse=True)
print(tmp) # Output: [(22, 'c'), (10, 'a'), (1, 'b')]

# %% id="lcKlH3u9leNh"
# Short version using list comprehension
print(sorted([(v, k) for k, v in d.items()]))

# %% [markdown] id="ijLKU-B4mpiU"
# ## Demo

# %% [markdown] id="K1ygHWEcnkIv"
# ### Real-life Example: Student Records Management with Tuples
#
# Problem: We need to store and process student formation,
# where each student has an ID, name, and a grade.
# It's important that individual student records, once eated,
# are not accidentally modified, but we might want to rt them
# or extract specific pieces of information efficiently.

# %% id="y688cYaKmvXV"
# Each student record will be a tuple: (ID, Name, Grade)
student_records = [
    (101, "Alice", 85),
    (102, "Bob", 92),
    (103, "Charlie", 78),
    (104, "David", 92),
    (105, "Eve", 88)
]

print("First student record:", student_records[0])
print("Name of the second student:", student_records[1][1]) # Accessing Bob's name

print("\nIterating through student records:")
for record in student_records:
    print(f"ID: {record[0]}, Name: {record[1]}, Grade: {record[2]}")

# %% id="nE9fCmWZn8MS"
# Tuples are immutable. Once a record is set, its individual components cannot be changed.
# This helps maintain data integrity for student records.
first_record = student_records[0]
print("Original first record:", first_record)

# Uncommenting the line below would raise a TypeError:
# first_record[2] = 90
# print("Attempting to change grade directly:", first_record)
print("Attempting to change a grade directly (e.g., first_record[2] = 90) would cause a TypeError, safeguarding data integrity.")

# If a record needs to be 'updated', a new tuple is created.
# Note: A list *containing* tuples can have its elements reassigned,
# but the tuples themselves remain immutable.
updated_first_record = (first_record[0], first_record[1], 90)
student_records[0] = updated_first_record
print("Updated first record (by creating a new tuple and reassigning in the list):", student_records[0])

# %% id="pIlvO8N_n3kz"
print("Unpacking student records for easier access:")
for student_id, name, grade in student_records:
    print(f"Student ID: {student_id}, Name: {name}, Grade: {grade}")

# Example of swapping variables using tuple assignment
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# %% id="k9zXUytPnz4q"
# Using student IDs as keys and the full record tuples as values in a dictionary
student_dict = {record[0]: record for record in student_records}
print("Student dictionary (ID -> full record):", student_dict)

print("\nSorting students by grade (highest first):")
# Create a list of (grade, student_id, name) tuples for sorting
# This allows sorting primarily by grade, and secondarily by ID/name if grades are the same.
sorted_by_grade = sorted([(grade, student_id, name) for student_id, name, grade in student_records], reverse=True)
for grade, student_id, name in sorted_by_grade:
    print(f"Grade: {grade}, Name: {name}, ID: {student_id}")

print("\nSorting students by name (alphabetical):")
# Create a list of (name, student_id, grade) tuples for sorting
sorted_by_name = sorted([(name, student_id, grade) for student_id, name, grade in student_records])
for name, student_id, grade in sorted_by_name:
    print(f"Name: {name}, ID: {student_id}, Grade: {grade}")

# %% id="FsmdlIpsY36e"
x = (1, 2, 2, 3, 2)
# print(x.count(2))
print(x.index(2))

# %% id="9yNDH0YCZC5P"
fhand = open('romeo.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

lst = []
for key, val in counts.items():
  newtup = (val, key)
  lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)

# %% id="ztBV7h9lfglo"
# =====================================================================
# 1. TUPLE: Lưu 4 đầu điểm cố định (Không đổi trong suốt học kỳ)
# =====================================================================
cac_dau_diem = ("Exercise 1", "Exercise 2", "Exercise 3", "Final Project")


# =====================================================================
# 2. LIST: Lưu danh sách 6 nhóm (Có thứ tự từ Nhóm 1 đến Nhóm 6)
# =====================================================================
danh_sach_nhom = ["Nhóm 1", "Nhóm 2", "Nhóm 3", "Nhóm 4", "Nhóm 5", "Nhóm 6"]


# =====================================================================
# 3. DICTIONARY: Lưu điểm Final Project của từng nhóm (Tra cứu bằng tên nhóm)
# =====================================================================
diem_final = {
    "Nhóm 1": 9.0,
    "Nhóm 2": 7.5,
    "Nhóm 3": 9.5,
    "Nhóm 4": 8.0,
    "Nhóm 5": 8.5,
    "Nhóm 6": 8.2
}


# --- DEMO TÍNH CHẤT ---

# 1. LIST: Có thể thêm nhóm mới nếu lớp đông lên
danh_sach_nhom.append("Nhóm 7")

# 2. DICTIONARY: Sửa điểm của Nhóm 2 sau khi chấm phúc khảo
diem_final["Nhóm 2"] = 8.0

# 3. TUPLE: Thử thêm đầu điểm "Exercise 4" -> Báo lỗi ngay (Cấm sửa)
# cac_dau_diem.append("Exercise 4")


# --- IN RA KẾT QUẢ ---
print(f"Các đầu điểm bắt buộc: {cac_dau_diem}")
print(f"Tổng số nhóm hiện tại: {len(danh_sach_nhom)} nhóm.")
print(f"Điểm Final Project của Nhóm 2 sau phúc khảo là: {diem_final['Nhóm 2']}")
