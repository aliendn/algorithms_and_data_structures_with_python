class QuickUnionUF:
    def __init__(self, n):
        # Initialize the id array where each element is its own component
        self.id = list(range(n))

    def root(self, i):
        # Chase parent pointers until reach root
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        # Two nodes are connected if they have the same root
        return self.root(p) == self.root(q)

    def union(self, p, q):
        # Connect the roots of the two elements
        root_p = self.root(p)
        root_q = self.root(q)
        self.id[root_p] = root_q

    def count_components(self):
        # Number of unique components
        roots = {self.root(i) for i in range(len(self.id))}
        return len(roots)

    def get_components(self):
        # Gather all components in a dictionary
        components = {}
        for i in range(len(self.id)):
            root = self.root(i)
            if root not in components:
                components[root] = set()
            components[root].add(i)
        return components

if __name__ == "__main__":
    import os

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tinyUF.txt')
    with open(file_path, 'r') as file:
        data = file.read().split()

    N = int(data[0])
    uf = QuickUnionUF(N)

    index = 1
    while index < len(data):
        p = int(data[index])
        q = int(data[index + 1])
        index += 2
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f"{p} {q}")

    print(f"Number of connected components: {uf.count_components()}")
    print("Connected components:")
    components = uf.get_components()
    for comp in components.values():
        print(comp)
