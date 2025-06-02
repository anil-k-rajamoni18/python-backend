import os

# 1. User-defined exception
class InvalidFileTypeError(Exception):
    pass

# 2. File processing function
def process_file(filename):
    try:
        # Check file extension
        if not filename.endswith(".txt"):
            raise InvalidFileTypeError("Only .txt files are allowed.")

        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print("File not found.")
        else:
            print("File opened successfully.")
            lines = file.readlines()
            print(f"Total lines: {len(lines)}")
            for line in lines:
                print(line.strip())
        finally:
            if 'file' in locals():
                file.close()
                print("File closed.")
    except InvalidFileTypeError as e:
        print(e)
    except Exception as e:
        print("Unexpected error:", e)

# 3. Main execution
try:
    filename = input("Enter filename to process: ")
    if not filename.strip():
        raise ValueError("Filename cannot be empty.")
    process_file(filename)
except ValueError as e:
    print(e)
except Exception as e:
    print("General error:", e)
else:
    print("File processed successfully.")
finally:
    print("Program ended.")
