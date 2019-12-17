#! usr/bin/env python
#! -*- coding: utf-8 -*-
"""
=============================================
Part 1 -Implement Simulations with One Server
=============================================
1. Create two classes (similar to the Printer and Task class in the reading):
    a. Server
    b. Request
2. The csv file input format (e.g. '7, /images/test.gif, 1') where each
request line contains:
    a. when the request was received in (seconds)
    b. the file requested
    c. the time (seconds) needed for processing the request
3. Update the Request class; You don't needd the newPrintTask().
4. Implement simulateOneServer() function that takes in the input file.
5. simulateOneServer function should print the average request completion time;
    a. e.g. how long, on average, did a request take in the server queue before
     being processed)
    b. The average should be returned
5. The main function should accept '--file' parameter, which points to the file
 to read.
6. Save file as 'simulation.py'
"""
import urllib.request

csv_file = "http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv"

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Server:
    def __init__(self):
        self.request_number = 0
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
           return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

class Request:
    def __init__(self, time):
        self.timestamp = time
        self.file_request = ''

    def get_stamp(self):
        return self.timestamp

    def get_file_request(self):
        return self.file_request

    def wait_time(self, current_time):
        return current_time - self.timestamp

"""
1) A file request is placed containing the timestamp and requested file
2) The server receives the request, adds it to the queue.
3) From the queue, it will the request in order and calculate the duration time.
It will display the average processing time.
"""


def simulateOneServer(file):
    server = Server()
    server_queue = Queue()
    waiting_times = []

    if new_server_request():
        requests = urllib.request.urlopen(file).read()
        requests = str(requests).split('\\r\\n')
    for file_request in requests:
        file_request = file_request.strip("\\'").strip("b\\'")
        file_request = file_request.split(',')
        request = Request(current_second)
        server.timestamp, request.request, server.duration = line[0], line[1], line[2]
        server_queue.enqueue(line)
        if new_server_request():
            request = Request(file_request[0])
            server_queue.enqueue(request)

def new_server_request():
    pass

"""
        if (not server.busy()) and (not server_queue.is_empty()):
            next_task = server_queue.dequeue()
            waiting_times.append(next_task.wait_time(file_request[0]))
            server.start_next(next_task)

        server.tick()

        average_wait = sum(waiting_times) / len(waiting_times)
        print("Average Wait %6.2f sec %3d task remaining."%(average_wait, server_queue.size()))
"""

"""
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
"""

if __name__ ==  "__main__":
        print(simulateOneServer(csv_file))
