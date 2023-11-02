class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
 

# This function receives a node of the syntax tree and recursively evaluate it
def evaluateExpressionTree(root):
 
    # Arbol vacio
    if root is None:
        return 0
 
    # Nodo hoja
    if root.left is None and root.right is None:
        return int(root.data)
 
    # Evalua arbol izquierdo
    left_sum = evaluateExpressionTree(root.left)
 
    # Evalua arbol derecho
    right_sum = evaluateExpressionTree(root.right)
 
    # Verifíca que operación aplicar
    if root.data == '+':
        return left_sum + right_sum
 
    elif root.data == '-':
        return left_sum - right_sum
 
    elif root.data == '*':
        return left_sum * right_sum
 
    else:
        return left_sum // right_sum
 
 
# Driver function to test above problem
if __name__ == '__main__':
 
    # Crea un arbol
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('-4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('20')
    print ("El resultado de la expresion es:",evaluateExpressionTree(root))
 
    root = None
 
    # Crea un arbol
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('/')
    root.right.right.left = node('20')
    root.right.right.right = node('2')
    print ("El resultado de la expresion es:",evaluateExpressionTree(root))