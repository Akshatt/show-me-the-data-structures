class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    check = []
    unionLL = LinkedList()
    def adding(current):
        while current:
            #checking if current value already added in union list 
            if current.value not in check:
                check.append(current.value)
                unionLL.append(current.value)
            current = current.next
    adding(llist_1.head)
    adding(llist_2.head)
    return unionLL
    

def intersection(llist_1, llist_2):
    set_LL1 = set()
    set_LL2 = set()
    intersectionLL = LinkedList()
    current1, current2 = llist_1.head, llist_2.head
    while current1:
        set_LL1.add(current1.value)
        current1 = current1.next
    while current2:
        set_LL2.add(current2.value)
        current2 = current2.next
    for x in set_LL1.intersection(set_LL2):
        intersectionLL.append(x) 
    return intersectionLL
    
'''
Complexity analysis:
    Union:
        1. creating empty list                          ---- O(1)
        2. creatinf empty LinkedList                    ---- O(1)
        3. adding function
        4.      while current                           ---- O(1)
        5.      look for current.value in check         ---- O(n)
        6.          append in check                     ---- O(1)
        7.          append in union LL                  ---- O(1)
        8.      iterate current                         ---- O(1)
        9. call adding function for first LinkedList    ---- O(1)
        10. call adding function for second LinkedList  ---- O(1)
        11. return 
        
        Here, the adding function's time complexity is O(n)
        So, total time complexity for UNION is O(n)
    
    Intersection:
        1. empty set for linkedlist_1                                   ---- O(1)
        2. empty set for linkedlist_2                                   ---- O(1)
        3. New linkedList of intersection                               ---- O(1)
        4.storing head values of both linked lists in current variables ---- O(1)
        5.moving through linked_list_1 to add its values to set         ---- O(m) 
        6. moving through linked_list_2 to add its values to set        ---- O(n)
        7. looping through each element in intersection of two sets     ---- O(min(m,n))
        8.      appending element into intersection linkedlist          ---- O(1)
        9. return
        
        Here, the intersection set takes O(min(len(LL1),len(LL2))) so 
        total time complexity for INTERSECTION is O(n) 
'''


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print("Test Case1")

print("\nUnion: ",union(linked_list_1,linked_list_2))
print("\nIntersection: ",intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print("\nTest Case2")
print ("\nUnion: ",union(linked_list_3,linked_list_4))
print ("\nIntersection: ",intersection(linked_list_3,linked_list_4))

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,4,5,6,7,8,9]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)
print("\nTest Case3")
print ("\nUnion: ",union(linked_list_5,linked_list_6))
print ("\nIntersection: ",intersection(linked_list_5,linked_list_6))

# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [1,2,11,5,6,7,8]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)
print("\nTest Case4")
print ("\nUnion: ",union(linked_list_7,linked_list_8))
print ("\nIntersection: ",intersection(linked_list_7,linked_list_8))








