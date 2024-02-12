# 위상 정렬 : Topological Sort
import collections
from collections import defaultdict


class TopologicalSort:
    def __init__(self, degrees, links):

        self.degrees = degrees
        self.links = links

    def sort(self):

        queue = collections.deque()

        for k, v in self.links.items():
            if v == 0:
                queue.append(k)

        answer = []

        while queue:

            node = queue.pop()
            answer.append(node)

            for sub_node in self.degrees:
                links[sub_node] -= 1

                if links[sub_node] == 0:
                    queue.append(sub_node)

        return ' '.join(map(str, answer))


if __name__ == '__main__':

    n, m = map(int, input().split())

    degrees = collections.defaultdict(list)
    links = collections.defaultdict(int)

    for _ in range(m):
        a, b = map(int, input().split())
        degrees[a].append(b)
        links[b] += 1

    topo_sort = TopologicalSort(degrees, links)

    print(topo_sort.sort())