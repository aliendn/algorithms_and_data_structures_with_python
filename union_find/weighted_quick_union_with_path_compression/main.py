class WeightedQuickUnionUF:
    def __init__(self, n):
        self.id = list(range(n))
        self.size = [1] * n  # Initialize size array

    def root(self, i):
        # Path Compression: make every other node in path point to its grandparent
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)

        if root_p != root_q:
            # Make the smaller tree a subtree of the larger tree
            if self.size[root_p] < self.size[root_q]:
                self.id[root_p] = root_q
                self.size[root_q] += self.size[root_p]
            else:
                self.id[root_q] = root_p
                self.size[root_p] += self.size[root_q]

    def count_components(self):
        roots = {self.root(i) for i in range(len(self.id))}
        return len(roots)

    def get_components(self):
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
    uf = WeightedQuickUnionUF(N)

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
