student_count = int(input())
student_list = []
for i in range(student_count):
    temp = input().split(" ")
    student = (temp[0], int(temp[1]))
    student_list.append(student)


# 정렬 기준 (key 함수) : 받은 데이터를 이용하여, 정렬할 값 기준을 반환
def sort_setting(data):
    return data[1]


# key 기준 정렬
student_list.sort(key=sort_setting)

# 출력
for student in student_list:
    print(student[0], end=" ")
print()
