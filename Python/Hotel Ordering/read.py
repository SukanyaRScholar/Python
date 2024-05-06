import MenuItem
from collections import defaultdict

def read_load_Menu() :
    readFile = open("menu.txt", "r") # to read lines as string
    rawData = readFile.readlines()
    readFile.close()

    m = []
    list1 = []  # temp list to strip the data off \n [ ] '
    menu = MenuItem.Menu( m )
    for i in rawData:
        i = i.splitlines()  # removes \n from the list
        list1.append(i)

    for item in list1:
        item = str(item)
        item = item.strip('[]\'')  # list [,] &'
        item = item.split(' ')
        item[2] = float(item[2])  # convert price from str to float
        #menu.append(item)
        bufMI = MenuItem.MenuItem( item[0], item[1], item[2]) #create the menuitem
        menu.addItem( bufMI )
    #print("List of Menu:", menu)
    return menu

mainMenu = read_load_Menu()
for i in mainMenu:
    if isinstance(i, MenuItem.MenuItem):
        print( i )
    else:
        print( "usual list")

def read_load_Table_Info() :
    readFile = open("config.txt", "r")
    rawData = readFile.readlines()
    # reads each line as string & then
    #   returns a list with the read lines
    readFile.close()

    bufferTables = []
    list1 = []  # temp list to strip the data off \n [ ] '
    for i in rawData:
        i = i.splitlines()  # removes \n from the list
        list1.append(i)

    for item in list1:
        item = str(item)
        item = item.strip('[]\'')  # list [,] &'
        item = item.split(' ')
        item[0] = int( item[0] )
        item[1] = int( item[1] )  # convert price from str to int
        #menu.append(item)
        #print( item )
        bufT = MenuItem.Table(item[0], item[1], mainMenu) #create the menuitem
        bufferTables.append( bufT )
    #print("List of Menu:", menu)
    return bufferTables


def read_load_table_updated():
    readConfig = open("config.txt", 'r')
    data = readConfig.readlines()
    readConfig.close()
    tbl = []

    for i in range(len(data)):
        oneLine = data[i].strip('\n')
        oneLine = oneLine.strip(" ")
        oneLine = oneLine.split(" ")
        #     print(oneLine)
        tbl.append(MenuItem.Table(int(oneLine[0]), int(oneLine[1]), []))
        # tbl[oneLine[0]] = int(oneLine[1])

    return tbl

tables = read_load_table_updated()
# for i in range(len(tables)):
#     print(tables[i].getTableNum())


def getUserEntry() :
    ui = input("Enter your command <table_number command>:")
    ui = ui.split(" ")
    currentTable=0
    # print( ui, " type of ui[0]", type(ui[0]), ui[0].isdigit() )
    if not ui[0].isdigit():
        currentTable = -1
    else:  # made sure first entered command is a number
        for i in range(len(tables)):
            if int(tables[i].getTableNum()) != int(ui[0]):
                currentTable = -1
            else:# user entered an existing table number
                currentTable = i #ui[0]
                break
    return currentTable, ui


while True :
    tblNum, cmd = getUserEntry()
    tblNum = int(tblNum)
    if tblNum == -1:
        print("Entered invalid table number")
        continue
    else:
        if cmd[1].startswith('P') or cmd[1].startswith('p'):
            # expecting tableNumber P numberOfPPL
            # waiter is requesting to seat
            tables[tblNum].assign(int(cmd[2]))

        elif cmd[1].startswith('C') or cmd[1].startswith('c'):
            # waiter is requesting to close the bill
            #print("now calling closing bill for table #", tblNum)
            tables[tblNum].closeBill()

        elif cmd[1].startswith('S') or cmd[1].startswith('s'):
            # waiter is requesting to serve the food to a table
            #print("now calling serving for table #", tblNum)
            tables[tblNum].serve()

        elif cmd[1].startswith('O') or cmd[1].startswith('o'):
            buffer = cmd[2:]
            #print("now calling place order", buffer, "for table #", tblNum)
            tables[tblNum].placeOrder( buffer )

        else:#gave valid table number but invalid command
            print("Allowed Commands P(seat), O(order), S(serve), C(close)")
        # for i in tables:
        #     print( i )

