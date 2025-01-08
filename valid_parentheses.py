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
            return False

    return True


print(is_valid(s='{(([]))[]}'))