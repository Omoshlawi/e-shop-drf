class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, data):
        self._queue.append(data)

    def dequeue(self):
        try:
            return self._queue.pop(0)
        except IndexError:
            print("Your Queue is empty")

    def __str__(self):
        return str(self._queue)


myqueue = Queue()
myqueue.enqueue("Olympus")
myqueue.enqueue("Moses")
myqueue.enqueue("Tongoyo")
myqueue.dequeue()
myqueue.dequeue()
myqueue.dequeue()
myqueue.dequeue()
print(myqueue)

