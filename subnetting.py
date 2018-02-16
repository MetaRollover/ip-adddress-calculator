import re

#Define the variables
ipAddr = []
subMask = []
subAddr = []

#Begin code

print("#############################################\n"
      + "@When entering IP Addresses and Subnet Masks,\n"
      + "@Be sure to enter them in the form:\n"
      + "@ '192.168.1.0'\n"
      + "############################################\n\n")

#Function to ask user to enter IP Address and separate its octets

def GetIPSeparate():

    ip = input("What is the IP Address you would like to enter?\n")

    start = ip.split(".",4)
    print("\n")
    return start

#Function to ask user to enter Subnet Mask and separate its octets

def GetSubSeparate():

    sub = input("What is the Subnet Mask you would like to enter?\n")

    start = sub.split(".",4)
    print("\n\n\n\n")

    return start

#Acquire values for the IP address and Subnet Mask
    
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
        subAddr.append(ipAddr[i])
        i = i + 1
    #If the selected octet in the SubMask is 0...
    elif sub == '0':
        #Make the corresponding octet in the NetAddr equal to 0
        subAddr.append('0')
        i = i + 1
    #If the selected octet in the SubMask is not 255 OR 0...
    else:
        #Find the Magic Number...
        magicN = 256 - int(ipAddr[i])
        #Continually add the magicN up until it is one addition greater than the ipAddr value...
        while numList[-1] < int(ipAddr[i]):
            numList.append(numList[-1] + magicN)
        #Select the number that is equal to, or as close to the value of the ipAddress...
        subAddr.append(str(numList[len(numList) - 1]))

#Print Everything. EVERYTHING. PRINT ALL THE PRINTS.

print("The Network Address is: ")
print(ipAddr[0] + "." + ipAddr[1] + "." + ipAddr[2] + "." + ipAddr[3] + "\n")
print("The Subnet Mask for this network is: ")
print(subMask[0] + "." + subMask[1] + "." + subMask[2] + "." + subMask[3] + "\n")
print("The Subnet Address is: ")
print(subAddr[0] + "." + subAddr[1] + "." + subAddr[2] + "." + subAddr[3] + "\n")

#Good enough for now.
