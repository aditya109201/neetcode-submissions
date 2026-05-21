class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        while index != 0 and curr:
            index = index - 1
            curr = curr.next

        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = ListNode(val)

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
            
        curr = self.head
        prev = None
        while index != 0 and curr:
            prev = curr
            curr = curr.next
            index = index - 1

        if curr and index == 0:
            prev.next = curr.next
            return True

        return False

    def getValues(self) -> List[int]:
        curr = self.head
        arr = []

        while curr:
            arr.append(curr.val)
            curr = curr.next        

        return arr