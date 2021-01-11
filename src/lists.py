a = [11, 22, 33, 44]

for elem in a:
    print(elem)

print()

for i, elem in enumerate(a):
    print(f"Index {i} holds the value {elem}")

print()

for i in range(len(a)):
    elem = a[i]
    print(f"Index {i} holds the value {elem}")