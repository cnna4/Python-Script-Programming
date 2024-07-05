#Chidi Nna
#Program #9
#Python Programming CSCI-6651-01
#Program #9 will involve the creation a Polygon Class This class must include the following;  A class variable to track the number of instantiated Polygons
#Instance variables for the polygon name, number of vertices, location of vertices (x,y) Class methods for;
#a.  side counting b.  side length calculation c.  printing nicely formatted results for a and b above as well as any and all instance variable your class uses.
#Import your class into a main module and demonstrate all of the items listed above.
import math

class Polygon:

    num_of_polygons = 0

    def __init__(self, name, num_of_vertices, location):
        self.name = name
        self.num_of_vertices = num_of_vertices
        self.location = location

    #  Below are all the Getter and Setter for all the instance varivables for a polygon we are using
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_num_of_vertices(self):
        return int(self.num_of_vertices)

    def set_num_of_vertices(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices

    # Getter and Setter for location
    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def side_counting (self): 
        sides = self.num_of_vertices
        return sides
        

    def side_length_calculation (self):
        perim = 0
        num_vertices = len(self.location)
        for i in range(num_vertices):
            x1, y1 = self.location[i]  
            x2, y2 = self.location[(i + 1) % num_vertices]  # when i gets to num of vertices it will calculate the distnce 
            #from the last point to the first point  wrap arpund t0 get to the first index only when it = numvertices
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)   #this is the distance code found online of distance=(x2​−x1​)2+(y2​−y1​)2
            perim += distance
        return perim

            

    def printInfo(self):
        print(f'Polygon Name is {self.get_name}')
        print(f'Number of vertices is {self.get_num_of_vertices}')
        print(f'The location of each is at ')
        for index, value in self.location:
            print(self.location[value])
        print(f'The number of sides is {self.side_counting()}')
        print(f'The toal side length calculation is {self.side_length_calculation()}')

