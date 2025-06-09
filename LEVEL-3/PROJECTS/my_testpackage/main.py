import sys
import os

# Add project root to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("path", sys.path)

from my_package.math_utils import add

result = add(5, 3)
print(f"The result is: {result}")