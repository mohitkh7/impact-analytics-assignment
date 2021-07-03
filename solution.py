class Solution:
    def __init__(self, days):
        if type(days) == 'int':
            raise TypeError("Days argument should be of integer type")
        self.days = days
        self.ways_to_attend = self._ways_to_attend_classes()
    
    def number_of_ways_to_attend_classes(self):
        return len(self.ways_to_attend)

    def probability_to_miss_gradution_ceremony(self):
        ineligible_ways = self._ineligible_ways_to_attend_classes()
        return len(ineligible_ways) / self.number_of_ways_to_attend_classes()

    def _ways_to_attend_classes(self):
        arr = []
        pattern = ""
        self._util(self.days, pattern, arr)
        return arr
    
    def _util(self, days, pattern, arr):
        if days == 0:
            arr.append(pattern)
        else:
            # At any given day there are only two possibalities
            self._util(days - 1, pattern + 'A', arr)  # absent in class
            self._util(days - 1, pattern + 'P', arr)  # present in class
    
    def _ineligible_ways_to_attend_classes(self):
        # Filter out ways where 4 or more consective days classes are missed
        return list(filter(lambda way: "AAAA" in way, self.ways_to_attend))
