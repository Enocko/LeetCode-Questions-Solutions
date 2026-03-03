class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        h = {n: i for i, n in enumerate(s)}
        stack = []
        visited = set()

        for i, n in enumerate(s):
            if n not in visited:
                while stack and n < stack[-1] and i < h[stack[-1]]:
                    visited.remove(stack.pop())

                stack.append(n)
                visited.add(n)

        return ''.join(stack)