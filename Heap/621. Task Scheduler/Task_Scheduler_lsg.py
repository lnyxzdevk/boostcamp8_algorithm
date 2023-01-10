from collections import Counter
import heapq as hq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counter = Counter(tasks)
        scheduler = [(0, -res, name) for name, res in counter.items()]
        hq.heapify(scheduler)
        while scheduler:
            end_time, m_res, name = hq.heappop(scheduler)
            if end_time < time:
                hq.heappush(scheduler, (time, m_res, name))
            else:
                time = end_time + 1
                if m_res + 1 < 0:
                    hq.heappush(scheduler, (time + n, m_res + 1, name))
        return time
        
