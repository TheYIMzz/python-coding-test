def is_valid(s):
    stack = list()

    for i in s:
        print(i)
        if i == "(":
            stack.append(")")
        elif i == "{":
            stack.append("}")
        elif i == "[":
            stack.append("]")
        elif not stack or stack.pop() != i:
            print('짝이 안맞는 괄호 발견 -> ', i)
            return False

    return True


print(is_valid(s='{(([]))[]}'))
print('===========')
print(is_valid(s='{(([}))[]}'))