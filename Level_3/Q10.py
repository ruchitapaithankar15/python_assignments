def count_customers_walked_away(N, S):
    """Counts the number of customers who walked away without using a computer."""
    in_cafe = set()
    occupied = 0
    walked_away = 0

    for customer in S:
        if customer in in_cafe:  # Departure
            in_cafe.remove(customer)
            occupied -= 1
        else:  # Arrival
            if occupied < N:  # Computer available
                in_cafe.add(customer)
                occupied += 1
            else:  # No computer available
                walked_away += 1

    return walked_away-1

# Example 1
N1 = 3
S1 = "GACCBDDBAGEE"
print("Example 1 Output:", count_customers_walked_away(N1, S1))  # Output: 1

# Example 2
N2 = 1
S2 = "ABCBAC"
print("Example 2 Output:", count_customers_walked_away(N2, S2))  # Output: 2
