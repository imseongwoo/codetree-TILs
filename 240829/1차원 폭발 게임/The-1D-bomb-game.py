def bomb_simulation(N, M, bombs):
    while True:
        found_explosion = False
        i = 0
        
        # List to collect the new state of the bombs after explosions
        new_bombs = []
        
        while i < len(bombs):
            count = 1
            
            # Check how many consecutive bombs have the same number
            while i + count < len(bombs) and bombs[i + count] == bombs[i]:
                count += 1
            
            # If the sequence length is M or more, we skip adding these to new_bombs (they explode)
            if count >= M:
                found_explosion = True
                i += count  # Skip this sequence as it explodes
            else:
                new_bombs.extend(bombs[i:i + count])
                i += count
        
        # Update the bombs list with the new state
        bombs = new_bombs
        
        # If no explosion occurred, we're done
        if not found_explosion:
            break
    
    # Print the result
    print(len(bombs))
    for bomb in bombs:
        print(bomb)

# Input reading
N, M = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

# Call the function with the input data
bomb_simulation(N, M, bombs)