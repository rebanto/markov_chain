import random
import time

# directed graph to model states and probabilities
graph = {
    'A': [0.2, 0.35, 0.45],
    'B': [0, 0.4, 0.6],
    'C': [0.3, 0.15, 0.25]
}

# params for markov chain
state = 'A'
steps = 100000  # set to 100000 for fair comparison across methods

states = [state] # list to store the states through the steps

start_time = time.time()  # track simulation start

for i in range(steps - 1):
    choice = random.choices([0, 1, 2], graph[state], k=1)[0] # weighted random choice from current state
    if choice == 0:
        state = 'A'
    elif choice == 1:
        state = 'B'
    else:
        state = 'C'
    states.append(state)

elapsed = time.time() - start_time  # total simulation time

# for i in range(len(states) - 1):
#     print(f"{states[i]} -> ", end="")
# print(states[-1])

# calculate probabilities of each state for stationary distribution
p_a = states.count('A') / len(states)
p_b = states.count('B') / len(states)
p_c = states.count('C') / len(states)

print(f"\nStationary Distrbution:\nState A = {p_a}\nState B = {p_b}\nState C = {p_c}")

# efficiency metrics
print(f"Simulation steps: {steps}")
print(f"Elapsed time (seconds): {elapsed:.4f}")
if elapsed > 0:
    print(f"Steps per second: {steps / elapsed:.2f}")
else:
    print("Steps per second: (elapsed time too small to measure)")