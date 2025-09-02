import numpy as np
import random
import time

graph = {
    'A': [0.2, 0.35, 0.45],
    'B': [0, 0.4, 0.6],
    'C': [0.4, 0.35, 0.25]
}

states = ['A', 'B', 'C']
num_steps = 100000  # set to 100000 for fair comparison across methods
current_state = 0
visit_counts = [0, 0, 0]

start_time = time.time()  # track simulation start

for _ in range(num_steps):
    visit_counts[current_state] += 1  # log visit for empirical data
    probs = graph[states[current_state]]  # grab transition weights
    current_state = np.random.choice([0, 1, 2], p=probs) # weighted choice

elapsed = time.time() - start_time  # total simulation time

stationary_distribution = np.array(visit_counts) / num_steps # normalize to get empirical frequencies
print(stationary_distribution)

# efficiency metrics
print(f"Simulation steps: {num_steps}")
print(f"Elapsed time (seconds): {elapsed:.4f}")
if elapsed > 0:
    print(f"Steps per second: {num_steps / elapsed:.2f}")
else:
    print("Steps per second: (elapsed time too small to measure)")