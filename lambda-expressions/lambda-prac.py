nums = [1, 2, 3]
ans = [lambda args=x: args ** 2 for x in nums]

print(ans)
for i in ans:
    print(i())



#Evev-Odd

ans = lambda x:"Even" if x%2 == 0 else "Odd"
print(ans(4))

