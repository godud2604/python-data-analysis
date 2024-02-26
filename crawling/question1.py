# %%
interest = 0.087
print(format(interest, ".2f"))

# %%
"""
exercise 3. 출력
* 소수점 아래 첫 번쨰 자리까지만 표시되게 하세요.
"""

a = 3.1415
result = format(a, ".1f")

print('result', result)

# %%
"""
exercise 4. 형 변환
* 문자열 '720'를 정수형으로 변환하라. 정수 100을 문자열 '100'으로 변환하라.
"""

a = "720"
result = int(a)

b = 100
result2 = str(b)


print('result', result, type(result))
print('result2', result2, type(result2))
# %%
"""
Exercise 7.  입력과 출력
* 사용자로부터 두 개의 숫자를 입력받은 후 두 개의 숫자를 더한 값을 각각 출력하는 프로그램을 작성하세요.
"""

a = lambda a, b: a + b
print(a(2, 4))

