from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        heap = []
        max_rooms = 0
        intervals.sort(key=lambda interval:interval.start)
        for interval in intervals:
            start = interval.start
            end = interval.end
            while heap and start >= heap[0]:
                heappop(heap)
            heappush(heap, end)
            max_rooms = max(max_rooms, len(heap))
        return max_rooms
            