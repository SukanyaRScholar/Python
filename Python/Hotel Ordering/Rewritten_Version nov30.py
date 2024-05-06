# importing dictionary from collections
from collections import defaultdict
# import pdb

tbl ={} # declaring a dict
readConfig = open("config.txt", 'r') # to read the config.txt file
data = readConfig.readlines()
readConfig.close() # close the file

# writing the read data into a dict
for i in range(len(data)):
    oneLine = data[i].strip('\n')  # removing the next line escape sequence
    oneLine = oneLine.strip(" ")  # removing the space
    oneLine = oneLine.split(" ")
    #     print(oneLine)
    tbl[oneLine[0]] = int(oneLine[1]) # storing the values converting the max count to integer


# creating a class for menu item

class MenuItem:

    def __init__(self, item_code='', name='', price=''): # constructor with 3 arguments
        self.item_code = item_code
        self.name = name
        self.price = price

    # method to get the item code
    def getitemcode(self):
        return self.item_code

    # method to get the name
    def getname(self):
        return self.name

    # method to get the price of the menu
    def getprice(self):
        return self.price

    # to return the values
    def __str__(self):
        return self.item_code + " " + self.name + " " + str(self.price)


# Declaring class menu
class Menu:

    readMenu = open("menu.txt", 'r') # reading the menu text file
    data = readMenu.readlines()
    readMenu.close()  # closing the text file
    menulist = defaultdict(list)  # menu list is a dict

    for i in range(len(data)):
        aLine = data[i].strip('\n')
        aLine = aLine.strip(' ')
        aLine = aLine.split(' ')
        #     mnu[aLine[0]] = mnu[aLine[1:]]
        mnuitem = MenuItem() # instantiate an object of MenuItem class
        mnuitem.item_code = aLine[0]
        mnuitem.name = aLine[1] # menu item name is in the index 1 of aline in the menu
        mnuitem.price = float(aLine[2])  # price is stored as float
        menulist[mnuitem.getitemcode()].append(mnuitem.getname())  # updating instances with required menu details
        menulist[mnuitem.getitemcode()].append(mnuitem.getprice())

    def getMenu(self):
        return self.menulist

    def __str__(self):
        return self.menulist


# creating a class for order. this is a static class. The orders are stored in a list
class Order:
    orderlist = defaultdict(list)


# creating the class table. it has the status, total guests, party count and orderlist
class Table:

    def __init__(self): # default constructor
        self.status = {}
        self.totalguest = 0
        self.partyCount = {}  # count of ppl in a user defined party
        self.orderlist = Order().orderlist # instance of Order class- orderlist variable

    # class assigntable to compare the table selected and the max people count value for that table
    def assigntable(self,argselectedTable, argpartyCount):
        # pdb.set_trace()
        if argselectedTable not in self.status.keys(): # if table number not in the available
            if tbl[argselectedTable] >= int(partyCount):
                self.status[argselectedTable] = False # assigning boolean value false here
                self.partyCount[argselectedTable] = argpartyCount
                self.totalguest = tbl[argselectedTable]
                print('Party of {} assigned to Table {}'.format(argpartyCount, argselectedTable))
            elif tbl[argselectedTable] != int(partyCount): # if count exceeds the max
                print ('Sorry, max {} seats in Table {}!'.format(tbl[argselectedTable], argselectedTable))
        else:
            print("{} already occupied!".format(argselectedTable)) # if the table is occupied having boolean false

    # defining a class takeorder with two arguments- table number and orders
    def takeorder(self, argselectedTable, argInputOrder):

        temp_orders = [] # creating a temporary list of the orders
        if argselectedTable  in self.status.keys():
            if argselectedTable in self.orderlist.keys():
                for i in argInputOrder:
                    if i in menu.keys():
                        self.orderlist[argselectedTable].append(i)
                        temp_orders.append(i) # if item in list, it gets added to the temp listy
                    else:
                        print("No item with code {}".format(i))
                print(" {} additional items ordered for Table {}".format(len(temp_orders), argselectedTable))
            else:
                # pdb.set_trace()
                for i in argInputOrder:
                    if i in menu.keys():
                        self.orderlist[argselectedTable].append(i)
                        temp_orders.append(i)
                    else:
                        print("No item with code {}".format(i)) # if the code is not available in the menu
                print("{} items ordered for Table {}".format(len(temp_orders), argselectedTable))
        else:
            # pdb.set_trace()
            print("No party assigned to table {} ".format(argselectedTable)) # if the boolean is false under status

    # defining a method with two arguments
    def checkoutOrder(self, argselectedTable, argpartyCount):
        if argselectedTable in self.status.keys():
            if self.status[argselectedTable]: # only if the tables are served
                print("Table {} is closed. Here is the bill.".format(argselectedTable))
                self.calculateTotal(argselectedTable, argpartyCount)
                self.status.pop(argselectedTable)
                self.orderlist.pop(argselectedTable)
            else:
                print("Food not served for Table {}".format(argselectedTable))  # if tables are not served but assigned
        else:
            print("No Party assigned to Table {}".format(argselectedTable)) # if tables are not assigned to party

    def serveTable(self, argselectedTable):
        if argselectedTable in self.status.keys():
            if len(self.orderlist)>0 :
                self.status[argselectedTable] = True
                print ("Food served in table {}".format(argselectedTable))

            else:
                print("Order not placed at Table {}".format(argselectedTable)) # order not served when order not placed
        else:  # If food served without assigning table
            print("No Party assigned to Table {}".format(argselectedTable))  # if tables are not assigned to party

    def calculateTotal(self, argselectedTable, argpartyCount):

        total = 0  # initializing the total with zero
        # pdb.set_trace()
        print("Receipt Table# {} Party {}".format(argselectedTable, argpartyCount[argselectedTable]))

        for food_and_price in self.orderlist[argselectedTable]:
            print(food_and_price, '\t', menu[food_and_price][0], '\t', menu[food_and_price][1])
            price = menu[food_and_price][1]
            total = total + price
        print('\t', 'Total: $', round(total,2))  # rounding off to two digits


