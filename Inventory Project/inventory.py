
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        #give the class the listed attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        #print the cost of the shoe and return the value
        return float(self.cost)

    def get_quantity(self):
        #print the quantity of the shoe and return it
        return int(self.quantity)

    def __str__(self):
        #return the shoe information as a string (using string formatting)
        return f"Country = {self.country} \nCode = {self.code} \nProduct = {self.product} \nCost = {self.cost} \nQuantity = {self.quantity}"


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
#empty list to store the shoe objects
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
        #open the file as read only
    f = open('inventory.txt', 'r')
    #iterate through the lines in the file
    for line in f:
        #strip the \n character and split the line into a list by the commas
        line = line.strip('\n').split(',')
        #ensuring the first line is skipped
        if line[0] != 'Country':
            try:
                #trying to create a shoe object from the line using each item in the list
                shoe_object = Shoe(line[0], line[1], line[2], float(line[3]), int(line[4]))
                shoe_list.append(shoe_object)
            except IndexError:
                #anticipating an index error - eg too few items in the list (for example if a comma had been missed
                #printing the line that produced the error
                print(f"There is not enough items in the following line: \n{line} \nPlease fix this and try again")
            except TypeError:
                #anticipating a type error, eg if the cost or quantity could not be converted into a float or an integer respectively
                #printing the line that produced the error
                print("Please ensure that the cost and quantity are in the correct position. The error appears in the following line: \n{line}")

    f.close() 
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

def capture_shoes():
    #take input for each of the attributes required to make a shoe object
    #cost is converted to a float and quantity is converted to an integer
    country = input("Please enter the shoe's country: ")
    code = input("Please enter the shoes code: ")
    product = input("Please enter the product name: ")
    cost = float(input("Please enter the shoes cost: "))
    quantity= int(input("Please enter the shoes quantity: "))

    #creating a shoe object using the inputs and adding it to the shoe list
    shoe_object = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_object)
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    print(shoe_list)
    #I don't understand the problem with this function - is it printing in the wrong format? 
    #calling the __str__ method for each object in the shoe list
    for i in shoe_list:
        #printing an arbitrary item number to seperate out the objects
        print(f"\nItem {shoe_list.index(i)}:\n")
        print(i.__str__())
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''


def re_stock():
    #set a value for the quantity variable and an item for the shoe variable (the quantity for the first item in the list)
    quantity = shoe_list[0].get_quantity()
    shoe = shoe_list[0]
    #iterate through the shoe list 
    for i in shoe_list:
        #chek to see if the quantity in each object is less than the current quantity value
        if i.get_quantity() < quantity:
            #if it is less, reassign the quantity varaible to be the new, lower quantity, and reassign the shoe variable to the object with the lower quantity
            shoe = i
            quantity = i.get_quantity()
    #print the details of the object with the lowest quantity
    print(f"{shoe.__str__()} is the shoe with the lowest quantity.")
    #create a while loop so that the user can be asked again if they would like to update the quantity of the shoe if they enter an invalid input
    while True:
        update_quantity = input("Would you like to update the quantity of this shoe? y/n ")
        if update_quantity == 'y':
            #take input for the new quantity of the shoe and reassign the value for the objects quantity
            new_quantity = int(input("Please enter the new quantity of the shoe: "))
            shoe.quantity = new_quantity
            #open the text file
            f = open('inventory.txt', 'r')
            #create empty list to store the contents of the text file for when it is overwritten. 
            store_inventory = []
            #iterate through the lines in the file
            for line in f:
                line = line.strip('\n').split(',')
                if line[1] == shoe.code:
                    #check for the object that needs the quantiy updated using the code. Change the quantity in the list of the line
                    line[4] = str(new_quantity)
                #add the list created from the line to the store_inventory list
                store_inventory.append(line)
            #close the file and open it again to write
            f.close()
            f = open('inventory.txt', 'w')
            #for each item in the inventory write it to the file, including the shoe with the updated quantity
            for i in store_inventory:
                f.write(','.join(i)+'\n')
            f.close()
            #exit the while loop
            break
        elif update_quantity == 'n':
            #if the user chooses not to update the quantity, exit the while loop without doing anything
            break
        else:
            #if any invalid input is entered, print a message, go to the top of the while loop
            print("Invalid response. Please enter 'y' or 'n'. \n")

    
        
        
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe():
    #this function is working for me - is it printing the result in the wrong format? 
    code_found = 0
    shoe_code = 0
    while shoe_code != '-1':
        #take input for the code of the shoe to look up
        shoe_code = input("Please enter the code of the shoe that you would like to view, or -1 to exit: ")
        #iterate through the shoe_list and check the codes againt the inputted code
        for i in shoe_list:
            if i.code == shoe_code:
                #when the code matches,print the details of the shoe, and leave the while loop
                code_found = 1
                print(i.__str__())
                break
        if code_found == 0:
            #if the code doesn't match any of the codes in the inventory, print an error message and go to the top of the while loop to ask again. 
            print("Code entered did not match any of the shoes in the inventory")
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    #this function was also working for me - I have changed the print format slightly to make it clearer now
    #iterate through each shoe in the inventory list and calculate the value. Print the value for each item. 
    for i in shoe_list:
        value = float(i.get_cost())*int(i.get_quantity())
        print(f"The value for shoe {i.code} is: = R{value}")
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    #assign a value to the quantity variable (the quantity of the shoe at the 0th index) and the shoe variable (object at 0th index)
    quantity = shoe_list[0].get_quantity()
    shoe = shoe_list[0]
    #iterate through all the objects in shoe list, and reassign the quantity and shoe variables when a shoe with a higher quantity is found.
    #after going through the whole list, the highest quantity and its shoe will be stored
    for i in shoe_list:
        if i.get_quantity() > quantity:
            shoe = i
            quantity = i.get_quantity()
    #print that this shoe is for sale. 
    print(f"{shoe.__str__()}\n is for sale!.")
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

#create while loop for the menu
read_shoes_data()
while True:
    choice = input("""Please enter what task you would like to do:
r - read shoes data from the inventory file
c - enter information to add a shoe to inventory
va - view all shoes in inventory
rs - re-stock the shoe with the lowest quantity
s - search for a shoe
v - view the total value of the stock of each shoe
h - view the shoe with the highest quantity
e - exit
""")
    #go through possible options to choose using if, elif and else statements and using the functions. 
    if choice == 'r':
        read_shoes_data()
        print("Data has been read.")
    elif choice == 'c':
        capture_shoes()
    elif choice == 'va':
        view_all()
    elif choice == 'rs':
        re_stock()
    elif choice == 's':
        search_shoe()
    elif choice == 'v':
        value_per_item()
    elif choice == 'h':
        highest_qty()
    elif choice == 'e':
        print('Goodbye')
        break
    else:
        print("Invalid choice entered")





    
