from Stack import Stack;

'''
Balanced example: {[]}

{}{}

[ ]

{ }

Non-Balanced example: (()

Non-Balanced example: ))

'''


def is_match(p1, p2):
    if p1 == "{" and p2 == "}":
        return True
    else:
        return False


def ValidateBalance(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()

                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty and is_balanced:
        return True
    else:
        return False


if __name__ == '__main__':
    print(ValidateBalance("{{}}"))
