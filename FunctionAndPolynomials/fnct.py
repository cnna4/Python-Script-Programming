#Chidi Nna
#Program #7
#Python Programming CSCI-6651-01
#will require the creation of a Python Application that makes use of multiple modules along with external libraries.
#The program will involve the input of a polynomial ax^n+bx^(n-1)+.....c=f(x).
import matplotlib

class fnct:
    
    def __init__(self):
        self.degree = 0
        self.coefficients = []
        self.domain = (0, 0, 1)
    
    def polyDeg(self):
        self.degree = input("Enter the degree of the polynomial: ")
 
    def collectCoefs(self):
        start = self.degree
        for i in range(start, -1, 0):
          x = input(f"Enter the coefficient for x^{i}: ")
          self.coefficients.append(x)
        
    def setDomain(self):
        start = input("Enter the start of the domain: ")
        stop = input("Enter the end of the domain: ")
        step = input("Enter the step for the domain: ")
        self.domain = (start, stop, step)

    def  pltFnct(self):
        x = list(range(self.domain[0], self.domain[1], self.domain[2]))
        
        y = []
        for i in x:
            result = 0
            for j, coef in enumerate(self.coefficients):
                result += coef * (i ** (self.degree - j))
            y.append(result)
        
        # Plot the polynomial
        plt.figure('Polynomial Plot')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.plot(x, y, "b")
        plt.title("Polynomial Plot")
        plt.show()

         
   
    def menu(self):
        # It should contain an infinite loop with a "quit" input to exit capability.
        while True:
            print("---------------------------------------------------------------------------------------")
            print("\nMenu:")
            print("1. Enter the degree of the polynomial")
            print("2. Collect the coefficients of the polynomial")
            print("3. Set the domain to evaluate the polynomial over")
            print("4. Plot the polynomial over the specified domain")
            print("q. Quit")
            value = input("Choose an option: ").upper()
            
            if value == '1':
                self.polyDeg()
            elif value == '2':
                if self.degree is None:
                    print("Please enter the degree of the polynomial first.")
                else:
                    self.collectCoefs()
            elif value == '3':
                if self.coefficients is None:
                        print("Please enter the Coefficcentids of the polynomial first.")
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


            

        
