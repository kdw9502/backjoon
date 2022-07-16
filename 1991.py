n = int(input())
left = dict()
right = dict()

for _ in range(n):
    _root, _left, _right = input().split()
    left[_root] = _left
    right[_root] = _right


def pre(root):
    print(root, end="")
    if left[root] != ".":
        pre(left[root])
    if right[root] != ".":
        pre(right[root])

def inorder(root):
    if left[root] != ".":
        inorder(left[root])
    print(root, end="")
    if right[root] != ".":
        inorder(right[root])

def post(root):
    if left[root] != ".":
        post(left[root])
    if right[root] != ".":
        post(right[root])
    print(root, end="")
pre("A")
print()
inorder("A")
print()
post("A")
print()