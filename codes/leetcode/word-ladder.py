# LeetCode
# https://leetcode.com/problems/word-ladder/
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def movable(a, b):
            return len([c for c in zip(a, b) if c[0] != c[1]]) == 1

        def bfs(begin, target, words):

            if target not in words:
                return 0

            dist = collections.defaultdict(int)

            queue = collections.deque()
            queue.append(begin)
            dist[begin] = 0

            while queue:

                top = queue.popleft()

                for word in words:
                    if word not in dist and movable(top, word):
                        dist[word] = dist[top] + 1
                        queue.append(word)

            return dist[target]

        return bfs(beginWord, endWord, wordList)
