input_count = int(input())
input_list = []
for i in range(input_count):
    input_list.append(int(input()))

input_list.sort(reverse=True)

for i in range(input_count):
    print(input_list[i], end=" ")

print()
