import numpy as np # only using this for .sqrt() function, hope its OK.

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
        #print(X_n)
        
    return RNGnums  # Optionally return the generated numbers

# This uniformity test follows the steps that are outlined 
# in the referenced course material on MyMoodle
# M2.1 reading material page 12
def KS_test(RNGnums, m):

    # step 1: rank the data from smallest to largest

    RNGnums = [x / m for x in RNGnums]
    print(f"\nnormalized RNGnums: {RNGnums}")

    RNGnums.sort()

    # step 2: compute D+ and D-
    N = len(RNGnums)
    D_plus_arr = []
    D_minus_arr = []

    for i in range(len(RNGnums)):
        j = i + 1
        R_i = RNGnums[i]
        D_plus_i = j/N - R_i
        D_minus_i = R_i - (j-1)/N
        D_plus_arr.append(D_plus_i)
        D_minus_arr.append(D_minus_i)

    D_plus = max(D_plus_arr)
    D_minus = max(D_minus_arr)

    # step 3: Compute D
    D = max(D_plus, D_minus)
    print(f"\nD: {D}")

    # step 4: Locate the critical value

    D_alpha = 0.29  # from appendix table --> alpha = 0.01
    #D_alpha = 0.24  # from appendix table --> alpha = 0.05
    print(f"D_alpha: {D_alpha}")

    # step 5: compare D and D_alpha and make a decision
    if D <= D_alpha:
        print("\nThe numbers are uniformly distributed")
    else:
        print("\nThe numbers are not uniformly distributed")

# This autocorrelation test follows the steps that are outlined
# in the referenced course material on MyMoodle
# M2.1 reading material page 16
def autocorrelationTest(RNGnums, lag):

    N = len(RNGnums)
    M = (N - lag) // lag - 1

    rho_hat = 0

    for i in range(M + 1):
        rho_hat += RNGnums[i] * RNGnums[i + lag]

    rho_hat = (1 / (M + 1)) * rho_hat - 0.25

    sigma_rho_hat = np.sqrt((13 * M + 7) / (12 * (M + 1)))

    Z_0 = rho_hat / sigma_rho_hat
    Z_alpha_2 = 1.96  # from appendix table --> alpha = 0.05

    if -Z_alpha_2 <= Z_0 <= Z_alpha_2:
        print(f"\nAt lag = {lag}, do not reject the null hypothesis (Z_0 = {Z_0})")
        print("No significant autocorrelation")
    else:
        print(f"\nAt lag = {lag}, reject the null hypothesis (Z_0 = {Z_0})")
        print("Significant autocorrelation")



# main
print('\nRNG for parameters (X_0 = 8, a = 13, m = 16)')
RNG_1 = multiplicativeCongruentialMethod(8, 13, 16)
print('Uniformity test for parameters (X_0 = 8, a = 13, m = 16)', )
KS_test(RNG_1, 16)
print('\nAutocorrelation test for parameters (X_0 = 8, a = 13, m = 16)')
autocorrelationTest(RNG_1, 1)
autocorrelationTest(RNG_1, 5)
autocorrelationTest(RNG_1, 10)

print('\nRNG for parameters (X_0 = 8, a = 11, m = 30)')
RNG_2 = multiplicativeCongruentialMethod(8, 11, 30)
print('\nUniformity test for parameters (X_0 = 8, a = 11, m = 30)')
KS_test(RNG_2, 30)
print('\nAutocorrelation test for parameters (X_0 = 8, a = 11, m = 30)')
autocorrelationTest(RNG_2, 1)
autocorrelationTest(RNG_2, 5)
autocorrelationTest(RNG_2, 10)

print('\nRNG for parameters (X_0 = 7, a = 7, m = 16)')
RNG_3 = multiplicativeCongruentialMethod(7, 7, 16)
print('\nUniformity test for parameters (X_0 = 7, a = 7, m = 16)')
KS_test(RNG_3, 16)
print('\nAutocorrelation test for parameters (X_0 = 7, a = 7, m = 16)')
autocorrelationTest(RNG_3, 1)
autocorrelationTest(RNG_3, 5)
autocorrelationTest(RNG_3, 10)

print('\nRNG for parameters (X_0 = 8, a = 7, m = 25)')
RNG_4 = multiplicativeCongruentialMethod(8, 7, 25)
print('\nUniformity test for parameters (X_0 = 8, a = 7, m = 25)')
KS_test(RNG_4, 25)
print('\nAutocorrelation test for parameters (X_0 = 8, a = 7, m = 25)')
autocorrelationTest(RNG_4, 1)
autocorrelationTest(RNG_4, 5)
autocorrelationTest(RNG_4, 10)


