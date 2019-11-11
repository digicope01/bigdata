# python_basic.py

a = 10
b = 20
c = a + b
print(c)


#  단축키
#
# (1) Ctrl + / : 주석문 설정 / 해제
# (2) Tab : 들여쓰기 (Indent)
# (3) Shift + Tab : 들여쓰기 해제(Unindent)

# (4) Shift + F10 : Run (기존 수행했던 소스코드를 실행)
# (5) Ctrl + Shift + F10 : Run (새로 작성된 소스코드를 실행)
#                    --> 오른쪽 마우스 버튼을 클릭하여 실행
# (6) F8 : 디버거 모드에서 Step Over

a = 30
b = 80
c = eval('a + b')
print(c)

# 표준 입력 : input()
def test_input():
    a = int(input('첫번째 숫자는:'))
    b = int(input('두번째 숫자는:'))
    c = a * b
    print(c)

# test_input()
#
# input()

print( '{0:<10}{1:5.2f}'.format( 'apple', 7.77 ) )
print( '{0:>10}{1:5.2f}'.format( 'apple', 7.77 ) )
print( '{0:=^10}'.format( 'hi' ) )

print( '{0:=^10}'.format( '1번' ) )
print('-'*50)