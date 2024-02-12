# 위상 정렬 : Topological Sort
import collections

class TopologicalSort:
    def __init__(self, n, degrees, links):

        self.n = n
        self.degrees = degrees
        self.links = links

    def sort(self):

        queue = collections.deque()

        for i in range(1, self.n+1):
            if links[i] == 0:
                queue.append(i)

        answer = []

        while queue:

            node = queue.pop()
            answer.append(node)

            for sub_node in self.degrees[node]:
                self.links[sub_node] -= 1

                if self.links[sub_node] == 0:
                    queue.append(sub_node)

        return ' '.join(map(str, answer))


n, m = map(int, input().split())

degrees = collections.defaultdict(list)
links = collections.defaultdict(int)

for _ in range(m):
    a, b = map(int, input().split())
    degrees[a].append(b)
    links[b] += 1

topo_sort = TopologicalSort(n, degrees, links)

print(topo_sort.sort())
