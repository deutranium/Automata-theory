## Automata Theory
[![forthebadge](https://forthebadge.com/images/badges/fixed-bugs.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)](https://forthebadge.com)

[[Link to the YouTube Demo Video]](https://youtu.be/VMaDY00yHgY)

### How to run

``` bash
python3 gx.py <path to input json> <path to output json>
```
Here, `x` can be anything out of `{1, 2, 3, 4}`

### 1. Regex -> NFA
- Add the concatenation oprator `.` at the required places
- Convert the given expression to a **postfix** expression for easier processing -- Uses **Shunting Yard Algorithm**
- Use this postfix expression obtained to create NFA using **Thompson's Contruction**
- During this process, we keep on splitting the regex till each edge of our NFA represents only one character -- addition of these different edges is done in accordance with the operator (like union, concatenation etc.)

### 2. NFA -> DFA
- **States:** Powerset of the states of NFA
- **Letters:** Same as that of input NFA
- **Start States:** Single valued sets containing only the input NFA's start states
- **Final States:** Sets containing any of the final states of input NFA
- **Transition Function:** Per combination of DFA state and a letter, we find the results of transition from the given NFA. The union of the above mentioned transitions when done for all the states and letter combinations, gives us the final transition function for the DFA

### 3. DFA -> regex
- Removing the unnecessary dead states
- Create new start and final states which are connected usnig epsilon edges with DFA start states and DFA final states respectively
- Fix parallel edges -- where the start state, letter and the final state all are the same
- Remove any self loops if there
- Eliminate states while getting their regex. For example, if there are transitions `Q1 -a-> Q2` and `Q2 -b-> Q3`, it can be converted to `Q1 -a.b-> Q3` and the regex of the same would be `a.b` where `.` is the concatenation operator
- Doing this elimination for all the states will eventually give us the final regex which represents the input DFA

### DFA minimization
- Removal of dead states
- Use the equivalence theorem and separate the states into final and non-final states
- This is followed by iteration and grouping of equivalent states and is done till the two consecutive partitions are identical
- These states obtained in the end represent the **states** of our **minimized DFA**
- **Letters** would be same as that of the input DFA
- Similarly, the **start states** and **end states** are also same as that of the input
- For the transition function, we can look at the following example to uderstand the process well
    - Say the `start_states` are something like `[Q1, Q2, Q3], [Q4, Q5], [Q6, Q7]` and let one of the transitions be `Q2 -a-> Q6`. From this, we can get the new transition of the minimized DFA as `[Q1, Q2, Q3] -a-> [Q6, Q7]`
    - The above step is done for all the states to obtain the final transition matrix



-- Thank you --
