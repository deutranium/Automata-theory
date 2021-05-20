import sys
import json

PRECEDENCE = {"*": 3, ".": 2, "+": 1}
OPERATORS = ["*", "+", "."]



INPT_FILE = sys.argv[1]
OTPT_FILE = sys.argv[2]

with open(INPT_FILE, "r") as f:
    INPT = json.load(f)


transition_matrix = []
flag = 1
state_count = 1
states = []
states.append(0)
states.append(1)
start_states = [0]
final_states = [1]
alphabets = []
final_matrix =[]




def infix_to_postfix(exp):
    opening_brackets = ["(", "[", "{"]
    closing_brackets = [")", "]", "}"]

    for idx in range(len(exp)):
        if (
            (exp[idx].isalnum() or exp[idx] == "*" or exp[idx] in closing_brackets)
            and (exp[idx+1].isalnum() or exp[idx + 1] in opening_brackets)
        ):
            exp = exp[: idx + 1] + "." + exp[idx + 1 :]
 
    shunt = []
    stack = []

    for ch in exp:
        if ch in OPERATORS:
            while stack:
                c2 = stack[-1]
                if c2 in opening_brackets or PRECEDENCE[c2] < PRECEDENCE[ch]:
                    break
                else:
                    stack.pop()
                    shunt.append(c2)
            stack.append(ch)
        elif ch in opening_brackets:
            stack.append(ch)
        elif ch in closing_brackets:
            while stack and stack[-1] not in opening_brackets:
                ch = stack.pop()
                shunt.append(ch)
            if stack[-1] in opening_brackets:
                stack.pop()
        else:
            shunt.append(ch)

    while stack:
        ch = stack.pop()
        shunt.append(ch)
    return ''.join(shunt)

def split(postfix):
    flag = 0
    last_ch = postfix[len(postfix)-1]

    if last_ch == "." or last_ch == "+":
        flag = 1

    i = len(postfix) - 1
    while(flag != 0):
        i -= 1
        if (postfix[i] == "." or postfix[i] == "+"):
            flag += 1
        elif (postfix[i].isalnum()):
            flag -= 1

    postfix = list(postfix)
    cur_op = postfix.pop()
    temp = ''.join(postfix)
    str1 = temp[0:i]
    str2 = temp[-(len(postfix) - i):]

    return ([str1, str2, cur_op])


postfix = infix_to_postfix(INPT["regex"])
transition_matrix = []
transition_matrix.append(['0', '1', postfix])


def check_splitted():
    for i in range(len(transition_matrix)):
        if(len(transition_matrix[i][2]) != 1):
            return False
    return True


while(not check_splitted()):
    temp_matrix = transition_matrix.copy()
    # print("Transition matrix: ", temp_matrix)
    for i in range(len(temp_matrix)):
        if(len(temp_matrix[i][2]) > 1):
            # print(temp_matrix[i][2], "////////")
            ret = split(temp_matrix[i][2])

            temp = temp_matrix[i]
            # print(ret, "........")
            transition_matrix.remove(temp_matrix[i])

            if(ret[2] == "+"):
                transition_matrix.append([temp[0], temp[1], ret[0]])
                transition_matrix.append([temp[0], temp[1], ret[1]])

            if(ret[2] == "."):
                state_count += 1
                states.append(state_count)
                transition_matrix.append([temp[0], state_count, ret[0]])
                transition_matrix.append([state_count, temp[1], ret[1]])

            if(ret[2] == "*"):
                state_count += 1
                states.append(state_count)
                state_count += 1
                states.append(state_count)
                transition_matrix.append([temp[0], state_count-1, '$'])
                transition_matrix.append([state_count, temp[1], '$'])
                transition_matrix.append([state_count-1, state_count, ret[0]])
                transition_matrix.append([state_count, state_count-1, '$'])
                transition_matrix.append([temp[0], temp[1], '$'])
                

for idx, val in enumerate(transition_matrix):
    if(val[2] not in alphabets):
        alphabets.append(val[2])
# print(transition_matrix)

for i in transition_matrix:
    final_matrix.append(['q' + str(i[0]), str(i[2]), 'q' + str(i[1])])


alphabets = [alphabet for alphabet in alphabets if alphabet != "$" ]

states = [('q' + str(state)) for state in states]
start_states = [('q' + str(state)) for state in start_states]
final_states = [('q' + str(state)) for state in final_states]

# print(final_matrix)

otpt = {
    'states': states,
    'letters': alphabets,
    'transition_matrix': final_matrix,
    "start_states" : start_states,
    "final_states" : final_states
}

with open(OTPT_FILE, "w") as f:
    json.dump(otpt, f, indent=4)
