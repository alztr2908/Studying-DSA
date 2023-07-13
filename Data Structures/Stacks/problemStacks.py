def getReversedBracket(bracket):
    if bracket == "(":
        return ")"
    elif bracket == ")":
        return "("
    elif bracket == "[":
        return "]"
    elif bracket == "]":
        return "["
    elif bracket == "{":
        return "}"
    elif bracket == "}":
        return "{"

def isLeftBracket(bracket):
    if bracket == "(" or bracket == "[" or bracket == "{":
        return True

    return False

def matchBrackets(bracket_input):
    stack = []

    for bracket in bracket_input:
        rev = getReversedBracket(bracket)

        if isLeftBracket(bracket):
            stack.append(bracket)
        elif len(stack) == 0 or stack.pop() != rev:
            return False
    
    return len(stack) == 0

def main():
    bracket_input = input()
    print(matchBrackets(bracket_input))

if __name__ == '__main__':
    main()

"""
Code observations:
    - each function has a specific and separated task
"""