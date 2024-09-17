# Task 1: Customer Order Processing

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2)
]

for order in orders:
    name, item, quantity = order
    print(f"{name} ordered {quantity} {item}(s)")
