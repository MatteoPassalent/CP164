"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matteo Passalent
ID:      210597410
Email:   pass7410@mylaurier.ca
__updated__ = "2023-01-31"
-------------------------------------------------------
"""

from Queue_array import Queue
from utilities import array_to_queue
from utilities import queue_to_array
from utilities import queue_test

q = Queue()


source = [1, 2, 3, 4, 5]
target = []
a = []

array_to_queue(q, source)

for i in q:
    print(i)

queue_to_array(q, target)
print(target)

queue_test(a)
queue_test(target)
