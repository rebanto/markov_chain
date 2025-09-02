import numpy as np

graph = {
    'A': [0.2, 0.35, 0.45],
    'B': [0, 0.4, 0.6],
    'C': [0.4, 0.35, 0.25]
}

# shape: (num_states, num_states). each row sums to 1 for a valid stochastic matrix.
transition_matrix = np.array([graph['A'], graph['B'], graph['C']])

p_states = np.array([1, 0, 0]) # initial probability distribution (starts in state A in this case)

counter = 0
max_iter = 100000  # non-convergence threshold

# p_states_n = p_states_0 @ (transition_matrix ** n)
# as n increases, p_states converges to the stationary distribution (the left eigenvector of the matrix with eigenvalue 1)
while counter < max_iter:
    prev_state = p_states
    p_states = p_states @ transition_matrix
    
    if np.array_equal(prev_state, p_states): # convergence check
        break
    counter += 1

print(p_states, counter) # print stationary distribution and iteration count