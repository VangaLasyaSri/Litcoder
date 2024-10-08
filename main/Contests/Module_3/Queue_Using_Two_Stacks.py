# Problem Statement:
# Write a program to implement a custom queue using two stacks. The queue should support the following three types of queries: 
# Enqueue: This query type is denoted by "1 x", where x is an element to be enqueued. It means that you need to insert element x at the end of the queue. 
# Dequeue: This query type is denoted by "2". It indicates that you should remove the element at the front of the queue. 
# Print Front: This query type is denoted by "3". It instructs you to print the element at the front of the queue without removing it.

# Exercise-1 input: 1 42,2,1 14,3
# output: 14

# Exercise-2 input: 1 23,2,1 14,3,2,1 78,3
# Output: 14 78

input1 = input()
queries = input1.split(",")
stack1 = []
stack2 = []
for query in queries:
    if query.startswith("1"):
        element = int(query.split(" ")[1])
        stack1.append(element)
    elif query == "2":
        if len(stack2) == 0:
            while len(stack1) != 0:
                stack2.append(stack1.pop())
        if len(stack2) != 0:
            stack2.pop()
    elif query == "3":
        if len(stack2) == 0:
            while len(stack1) != 0:
                stack2.append(stack1.pop())
        if len(stack2) != 0:
            print(stack2[-1])