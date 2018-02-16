import re

#define the variables
ipAddr = []
subMask = []
broadAddr = []

#begin code

print("#############################################\n"
      + "@When entering IP Addresses and Subnet Masks,\n"
      + "@Be sure to enter them in the form:\n"
      + "@ '192.168.1.0'\n"
      + "############################################\n\n")

#function to ask user to enter IP Address and separate its octets

def GetIPSeparate():

    ip = input("What is the IP Address you would like to enter?\n")

    start = ip.split(".",4)
    print("\n")
    return start

#function to ask user to enter Subnet Mask and separate its octets

def GetSubSeparate():

    sub = input("What is the Subnet Mask you would like to enter?\n")

    start = sub.split(".",4)
    print("\n\n\n\n")

    return start

#acquire values for the IP address and Subnet Mask
    
ipAddr = GetIPSeparate()
subMask = GetSubSeparate()

#Now lets begin building the Network Address

i = 0
magicN = 0
numList = [0]

for sub in subMask:
    #If the selected octet in the SubMask is 255...
    if sub == '255':
        #Make the corresponding octet in the NetAddr equal to the corresponding octet in the ipAddress
        broadAddr.append(ipAddr[i])
        i = i + 1
    #If the selected octet in the SubMask is 0...
    elif sub == '0':
        #Make the corresponding octet in the NetAddr equal to 0
        broadAddr.append('0')
        i = i + 1
    #If the selected octet in the SubMask is not 255 OR 0...
    else:
        #find the Magic Number...
        magicN = 256 - int(ipAddr[i])
        #Continually add the magicN up until it is one addition greater than the ipAddr value...
        while numList[-1] < int(ipAddr[i]):
            numList.append(numList[-1] + magicN)
        #Select the number that is equal to, or as close to the value of the ipAddress...
        broadAddr.append(str(numList[len(numList) - 1]))

#Print Everything. EVERYTHING. PRINT ALL THE PRINTS.

print("The Network Address for this network is: ")
print(ipAddr[0] + "." + ipAddr[1] + "." + ipAddr[2] + "." + ipAddr[3] + "\n")
print("The Subnet Mask for this network is: ")
print(subMask[0] + "." + subMask[1] + "." + subMask[2] + "." + subMask[3] + "\n")
print("The Broadcast Address for this network is: ")
print(broadAddr[0] + "." + broadAddr[1] + "." + broadAddr[2] + "." + broadAddr[3] + "\n")

#Now sit back and enjoy some coffee.



































































#Shit...I probably should include some sort of error for if the user puts in anything but numbers.
#Or if they mis-type the IP address.

































































#...Nah. *sips coffee and calls it a day*
