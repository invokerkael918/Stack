from Stack import Stack;
def removeOuterParentheses(s):
    '''
    Exmaple 1:
    Input: "(()())(())"
    Output: "()()()"

    Example 2:
    Input: "(()())(())(()(()))"
    Output: "()()()()(())"

    Example 3:
    Input: "()()"
    Output: ""
    '''
    index = 0
    subS = ""
    result = ""
    while index < len(s):
        subS = subS + s[index]
        if ValidateBalance(subS):
            subS = subS[1:-1]
            result+=subS
        index += 1

    return result


def is_match(p1,p2):
    if p1 =="(" and p2 == ")":
        return True
    else:
        return False


def ValidateBalance(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "(":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()

                if not is_match(top, paren):
                    is_balanced = False
        index +=1

    if s.is_empty and is_balanced:
        return True
    else:
        return False




if __name__ == '__main__':
    print(removeOuterParentheses("()()"))