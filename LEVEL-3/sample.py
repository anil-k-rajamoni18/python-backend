import sys
import math

# 1. sys.argv - Command-line arguments
print("Command-line arguments (sys.argv):", sys.argv)

# 2. sys.exit - Uncomment to exit the program early
# sys.exit("Exiting program.")

# 3. sys.path - Module search paths
print("Module search paths (sys.path):", sys.path[:2])  # Show only first 2 for brevity

# 4. sys.platform - Detect OS platform
print("Platform (sys.platform):", sys.platform)

# 5. sys.version / sys.version_info - Python version
print("Python version (sys.version):", sys.version)
print("Version info (sys.version_info):", sys.version_info)

# 6. sys.stdin, sys.stdout, sys.stderr - Standard I/O streams
sys.stdout.write("Writing to standard output using sys.stdout.write\n")

# 7. sys.getsizeof - Size of an object in bytes
sample_string = "Hello, sys!"
print(f"Size of '{sample_string}' (sys.getsizeof):", sys.getsizeof(sample_string), "bytes")

# 8. sys.modules - List loaded modules
print("Is 'math' module loaded? ('math' in sys.modules):", 'math' in sys.modules)

# 9. sys.maxsize - Maximum size of a Python int
print("Maximum integer size (sys.maxsize):", sys.maxsize)

# 10. sys.exc_info - Exception information
try:
    1 / 0
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Exception info (sys.exc_info):", exc_type, exc_value)