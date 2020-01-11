import statistics
class FirstClass:
    mean = 0
    median = 0
    mode = 0
    @staticmethod
    def calc_mean(arr):
        total = sum(arr)
        return total/len(arr)
        
    @classmethod
    def calc_median(cls,arr):
        # cls.median = sorted(arr)[len(arr)//2]
        cls.median = statistics.median(arr)

    def calc_mode(self, arr):
        # self.mode = max(arr, key = arr.count)
        self.mode = statistics.mode(arr)

    def update(self, arr):
        self.mean = self.calc_mean(arr)


