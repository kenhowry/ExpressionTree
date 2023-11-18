from binary_tree import BinaryTree

class ExpressionTree(BinaryTree):
    def __str__(self) -> str:
        """
            Description:
                returns a string representation of an expression tree
            Parameters:
                None
            Return:
                str
        """
        return self._str_helper(self.root)
    
    def _str_helper(self, node) -> str:
        """
        Private method:
            Description:
                Helper method for __str__
            Parameters:
                node: TreeNode object
            Return:
                str
        """
        #base case
        if node is None:
            return ""
        
        else:
            if node.is_external():
                return self._str_helper(node.left_child) + str(node.value) + self._str_helper(node.right_child)
            else:
                return "(" + self._str_helper(node.left_child) + str(node.value) + self._str_helper(node.right_child) + ")"
    
    def evaluate(self, node) -> float:
        """
            Description:
                evaluates an expression tree
            Parameters:
                node: TreeNode object
            Return:
                float
        """
        #base case
        if node.is_external():
            return float(node.value)
        
        #addition case
        if node.value == "+":
            return self.evaluate(node.left_child) + self.evaluate(node.right_child)
        
        #subtraction case
        elif node.value == "-":
            return self.evaluate(node.left_child) - self.evaluate(node.right_child)
        
        #multiplication case
        elif node.value == "*":
            return self.evaluate(node.left_child) * self.evaluate(node.right_child)
        
        #division case
        elif node.value == "/":
            return self.evaluate(node.left_child) / self.evaluate(node.right_child)

def _main():
    tree = ExpressionTree()

    r = tree.add_root("*")
    rl = tree.add_left(r, "-")
    rll = tree.add_left(rl, "+")
    rlll = tree.add_left(rll, "+")
    rllll = tree.add_left(rlll, "12")
    rlllr = tree.add_right(rlll, "2")
    rllr = tree.add_right(rll, "4")
    rlr = tree.add_right(rl, "+")
    rlrl = tree.add_left(rlr, "-")
    rlrll = tree.add_left(rlrl, "9")
    rlrlr = tree.add_right(rlrl, "5")
    rlrr = tree.add_right(rlr, "2")
    rr = tree.add_right(r, "+")
    rrl = tree.add_left(rr, "*")
    rrll = tree.add_left(rrl, "3")
    rrlr = tree.add_right(rrl, "-")
    rrlrl = tree.add_left(rrlr, "*")
    rrlrll = tree.add_left(rrlrl, "3")
    rrlrlr = tree.add_right(rrlrl, "9")
    rrlrr = tree.add_right(rrlr, "+")
    rrlrrr = tree.add_right(rrlrr, "4")
    rrlrrl = tree.add_left(rrlrr, "5")
    rrr = tree.add_right(rr, "6")

    print(tree, end='')
    print('=',tree.evaluate(tree.root))


if __name__ == '__main__':
    _main()
