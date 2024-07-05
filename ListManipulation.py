#Chidi Nna
#Program #3
#Python Programming CSCI-6651-01
#Assignment will be focused on Lists and List Manipulations

cityList = ['Framingham','West Haven','Smithfield','Natick','New Haven']  #Create a List of Cities and a List of Zip Codes
zipList = ['01701','06516','01150','01760','06501'] # The  Cities and Zip Codes are associated positionally within the list
compList=[cityList, zipList] #Create a List of the City and Zip Code Lists 

#Demonstrate how to index, append and delete elements fpr the individual and composite Lists 
print("This is the Orginal Complete List",compList,"\n")

cityList.append("Amherst") #Appending Cities and Zip Codes From Individual List and Composite Lsts
zipList.append("01002")
compList[0].append("Boston") 
compList[1].append("02108")
print("Updated City list after adding Amherst", cityList,"\n")
print("Updated Zip list after adding 01002", zipList,"\n")
print("Updated Composite list after adding Boston and its Zip 02108", compList,"\n")



cityList.remove("Framingham")#Removing Cities and Zip Codes From Individual List and Composite Lsts
zipList.remove("01701")
compList[0].remove("Natick") 
compList[1].remove("01760")

print("Updated City list after deleting Framingham", cityList,"\n")
print("Updated Zip list after deleting 01701", zipList,"\n")
print("Updated Composite list after deleting Natick and its Zip 01760", compList,"\n")


print("The Index of Boston in the list is", cityList.index("Boston")) #Finding the Idexes of  Cities and Zip Codes From Individual List and Composite Lsts
print("The Index of 06516 in the list is", zipList.index("06516"))
print("The Index of Amherst in the list is", compList[0].index("Amherst"))

print ("At the end of all the changes") #Demonstrate obtaining the size of the composite as well as individual Lists
print("The size of the ZipCode List is", len(zipList))
print("The size of the Cities List is",len(cityList))
print("The size of the Composite List is ",len(compList),"The size of all Elements in both lists",len(compList[0])+len(compList[1]),"\n")


#Demonstrate indexing from the end to the beginning of the individual and composite Lists


count =1
print("The new order is after indexing from the end to the beginning  of Zip codes is")  
for i in range(-1,-len(zipList)-1,-1): #Example of indexing from the end to the beginning of the individual
    print(count, zipList[i])
    count +=1

print("")
print("The new order is after indexing from the end to the beginning of Cities codes is")
for i in range(-1,-len(compList[0])-1,-1): #Example of indexing from the end to the beginning of the Composite 
    print(compList[0][i])

print ("----------------------------------------------------------------------------------------------------")

#Example Format Requested 
print()
entries = len(compList[0] +compList[1]) #Count number of Total Unique Entries
print("Listing of Cities & Zip Codes",compList,"\n")
print(f"Total Unique Entries: {entries}","\n")
count =1
for i in range (len(cityList)):
    print("City #:",count,cityList[i],"ZipCode#",count,zipList[i],)  # Genereates all Cities and Zip codes right besdies them 
    count+=1 

print ("----------------------------------------------------------------------------------------------------")

#Demonstrate how to creare individual and composite Tuples 
cityTuple = ('Framingham', 'West Haven', 'Smithfield', 'Natick', 'New Haven')
zipTuple = ('01701', '06516', '01150', '01760', '06501')

compTuple = (cityTuple, zipTuple)
print("This is the Original Complete Tuple", compTuple)


NewcityList = list(cityTuple)  #Turn the Tuples Into Lists
NewzipList = list(zipTuple)

#Demonstrate how to index, append and delete elements fpr the individual and composite Lists from previous Tuples
NewcityList.append("Amherst")
NewzipList.append("01002")

# Re-create the composite list with the updated individual lists that were once tuples
NewcompList = [NewcityList, NewzipList]


print("Updated City list after adding Amherst", NewcityList, "\n")
print("Updated Zip list after adding 01002", NewzipList, "\n")
print("Updated Composite list after adding Amherst and its Zip 01002", NewcompList, "\n")

# Removing Cities and Zip Codes From Individual List and Composite Lsts from prior tuples
NewcityList.remove("Framingham")
NewzipList.remove("01701")

#Removing Cities and Zip Codes From The Newcomplist after once a tuple
NewcompList[0].remove("Natick")
NewcompList[1].remove("01760")

print("Updated City list after deleting Framingham", NewcityList, "\n")
print("Updated Zip list after deleting 01701", NewzipList, "\n")
print("Updated Composite list after deleting Natick and its Zip 01760", NewcompList, "\n")


#Finding Cities and Zip Codes From The Newcomplist after once a tuple
print("The Index of West Haven in the list is", NewcityList.index("West Haven")) #Finding the Idexes of  Cities and Zip Codes From Individual List and Composite Lsts
print("The Index of 06516 in the list is", NewzipList.index("06516"))
print("The Index of Amherst in the list is", NewcompList[0].index("Amherst"))


# Demostrating turning lists back to tuples
cityTuple = tuple(cityList)
zipTuple = tuple(zipList)
compTuple = (cityTuple, zipTuple)

# Print the final updated tuple after the conversion back to a Tuple from a list
print()
print("Final Updated Composite Tuple", compTuple, "\n")


#Demonstrate indexing from the end to the beginning of the individual and composite Tuples
newcount =1
print("The new order is after indexing from the end to the beginning  of Zip codes is")  
for i in range(-1,-len(zipTuple)-1,-1): #Example of indexing from the end to the beginning of the individual tuple
    print(newcount, zipTuple[i])
    newcount +=1

print("")
print("The new order is after indexing from the end to the beginning of Cities codes is")
for i in range(-1,-len(compTuple[0])-1,-1): #Example of indexing from the end to the beginning of the Composite tuple
    print(compTuple[0][i])


print ("----------------------------------------------------------------------------------------------------")

#Example Format Requested but for Tuples
print()
entries = len(compTuple[0] +compTuple[1]) #Count number of Total Unique Entries in tuple
print("Listing of Cities & Zip Codes",compTuple,"\n")
print(f"Total Unique Entries: {entries}","\n")
count =1
for i in range (len(cityTuple)):
    print("City #:",count,cityTuple[i],"ZipCode#",count,zipTuple[i],)  # Genereates all Cities and Zip codes right besdies them with a tuple now
    count+=1 

print ("----------------------------------------------------------------------------------------------------")








