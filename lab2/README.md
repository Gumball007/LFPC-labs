# Conversion of Nondeterministic Finite Automato to Deterministic Finite Automato
## Variant 5

## Tasks:

1. Convert NFA from your variant to DFA on paper, writing all transitions and drawing converted automato.

<img src="./lab-lfpc.png">

2. The output:

```
NFA table:
+----+--------------+-----+
|    | a            | b   |
+====+==============+=====+
| q0 | q1           | q0  |
+----+--------------+-----+
| q1 | ['q2', 'q3'] | nan |
+----+--------------+-----+
| q2 | q3           | q0  |
+----+--------------+-----+
| q3 | nan          | nan |
+----+--------------+-----+
Final state of NFA:  ['q3']

DFA is:  {'q0': {'a': 'q1', 'b': 'q0'}, 'q1': {'a': ['q2', 'q3']}, 'q2': {'a': 'q3', 'b': 'q0'}, 'q3': {}, 'q2q3': {'a': 'q3', 'b': 'q0'}}
DFA table:
+------+--------------+-----+
|      | a            | b   |
+======+==============+=====+
| q0   | q1           | q0  |
+------+--------------+-----+
| q1   | ['q2', 'q3'] | nan |
+------+--------------+-----+
| q2   | q3           | q0  |
+------+--------------+-----+
| q3   | nan          | nan |
+------+--------------+-----+
| q2q3 | q3           | q0  |
+------+--------------+-----+
Final states of DFA: ['q3', 'q2q3']
```
