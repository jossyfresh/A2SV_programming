class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    # def __init__(self,data):
    #     self.data = data
    #     self.next = None

class MyLinkedList:
    
    def __init__(self):
        self.head = None
        self.count = 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
            return -1

        temp = self.head

        for _ in range(0, index):
            temp = temp.next

        return temp.data
    def addAtHead(self, val: int) -> None:
        temp = self.head
        temp1 = node(val)
        temp1.next = temp
        self.head = temp1
        self.count+=1
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.count,val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return

        temp = self.head
        temp1 = node(val)
        if index <= 0:
            temp1.next = temp
            self.head = temp1
        else:
            for _ in range(index - 1):
                temp = temp.next
            temp1.next = temp.next
            temp.next = temp1

        self.count += 1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.count:
            return

        temp = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                temp = temp.next
            temp.next = temp.next.next

        self.count -= 1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)