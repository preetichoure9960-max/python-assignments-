class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def restore_linked_list_from_file(filename):
    head = None
    current = None
    with open(filename, 'r') as file:
        for line in file:
            data = int(line.strip())
            new_node = Node(data)
            if not head:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = current.next
    return head
restored_head = restore_linked_list_from_file('linked_list.txt')
temp = restored_head
while temp:
    print(temp.data)
    temp = temp.next