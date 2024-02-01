# LeetCode
# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]

        for i in range(len(word1)):
            dp[i][0] = i
        for i in range(len(word2)):
            dp[0][i] = i

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])+1

        return dp[len(word1)][len(word2)]


if __name__ == '__main__':

    s1 = "horse"
    s2 = "ros"
    sol = Solution()
    if sol.minDistance(s1, s2) == 3:
        print('ok')

    s1 = "intention"
    s2 = "execution"
    if sol.minDistance(s1, s2) == 5:
        print('ok')
