import math


def magnitude(u):
    index = 0
    sum = 0
    for i in u:
        mag = (u[index])**2
        index += 1
        sum = sum + mag
    return math.sqrt(sum)


def dotProduct(u, v):
    index = 0
    sum = 0
    for i in u:
        dot = (u[index] * v[index])
        sum = sum + dot
        index += 1
    return sum


def angleBtwnVectors(u, v):
    theta = math.acos((dotProduct(u, v))/((magnitude(u))*(magnitude(v))))
    return math.degrees(theta)


def crossProduct(u, v):
    cross = [(u[1]*v[2]-v[1]*u[2]),
             (v[0]*u[2]-u[0]*v[2]),
             (u[0]*v[1]-u[1]*v[0])]
    return cross


choice = raw_input('You can choose:\n'
                   'a) Magnitude\n'
                   'b) Angle btwn two vectors\n'
                   'c) Dot Product\n'
                   'd) Cross Product\n')

if choice == 'a':
    print 'You chose magnitude!'
    u = raw_input("Enter vector u seperated by spaces: ")
    u = map(int, u.split())
    print "Magnitude of vector u = ", magnitude(u)

elif choice == 'b':
    print 'You chose angle!'
    u = raw_input("Enter vector u seperated by spaces: ")
    u = map(int, u.split())

    v = raw_input("Enter vector v seperated by spaces: ")
    v = map(int, v.split())

    print "Angle btwn these vectors = ", angleBtwnVectors(u, v), "degrees"

elif choice == 'c':
    print 'You chose Dot Product!'
    u = raw_input("Enter vector u seperated by spaces: ")
    u = map(int, u.split())

    v = raw_input("Enter vector v seperated by spaces: ")
    v = map(int, v.split())

    print "The Dot Product of these two vectors = ", dotProduct(u, v)

elif choice == 'd':
    print 'You chose Cross Product!'
    u = raw_input("Enter vector u seperated by spaces: ")
    u = map(float, u.split())

    v = raw_input("Enter vector v seperated by spaces: ")
    v = map(float, v.split())

    print "The Cross Product of these two vectors = ", crossProduct(u, v)

else:
    print "Sorry, that is not a valid option."
