import json
import sys


INPT_FILE = sys.argv[1]
OTPT_FILE = sys.argv[2]

with open(INPT_FILE, "r") as f:
    INPT = json.load(f)


states = INPT["states"]
transition_matrix = INPT["transition_matrix"]
final_states = INPT["final_states"]

def powerset(states):
    lgt = len(states)
    new_states = []
    for i in range(1 << lgt):
        new_states.append([states[j] for j in range(lgt) if (i & (1 << j))])
    return new_states

def dfa_final(states):
    p_set = powerset(INPT["states"])
    ret = []
    for s in states:
        ret += [p for p in p_set if (s in p) and (p not in ret)]
    
    return ret


DFA = {
    'states': powerset(INPT["states"]),
    'letters': INPT["letters"],
    'start_states': INPT["start_states"],
    'final_states': dfa_final(INPT["final_states"])
}


def get_state(s, tm, l):
    f = set()
    for e in tm:
        if(e[0] in s and e[1] == l):
            f.add(e[2])
    if(not f):
        return []
    else:
        return list(f)


dfa_transition_func = []

for s in DFA["states"]:
    for l in DFA["letters"]:
        new_state = get_state(s, INPT["transition_matrix"], l)
        dfa_transition_func.append([s, l, new_state])

DFA['transition_matrix'] = dfa_transition_func


with open(OTPT_FILE, "w") as f:
    json.dump(DFA, f, indent=4)

