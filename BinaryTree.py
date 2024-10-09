from NodeClass import NodeClass

tree = None

#first value
dig = int(input("Type a positive value (or not to end): "))

#start the tree
if dig > 0:
    tree = NodeClass(dig)

    #new value
    dig = int(input("Type a positive value (or not to end): "))

while dig > 0:
    #insert into the tree
    tree.AddValue(dig)

    #new value
    dig = int(input("Type a positive value (or not to end): "))

#tree.ShowTree()
tree.ShowPath()

#to find
dig = int(input("Type a positive value to find in the tree (or not to end): "))

while dig > 0:
    #try to find
    f = tree.Find(dig)
    if f == None:
        print("Value does not exist!")
    else:
        print("Value Found!")

    #new value
    dig = int(input("Type a positive value to find in the tree (or not to end): "))