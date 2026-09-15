"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        busy_times: list[Interval] = []

        for interval in intervals:
            for busy_time in busy_times:
                if (busy_time.start <= interval.start < busy_time.end) or (busy_time.start < interval.end < busy_time.end) or (interval.start < busy_time.start and busy_time.end < interval.end):
                    return False
                
            busy_times.append(interval)
        
        return True