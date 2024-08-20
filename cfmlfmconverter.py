#define the variables
mode=0
cfm=0
lfm=0
area=0

#define the functions
def cfm2lfm():
    global cfm, lfm, area
    cfm=int(input("Please enter the CFM: "))
    area=int(input("Please enter the area in ft^2: "))
    lfm=cfm/area
    print(lfm)

def lfm2cfm():
    global cfm, lfm, area
    lfm=int(input("Please enter the LFM: "))
    area=int(input("Please enter the area in ft^2: "))
    cfm=lfm*area
    print(cfm)

#Run the main stuff
while True:
    print("Please select from the options below:")
    print("(1) Convert CFM to LFM")
    print("(2) Convert LFM to CFM")
    print("(3) Quit")
    mode=int(input("Selection: "))

    if mode==1:
        cfm2lfm()

    elif mode==2:
        lfm2cfm()

    elif mode==3:
        exit()

    else:
        print("Invalid option, please try again")