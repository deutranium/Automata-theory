import json
import sys


INPT_FILE = sys.argv[1]
OTPT_FILE = sys.argv[2]

with open(INPT_FILE, "r") as f:
    INPT = json.load(f)


blem = [set(), set()]

for s in INPT["states"]:
    if s in INPT["final_states"]:
        blem[0].add(s)
    else:
        blem[1].add(s)

def i_want_cats(s, p):
    for i, elem in enumerate(p):
        if s in elem:
            return i
    return -1

def i_wanna_slep(s1, s2, p, tf, ls):
    for l in ls:
        i1 = -1
        i2 = -1
        for e in tf:
            if e[0] == s1 and e[1] == l:
                i1 = i_want_cats(e[2], p)
            if e[0] == s2 and e[1] == l:
                i2 = i_want_cats(e[2], p)
        if i1 != i2:
            return 0

    return 1

f = 0

while(not f):
    f = 1
    black_catto = []
    for p in blem:
        for s in p:
            if(i_want_cats(s, black_catto) == -1):
                new_s = {s}

                for s2 in p:
                    if(i_want_cats(s2, black_catto) == -1):
                        if(i_wanna_slep(s, s2, blem, INPT["transition_matrix"], INPT["letters"])):
                            new_s.add(s2)
                black_catto.append(new_s)
    for i in black_catto:
        if i not in blem:
            f = 0
    blem = black_catto

white_catto = []

for p in blem:
    cur_mlem = list(p)[0]
    for e in INPT["transition_matrix"]:
        if(e[0] == cur_mlem):
            white_catto.append([p, e[1], blem[i_want_cats(e[2], blem)]])

hell_start = []
hell_end = []

for p in blem:
    for s in p:
        if s in INPT["start_states"] and p not in hell_start:
            hell_start.append(p)
        if s in INPT["final_states"] and p not in hell_end:
            hell_end.append(p)

blem2 = [list(i) for i in blem]

OTPT = {
    "states": blem2,
    "letters": INPT["letters"],
    "transition_matrix": [
        [list(i[0]), i[1], list(i[2])] for i in white_catto
    ],
    "start_states" : [list(i) for i in hell_start],
    "final_states" : [list(i) for i in hell_end]
}

with open(OTPT_FILE, "w") as f:
    json.dump(OTPT, f, indent=4)