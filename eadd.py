# Single-Layer Architecture
def single_layer_operations(a, b):
    print("Single Layer Architecture:")
    print(f"Sum: {a + b}")
    print(f"Difference: {a - b}")
    print(f"Multiplication: {a * b}")
    if b != 0:
        print(f"Division: {a / b}")
    else:
        print("Division: Cannot divide by zero")

# Multi-Layer Architecture
class MultiLayerCalculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

# Main Program
if __name__ == "__main__":
    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Single-layer computation
    single_layer_operations(num1, num2)
    
    # Multi-layer computation
    print("\nMulti Layer Architecture:")
    calculator = MultiLayerCalculator()
    print(f"Sum: {calculator.add(num1, num2)}")
    print(f"Difference: {calculator.subtract(num1, num2)}")
    print(f"Multiplication: {calculator.multiply(num1, num2)}")
    print(f"Division: {calculator.divide(num1, num2)}")
