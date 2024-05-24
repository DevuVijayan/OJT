class MathOperations:
    @classmethod
    def add(cls, num1, num2):
        return num1 + num2

    @classmethod
    def sub(cls, num1, num2):
        return num1 - num2

    @classmethod
    def mul(cls, num1, num2):
        return num1 * num2

    @staticmethod
    def fact(num):
        if num == 0:
            return 1
        else:
            return num * MathOperations.fact(num - 1)

# Example usage:
print("Addition:", MathOperations.add(5, 3))          # Output: Addition: 8
print("Subtraction:", MathOperations.sub(5, 3))    # Output: Subtraction: 2
print("Multiplication:", MathOperations.mul(5, 3))  # Output: Multiplication: 15
print("Factorial:", MathOperations.fact(5))           # Output: Factorial: 120