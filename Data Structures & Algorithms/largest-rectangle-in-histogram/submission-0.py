class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        open_streams: dict = defaultdict(int)
        max_area: int = 0

        for height in heights:
            for i in range(1, height + 1):
                open_streams[i] += i
                max_area = max(open_streams[i], max_area)
            
            for i in list(open_streams.keys()):
                if i > height:
                    open_streams.pop(i)
        
        return max_area

            