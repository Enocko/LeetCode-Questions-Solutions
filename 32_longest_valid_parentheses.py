class Solution:
    def longestValidParentheses(self, s: str) -> int:
        h = {')': '('}
        stack = []
        cnt = 0

        for n in s:
            if n in h:
                if stack and stack[-1] == h[n]:
                    cnt += 1
                    stack.pop()
                else:
                    continue
            else:
                stack.append(n)
        
        return 2 * cnt