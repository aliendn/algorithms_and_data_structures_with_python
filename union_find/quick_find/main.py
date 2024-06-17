class QuickFindUF:
    def __init__(self, n):
        # Initialize the id array where each element is its own component
        self.id = list(range(n))

    def connected(self, p, q):
        # Two nodes are connected if they have the same id
        return self.id[p] == self.id[q]

    def union(self, p, q):
        # Find the component id for p and q
        pid = self.id[p]
        qid = self.id[q]
        
        # Change all entries from pid to qid
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid

    def count_components(self):
        # Number of unique components
        return len(set(self.id))

    def get_components(self):
        # Gather all components in a dictionary
        components = {}
        for i in range(len(self.id)):
            root = self.id[i]
            if root not in components:
                components[root] = set()
            components[root].add(i)
        return components

if __name__ == "__main__":
    import sys
    input = sys.stdin.read

    data = input().split()
    N = int(data[0])
    uf = QuickFindUF(N)

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
