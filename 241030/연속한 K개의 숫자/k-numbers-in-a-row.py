def min_additions_to_k_consecutive(N, K, B, missing_numbers):
    # Create a set of missing numbers for O(1) lookups
    missing_set = set(missing_numbers)

    # Initial count of missing numbers in the first window of length K
    missing_count = sum(1 for i in range(1, K + 1) if i in missing_set)
    min_missing = missing_count

    # Sliding window: for each new position, adjust the count
    for i in range(2, N - K + 2):
        # Remove the influence of the number that slides out
        if i - 1 in missing_set:
            missing_count -= 1
        # Add the influence of the new number that slides in
        if i + K - 1 in missing_set:
            missing_count += 1
        # Track the minimum count of missing numbers in any K-length segment
        min_missing = min(min_missing, missing_count)

    return min_missing

# Example usage
N = 10
K = 6
B = 5
missing_numbers = [2, 10, 1, 5, 9]
print(min_additions_to_k_consecutive(N, K, B, missing_numbers))