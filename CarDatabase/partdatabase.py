from Allparts import Allparts

class PartDatabase:
    '''Class to manage parts'''

    def __init__(self):
        ''' Initializes the database with an empty dictionary and sets the total amount of of parts to 0'''
        self.partDatabase = {}
        self.total_parts = 0

    def addPart(self, part):
        '''This function ddds a part to the user discretion to the database'''
        self.partDatabase[part.get_partNumber()] = part
        self.total_parts += 1

    def deletePart(self, partNumber):
        ''' This function deletes part from the database by taking in a part number and and removing its entry from the database'''
        if partNumber in self.partDatabase:
            del self.partDatabase[partNumber]
            self.total_parts -= 1

    def findPart(self, key):
        '''This function Looks for a specific key in part database and returns that part'''
        return self.partDatabase.get(key, None)

    def updatePartAttribute(self, partNumber):
        ''' This function updates attributes of a specific part and accepts the partnumber as a refrence in order to call on
        findpart and be able to locates all alltributes of that part'''
        part = self.findPart(partNumber)

        if part is None:  #if find part doesnt not retrieve anything then the ir will say part not found 
            print("Part not found")
            return

        while True: #infinte loop to keep updatating as many attributes of that part that you see fit 
            userPart = input("What attribute do you want to update? (or type 'q' to quit): ")
            if userPart == 'q':  #breaks loop
                break

            if userPart in Allparts.attributeNames:  # itterates through the list of attribute names from Allparts and looks for a match
                newValue = input(f"Enter new value for {userPart}: ") #input new value 
                setattr(part, userPart, newValue)  # update an attribute of a part object based on user input.
                print(f"{userPart} updated to {newValue}")
            else:
                print("Attribute not found")

    def printDatabase(self):
        '''This function Prints the entire CAR database'''
        if not self.partDatabase:
            print("The database is empty.")
            return
        
        print("Car Part Database:")
        for partNumber, part in self.partDatabase.items():
            print(f"Part Number: {partNumber}")
            for attribute in Allparts.attributeNames:
                print(f"{attribute}: {getattr(part, 'get_' + attribute)()}")
            print("-----")
 
    def menu(self):
        ''' Function is just a basic menu to point to different functions in this class and gives a layout '''
        
        while True: # Infinite menu till user decides to quit 
            print("---------------------------------------------------------------------------------------")
            print("\nMenu:")
            print("1. Add a Part to the database")
            print("2. Delete a Part from the database")
            print("3. Find a Part in the database")
            print("4. Update a Part in the database")
            print("5. Print The entire database")
            print("Q. Quit")
            value = input("Choose an option: ").upper()
            
            if value == '1':          # Gives the user the ability to enter a brand new part
                partName = input("Enter part name: ")
                partNumber = input("Enter part number: ")
                manufacturerNumber = input("Enter manufacturer number: ")
                manufacturer = input("Enter manufacturer: ")
                description = input("Enter description: ")
                cost = float(input("Enter cost: "))
                model = input("Enter model: ")
                part = Allparts(partName, partNumber, manufacturerNumber, manufacturer, description, cost, model)
                self.addPart(part) # Calls addPart to add part
                print(f"Part {partName} was added to the car database.")
            elif value == '2':        # Calls deletePart to delete a part
                partNumber = input("Enter the part number you wish to delete: ")
                self.deletePart(partNumber)
                print(f"Part {partNumber} has been deleted from car database.")
            elif value == '3':        # Calls findPart to find a part
                partNumber = input("Enter part number to find: ")
                part = self.findPart(partNumber)
                if part:
                    print(f"Part found: {part.displayAttributes()}")
                else:
                    print(f"Part {partNumber} not found in database.")
            elif value == '4':        # Update a part bybcalling on updatepartattribute                partNumber = input("Enter part number to update: ")
                self.updatePartAttribute(partNumber)
            elif value == '5':       
                self.printDatabase()  # Print the entire database by calling on the functipn
            elif value == 'Q':      
                break
            else:
                print("Invalid option. Please try ag1ain.")

if __name__ == "__main__":
    # Test Example
    database = PartDatabase()
    database.menu()
