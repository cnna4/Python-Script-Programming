import matplotlib.pyplot as plt

# predefined varibales accoriding to porgram description
a = 0.01
b = 0.002
c = 0.0001


Myx = [i * 0.01 for i in range(0,101)] #gives me  x values range of 0 to 1 in steps of 0.01
#because .01 x 100 is 10 and the range starts at 0

Myy = [(a * x ** 2) + (b * x) + c for x in Myx] #evaluate the polynomial y=ax^2+bx+c over the range of 0 to 1 in steps of 0.01

def plot_signal(x, y):
    # Get a figure
    fig, ax = plt.subplots()
    # Set title
    ax.set_title('Poly Eval')
    # Set x label
    ax.set_xlabel('Range')
    # Set y label
    ax.set_ylabel('Domain')
    # Turn on grid
    ax.grid()
    # Plot
    ax.plot(x, y)
    # Display the plot
    plt.show()

# Plot the signal
plot_signal(Myx, Myy)


print ("-----------------------------------------------------------------")
MyxT = [i * 0.01 for i in range(101)] #gives me  x values range of 0 to 1 in steps of 0.01
#because .01 x 100 is 10 and the range starts at 0


XandY = [(x, (a * x ** 2) + (b * x) + c) for x in MyxT] #using a tuple now with () rather than a list 

#Using Tuples now so X and y are pointint to the the first element and second element in the tuple
MyxT = [XandY[0] for p in XandY]
MyyT = [XandY[1] for p in XandY]

def plot_signal(x, y):
    # Get a figure
    fig, ax = plt.subplots()
    # Set title
    ax.set_title('Poly Eval')
    # Set x label
    ax.set_xlabel('Range')
    # Set y label
    ax.set_ylabel('Domain')
    # Turn on grid
    ax.grid()
    # Plot
    ax.plot(x, y)
    # Display the plot
    plt.show()

# Plot the signal
plot_signal(MyxT, MyyT)