import numpy as np
import time

graph = {
    'A': [0.2, 0.35, 0.45],
    'B': [0, 0.4, 0.6],
    'C': [0.4, 0.35, 0.25]
}

# shape: (num_states, num_states). each row sums to 1 for a valid stochastic matrix.
transition_matrix = np.array([graph['A'], graph['B'], graph['C']])

p_states = np.array([1, 0, 0]) # initial probability distribution (starts in state A in this case)

counter = 0
max_iter = 100000  # set to 100000 for fair comparison across methods

start_time = time.time()  # track computation start

# p_states_n = p_states_0 @ (transition_matrix ** n)
# as n increases, p_states converges to the stationary distribution (the left eigenvector of the matrix with eigenvalue 1)
while counter < max_iter:
    prev_state = p_states
    p_states = p_states @ transition_matrix
    if np.array_equal(prev_state, p_states): # convergence check
        break
    counter += 1

elapsed = time.time() - start_time  # total computation time

print(p_states) # print stationary distribution

# efficiency metrics
print(f"Iterations: {counter}")
print(f"Elapsed time (seconds): {elapsed:.4f}")
if elapsed > 0:
    print(f"Steps per second: {counter / elapsed:.2f}")
else:
    print("Steps per second: (elapsed time too small to measure)")