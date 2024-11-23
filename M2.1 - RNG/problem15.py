# program that checks how many iterations it
# takes for the linear/multiplicative congruential method
# to create  cycöle

X_0 = 7
a = 11
c = 0 # change this if you want linear congruential generator
m = 16

X_n = ((X_0 * a) + c) % m
n_incrementor = 0


while X_n != X_0:
    X_n = ((X_n * a) + c) % m

    n_incrementor += 1
    print('X_', n_incrementor, ' = ', X_n)

    if X_n == X_0:
        print('it took ', n_incrementor + 1, ' iterations to get back to the original value')
        #break