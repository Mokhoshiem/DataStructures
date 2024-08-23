'''
Design a food ordering system where your python program eill run two threads,
i. Place Order: This thread will be placing an order and iserting into a queue every .5 second.
ii. Serve Order: This thread will serve an order every 2 seconds.
'''
import time
from queues import Queue
from multiprocessing import Pool

def add_order(queue,value):
    queue.enque(value)
    return

def serve_order(queu):
    queu.deque()
    return

def start_system(list):
    queue = Queue()
    for l in list:
        add_order(queue,l)
        print(f'Added Order: {l}')
        time.sleep(.5)
        
    time.sleep(1)
    while queue.empty() is False:
        time.sleep(2)
        print(f'Order Served: {queue.peek}')
        serve_order(queue)
    
    print('All Orders Are Served.')

if __name__ == '__main__':
    start_system(['Pizza','Samosa','Biryani','Burger'])
