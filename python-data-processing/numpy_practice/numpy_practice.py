import numpy as np # 수치 계산을 위한 핵심 라이브러리 로드
a = np.array([1, 2, 3]) # 1 차원 배열 생성
b = np.zeros((2, 3)) # 2x3 크기의 0 으로 채워진 배열
c = np.arange(0, 10, 2) # 0 부터 10 미만까지 2 간격으로 생성
d = np.linspace(0, 1, 5) # 0 부터 1 까지 5 개 균등 분할

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
