# 작은 수를 모아 최대한 큰 수와 곱하는게 최대한의 수를 만들 수 있을 것 -> 오름차순으로 리스트 정렬
# 각 단계마다 *, + 중 뭐가 좋은 지는 각각 다름 -> 직접 계산해보고 비교, 결정

#input_string = input()
input_string = "02984"
num_list = sorted(list(map(int, list(input_string))))


# 첫 항은 미리 빼두고 나머지를 탐색
result = num_list.pop()
for num in num_list:

    # 둘다 계산해보고 큰 쪽을 저장
    t1 = result + num
    t2 = result * num
    result = t1 if t1 > t2 else t2

print(result)
    
    
    
