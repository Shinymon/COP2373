# Function name: avg
# Function documentation:
# Help on function avg in module __main__:
#
# avg(a_list)
#     This function finds the average val in a list.

# Function using *args to count and print values
def my_var_func(*args):
    print('The number of args is', len(args))
    for item in args:
        print(item)

# Function using *args and a regular argument
def avg(units, *args):
    print(sum(args)/len(args), units)

# Function using **kwargs to print key-value pairs
def pr_named_vals(**kwargs):
    for k in kwargs:
        print(k, ':', kwargs[k])

# Sample usage
print(">>> my_var_func(10, 20, 30, 40)")
my_var_func(10, 20, 30, 40)

print("\n>>> avg('inches', 11, 22, 33)")
avg('inches', 11, 22, 33)

print("\n>>> pr_named_vals(a=10, b=20, c=30)")
pr_named_vals(a=10, b=20, c=30)

# Demonstration of argument unpacking
ls = [1, 2, 3]
print("\n>>> print(*ls)")
print(*ls)  # Print unpacked version: 1 2 3

print("\n>>> print(ls)")
print(ls)   # Print packed ordinary list: [1, 2, 3]

# Print formatting with end and sep
print("\n>>> print(10, 20, 30, end='.', sep=',')")
print(10, 20, 30, end='.', sep=',')