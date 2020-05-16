import hashlib
from datetime import datetime
        
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data + str(previous_hash))
        self.next = None

    def calc_hash(self,string):
        sha = hashlib.sha256()
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        
        return sha.hexdigest()    

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def addBlock(self, data):
        if data:
            if self.head == None:
                block = Block(datetime.utcnow(),data, 0)
                self.head = block
                self.tail = self.head
            else:
                block = Block(datetime.utcnow(), data, self.tail.hash)
                self.tail.next = block
                self.tail = block
            
    def printChain(self):
        cur = self.head
        while cur:
            print("Timestamp: {}\nData: {}\nHash value: {}\nPrevious Hash: {}\n".format(cur.timestamp,cur.data, cur.hash, cur.previous_hash))
            cur = cur.next

print("Testcase 1")
b = Blockchain()
string = "This is my implementation of blockchain!"
for i in string.split():
    b.addBlock(i)
b.printChain()


print("Testcase 2") # only one block should be created as block data is 
                    # separated by space in this implementation.
c = Blockchain()
string = "Thisismyimplementationofblockchain!"
for i in string.split():
    c.addBlock(i)
c.printChain()

print("Testcase 3") #No block created as no data was passed. So nothing should be printed.
d = Blockchain()
string = " "
for i in string.split():
    d.addBlock(i)
d.printChain()



