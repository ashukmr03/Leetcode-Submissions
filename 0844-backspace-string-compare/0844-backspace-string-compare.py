class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(text: str) -> str:
            stack = []

            for char in text:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)

            return "".join(stack)

        return process(s) == process(t)