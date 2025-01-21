def stone_piles(n):
    piles = []
    if n % 2 != 0:
        n -= 1  
    for i in range(2, n + 1, 2):
        piles.append(i)
    return piles

if __name__ == "__main__":
    n = int(input("Enter the number of stones: "))

    piles = stone_piles(n)

    print(f"Stones in the piles: {piles}")