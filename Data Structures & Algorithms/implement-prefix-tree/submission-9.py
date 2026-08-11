class TreeNode:
    value: str
    children: dict

    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else {}

    def __contains__(self, value):
        return value in self.children

    def __getitem__(self, value):
        if value in self.children:
            return self.children[value]
        
        raise f"{value} not present"

    def add_child(self, value: str):
        if value in self.children:
            return

        self.children[value] = TreeNode(value)

    def __repr__(self):
        return f"T({self.value}, {self.children})"


class PrefixTree:
    root: TreeNode

    def __init__(self):
        self.root = TreeNode("")

    def insert(self, word: str) -> None:
        target: TreeNode = self.root

        for char in word:
            if char not in target:
                target.add_child(char)
            target = target[char]

        target.add_child(None)

    def search(self, word: str) -> bool:
        target: TreeNode = self.root

        for char in word:
            if char in target:
                target = target[char]
            else:
                return False

        return None in target

    def startsWith(self, prefix: str) -> bool:
        target: TreeNode = self.root

        for char in prefix:
            if char in target:
                target = target[char]
            else:
                return False

        return True
