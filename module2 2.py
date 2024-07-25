first=13
second=13
third=30
print(first)
print(second)
print(third)
if first==second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)