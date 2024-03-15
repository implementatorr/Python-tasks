class Node:
    amount = 0

    def __init__(self, data: int):
        self.value = data
        self.left = None
        self.right = None

    def insert(self, new_data: int) -> bool:
        if self.value == new_data:
            return
        if self.value < new_data:
            if self.right is None:
                Node.amount += 1
                self.right = Node(new_data)
            else:
                self.right.insert(new_data)
        else:
            if self.left is None:
                Node.amount += 1
                self.left = Node(new_data)

            else:
                self.left.insert(new_data)

    def find(self, what: int, result=False):
        if self.value == what:
            result = True
            print(result)
        elif self.value < what:
            if not self.right:
                print(result)
            else:
                self.right.find(what, False)
        else:
            if not self.left:
                print(result)
            else:
                self.left.find(what, False)


my_data = [10, 9, 50, 6, 12, 3, 13]
tree = Node(my_data[0])
for i in my_data:
    tree.insert(i)

tree.find(111, False)
print(f"Roots:{Node.amount}")