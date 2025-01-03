#5.1
import time
class SimpleTask:
    def run_task(self):
        for i in range(1, 11):
            print('Đã in lần thứ :',i)
            time.sleep(2)
def main():
    task = SimpleTask()
    task.run_task()
if __name__ == "__main__":
    main()
#5.2
import threading
import time
class SimpleTask:
    def run_task(self):
        for i in range(1, 4):
            print('Đã in lần thứ :',i)
            time.sleep(1)
def main():
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
if __name__ == "__main__":
    main()
#5.3.1
class SimpleTask:
    def run_task(self):
        global counter
        for _ in range(4):
            time.sleep(2)
            counter += 1
            print(f"Counter đã tăng lên: {counter}")
def main():
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
if __name__ == "__main__":
    main()
#5.3.2
import threading
import time
counter = 0
counter_lock = threading.Lock()
class SimpleTask:
    def run_task(self):
        global counter
        for _ in range(3):
            time.sleep(2)
            with counter_lock:
                counter += 1
                print(f"Counter đã tăng lên: {counter}")
def main():
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
if __name__ == "__main__":
    main()
