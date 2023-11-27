#Example 1

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__count = 0


    def get_counter(self):
        return self.__count


    def pop(self):
        val = Stack.pop(self)
        self.__count += 1
        return val



stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

#Example 2

class QueueError(Exception):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.list_queue = []

    def put(self, elem):
        self.list_queue.insert(0, elem)

    def get(self):
        if not len(self.list_queue):
            raise QueueError
        else:
            elem = self.list_queue.pop()
        return elem


#     Альтернативний варіант
# def get(self):
#     if len(self.queue) > 0:
#         elem = self.queue[-1]
#         del self.queue[-1]
#         return elem
#     else:
#         raise QueueError

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
# print(que.get())
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")

#Task 1


class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.list_queue = []

    def put(self, elem):
        self.list_queue.insert(0, elem)

    def get(self):
        if not len(self.list_queue):
            raise QueueError("Queue is empty")
        else:
            elem = self.list_queue.pop()
        return elem




class SuperQueue(Queue):
    def isempty(self):
        return not bool(self.list_queue)


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")


