# 인원 수, 인원 별 공포도(최소 파티원 수)
#N = int(input())
#list = list(map(int, input().split()))
N = 5
list = [2, 3, 1, 2, 2]

# 최대의 그룹 수를 만들어야 함
# 공포도가 낮은 사람일 수록, 더 적은 인원수로 구성 가능 (널널함)
# 공포도가 높은 사람일 수록, 그룹으로 묶는 데 더 많은 인원 필요 (빡빡함)
# -> 공포도가 높은 사람부터 그룹에 배치한다.

# 높은 사람부터 배치하기 위해, 내림차순 정렬 필요
list.sort(reverse=True)
groups = []

# 제일 공포도가 높은 사람을 빼서, 해당 사람의 공포도만큼 리스트에서 pop하여 추가한다.
# 뒤에는 어차피 더 널널한 사람밖에 없기 때문에, 공포도 검사할 필요가 X
for val in list:
    group = []
    for i in range(val):
        group.append(list.pop())
    groups.append(group)

print(len(groups))