class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points: dict = {}

        for point in points:
            distance: float = math.sqrt(point[0]**2 + point[1]**2)
            if distance in closest_points:
                closest_points[distance].append(point)
            else:
                closest_points[distance] = [point]

        solution: list[list[int]] = []
        for key in sorted(closest_points.keys())[0:k]:
            if len(solution) == k:
                    break
                    
            for point in closest_points[key]:
                solution.append(point)

                if len(solution) == k:
                    break

        return solution
        
