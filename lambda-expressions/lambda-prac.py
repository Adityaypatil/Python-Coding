nums = [1, 2, 3]
ans = [lambda args=x: args ** 2 for x in nums]

print(ans)
for i in ans:
    print(i())



#Evev-Odd

ans = lambda x:"Even" if x%2 == 0 else "Odd"
print(ans(4))

# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))

from functools import reduce

# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)