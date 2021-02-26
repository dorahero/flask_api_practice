import numpy as np

class Statistics:
    def __init__(self, data, operator):
        self.data = data
        self.operator = operator

    def sum(self):
        return sum(self.data)
    
    def mean(self):
        _ = self.data
        ans = sum(_)/len(_)
        return ans
    
    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        return np.var(self.data)

    def stddev(self):
        return np.std(self.data)

    
