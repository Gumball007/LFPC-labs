from tabulate import tabulate
import pandas as pd


Q = ["q0", "q1", "q2", "q3"]
Sigma = ["a", "b"]
F = "q3"
initial_state = "q0"
NFA = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': ['q2', 'q3']},
    'q2': {'a': 'q3', 'b': 'q0'},
    'q3': {}
}
DFA = {}

# Create table
table_NFA = pd.DataFrame(NFA).T
head = ['a', 'b']
print('NFA table:')
print(tabulate(table_NFA, headers=head, tablefmt='grid'))
print('Final state of NFA: ', F)

all_nfa_states = list(NFA.keys())
input_alphabet = list(NFA[all_nfa_states[0]].keys())

for state, transitions in NFA.items():
    for transition_variable, next_state in transitions.items():
        if isinstance(next_state, list):
            NFA[state][transition_variable] = tuple(next_state)
            DFA[state] = NFA[state]
            DFA[tuple(next_state)] = {}

            for input in input_alphabet:
                my_set = set()
                for old_state in next_state:
                    if input in NFA[old_state]:
                        my_set.add(NFA[old_state][input])
                if len(my_set) == 1:
                    update_state = my_set.pop()
                else:
                    update_state = tuple(my_set)
                DFA[tuple(next_state)][input] = update_state
        else:
            DFA[state] = NFA[state]

print('\nDFA is: ', DFA)
table_DFA = pd.DataFrame(DFA).T
head = ['a', 'b']
print('DFA table:')
print(tabulate(table_DFA, headers=head, tablefmt='grid'))

# computing final states
new_final_states = [F]
for state in DFA:
    if F in state:
        new_final_states.append(state)

print(new_final_states)
