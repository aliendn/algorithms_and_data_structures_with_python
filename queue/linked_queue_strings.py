class LinkedQueueOfStrings:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None
    
    def push(self, item):
        old_last = self.last
        self.last = self.Node(item)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

    def pop(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.first.item
        self.first = self.first.next
        if self.is_empty():
            self.last = None
        return item


if __name__ == "__main__":
    stack = LinkedQueueOfStrings()
    print("Do you want to start your stack? (1, 0)")
    print("If you insert 0, the program will stop: ")
    start_point = int(input("? : "))
    
    while start_point == 1:
        insert = int(input("Do you want to push your item? (1, 0): "))
        if insert == 1:
            push = input("Push: ")
            stack.push(push)
        
        remove = int(input("Do you want to pull your item? (1, 0): "))
        if remove == 1:
            try:
                print(f"You removed: {stack.pop()}")
            except IndexError:
                print("There is no item. Please continue and add item to the stack!")

        start_point = int(input("Continue (1, 0)?: "))
    
    print("Thanks a lot!")