class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        no_nums = 0.0
        sum_of_nums = 0.0
        mini, maxi = float(1e9), 0
        max_freq, mode = 0, 0
        for i in range(256):
            if count[i] > 0:
                if mini > i:
                    mini = i
                if maxi < i:
                    maxi = i
                sum_of_nums += i * count[i]
                no_nums += count[i]
                if max_freq < count[i]:
                    max_freq = count[i]
                    mode = i
        mean = round(sum_of_nums / no_nums, 5)
        cumulative_freq = 0
        median = 0
        prev_val = None
        for i in range(256):
            if count[i] > 0:
                cumulative_freq += count[i]
                if cumulative_freq >= (no_nums / 2):
                    
                    if no_nums % 2 == 1:
                        median = round(i, 5)
                        break
                    elif prev_val is not None:
                        median = round((prev_val + i) / 2, 5) if cumulative_freq - count[i] <= (no_nums / 2) else round(prev_val, 5)
                        break
                    prev_val = i
        
        return [round(mini, 5), round(maxi, 5), mean, median, mode]