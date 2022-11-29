# 1 >> How to use collection.deque  module  to create a FIFO Queue 
from collections import deque
'''
customQueue = deque(maxlen= 3)
print(customQueue)
customQueue.append(2)
customQueue.append(5)
customQueue.append(4)
print(customQueue)
print(customQueue.popleft())
print(customQueue.clear())
print(customQueue)

'''

# 2 >> How to create a queue using the Queue Module  to create a FIFO Queue 
import queue as q
'''
customQueue = q.Queue(maxsize=3)
print(customQueue.empty())
# print(customQueue)
customQueue.put(2)
customQueue.put(5)
customQueue.put(4)
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())
'''

# 3>> MultiProccessing Queue  as FIFO queue
from multiprocessing import Queue
# '''
customQueue = Queue(maxsize=3)
customQueue.put(5)
print(customQueue.get())
# '''
