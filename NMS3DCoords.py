###
### NMS_SpacialCoordinatesConverter
### BY Edwiersma - 8/30/2017
###

#Promts the user to input Data for an axis.
def AskCoord(axis,limits):
  return input('Enter a vaue between 0 and '+str(limits[axis])+' for the '+axis+' coordinate:')

#Gather and process user Input
def GatherCoord():
  hexList = [];
  inputs = {"X":-1,"Y":-1,"Z":-1}
  limits = {"X":4095,"Y":255,"Z":4095}
  for axis, in ["X","Y","Z"]:
    inputs[axis] = AskCoord(axis,limits)
    while inputs[axis] <= 0 or inputs[axis] >= limits[axis]:
      print("Please enter Valid "+axis+" coordinate between 0 and "+str(limits[axis]))
      inputs[axis] = AskCoord(axis,limits)
    hexList.append(CoordToHex(inputs[axis]))
  return(hexList[0]+":"+hexList[1]+":"+hexList[2]+":0000")

#Converts Decimal Data to Hex Values 
def CoordToHex(coord):
  hexString = hex(coord).split('x')[-1].upper()
  for d in range(4-len(hexString)):
    hexString = "0"+hexString
  return hexString

#Run Script
def run():
  print("Welcome Explorer,")
  while True:
    print("Initialzing spacial coordinates converter\n...")
    output = GatherCoord()
    print("\nNo Man's Sky coordinates of given location are: "+output+"\n")
    
run()
