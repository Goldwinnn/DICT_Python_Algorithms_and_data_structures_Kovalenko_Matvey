from class_generator import Generator
from abstractlimitstructure_p5 import Stack, PriorQueue

def generate_rabbits():
    generator = Generator()
    return [generator.generate_single()[0] for _ in range(5)]

def print_rabbits(rabbits):
    print("Generated rabbits:")
    for rabbit in rabbits:
        print(rabbit)

def demonstrate_stack(rabbits):
    print("\nStack:")
    stack = Stack()
    stack.push(rabbits[0])
    stack.push(rabbits[1])
    stack.push(rabbits[2])
    print(stack)
    print("Top:", stack.top())
    print("Popped:", stack.pop())
    stack.push(rabbits[3])
    stack.push(rabbits[4])
    print(stack)
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print(stack)

def demonstrate_priority_queue(rabbits):
    print("\nPriority queue:")
    queue = PriorQueue()
    queue.enqueue(rabbits[0])
    queue.enqueue(rabbits[1])
    queue.enqueue(rabbits[2])
    print("Is empty:", queue.is_empty())
    print("Size:", queue.size())
    print("Peek:", queue.peek())
    dequeued_rabbit = queue.dequeue()
    print("Dequeued rabbit:", dequeued_rabbit)
    queue.enqueue(rabbits[3])
    queue.enqueue(rabbits[4])
    print("Size:", queue.size())
    dequeued_rabbit = queue.dequeue()
    print("Dequeued rabbit:", dequeued_rabbit)
    dequeued_rabbit = queue.dequeue()
    print("Dequeued rabbit:", dequeued_rabbit)
    print("Size:", queue.size())

def main():
    rabbits = generate_rabbits()
    print_rabbits(rabbits)
    demonstrate_stack(rabbits)
    demonstrate_priority_queue(rabbits)

if __name__ == "__main__":
    main()
