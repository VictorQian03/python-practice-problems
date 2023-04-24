from abc import ABC, abstractmethod
from typing import Union, Optional

class ExprNode(ABC):
    @abstractmethod
    def is_const(self) -> bool:
        raise NotImplementedError
    
    @abstractmethod
    def num_nodes(self) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def eval(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError

class Int(ExprNode):
    n: ExprNode
    def __init__(self, n: ExprNode) -> None:
        self.n = n

    def is_const(self) -> bool:
        return True

    def num_nodes(self) -> int:
        return 1

    def eval(self) -> int:
        return self.n

    def __str__(self) -> str:
        return str(self.n)


class Plus(ExprNode):
    op1: ExprNode
    op2: ExprNode
    def __init__(self, op1: ExprNode, op2: ExprNode) -> None:
        self.op1 = op1
        self.op2 = op2

    def is_const(self) -> bool:
        return False

    def num_nodes(self) -> int:
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()

    def eval(self) -> int:
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return op1_value + op2_value

    def __str__(self) -> str:
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} + {op2_str})"


class Times(ExprNode):
    op1: ExprNode
    op2: ExprNode
    def __init__(self, op1: ExprNode, op2: ExprNode) -> None:
        self.op1 = op1
        self.op2 = op2

    def is_const(self) -> bool:
        return False

    def num_nodes(self) -> int:
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()

    def eval(self) -> int:
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return op1_value * op2_value

    def __str__(self) -> str:
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} * {op2_str})"

class Exponent(ExprNode):
    op1: ExprNode
    op2: ExprNode
    def __init__(self, op1: ExprNode, op2: ExprNode) -> None:
        self.op1 = op1
        self.op2 = op2

    def is_const(self) -> bool:
        return False

    def num_nodes(self) -> int:
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()

    def eval(self) -> int:
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return op1_value ** op2_value

    def __str__(self) -> str:
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} ** {op2_str})"

class Modulus(ExprNode):
    op1: ExprNode
    op2: ExprNode
    def __init__(self, op1: ExprNode, op2: ExprNode) -> None:
        self.op1 = op1
        self.op2 = op2

    def is_const(self) -> bool:
        return False

    def num_nodes(self) -> int:
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()

    def eval(self) -> int:
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()

        return op1_value % op2_value

    def __str__(self) -> str:
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} % {op2_str})"

class Abs(ExprNode):
    op1: ExprNode
    def __init__(self, op1: ExprNode) -> None:
        self.op1 = op1

    def is_const(self) -> bool:
        return False

    def num_nodes(self) -> int:
        return 1 + self.op1.num_nodes()

    def eval(self) -> int:
        op1_value = self.op1.eval()

        return abs(op1_value)

    def __str__(self) -> str:
        op1_str = str(self.op1)

        return f"|{op1_str}|"

class BinOp(ExprNode):
    op1: ExprNode
    op2: ExprNode
    def __init__(self, op1: ExprNode, op2: ExprNode, operator: str) -> None:
        self.op1 = op1
        self.op2 = op2
        self.operator = operator

    def is_const(self) -> bool:
        return False

    def num_nodes(self) -> int:
        return 1 + self.op1.num_nodes() + self.op2.num_nodes()

    def eval(self) -> int:
        op1_value = self.op1.eval()
        op2_value = self.op2.eval()
        if self.operator == "plus":
            return op1_value + op2_value
        if self.operator == "times":
            return op1_value * op2_value
        if self.operator == "exponentiates":
            return op1_value ** op2_value
        if self.operator == "modulus":
            return op1_value % op2_value

    def __str__(self) -> str:
        op1_str = str(self.op1)
        op2_str = str(self.op2)

        return f"({op1_str} {self.operator} {op2_str})"

if __name__ == "__main__":

    op1 = Int(2)
    op2 = BinOp(Int(2), Int(4), "plus")
    op3 = BinOp(op2, op1, "exponentiates")
    op4 = BinOp(Int(100), op3, "modulus")

    print(f"{op4} = {op4.eval()}")