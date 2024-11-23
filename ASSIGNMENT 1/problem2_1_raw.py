# Multiplicative congruential generator parameters
# X_0 = initial seed
# a = multiplier
# m = modulus

def multiplicativeCongruentialMethod(X_0, a, m):
    # List to store random numbers
    RNGnums = []
    
    print('X_0 =', X_0)
    
    # Loop to generate 30 random numbers
    for i in range(30):
        X_n = (X_0 * a) % m  # Multiplicative congruential formula
        RNGnums.append(X_n)  # Store random number in the list
        X_0 = X_n  # Update X_0 for the next iteration
        print(f'X_{i+1} = {X_n}')  # Output the current random number
        
    return RNGnums  # Optionally return the generated numbers



# main
print('\nRNG for parameters (X_0 = 8, a = 13, m = 16)')
multiplicativeCongruentialMethod(8, 13, 16)

print('\nRNG for parameters (X_0 = 8, a = 11, m = 30)')
multiplicativeCongruentialMethod(8, 11, 30)

print('\nRNG for parameters (X_0 = 7, a = 7, m = 16)')
multiplicativeCongruentialMethod(7, 7, 16)

print('\nRNG for parameters (X_0 = 8, a = 7, m = 25)')
multiplicativeCongruentialMethod(8, 7, 25)
