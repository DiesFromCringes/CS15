def sum (x, y):
    return x + y

sum_lambda = lambda x, y : x + y
print(sum_lambda(10, 2))

students = (
    ('A', 12),
    ('E', 15),
    ('B', 13),
    ('D', 14),
    ('C', 11),
    ('F', 16),
    )
sorted_students =sorted(students)
print(sorted_students)

students_name = ['A', 'B', 'C', 'D', 'E', 'F']
students_name.sort()
students_name.sort(reverse=True)
print(students_name)

age = lambda item : item[1]
sorted_ages = sorted(students, key=age)
print(sorted_ages)

store_dollars = [("apple", 1), ("jacket", 50), ("paints", 40), ("skirt", 80)]
store_euros = lít(map(change_euros2, store dollars))