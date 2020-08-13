"""
형변환
"""

# 암시적 형변환 (implicit casting)
num_int = 3
num_float = 3.14
num_new = num_int + num_float
print("type of `num_int` :", type(num_int))
print("type of `num_float` :", type(num_float))
print("type of `num_new` :", type(num_new))

# str -> int는 암시적으로 불가능.
num_int = 3
num_str = "6"
num_new = num_int + num_str
print("type of `num_int` :", type(num_int))
print("type of `num_str` :", type(num_str))
print("type of `num_new` :", type(num_new))

# 명시적 형변환 (explicit casting)
num_int = 3
num_str = "6"
num_str2 = int(num_str)
num_new = num_int + num_str2
print("type of `num_int` :", type(num_int))
print("type of `num_str` :", type(num_str))
print("type of `num_str2` :", type(num_str2))
print("type of `num_new` :", type(num_new))

"""
list, tuple, set, dict
"""

# list 자료형은 여러개의 데이터를 가지고 있는 배열 자료형입니다. 배열은 같은 타입만 가지고 있지 않아도 됩니다.
# 배열의 각 요소에는 인덱스(번호) 가 붙으며, 배열의 각 요소에 접근할 때는 인덱스를 사용해 접근합니다.
# 배열의 인덱스는 0부터 시작하며, (배열의 길이-1) 까지 존재합니다.
array = [0, 1, "2", True, "4", 5.0]
print(array)
print(type(array))
print(array[2], array[3])

# list 자료형은 선언 이후에도 내부 데이터를 변경할 수 있습니다.
array[2] = 4
print(array[2])

# list 객체는 insert 메소드를 통해 원하는 위치에 데이터을 추가할 수도 있습니다.
array.insert(1, "6")

# list 객체는 append 메소드를 통해 가장 마지막에 새 데이터를 추가할 수 있습니다.
array.append(7)

# tuple 자료형은 list와 마찬가지로, 여러개의 데이터를 타입과 무관하게 저장할 수 있습니다.
# 그러나, list 자료형은 생성 이후에도 내부에 저장된 데이터들을 변경할 수 있지만, tuple은 선언할 때 저장한 데이터들을 이후에 변경할 수 없습니다.
# 프로그래밍 용어로는, list는 mutable(변경 가능) 하고 tuple은 immutable(변경 불가능) 하다고 말합니다.
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple, type(my_tuple))
print(my_tuple[2])
my_tuple[2] = 7

# set 자료형은 수학에서 배우는 `집합` 과 같은 자료형입니다.
A = {1, 2, 3, 4, 5}
# set 자료형은 데이터의 중복이 허용되지 않습니다.
B = set([3, 4, 5, 6, 6, 7, 7, 7, 8])
print(A, B)
print(type(A), type(B))
# set 자료형은 앞서 배웠던 list, tuple과는 다르게 내부의 데이터들이 순서를 가지지 않아 인덱싱을 사용할 수 없습니다.
print(A[0])

# set 자료형은 집합의 연산들을 사용할 수 있습니다.
# & 기호 혹은 intersection() 메소드를 사용해 두 집합의 교집합을 구할 수 있습니다.
intersection = A & B
print(intersection)
print(type(intersection))
print(A.intersection(B), B.intersection(A))
# | 기호 혹은 union() 메소드를 사용해 두 집합의 합집합을 계산할 수 있습니다.
union = A | B
print(union)
print(type(union))
print(A.union(B), B.union(A))
# - 기호 혹은 difference() 메소드를 사용해 두 집합의 차집합을 계산할 수 있습니다.
A_diff_B = A - B
B_diff_A = B.difference(A)
print(A_diff_B, type(A_diff_B))
print(B_diff_A, type(B_diff_A))
# set 자료형에 새 데이터를 추가하려면, add() 메소드를 사용할 수 있습니다.
A.add(6)
print(A)
# set 자료형의 여러개의 새 데이터를 추가하려면, update() 메소드를 사용할 수 있습니다.
A.update([7, 8, 9, 10])
print(A)


# dict 자료형은 키:값으로 데이터를 저장하는 딕셔너리 자료형입니다. 딕셔너리 자료형은 키와 값에 해당하는 데이터를 모두 저장하고, 값을 가져오기 위해서 키로 접근합니다.
dictionary = {}