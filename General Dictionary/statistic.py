class Statistic:

    def __init__(self, data_set):
        self.data_set = data_set

    def mean(self):
        mean = sum(self.data_set) / len(self.data_set)
        return f"The average is : {round(mean, 2)}"

    def median(self):
        length = len(self.data_set)
        data = sorted(self.data_set)
        if length % 2 == 0:
            p1 = int(length / 2)
            median = int((data[p1 - 1] + data[p1]) / 2)
        else:
            p1 = int((length + 1) / 2)
            median = data[p1 - 1]

        return f"The median is : {median}"

    def mode(self):
        count = {}
        mode = []
        for key in self.data_set:
            if count.__contains__(key):
                count[key] += 1
            else:
                count[key] = 1
        max_num = max(count.values())
        if max_num == 1:
            return f"no mode found"
        else:
            for i in self.data_set:
                if count[i] == max_num and i not in mode:
                    mode.append(i)
            return f"The mode is : {mode}"


stat = Statistic([3, 5, 2, 7, 1,  6,  8,  9])

print(stat.mean())
print(stat.median())
print(stat.mode())


