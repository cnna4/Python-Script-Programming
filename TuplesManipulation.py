#Chidi Nna
#Program #4
#Python Programming CSCI-6651-01
#Assignment will be focused on Lists and List Manipulations with A repeat using tuples


# Made up coordinates
PointList = ['MA', 'CT', 'NH', 'NY', 'RI', 'VT']
myCoordsList = [(1.1, 1.0, 1.5), (2.0, 2.1, 2.2), (3.1, 3.0, 3.5), (4.0, 4.1, 4.2), (5.1, 5.0, 5.5), (6.0, 6.1, 6.2)]

distanceList = []  # empty distance List
for i in range(len(myCoordsList) - 1):  # iterates over the coordinate List
    p1 = myCoordsList[i]   # first element
    p2 = myCoordsList[i + 1]  # second element
    distance = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2) ** 0.5  # based off of The Distance is computed as (x**2+y**2+z**)**.5
    distanceList.append(distance)

# iterates through PointList to get the List of states from one to another and stores them in distancenames
distanceNames = [f'Distance From {PointList[i]} To {PointList[i + 1]} is ' for i in range(len(PointList) - 1)]

# Combines the names and distances into one list
distanceList = [[distanceNames[i], distanceList[i]] for i in range(len(distanceNames))]

print("INitial  Lists:")
print("State List:", PointList)
print("Cooridnate Listt:", myCoordsList)


print("List of Distances:\n")
for item in distanceList:
    print(item)

print("-----------------------------------------------------------------------------------------------------")

# Made up coordinates
PointList = ['MA', 'CT', 'NH', 'NY', 'RI', 'VT']
myCoordsList = [(1.1, 1.0, 1.5), (2.0, 2.1, 2.2), (3.1, 3.0, 3.5), (4.0, 4.1, 4.2), (5.1, 5.0, 5.5), (6.0, 6.1, 6.2)]

distanceList = []  # empty distance List
for i in range(len(myCoordsList) - 1):  # iterates over the coordinate List
    p1 = myCoordsList[i]   # first element
    p2 = myCoordsList[i + 1]  # second element
    distance = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2) ** 0.5  # based off of The Distance is computed as (x**2+y**2+z**)**.5
    distanceList.append((f'Distance From {PointList[i]} To {PointList[i + 1]} is ', [distance, p1, p2]))

print("List of Distances but using tuples")
for item in distanceList:
    print(item)


#was confused on the tuples part of this assigment i beleive i did it right but not completely sure this time