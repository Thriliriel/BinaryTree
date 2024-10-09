class NodeClass:
    def __init__(self, value):
        self.value = value
        self.childrenLeft = None
        self.childrenRight = None

    #to add value, need to keep the binary tree structure
    def AddValue(self, value):
        #if the value is lower or equal
        if value <= self.value:
            #if left is free, add
            if self.childrenLeft == None:
                self.childrenLeft = NodeClass(value)
            #else, need to try next level
            else:
                self.childrenLeft.AddValue(value)
        #if the value is higher
        elif value > self.value:
            #if right is free, add
            if self.childrenRight == None:
                self.childrenRight = NodeClass(value)
            #else, need to try next level
            else:
                self.childrenRight.AddValue(value)

    #show the tree
    def ShowTree(self):
        print(self.value)
        if self.childrenLeft != None:
            self.childrenLeft.ShowTree()
        if self.childrenRight != None:
            self.childrenRight.ShowTree()

    #show the tree path
    def ShowPath(self):
        if self.childrenLeft != None:
            self.childrenLeft.ShowPath()
        print(self.value)
        if self.childrenRight != None:
            self.childrenRight.ShowPath()

    #find a value in the tree
    def Find(self, value):
        if value == self.value:
            return self.value
        elif value < self.value and self.childrenLeft != None:
            return self.childrenLeft.Find(value)
        elif value > self.value and self.childrenRight != None:
            return self.childrenRight.Find(value)
        else:
            return None