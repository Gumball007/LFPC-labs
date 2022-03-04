from tabulate import tabulate
import pandas as pd


Q = ["q0", "q1", "q2", "q3"]
Sigma = ["a", "b"]
F = ["q3"]
initial_state = "q0"
NFA = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': ['q2', 'q3']},
    'q2': {'a': 'q3', 'b': 'q0'},
    'q3': {}
}

# Create table
table_NFA = pd.DataFrame(NFA).T
head = ['a', 'b']
print('NFA table:')
print(tabulate(table_NFA, headers=head, tablefmt='grid'))
print('Final state of NFA: ', F)

# Starting DFA
all_nfa_states = list(NFA.keys())
input_alphabet = list(NFA[all_nfa_states[0]].keys())

new_state = ''.join(NFA[all_nfa_states[1]][input_alphabet[0]])
DFA = dict(NFA)
DFA[new_state] = {}

all_dfa_states = list(DFA.keys())
input_alphabet = list(DFA[all_dfa_states[0]].keys())

print(DFA.items())
for key, value in DFA.items():
    DFA[all_dfa_states[4]][input_alphabet[0]] = 'q3'
    DFA[all_dfa_states[4]][input_alphabet[1]] = 'q0'

# print(DFA)
table_DFA = pd.DataFrame(DFA).T
head = ['a', 'b']
print('DFA table:')
print(tabulate(table_DFA, headers=head, tablefmt='grid'))


# computing final states
F += [new_state]
print('Final states of DFA: ' + str(F))
