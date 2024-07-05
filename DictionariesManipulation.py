#Chidi Nna
#Program #6
#Python Programming CSCI-6651-01
#This code will provide you with some practice in working with DIctionaries.

my_dict = {"January": 31, "February": 29, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

full_month = []  #lists to append whhich months fit into whch catagory of lists so i can append the values 
avg_month = []
not_full_month = []

for month, days in my_dict.items():
    if isinstance(days, int):       # Had to google this because it wouldnt let me use append for iteraring through the dictionart items 
        if days < 30: #stores months which 29  days in not full momths
            not_full_month.append(month)
        elif days == 30:  #stores months with 30  days in avg months
            avg_month.append(month)
        else:  #stores months which more than 30  days in not full momths
            full_month.append(month)

not_full_month_dict = {month: my_dict[month] for month in not_full_month}   #value associated with each key is the number of days for that month obtained from the original my_dict dictionary
avg_month_dict = {month: my_dict[month] for month in avg_month}               # does this for all my created dictionaries
full_month_dict = {month: my_dict[month] for month in full_month}

print("Months with less than 30 days:", not_full_month_dict)
print("Months with 30 days:", avg_month_dict)
print("Months with 31 days:", full_month_dict)


sameletter = () 

for month in my_dict:
    first_letter = month[0]  # Get the first letter of the month
    if first_letter not in sameletter:
        sameletter[first_letter] = [month]  # Create a new list for the first letter
    else:
        sameletter[first_letter].append(month) # adds month with the same first letter found


for firstletter, months in sameletter.items():
    print(months)


Lastletter =()
for month in my_dict:
    last_letter = month[-1]  # Get the first letter of the month
    if first_letter not in sameletter:
    else:
        Lastletter[last_letter].append(month) # adds month with the same first letter found


for firstletter, months in Lastletter.items():
    print(months)

