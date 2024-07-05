#Chidi Nna
#Python ScriptPrograaming
#Extra
#This is a Project called  The Car Parts Database Management System is a Python OOD program designed to manage a
# collection of car parts. It allows users to perform  simple operations on the database, such as adding new parts, 
# deleting parts, updating part attributes, finding specific parts, and printing the entire database. 
# The application uses object-oriented programming practices and teqniques to define parts and manage the database.





class Allparts:

    attributeNames = ['partName', 'partNumber', 'manufacturerNumber', 'manufacturer', 'description', 'cost', 'model']

    def __init__(self, partName, partNumber, manufacturerNumber, manufacturer, description, cost, model):
        self.partName = partName
        self.partNumber = partNumber
        self.manufacturerNumber = manufacturerNumber
        self.manufacturer = manufacturer
        self.description = description
        self.cost = cost
        self.model = model

    def displayAttributes(self):
        ''' Displays the attributes for just part number and part name''' 
        return [self.partNumber, self.partName]
    
    #below are all the getters and setters that we will need for all the instance variables in our car database 
    def set_partName(self, partName):
        self.partName = partName

    def get_partName(self):
        return self.partName

    def set_partNumber(self, partNumber):
        self.partNumber = partNumber

    def get_partNumber(self):
        return self.partNumber

    def set_manufacturerNumber(self, manufacturerNumber):
        self.manufacturerNumber = manufacturerNumber

    def get_manufacturerNumber(self):
        return self.manufacturerNumber

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model
     
