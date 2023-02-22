import sys

# 학생들이 작성한 코드 파일 이름
student_code_filename = sys.argv[1]

# 학생들이 작성한 코드를 실행하고, 변수 x의 값을 확인
with open(student_code_filename) as f:
    code = compile(f.read(), student_code_filename, 'exec')
    exec(code, globals())
    x = globals().get('x')

# x가 23이면 100점, 아니면 0점 부여
if x == 23:
    print('100')
else:
    print('0')
