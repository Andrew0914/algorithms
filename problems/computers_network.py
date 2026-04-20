from collections import Counter


## TODO: solution is by using DFS OR BFS in a graph
class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        connected = Counter({key: 0 for key in range(n)})

        for computer in range(n):
            for connection in connections:
                if computer in connection:
                    connected[computer] += 1

        unconnected = 0
        for comp, count in connected.items():
            if count <= 0:
                unconnected += 1

        return unconnected


sol = Solution()
n = 4
connections = [[0, 1], [0, 2], [1, 2]]
print(sol.makeConnected(4, connections))
