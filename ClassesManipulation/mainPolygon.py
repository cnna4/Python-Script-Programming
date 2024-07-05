from Polygon import Polygon

def main():
    square = Polygon("square", 4,[(0,0),(0,2),(2,0),(2,2)])  #creates a object of Polygon 
    square.printInfo()

if __name__ == "__main__":
    main()