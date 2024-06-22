class LinkedStackOfStrings:
    class Node:
        def __init__(self, item, next_node=None):
            self.item = item
            self.next = next_node

    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first is None

    def push(self, item):
        old_first = self.first
        self.first = self.Node(item)
        self.first.next = old_first

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self.first.item
        self.first = self.first.next
        return item

if __name__ == "__main__":
    stack = LinkedStackOfStrings()
    print("do you want to start your stack? (1, 0)\n if you insert 0 the program will be stopped!!")
    start_point = input("? : ")
    while int(start_point):
        insert = input("do you want to push your item? (1, 0) ")
        if int(insert):
            push = input("push : ")
            stack.push(push)
        try:
            remove = input("do you want to pull your item? (1, 0) ")
            if int(remove):
                print(f"you removed : {stack.pop()}")
        except IndexError:
            print("there is no item please continue and add item to the stack!")
        start_point = int(input("continue(1, 0)?: "))
    print("thanks a lot!")