continueOption = 'y'  # assigning a default value (it can have any value other than x)
menu = Menu().getMenu()  # instantiating the Menu object and calling the get menu method
tableObject = Table()   # new object of the Table class for each table
while continueOption != 'x': # Start the loop and allow user to enter different options
    user_input = input("Enter your command: ").upper()  # prompting user for command
    user_input = user_input.split(" ")  # user input is split into strings

    selectedTable = user_input[0]  # user input first index is stored as table number

    if user_input[0] not in tbl.keys():  # if the user defined input not in the pre existing table numbers
        print ("Invalid table number. Please re-enter")
        continue  # loops through again until user enter correct value

    if len(user_input)<2: # if user only enters numbers or letters without giving complete command
        print("Enter complete command")
        continue

    if len(user_input) <= 2 and user_input[1].startswith('P'): # to find the party count
        inputOption = user_input[1][0:1] # the order is the index 1 , the string from its 1st index.
        partyCount = user_input[1][1:]
        if not user_input[1][1:].isnumeric():
            print("Invalid entry. Please re-enter")
            continue
    else:
        inputOption = user_input[1]

    if user_input[1].startswith('O'): # when order command is given
        inputOrder = [] # more than one orders for a table are stored in a list
        # pdb.set_trace()
        if len(user_input[1])>1:
            print("Invalid entry. Command should be only P or O or S or C after table num")
            continue
        for i in user_input[2:]:
            # if i in menu.keys():
            inputOrder.append(i)  # orders are added to the list

    if user_input[1].startswith('P'):
        if len(user_input) > 2: # if assigning party command has more than two inputs, gives error
            print("Invalid Input. Please try again")
            continue  # prompts the user to enter correct values and loops through until user enters correctly
        else:
            partyCount = user_input[1][1:]
            tableObject.assigntable(selectedTable, partyCount)  # assigning the assign command to the table object
    elif user_input[1].startswith('O'):
        # order table command calls the take order method of class table
        tableObject.takeorder(selectedTable, inputOrder)
    elif user_input[1].startswith('S'):  # If the table is served, this table objects serve table method is called
        if len(user_input[1])>1 or len(user_input)>2:
            print("Invalid entry. Command should be only P or O or S or C after table num")
            continue
        else:
            tableObject.serveTable(selectedTable)
    elif user_input[1].startswith('C') :  # if the customer closes the order, the bill is generated
        if len(user_input[1])>1  or len(user_input)>2:
            print("Invalid entry. Command should be only P or O or S or C after table num")
            continue
        else:
            tableObject.checkoutOrder(selectedTable, tableObject.partyCount)

    else:
        print("Invalid entry")
        continue
    # this loops through until the user enters x. clicking any other key keeps the program running
    continueOption = input("Press x to exit or any key to continue ").lower()




