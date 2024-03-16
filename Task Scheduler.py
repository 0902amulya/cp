class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_cnt=[0]*26
        for task in tasks:
            task_cnt[ord(task)-ord('A')]+=1
        task_cnt .sort(reverse=True)
        max_cnt=task_cnt[0]-1
        idle_slots=max_cnt*n
        for i in range(1,len(task_cnt)):
            idle_slots-= min(task_cnt[i],max_cnt)
        idle_slots=max(0,idle_slots)
        return len(tasks)+idle_slots
