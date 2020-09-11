# test field
class Binary:
    def binary_search(self, list, item):
        lowest = 0
        highest = len(list) - 1
        while lowest <= highest:
            midval = (lowest + highest)
            suggest = list[midval]
            if suggest == item:
                return midval
            if suggest > item:
                highest = midval - 1
            else:
                lowest = midval + 1 
        return None



        def smallest_number(self, arr):
            lowest_number = 0
            position = arr[0]
            for i in range(1, len(arr)):
                if arr[i] < position:
                    lowest_number = arr[i]
                    position = i
                return position




calls = Binary()
nice = calls.binary_search([4, 67, 78, 90], 90)
print(nice)

sorted = Binary()
sorting = sorted.smallest_number(nice)
print(sorting)
