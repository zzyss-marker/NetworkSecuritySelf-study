import Queue

queue = Queue.Queue()

for i in range(10):
    queue.put(i)
print(queue.empty())
print(queue.qsize())

#ȡ���� get����ȡ�����������
print(queue.get())
print(queue.get())
