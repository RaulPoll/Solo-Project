import math

#This function displays a greeting message for the user 
def Greeting():
    userName = input("\nEnter username: ")
    print(f"\nGreetings {userName}! \nPlease enjoy using this program.")


def EventList():
    # List length from user input
    listLength = int(input("\nEnter the number of events to calculate: "))
    listLength *= 2 # Doubles list size for accomodating event name-time
    # List for holding event variables
    list = []
    for i in range(1, listLength + 1, 2):
        # Event name input
        event = input("\nEnter name of event: ")
        list.append(event)
        # Time format user input
        TimeFormat = int(input("hrs->mins press (1), or mins->hrs press (2): "))
        # User specified conversion hrs->mins
        if TimeFormat == 1:
            TimeInput = input("Enter time in hours: ")
            # Conversion hrs->mins
            TimeInput = hrsToMins(TimeInput)
        # User specified conversion mins->hrs
        elif TimeFormat == 2: 
            TimeInput = input("Enter time in minutes: ")
            # Conversion mins->hrs
            TimeInput = minsToHrs(TimeInput)
        list.append(TimeInput)  
        print(list)
    print("""\n################ \nList is done! \n################""")
    return list
# From hour to minutes
def hrsToMins(h):
    h = float(h)
    h *= 60
    h = math.floor(h)
    return h

# Minutes to hours
def minsToHrs(m):
    m = int(m)
    m /= 60
##    m = round(m, 2)
    return m 
                                    
# Main function
Greeting()
EventList()
