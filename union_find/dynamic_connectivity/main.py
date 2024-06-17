class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Initially, there are n components

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            # Union by rank
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            self.count -= 1  # Decrease the number of components

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count_components(self):
        return self.count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read

    data = input().split()
    N = int(data[0])
    uf = UnionFind(N)

    index = 1
    while index < len(data):
        p = int(data[index])
        q = int(data[index + 1])
        index += 2
        if not uf.connected(p, q):
            uf.union(p, q)
            print(f"{p} {q}")

    print(f"Number of connected components: {uf.count_components()}")
