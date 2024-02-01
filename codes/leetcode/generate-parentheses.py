# LeetCode
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rs = []

        def generate(open, close, ss):
            if open == 0 and close == 0:
                rs.append(''.join(ss))
                return

            if 0 < open:
                generate(open - 1, close, ss + ['('])
            if open < close:
                generate(open, close - 1, ss + [')'])

        generate(n, n, [])
        return rs


if __name__ == '__main__':
    sol = Solution()
    result = sol.generateParenthesis(3)
    print(result)
