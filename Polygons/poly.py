#Chidi Nna
#Program #8
#Python Programming CSCI-6651-01
#will require the creation of a Python Application that makes use of multiple modules along with external libraries.
#The program will involve the input of a polynomial ax^n+bx^(n-1)+.....c=f(x). But use classes 


import matplotlib.pyplot as plt  # You need to import pyplot from matplotlib

class Poly:
    
    def __init__(self):
        self.degree = 0
        self.coefficients = []
        self.domain = (0, 0, 1)
    
    def polyDeg(self):
        '''Funtion to define the degree of the polyniomial '''
        self.degree = int(input("Enter the degree of the polynomial: ")) #asks the user to enter the degree of polynomial
 
    def collectCoefs(self):

        ''' Function to collect the coeffiecnets of the polynomial  '''
        start = self.degree   #Start is the degree we entered before so you must enter degree before moving on 
        for i in range(start, -1, -1):               #goes through range of start to enter in each coeffecient           
            x = float(input(f"Enter the coefficient for x^{i}: "))  # 
            self.coefficients.append(x)
        
    def setDomain(self):

        ''' THis function collects the start stop and step of the domain and makes the value all intergers'''
        start = int(input("Enter the start of the domain: "))  # 
        stop = int(input("Enter the end of the domain: "))  # 
        step = int(input("Enter the step for the domain: "))  # 
        self.domain = (start, stop, step)

    def pltFnct(self):

        ''' This Function is to plot the values given to us from above to the equation  ax^n+bx^(n-1)+.....c=f(x).'''
        x = list(range(self.domain[0], self.domain[1], self.domain[2]))   #creates a lsit of the values of the domain given 
        
        y = []
        for i in x:   #iteraterates through the list and 
            result = 0
            for j, coef in enumerate(self.coefficients):
                result += coef * (i ** (self.degree - j)) #    Stores the input of a polynomial ax^n+bx^(n-1)+.....c=f(x) in results
            y.append(result)  # adds the result to a list 
        
        # Below is given infromation to plot a grapgh
        plt.figure('Polynomial Plot')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.plot(x, y, "b")
        plt.title("Polynomial Plot")
        plt.show()

    def menu(self):

        ''' Funtion is just a basic menu to point to diffrenet functions in this class and gives a layout '''
       
        while True: # Loop Infinitne
            print("---------------------------------------------------------------------------------------")
            print("\nMenu:")
            print("1. Enter the degree of the polynomial")
            print("2. Collect the coefficients of the polynomial")
            print("3. Set the domain to evaluate the polynomial over")
            print("4. Plot the polynomial over the specified domain")
            print("q. Quit")
            value = input("Choose an option: ").upper()
            
            if value == '1':          # if else sequence to give the user option in the correctrer order it must be made 
                self.polyDeg()
            elif value == '2':
                if self.degree is None:
                    print("Please enter the degree of the polynomial first.")
                else:
                    self.collectCoefs()
            elif value == '3':
                if self.coefficients is None:
                    print("Please enter the coefficients of the polynomial first.")
                else:
                    self.setDomain()
            elif value == '4':
                self.pltFnct()
            elif value == 'Q':
                break
            else:
                print("Invalid option. Please try again.")
            
            if value == 'Q':
                break
            else:
                continue
