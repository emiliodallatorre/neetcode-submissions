class Solution:
    DIRECTIONS: list[tuple] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        explored: set = set()

        rows: int = len(grid)
        cols: int = len(grid[0])

        def start_bfs(x: int, y: int):
            dq = deque([(x, y)])
            explored.add((x, y))

            while dq:
                position: tuple = dq.popleft()
                x, y = position[0], position[1]

                for direction in self.DIRECTIONS:
                    new_position: tuple = (x + direction[0], y + direction[1])

                    if all(l >= 0 for l in new_position) and new_position[0] < rows and new_position[1] < cols and new_position not in explored and grid[new_position[0]][new_position[1]] == "1":
                        dq.append(new_position)
                        explored.add(new_position)

        counter: int = 0
        for x, row in enumerate(grid):
            for y, element in enumerate(row):
                if (x, y) in explored:
                    continue

                if element == "1":
                    counter += 1
                    start_bfs(x, y)

        return counter
