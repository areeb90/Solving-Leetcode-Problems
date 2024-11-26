class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n

        for src, dst in edges:
            incoming[dst] += 1

        champion = []

        for index, incoming_count in enumerate(incoming):
            if incoming_count == 0:
                champion.append(index)

        if len(champion) > 1:
            return -1
        return champion[0]