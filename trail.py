from lib.LinkedList import *

#insertion
ll1 = LinkedList()
ll1.insert_end(2)
ll1.insert_end(3)
ll1.insert_end(4)
ll1.insert_end(5)
ll1.print_ll()
print("Length of the List: ",ll1.length)

ll1.reverse_ll()
ll1.print_ll()