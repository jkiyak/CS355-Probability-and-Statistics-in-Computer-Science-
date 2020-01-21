import matplotlib.pyplot as plt
import numpy as np

def math_formula(j):
    math_formula = (1/3) * (j-1)**2
    return math_formula


a = 0
b = 3
results = []
for value in range(a, b):
    print ('For f(',(value),')', 'the number is:' , math_formula(value))
    results.append(math_formula(value))

print ('The maximum ofis:', max(results))
c = max(results)
print(c)


x = np.random.uniform(a,b,1000)
y = np.random.uniform(0,c,1000)

def desiredrandomvariable(x,y):
    for i in range(0,10000):
        if y <= math_formula(x):
            return (x)
        else:
            return (np.random.uniform(0,c,1000))

def main():
    count, bins, ignored = plt.hist(x, 15, density=True)
    plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
    plt.xlabel("Values Accumulated")
    plt.title("Have Mercy Please :(")
    plt.show()


main()



    


