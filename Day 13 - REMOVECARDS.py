def min_moves_to_unify_cards(test_cases):
    results = []
    
    for case in test_cases:
        N, cards = case
        frequency = {}
        
        for card in cards:
            if card in frequency:
                frequency[card] += 1
            else:
                frequency[card] = 1
        
        max_frequency = max(frequency.values())
        min_moves = N - max_frequency
        results.append(min_moves)
    
    return results

# Reading input
T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    test_cases.append((N, cards))

# Getting the results
results = min_moves_to_unify_cards(test_cases)

# Printing the results
for result in results:
    print(result)
