from random import choice

class RandomizedSet:

    def __init__(self):
        self.__data_table = {}
        self.__data = []

    def insert(self, val: int) -> bool:
        # present, return False
        # faster than `val in self.data.keys()`
        if val in self.__data_table:
            return False
        # insert value to the end of data, so we know the index (the current len)
        self.__data_table[val] = len(self.__data)
        self.__data.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        # present, return true
        if val in self.__data_table:
            to_swap = self.__data[-1]
            index_to_swap = self.__data_table[val]
            self.__data[index_to_swap] = to_swap
            self.__data_table[to_swap] = index_to_swap
            self.__data.pop()
            self.__data_table.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        # memorisation doubled the speed of the eval from 2 seconds to 1 seconds
        # i think better is this solution here
        # https://leetcode.com/problems/insert-delete-getrandom-o1/solutions/455253/python-super-efficient-detailed-explanation/?source=submission-ac
        # uses list and dict together to keep track of index
        # if self.__current_count == self.__memorised_count:
        #     return choice(self.__memorised_choices)
        # self.__memorised_choices = [x for x in self.__table.keys() if self.__table[x] == True]
        # self.__current_count = self.__memorised_count

        # old code above using memorisation
        return choice(self.__data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()