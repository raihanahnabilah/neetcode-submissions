class LRUCache:

    def __init__(self, capacity: int):
        self.hashKey = {}
        self.capacity = capacity;
        self.counter = 0

    def get(self, key: int) -> int:
        self.counter += 1
        if key not in self.hashKey:
            return -1
        value = self.hashKey[key][0]
        self.hashKey[key] = (value, self.counter)
        return value

    def put(self, key: int, value: int) -> None:
        # if len(self.hashKey) < self.capacity:
            # print("checking self.hashKey.items()", self.hashKey.items())
        if len(self.hashKey) >= self.capacity and key not in self.hashKey:
            # print("has reached here")
            # print("checking self.hashKey.items()", self.hashKey.items())
            keyToRemove = min(self.hashKey.items(), key = lambda item: item[1][1])[0]
            del self.hashKey[keyToRemove]

        self.counter += 1
        self.hashKey[key] = (value, self.counter)


# # [1,5]
# # [1,2]
# # [2,6]
# # []


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.hashSet = set()
#         self.hashMap = {}
#         self.capacity = capacity
#         self.latestCounter = 1

#     def get(self, key: int) -> int:
#         if key not in self.hashSet:
#             return -1
        
#         self.hashMap[key] = (self.hashMap[key][0], self.latestCounter)
#         self.latestCounter += 1

#         return self.hashMap[key][0]

#     def put(self, key: int, value: int) -> None:
#         if key not in self.hashSet:
#             # if it exceeds capacity
#             if len(self.hashSet) >= self.capacity:
#                 leastUsedKey = min(self.hashMap, key = lambda x: self.hashMap[x][1])
#                 self.hashSet.remove(leastUsedKey)
#                 del self.hashMap[leastUsedKey]

#             self.hashSet.add(key)
#             self.hashMap[key] = (value, self.latestCounter)
#             self.latestCounter += 1
#         else:
#             self.hashMap[key] = (value, self.latestCounter)
#             self.latestCounter += 1



