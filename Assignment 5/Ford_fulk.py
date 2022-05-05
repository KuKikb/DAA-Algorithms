from collections import deque
class DirectedGraph:
    
    def __init__(self,graph,s1,s2):
        self.graph = graph
        self.queue = deque()
        self.source = s1
        self.sink = s2
           
    def AugmentingPath(self):






graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

source = 0 
sink = 5