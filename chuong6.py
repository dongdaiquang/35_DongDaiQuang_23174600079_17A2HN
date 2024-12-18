#6.1
import threading
def print_message():
    print("1, 2, 3, 4, n")
threads = []
for i in range(5):  
    thread = threading.Thread(target=print_message) 
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
#6.3
import threading
def chan():
    for i in range(30,51):
        if i%2==0:
            print(f"chan:{i}")
def le():
    for i in range(30,51):
        if i%2!=0:
            print(f"le:{i}")
chan_thread=threading.Thread(target=chan)
le_thread=threading.Thread(target=le)
chan_thread.start()
le_thread.start()
chan_thread.join()
le_thread.join()
#6.4
import threading
def thua_so(n, ketqua):
    kq=1
    for i in range(1, n+1):
        kq*=i
    ketqua[n]=kq
    print(f"ketqua of {n}: {kq}")
numbers = [5, 7, 10]
ketqua = {}
threads = []
for num in numbers:
    thread = threading.Thread(target=thua_so, args=(num, ketqua))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print(ketqua)
#6.6
import threading
def chan(n):
    for i in range(0, n + 1, 2):
        print(f"chan: {i}")
def le(limit):
    for i in range(1, n + 1, 2):
        print(f"le: {i}")
n = 10
chan_thread = threading.Thread(target=chan, args=(n,))
le_thread = threading.Thread(target=le, args=(n,))
chan_thread.start()
le_thread.start()
chan_thread.join()
le_thread.join()


