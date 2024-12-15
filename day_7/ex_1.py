from collections import deque

sample_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

equations = sample_input.split("\n")

# Multiply as first operation
# Multiply the first 2 numbers. If result > target, then do addition instead
# A stack to trace our ops.
# Work out the algorithm:

# 81 40 27:
# stack.add("x") -> 81 x 40 = 3240
# check : if 3240 < 3267
# stack.add("x") -> 2376 x 27
# stack.pop("x") -> 3240 + 27
# stack.add("+")
# stack = ["x", "+"] not allowed? -> Not possible. 
# stack.pop()
# stack.pop ["+", "x"]

# add state to visiited

def create_state_string(stack):
    return ''.join(k for k in stack)

def compute(input, stack):
    result = input[0]
    for i, op in enumerate(stack):
        if op == "x":
            result *= input[i+1]
        if op == "+":
            result += input[i+1]
    return result

def find_eq(input, result):

    traversed = set()
    stack = deque()
    stack.append["x"]
    traversed.add(create_state_string(stack))
    output = compute(input, stack)
    # check if we get the result
    if len(stack) == len(input) and output == result:
        return True 
    if 






    




# ["x", "x", "x", ...]

# Need: a stack of operations



if __name__ =="__main__":
    stack = deque()
    stack.append("x")
    stack.append("x")
    stack.append("y")
    print(create_state_string(stack))