# States are (a, b) such that a + b <= 7
states = []
for a in range(8):
    for b in range(8):
        if a + b <= 7:
            states.append((a, b))

state_to_idx = {s: i for i, s in enumerate(states)}
num_states = len(states)

# Initialize DP for length 2
# d1 cannot be 0.
dp = [0] * num_states
for d1 in range(1, 8):
    for d2 in range(8):
        if d1 + d2 <= 7:
            if (d1, d2) in state_to_idx:
                dp[state_to_idx[(d1, d2)]] = 1

# Iterate for length 3 to 77 (75 steps)
for _ in range(75):
    new_dp = [0] * num_states
    for idx, count in enumerate(dp):
        if count == 0: continue
        a, b = states[idx]
        
        # Try adding digit c
        for c in range(8):
            if a + b + c <= 7:
                # The next state is (b, c)
                # We know a+b+c <= 7 implies b+c <= 7 since a >= 0
                next_idx = state_to_idx[(b, c)]
                new_dp[next_idx] = (new_dp[next_idx] + count) # % 1000 if needed, but Python handles large ints
    dp = new_dp

total = sum(dp)
print(total % 1000)
# OR the method below using matrix exponentiation
def solve_77_digit_problem():
    """
    Calculates the number of 77-digit integers where the sum of any 
    three consecutive digits is at most 7.
    """
    MOD = 1000  # We only need the last 3 digits

    # 1. Generate Valid States
    # A state is a pair of digits (u, v) such that u + v <= 7.
    # Digit range: 0-7 (since if sum <= 7, no single digit can be > 7)
    states = []
    for u in range(8):
        for v in range(8):
            if u + v <= 7:
                states.append((u, v))
    
    num_states = len(states)
    state_to_idx = {state: i for i, state in enumerate(states)}

    # 2. Build Transition Matrix
    # We can move from (u, v) to (v, w) if u + v + w <= 7
    matrix = [[0] * num_states for _ in range(num_states)]
    
    for i in range(num_states):
        u, v = states[i]
        for w in range(8):
            # Check condition for next digit w
            if u + v + w <= 7:
                next_state = (v, w)
                if next_state in state_to_idx:
                    j = state_to_idx[next_state]
                    matrix[i][j] = 1

    # 3. Define Initial Vector
    # The first two digits (d1, d2) must satisfy d1 + d2 <= 7
    # AND d1 != 0 (leading digit cannot be 0)
    initial_vector = [0] * num_states
    for i in range(num_states):
        u, v = states[i]
        if u != 0: 
            initial_vector[i] = 1

    # 4. Matrix Exponentiation Function
    def multiply_matrices(A, B, mod):
        C = [[0] * len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
        return C

    def matrix_pow(A, p, mod):
        res = [[0] * len(A) for _ in range(len(A))]
        for i in range(len(A)): res[i][i] = 1 # Identity matrix
        base = A
        while p > 0:
            if p % 2 == 1:
                res = multiply_matrices(res, base, mod)
            base = multiply_matrices(base, base, mod)
            p //= 2
        return res

    # 5. Compute Final Result
    # We start with 2 digits. We need 77 digits.
    # So we need 75 transitions.
    transitions = 77 - 2
    final_matrix = matrix_pow(matrix, transitions, MOD)

    # Multiply initial vector by the final transition matrix
    total_count = 0
    for i in range(num_states): # For every starting state
        for j in range(num_states): # Sum all possible ending states
            # initial_vector[i] represents the count of starting in state i
            # final_matrix[i][j] represents paths from i to j
            total_count = (total_count + initial_vector[i] * final_matrix[i][j]) % MOD

    return total_count

if __name__ == "__main__":
    result = solve_77_digit_problem()
    print(f"The last three digits of N are: {result}")