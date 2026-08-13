class KthLargest:
    content: List[int]
    k: int

    def __init__(self, k: int, nums: List[int]):
        self.content = []
        self.k = k

        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if not self.content:
            self.content.append(val)
            return val
        
        pos: int = len(self.content)
        par: int = (pos - 1) // 2
        self.content.append(val)

        while self.content[pos] <= self.content[par] and pos > 0:
            self.content[par], self.content[pos] = self.content[pos], self.content[par]
            pos, par = par, (par - 1) // 2


        print(self.content)
        if len(self.content) > self.k:
            self.content.pop(0)
            content: list = [x for x in self.content]
            self.content = []

            for n in content:
                self.add(n)

        result: int = self.content[0]
        return result
        