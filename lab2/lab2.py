Q = ["q0", "q1", "q2", "q3"]
Sigma = ["a", "b"]
F = ["q3"]
initial_state = "q0"
transition_func = [
    "(q0, a)=q1",
    "(q0, b)=q0",
    "(q1, a)=q2",
    "(q1, a)=q3",
    "(q2, a)=q3",
    "(q2, b)=q0"
]

adjacencyList = {}

for state in Q:
    if state not in adjacencyList.keys():
        adjacencyList[state] = []

print(adjacencyList)
