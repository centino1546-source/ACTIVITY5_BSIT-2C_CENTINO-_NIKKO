from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def run_stack(stack, label):
    while True:
        print(f"\n{label}: {stack}")
        print("1. Push\n2. Pop\n3. Peek\n4. Check empty\n5. Check full\n0. Back")
        choice = input("Choose an operation: ").strip()
        try:
            if choice == "1":
                value = input("Enter a value: ").strip()
                stack.push(value)
                print("Pushed:", value)
            elif choice == "2":
                print("Popped:", stack.pop())
            elif choice == "3":
                print("Top element:", stack.peek())
            elif choice == "4":
                print("Is empty?", stack.is_empty())
            elif choice == "5":
                print("Is full?", stack.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid option.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
        print("Current state:", stack)


def run_queue(queue, label):
    while True:
        print(f"\n{label}: {queue}")
        print("1. Enqueue\n2. Dequeue\n3. Peek front\n4. Check empty\n5. Check full\n0. Back")
        choice = input("Choose an operation: ").strip()
        try:
            if choice == "1":
                value = input("Enter a value: ").strip()
                queue.enqueue(value)
                print("Enqueued:", value)
            elif choice == "2":
                print("Dequeued:", queue.dequeue())
            elif choice == "3":
                print("Front element:", queue.peek_front())
            elif choice == "4":
                print("Is empty?", queue.is_empty())
            elif choice == "5":
                print("Is full?", queue.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid option.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
        print("Current state:", queue)


def main():
    while True:
        print("\nSTACKS AND QUEUES - MAIN MENU")
        print("1. Array Stack (capacity 3)")
        print("2. Linked Stack")
        print("3. Circular Array Queue (capacity 3)")
        print("4. Linked Queue")
        print("0. Exit")
        choice = input("Choose an implementation: ").strip()

        if choice == "1":
            run_stack(ArrayStack(3), "Array Stack")
        elif choice == "2":
            run_stack(LinkedStack(), "Linked Stack")
        elif choice == "3":
            run_queue(ArrayQueue(3), "Circular Array Queue")
        elif choice == "4":
            run_queue(LinkedQueue(), "Linked Queue")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
