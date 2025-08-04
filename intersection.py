def intersection(list1, list2):
    # Convert both lists to sets and find the intersection
    common_elements = set(list1) & set(list2)
    print(common_elements)

n, m = map(int, input().split())
list1 = []
list2 = []

for _ in range(n):
    list1.append(int(input()))
for _ in range(m):
    list2.append(int(input()))

intersection(list1, list2)
