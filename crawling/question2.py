# %%
"""
Exercise 12. 기본 자료형
* 10, 2.2, "fun-coding" 각각을 변수에 넣고, 각 데이터 타입을 출력하세요.
"""

array = [10, 2.2, "fun-coding"]

for i in range(0, len(array)):
    result = array[i]

    print(result, type(result))

# %%
"""
### Exercise 14. 조건문
* 사용자로부터 두 개의 숫자를 입력 받은 후 큰 숫자를 화면에 출력하세요.
"""

result = lambda a, b: max(a, b)

print(result(3, 5))


# %%
"""
### Exercise 15. 조건문
* 사용자로부터 입력 받은 숫자가 홀수인지 짝수인지 출력하세요.
"""
num = int(input())

if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# %%
def temp(a, b, c):
    result = min(a, b, c)
    print('result', result)

temp(10, 2, 3)
# %%
