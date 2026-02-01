class RandomizedSet:

    def __init__(self):
        self.stack = []
        self.h = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val not in self.h:
            self.stack.append(val)
            self.h[val] = len(self.stack) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.stack:
            return False
        
        idx = self.h[val]
        last_val = self.stack[-1]
        
        self.stack[idx] = last_val
        self.h[last_val] = idx

        self.stack.pop()
        del self.h[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.stack)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()