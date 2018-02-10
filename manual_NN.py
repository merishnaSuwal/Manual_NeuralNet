import numpy as np

class Operation():
    def __init__(self,input_nodes=[]):
        self.input_nodes =input_nodes
        self.output_nodes = []

        for node in input_nodes:
            node.output_nodes.append(self)

    def compute(self):
        pass


class add(Operation):
    def __init__(self,x,y):
        super().__init__([x,y])

    def compute(self, x1, y1):
        self.inputs=[ x1, y1]
        return x1 + y1


class multiply(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self, x1, y1):
        self.inputs = [x1, y1]
        return x1 * y1


class matmul(Operation):
    def __init__(self, x, y):
        super().__init__([x, y])

    def compute(self,  x1, y1):
        self.inputs = [ x1, y1]
        return x1.dot(y1)