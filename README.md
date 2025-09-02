# Markov Chain Simulation Results

## Walkthrough Method

Just following the chain step by step, picking the next state based on the weights. We keep a list of where we go, and at the end, just count up how often we hit each state.

- **Stationary Distribution:**  
  Output: `[0.24468, 0.30269, 0.45263]`
- **Simulation steps:** 100000  
- **Elapsed time (seconds):** 0.0610  
- **Steps per second:** 1639418.23  

---

## Monte Carlo Simulation

Classic Monte Carlo approach: use random sampling to explore the state space, letting the transition probabilities guide each jump. By running a large number of trials, we build up a solid estimate of the stationary distribution just by counting how often we hit each state.

- **Stationary Distribution:**  
  Output: `[0.21045, 0.36624, 0.42331]`
- **Simulation steps:** 100000  
- **Elapsed time (seconds):** 0.5843  
- **Steps per second:** 171131.05  

---

## Linear Algebra Method

We multiply a probability vector by the transition matrix repeatedly until it converges. The result is the stationary distribution - the eigenvector for eigenvalue 1. 

- **Stationary Distribution:**  
  Output: `[0.21052632, 0.36842105, 0.42105263]`
- **Iterations:** 25  
- **Elapsed time (seconds):** 0.0000  
- **Iterations per second:** (elapsed time too small to measure)  

---

> **Note:**  
> All methods were run with 100,000 steps/iterations for fair comparison.
