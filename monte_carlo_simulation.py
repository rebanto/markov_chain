import numpy as np
import random

graph = {
    'A': [0.2, 0.35, 0.45],
    'B': [0, 0.4, 0.6],
    'C': [0.4, 0.35, 0.25]
}

states = ['A', 'B', 'C']
num_steps = 100000
current_state = 0
visit_counts = [0, 0, 0]      # We'll tally visits to each state as we go.

for _ in range(num_steps):
    visit_counts[current_state] += 1  # log visit for empirical data
    probs = graph[states[current_state]]  # grab transition weights

    current_state = np.random.choice([0, 1, 2], p=probs) # weighted choice

stationary_distribution = np.array(visit_counts) / num_steps # normalize to get empirical frequencies
print(stationary_distribution)