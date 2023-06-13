import threading
from one_note import Add_Note

def input_name():
    name = input("enter name: ")
    print("Hello, ", name)

class MyThread(threading.Thread):
    def __init__(self, id=0):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        Add_Note()


if __name__ == "__main__":
    thread = threading.Thread(target=input_name)
    thread.start()
    print("After thread")
    mythread = MyThread()
    mythread.run()
