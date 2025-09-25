class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def collect_values(root):
    if root is None:
        return []
    values = [root.value]
    values += collect_values(root.left)
    values += collect_values(root.right)
    return values

def find_max_and_average(root):
    values = collect_values(root)
    maximum = max(values)
    average = sum(values) / len(values)
    return maximum, average

tree = Node(5)
tree.left = Node(3)
tree.left.left = Node(2)
tree.right = Node(8)
tree.right.left = Node(6)
tree.right.right = Node(10)

maximum, average = find_max_and_average(tree)

print("Макс:", maximum)
print("Среднее:", average)
