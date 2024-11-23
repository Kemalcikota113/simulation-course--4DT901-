# Generate 10 random numbers using
# the linear congruential generator

X_0 = 7
a = 11
c = 0 # change this if you want linear congruential generator
m = 16

n_incrementor = 0

# Formula for linear congruential generator
X_n = ((X_0 * a) + c) % m


# create a loop to generate 10 random numbers
print('X_0 = ', X_0)
for i in range(10):
    X_n = ((X_0 * a) + c) % m
    X_0 = X_n # update the value of X_0
    n_incrementor += 1
    print('X_', n_incrementor, ' = ', X_n)