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

def main():
    global cfm, lfm, area
    print("Please select the conversion you want to do:")
    print("(1) Convert CFM to LFM")
    print(
    mode=int(input("

#Run the main stuff
