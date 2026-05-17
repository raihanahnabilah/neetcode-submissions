class LRUCache:

    def __init__(self, capacity: int):
        self.hashSet = set()
        self.hashMap = {}
        self.capacity = capacity
        self.latestCounter = 1

    def get(self, key: int) -> int:
        if key not in self.hashSet:
            return -1
        
        self.hashMap[key] = (self.hashMap[key][0], self.latestCounter)
        self.latestCounter += 1

        return self.hashMap[key][0]

    def put(self, key: int, value: int) -> None:
        if key not in self.hashSet:
            # if it exceeds capacity
            if len(self.hashSet) >= self.capacity:
                leastUsedKey = min(self.hashMap, key = lambda x: self.hashMap[x][1])
                self.hashSet.remove(leastUsedKey)
                del self.hashMap[leastUsedKey]

            self.hashSet.add(key)
            self.hashMap[key] = (value, self.latestCounter)
            self.latestCounter += 1
        else:
            self.hashMap[key] = (value, self.latestCounter)
            self.latestCounter += 1


