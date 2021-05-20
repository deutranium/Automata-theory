import json
import sys


INPT_FILE = sys.argv[1]
OTPT_FILE = sys.argv[2]

with open(INPT_FILE, "r") as f:
    INPT = json.load(f)

blah = INPT["transition_matrix"].copy()


def yeet_state(s, b):
    innnnn = [e for e in b if e[2] == s]
    ouuttt = [e for e in b if e[0] == s]

    for e in innnnn + ouuttt:
        b.remove(e)
    for ie in innnnn:
        for oe in ouuttt:
            e = [ie[0], (ie[1] + oe[1]), oe[2]]
            b.append(e)

    ancient = []
    lgt = len(b)

    for i in range(lgt):
        for j in range(i+1, lgt):
            if(b[i][0] == b[j][0]) and (b[i][2] == b[j][2]):
                ne = [
                    b[i][0], 
                    "(" + b[i][1] + "+" + b[j][1] + ")",
                    b[i][2]
                ]
                b.remove(b[j])
                b.append(ne)
                ancient.append(b[i])
                i += 1
    for oldie in ancient:
        if oldie in b:
            b.remove(oldie)

    loopies = []
    for e in b[:]:
        if e[0] == e[2]:
            b.remove(e)
            loopies.append(e)
    for l in loopies:
        for idx, e in enumerate(b):
            if(l[0] == e[0]):
                b[i][1] = "(" + l[1] + ")*" +  str(e[1])

    return b
    

# dead stuff
aiyo = {}
for s in INPT["states"]:
    aiyo.update({s: False})
for ss in INPT["start_states"]:
    aiyo[ss] = True
for e in blah:
    aiyo[e[2]] = True

blah = [e for e in blah if aiyo[e[0]]]
valid_s = [s for s in aiyo if aiyo[s]]


# start, end shiz
start_s = "Qs"
final_s = "Qf"

for s in INPT["start_states"]:
    blah.append([start_s, '$', s])

for f in INPT["final_states"]:
    blah.append([f, "$", final_s])

ancient = []
lgt = len(blah)

for i in range(lgt):
    for j in range(i+1, lgt):
        if(blah[i][0] == blah[j][0]) and (blah[i][2] == blah[j][2]):
            ne = [
                blah[i][0], 
                "(" + blah[i][1] + "+" + blah[j][1] + ")",
                blah[i][2]
            ]
            blah.remove(blah[j])
            blah.append(ne)
            ancient.append(blah[i])
            i += 1
for oldie in ancient:
    if oldie in blah:
        blah.remove(oldie)

# just get over already smh

# self loopn't

loopies = []
for e in blah[:]:
    if e[0] == e[2]:
        blah.remove(e)
        loopies.append(e)
for l in loopies:
    for idx, e in enumerate(blah):
        if(l[0] == e[0]):
            blah[idx][1] = "(" + l[1] + ")*" +  str(e[1])

for s in valid_s:
    blah = yeet_state(s, blah)

regex = {
    "regex": blah[0][1]
}

with open(OTPT_FILE, "w") as f:
    json.dump(regex, f, indent=4)


