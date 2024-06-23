class ResizingArrayStackOfStrings:
    def __init__(self) -> None:
        self.s = [None] * 1
        self.N = 0

    def is_empty(self):
        return self.N == 0

    def resize(self, capacity):
        copy = [None] * capacity
        for i in range(self.N):
            copy[i] = self.s[i]
        self.s = copy

    def push(self, item):
        if self.N == len(self.s):
            self.resize(2 * len(self.s))
        self.s[self.N] = item
        self.N += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        self.N -= 1
        item = self.s[self.N]
        self.s[self.N] = None
        if self.N > 0 and self.N == len(self.s) // 4:
            self.resize(len(self.s) // 2)
        return item


if __name__ == "__main__":
    stack = ResizingArrayStackOfStrings()
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
