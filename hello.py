


'''
def get_square(l1):
    for i in l1:
        time.sleep(0.2)
        print(i*i)

def get_cube(l1):
    for i in l1:
        time.sleep(0.2)
        print(i*i*i)

l1 = [1,2,3,4]

t1 = threading.Thread(target=get_square , args=(l1,))
t2 = threading.Thread(target=get_cube , args=(l1,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Finish___________")
'''
'''
def get_square(l1):
    for i in l1:
        time.sleep(0.2)
        print(i*i)

def get_cube(l1):
    for i in l1:
        time.sleep(0.2)
        print(i*i*i)


if __name__ == "__main__":

    l1 = [1,2,3,4]

    starttime_linear = time.time()
    get_square(l1)
    get_cube(l1)
    print("Time took for linear process is ",time.time()-starttime_linear)

    p1 = multiprocessing.Process(target=get_square, args=(l1, ))
    p2 = multiprocessing.Process(target=get_cube, args=(l1, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Finish__________",time.time()-starttime_linear)

'''

'''
def get_square(l1,q):
    for i in l1:
        q.put(i*i)
    while q.empty() is False:
        print(q.get())

if __name__ == "__main__":

    l1 = [1,2,3,4]
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=get_square, args=(l1 ,q))

    p1.start()    
    p1.join()

'''
'''
import time 
import multiprocessing

def deposit(balance):
    for i in range(100):
        balance.Value = balance.Value+1


def withdraw(balance):
    for i in range(100):
        balance.Value = balance.Value-1


if __name__ == "__main__":

    balance = multiprocessing.Value('i',1000)

    p1 = multiprocessing.Process(target = deposit,args=(balance,))
    p2 = multiprocessing.Process(target = withdraw,args=(balance,))
   
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(balance.Value)


'''
'''
import time
from multiprocessing import pool

def get_sum():
    sum = 1
    for i in range(1,1000):
        sum+=i*i
    return sum

if __name__ == '__main__':
    
    start = time.time()
    
    p = Pool()
    sum_list = p.map(get_sum,range(100))
    p.close()
    p.join()

    for i in range(100):
        get_sum()
    print("Time taken is ",time.time()-start)


'''
