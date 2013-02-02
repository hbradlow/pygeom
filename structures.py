import heappq

class Segment:
    def __init__(self,start,end):
        self.start = start
        self.end = end

class StatusLine:
    def __init__(self):
        self.segments = []

class EventQueue:
    LEFT = "left"
    RIGHT = "right"
    INTERSECT = "intersect"
    def __init__(   self,
                    left_event=lambda segments: None,
                    right_event=lambda segments: None,
                    intersect_event=lambda segments: None):
        queue = PriorityQueue() #sort points by x value
        self.status = StatusLine()
        self.left_event = left_event
        self.right_event = right_event
        self.intersect_event = intersect_event

    def process_left_event(status,segments):
        pass
    def push_point(self,point,segments,event_type):
        queue.push((point,segments,event_type),point[0]) #push tuple sorted based on x value
    def pop_point(self):
        (point,segments,event_type) = queue.pop()
        if event_type == LEFT:
            self.left_event(status,segments)
        elif event_type == RIGHT:
            self.right_event(status,segments)
        else
            self.intersect_event(status,segments)

class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """
    def  __init__(self):
        self.heap = []

    def push(self, item, priority):
        pair = (priority,item)
        heapq.heappush(self.heap,pair)

    def pop(self):
        (priority,item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

class PriorityQueueWithFunction(PriorityQueue):
    """
    Implements a priority queue with the same push/pop signature of the
    Queue and the Stack classes. This is designed for drop-in replacement for
    those two classes. The caller has to provide a priority function, which
    extracts each item's priority.
    """
    def  __init__(self, priorityFunction):
        "priorityFunction (item) -> priority"
        self.priorityFunction = priorityFunction      # store the priority function
        PriorityQueue.__init__(self)        # super-class initializer

    def push(self, item):
        "Adds an item to the queue with priority from the priority function"
        PriorityQueue.push(self, item, self.priorityFunction(item))
