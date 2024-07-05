#Chidi Nna
#Script Programming/Python
#Program 2 
#Write a python module that will allow a user to input a String that will represent a person's First Name & Last Name.
#The First Name and Last Name will be separated by a space.
#The names may or may not be capitalized.
#Demonstrate how you would...



# Question 1 Separate the two names and only moves forward if it is 

while True:
    fullname = input("Enter First & Last Name Separated by a SPACE: ")

    firstandLast = fullname.split()

    if fullname.count(' ') != 1:
        print("Please enter exactly two names separated by a space.")
        continue

    fname, lname = firstandLast



    if fname.isalpha():     #2.  Check to ensure they only contain alpha characters and only moves forward if it is 
        print("First Name is valid.")
    else:
        print("Invalid Entry - First Name Contains A Numeric!")
        continue

    if lname.isalpha():
        print("Last Name is valid.")
    else:
        print("Invalid Entry - Last Name Contains A Numeric!")
        continue
    


    if fname == lname: #3 Check to ensure two names are given and are different and only moves forward iff they are 
        print("First and Last Names Have to be Different")
        continue
    else:
        print("First and Last Names are different.")

    cap_fname = fname.capitalize()# 4 capitalize the first letter of each name 
    cap_lname = lname.capitalize()

    print("First Name:", cap_fname)
    print("Last Name:", cap_lname)
    
    break  #code ends after the name 
