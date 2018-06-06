import numpy, sys, time
import matplotlib.pyplot as plt

# n = int(input("Input an integer: "))
n = 200


def multiply(n: int, flag: int):
    # n = int(sys.argv[1])
    a = numpy.zeros((n, n))  # Matrix A
    b = numpy.zeros((n, n))  # Matrix B
    c = numpy.zeros((n, n))  # Matrix C

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    ######################################
    # Write code to calculate C = A * B. #
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0
            for k in range(n):
                c[i, j] += a[i, k] * b[k, j]
    ######################################

    end = time.time()
    t = end - begin
    if (flag == 1):
        return sum(c)

    return t


# Print C for debugging. Comment out the print before measuring the execution time.
total = 0
total += multiply(200, 1)

print(sum(total))

t = []
num = range(1, 201)

for i in range(1, n + 1):
    t.append(multiply(i, 0))
    if (i % 10 == 0):
        print("The python step is: ", i)

java_time = []
c_time = []

with open("matrix_java.txt", "r")as javaf:
    lines = javaf.readlines()
    for line in lines:
        java_time.append(float(line.split('\n')[0]))

with open("matrix_c.txt", "r")as cf:
    lines = cf.readlines()
    for line in lines:
        c_time.append(float(line.split('\n')[0]))

plt.plot(num, t, label='python', color='r')
plt.plot(num, java_time, label='java', color='g')
plt.plot(num, c_time, label='c', color='b')
plt.xlabel('n')
plt.ylabel('time(s)')
plt.legend()
plt.show()
