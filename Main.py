class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
        new = Node(data)
        if self.last is not None:
            self.last.next = new
        if self.head is None:
            self.head = new
        self.last = new

  def dequeue(self) -> None:
        if not self.head is None:
            self.head = self.head.next
            if self.head is None:
              self.last = None

  def status(self) -> None:
        current = self.head
        while current is not None:
          print(current.data, end = "=>")
          current = current.next
        print("None")


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
