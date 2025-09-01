import numpy as np

graph = {
    'A': [0.2, 0.35, 0.45],
    'B': [0, 0.4, 0.6],
    'C': [0.3, 0.15, 0.25]
}

transition_matrix = np.array([graph['A'], graph['B'], graph['C']])
p_states = [1, 0, 0]  # initial state probabilities

new_state = np.matmul(p_states, transition_matrix)
print(new_state)