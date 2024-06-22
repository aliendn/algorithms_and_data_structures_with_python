class FixedCapacityStackOfStrings:
    def __init__(self, capacity):
        self.s = [None] * capacity
        self.N = 0

    def is_empty(self):
        return self.N == 0

    def push(self, item):
        self.s[self.N] = item
        self.N += 1

    def pop(self):
        self.N -= 1
        item = self.s[self.N]
        self.s[self.N] = None
        return item

if __name__ == "__main__":
    capacity = input("give me capacity ;D : ")
    stack = FixedCapacityStackOfStrings(capacity)
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

