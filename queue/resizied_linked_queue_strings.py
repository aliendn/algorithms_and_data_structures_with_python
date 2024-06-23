class ResizingArrayQueueOfStrings:
    def __init__(self):
        self.q = [None] * 2  # initial capacity of 2
        self.head = 0
        self.tail = 0
        self.n = 0  # number of elements in the queue

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def resize(self, capacity):
        assert capacity >= self.n
        copy = [None] * capacity
        for i in range(self.n):
            copy[i] = self.q[(self.head + i) % len(self.q)]
        self.q = copy
        self.head = 0
        self.tail = self.n
        print(self.size())

    def enqueue(self, item):
        if self.n == len(self.q):
            self.resize(2 * len(self.q))  # double the array size if necessary
        self.q[self.tail] = item
        self.tail = (self.tail + 1) % len(self.q)
        self.n += 1
        print(self.size())

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.q[self.head]
        self.q[self.head] = None
        self.head = (self.head + 1) % len(self.q)
        self.n -= 1
        if 0 < self.n <= len(self.q) // 4:
            self.resize(len(self.q) // 2)  # shrink the array if necessary
        print(self.size())
        return item


if __name__ == "__main__":
    queue = ResizingArrayQueueOfStrings()
    print("Do you want to start your queue? (1, 0)")
    print("If you insert 0, the program will stop: ")
    start_point = int(input("? : "))
    
    while start_point == 1:
        insert = int(input("Do you want to enqueue your item? (1, 0): "))
        if insert == 1:
            enqueue_item = input("Enqueue: ")
            queue.enqueue(enqueue_item)
        
        remove = int(input("Do you want to dequeue your item? (1, 0): "))
        if remove == 1:
            try:
                print(f"You removed: {queue.dequeue()}")
            except IndexError:
                print("There is no item. Please continue and add item to the queue!")

        start_point = int(input("Continue (1, 0)?: "))
    
    print("Thanks a lot!")
