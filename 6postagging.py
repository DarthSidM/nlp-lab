import numpy as np

# States (POS Tags)
states = ['Noun', 'Verb', 'Adjective']

# Observations (Words)
observations = input("Enter a sentence:\n").lower().split()

# Initial Probabilities
start_prob = {
    'Noun': 0.4,
    'Verb': 0.3,
    'Adjective': 0.3
}

# Transition Probabilities
trans_prob = {
    'Noun': {'Noun': 0.1, 'Verb': 0.6, 'Adjective': 0.3},
    'Verb': {'Noun': 0.5, 'Verb': 0.2, 'Adjective': 0.3},
    'Adjective': {'Noun': 0.6, 'Verb': 0.2, 'Adjective': 0.2}
}

# Emission Probabilities (example vocabulary)
emit_prob = {
    'Noun': {'dog': 0.3, 'cat': 0.3, 'college': 0.4},
    'Verb': {'runs': 0.5, 'eats': 0.3, 'studies': 0.2},
    'Adjective': {'fast': 0.5, 'smart': 0.3, 'big': 0.2}
}

# Viterbi Algorithm
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
    
    # Initialize base cases
    for state in states:
        # Default to 1e-6 if the word is not in our known vocabulary
        V[0][state] = start_p[state] * emit_p[state].get(obs[0], 1e-6)
        path[state] = [state]
        
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        new_path = {}
        
        for curr_state in states:
            # Calculate the maximum probability for the current state
            (prob, prev_state) = max(
                (V[t-1][y0] * trans_p[y0][curr_state] * emit_p[curr_state].get(obs[t], 1e-6), y0)
                for y0 in states
            )
            V[t][curr_state] = prob
            new_path[curr_state] = path[prev_state] + [curr_state]
            
        path = new_path
        
    # Backtrack to find the best path
    n = len(obs) - 1
    (prob, state) = max((V[n][y], y) for y in states)
    return path[state]

# Execute the algorithm
result = viterbi(observations, states, start_prob, trans_prob, emit_prob)

# Print results
print("\nPOS Tags:")
for word, tag in zip(observations, result):
    print(f"{word} --> {tag}")
