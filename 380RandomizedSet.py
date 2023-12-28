from collections import defaultdict
from random import choice
# seems like hashtable data struct
def f(): return False

class RandomizedSet:

    def __init__(self):
        # default is False, not there
        self.__table = defaultdict(f)
        self.__memorised_count = 0
        self.__memorised_choices = []
        self.__current_count = 0

    def insert(self, val: int) -> bool:
        # present, return False
        if self.__table[val]:
            return False
        self.__table[val] = True
        self.__memorised_count += 1
        return True
        

    def remove(self, val: int) -> bool:
        # present, return true
        if self.__table[val]:
            self.__table[val] = False
            self.__memorised_count += 1
            return True
        return False

    def getRandom(self) -> int:
        # memorisation doubled the speed of the eval from 2 seconds to 1 seconds
        # i think better is this solution here
        # https://leetcode.com/problems/insert-delete-getrandom-o1/solutions/455253/python-super-efficient-detailed-explanation/?source=submission-ac
        # uses list and dict together to keep track of index
        if self.__current_count == self.__memorised_count:
            return choice(self.__memorised_choices)
        self.__memorised_choices = [x for x in self.__table.keys() if self.__table[x] == True]
        self.__current_count = self.__memorised_count
        return choice(self.__memorised_choices)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()