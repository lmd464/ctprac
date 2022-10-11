# 0 구역의 수와, 1 구역의 수를 확인하여 적은 쪽을 뒤집는다.
# 구역의 수가 더 적은 곳을 구하면 됨

#input_str = input()
input_str = '0001100'
input_list = list(input_str)


# 연속된 숫자들 제거하여, 새로운 리스트에 추가
reduced = []
reduced.append(input_list.pop())

for ch in input_list:
    if ch != reduced[len(reduced) - 1]:
        reduced.append(ch)


# 0과 1이 번갈아서 한번씩 나오는 리스트에서, 0 개수와 1 개수를 찾음
# 더 개수가 적은 것을 고르면 됨
freq_0 = reduced.count('0')
freq_1 = reduced.count('1')
res = freq_0 if freq_0 < freq_1 else freq_1

print(res)