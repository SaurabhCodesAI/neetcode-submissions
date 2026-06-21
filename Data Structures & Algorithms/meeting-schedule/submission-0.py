class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval:interval.start)
        for i in range(1, len(intervals)):
            previous = intervals[i - 1].end
            current = intervals[i].start
            if previous > current:
                return False
        return True