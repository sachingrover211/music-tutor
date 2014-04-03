__author__ = 'Jitter'

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append('hello')
strings.append("world")
second_name = names[1] #Lists start at zero


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
