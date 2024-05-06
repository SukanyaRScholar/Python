empty = 1
occupied = 2
ordered = 3
served = 4
closed = 5


class MenuItem:
    def __init__(self, argC, argN, argP):
        self.code = argC
        self.name = argN
        self.price = argP

    def getCode(self):
        return self.code

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def __str__(self):
        return self.code + " " + self.name + " " + str(self.price)


class Menu:
    def __init__(self, argList):
        if isinstance( argList , list) :
            self.items = argList
        else:
            self.items = list(argList)

    def addItem(self, argMI):
        self.items.append(argMI)

    def getMenuItem(self, argMenuCode):
        for i in self.items:
            if i.getCode() == argMenuCode.upper():
                return i
        else:
            return None

    def __iter__(self):
        return iter( self.items )


class Order() :
    def __init__(self, argMenu):
        self.anOrder = []
        self.menu = argMenu

    def addItem(self, argMenuCode):
        buf = self.menu.getMenuItem(argMenuCode)
        if buf == None:
            print( "No item with code", argMenuCode)
            buf = False
        else:
            self.anOrder.append( buf )
            buf = True
        return buf

    def deleteAll(self):
        self.anOrder.clear()

    def __len__(self):
        return len(self.anOrder)

    def __str__(self):
        msg = ""
        for i in self.anOrder :
            msg = msg + i +"\n"
        return msg

    def prepareBill(self):
        #print( self.__anOrder )
        msg = ""
        for i in self.anOrder:
            msg = msg + str(i) + "\n"
        print( msg )


class Table:
    def __init__(self, argTableNumber, argMaxSeats, argMenu):
        self.tableNumber = argTableNumber
        self.maxSeats = argMaxSeats
        self.status = empty
        self.numSeated = 0
        self.order = Order(argMenu)
        #print( self )

    def __str__(self):
        return "Table #" + str(self.tableNumber) + \
               " 's status is " + str(self.status) + \
                " has " + str(self.numSeated) + "ppl seated"

    def getTableNum(self):
        return self.tableNumber

    def assign(self,argNumPpl):
        #print("inside assign & have values", self.__status, self.__numSeated)
        #print("inside assign - got command to seat ", argNumPpl, " in ", self.__tableNumber)
        if self.status == occupied or self.status == ordered or self.status == served :
            print("Table already occupied")
        elif self.status == empty and argNumPpl > self.maxSeats :
            print( "Sorry, max ONLY ", self.maxSeats, " can be assigned to ", self.tableNumber)
        elif self.status == empty and argNumPpl < self.maxSeats :
            self.status = occupied
            self.numSeated = argNumPpl
            print( "Party of ", self.numSeated, " in table #", self.tableNumber)

    def placeOrder(self, argOrder):
        if self.status == EMPTY or self.status == CLOSED:
            print("Table #", self.getTableNum()," is empty - cannot place order" )
            return

        if self.status == OCCUPIED or self.status == ORDERED or self.status == SERVED :

            msg = " items ordered for table #", self.tableNumber
            if len(self.order) == 0 :
                print(len(argOrder), msg )
            else:
                print(len(argOrder), "additional ", msg )
            count = 0
            for i in argOrder :
                if self.order.addItem( i ) :
                    count = count + 1
            print( count, "items order for table #", self.getTableNum() )
            if len(self.order) > 0:
                self.status = ORDERED

    def closeBill(self):
        if self.status == SERVED:
            print( "Table " , self.tableNumber, " Here is the bill " )
            self.order.prepareBill()
            self.status = EMPTY
            self.numSeated = 0
            #self.__order
        elif self.status == ORDERED :
            print("Table has not served food yet")
        elif self.status == OCCUPIED :
            print("Table has not even ordered yet ")
        elif self.status == EMPTY :
            print("This is an empty table. Please check your table number")

    def serve(self):
        if self.status >= OCCUPIED :
            if self.status == ORDERED :
                self.status = SERVED
            elif self.status != ORDERED :
                print( "Order not placed in table ", self.tableNumber , "yet")
            elif self.status == CLOSED :
                print("Table #" , self.tableNumber, "'s order has been closed. Please check table number")
        else:
            print("Table #" , self.tableNumber, " is currently empty")