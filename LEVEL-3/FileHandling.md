# 📘 File  in Python

## 📁 What is a File and Directory?

### 🔸 File

* A **file** is a named location on disk used to store data.
* Files can contain text, images, videos, or data in specific formats like .txt, .csv, .json, etc.
* Files are essential for **persistent storage** of data.
* They store data in non-volatile memory (e.g., hard drive), unlike RAM, which is volatile.

### 🔸 Directory

* A **directory** (or folder) is a container that holds files and/or other directories.
* It helps organize files on a storage device.

```
ocuments/
  |-- resume.txt
  |-- project/
        |-- code.py
        |-- data.csv
```
---

## 📝 What is File Handling in Python?

File handling is the ability of Python to **create, read, write, and manipulate files** on a storage device.

### ❓ Why is File Handling Important?

* To store output data permanently (e.g., logs, reports).
* To read configurations or external data.
* To interact with the file system for automation.

**Example**
- Saving a user's feedback in feedback.txt
- Reading configuration from settings.json
- Automatically creating a logs/ directory before writing log files.

---

## 🧰 Overview of the `os` Module

The `os` module provides a way of using operating system-dependent functionality.

### 🔹 Commonly Used `os` Methods:

| Method                 | Description                                |
| ---------------------- | ------------------------------------------ |
| `os.getcwd()`          | Returns current working directory          |
| `os.chdir(path)`       | Changes current working directory          |
| `os.listdir(path)`     | Lists files and directories in given path  |
| `os.mkdir(path)`       | Creates a new directory                    |
| `os.makedirs(path)`    | Creates intermediate directories if needed |
| `os.remove(file)`      | Removes a file                             |
| `os.rmdir(dir)`        | Removes a directory                        |
| `os.path.exists(path)` | Checks if a path exists                    |
| `os.path.join()`       | Joins one or more path components          |


```python
import os

# Get current working directory
print(os.getcwd())

# Change directory
os.chdir('/path/to/another/folder')

# List files and directories
print(os.listdir())

# Create a directory
os.mkdir("new_folder")

# Remove a directory
os.rmdir("new_folder")

# Check if file exists
print(os.path.exists("data.txt"))
```
---
## 🔓 open() Function in Python
- The open() function is used to open a file and returns a file object. It supports multiple parameters for fine-tuned control.
```python
open(
    file,                # Path to the file (string or path-like object)
    mode='r',            # Mode in which to open the file
    buffering=-1,        # Buffering policy (-1 means system default)
    encoding=None,       # Encoding type (used in text mode)
    errors=None,         # Error handling scheme
    newline=None,        # Controls universal newlines
    closefd=True,        # If False, the file descriptor won't be closed
    opener=None          # Custom opener (used for low-level file access)
)
```

**📖 File Opening Modes**
| Mode  | Description                                                                  |
| ----- | ---------------------------------------------------------------------------- |
| `'r'` | Read mode (default). Opens the file for reading. File must exist.            |
| `'w'` | Write mode. Opens the file for writing and **overwrites** existing content.  |
| `'x'` | Exclusive creation. Fails if the file already exists.                        |
| `'a'` | Append mode. Opens the file for writing and appends to the end if it exists. |
| `'b'` | Binary mode. Used for binary files (e.g., images, audio).                    |
| `'t'` | Text mode (default). Used for text files.                                    |
| `'+'` | Read and write mode. Allows both reading and writing.                        |
| `'U'` | Universal newline mode (deprecated). Use `newline=None` instead.             |



---

## 📖 How to Read a File

### 🔸 Steps to Read a File:
- Open the file using open().
- Read using read methods.
- Close the file (or use with block).

```python
# Open file in read mode
file = open("example.txt", "r")

# Read contents
content = file.read()
print(content)

# Close file
file.close()
```

```python
# Read entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Read line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Read specific number of characters
with open('example.txt', 'r') as file:
    part = file.read(10)
    print(part)
```

### 🔹 Reading Methods:

| Method             | Description                        |
| ------------------ | ---------------------------------- |
| `file.read()`      | Reads the entire file as a string  |
| `file.readline()`  | Reads a single line                |
| `file.readlines()` | Reads all lines and returns a list |



**Reading from an Unknown File**
```python
f = open('sample.txt', mode='r')
print(f.read())


# User provides a file name at runtime. The program reads and prints the content if the file exists.
import os

filename = input("Enter the name of the file to read: ")

if os.path.exists(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print("\n📄 File Content:\n")
        print(content)
else:
    print("❌ File not found.")

```

---

## ✍️ How to Write a File 

### 🔸 Steps to Write a File:

```python
# Open file in write mode (creates or overwrites file)
file = open("example.txt", "w")

# Write content
file.write("Hello, world!\n")

# Close file
file.close()
```

### 🔹 Writing Modes:

| Mode   | Description                           |
| ------ | ------------------------------------- |
| `"w"`  | Write mode (overwrites existing file) |
| `"a"`  | Append mode (adds to the end of file) |
| `"x"`  | Create mode (fails if file exists)    |
| `"r+"` | Read and write mode                   |

**E1: Writing to an Unknown File**
- The user specifies the file name and content to write. If the file doesn’t exist, it’s created.
```python
filename = input("Enter the name of the file to write to: ")
text = input("Enter the text you want to write: ")

with open(filename, 'w') as file:
    file.write(text)
    print(f"✅ Text successfully written to {filename}")
```

**E2:  Appending to an Unknown File**
```python
filename = input("Enter the file name to append to: ")
more_text = input("Enter the text to append: ")

with open(filename, 'a') as file:
    file.write('\n' + more_text)
    print("✅ Text appended.")

```

---

## ✅ Best Practices

* Always **close** the file after use.
* Use `with` statement to automatically close files:

```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```

* Use `os.path.exists()` before reading/writing to prevent errors.
---

### 📄 Common File Object Attributes
| Attribute         | Description                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------- |
| `file.name`       | Returns the **name** of the file.                                                        |
| `file.mode`       | Returns the **mode** in which the file was opened (e.g., `'r'`, `'w'`).                  |
| `file.closed`     | Returns `True` if the file is **closed**, otherwise `False`.                             |
| `file.encoding`   | Returns the **encoding** used to decode or encode the file (only for text files).        |
| `file.newlines`   | Shows the **line-ending conventions** used in the file (`None`, `'\n'`, `'\r\n'`, etc.). |
| `file.readable()` | Returns `True` if the file is opened in a **readable mode**.                             |
| `file.writable()` | Returns `True` if the file is opened in a **writable mode**.                             |
| `file.seekable()` | Returns `True` if the file supports **random access** (i.e., you can use `seek()`).      |


```python
with open("example.txt", "r") as f:
    print("Name:", f.name)
    print("Mode:", f.mode)
    print("Closed:", f.closed)
    print("Encoding:", f.encoding)
    print("Is Readable?", f.readable())
    print("Is Writable?", f.writable())
    print("Is Seekable?", f.seekable())
```

### 📘 File Object Methods
| Method             | Description                                      | Example Usage                           |
| ------------------ | ------------------------------------------------ | --------------------------------------- |
| `read([size])`     | Reads the entire file or up to `size` characters | `file.read()`                           |
| `readline()`       | Reads one line from the file                     | `file.readline()`                       |
| `readlines()`      | Reads all lines into a list                      | `file.readlines()`                      |
| `write(str)`       | Writes a string to the file                      | `file.write(\"Hello\")`                 |
| `writelines(list)` | Writes a list of strings to the file             | `file.writelines([\"a\\n\", \"b\\n\"])` |
| `close()`          | Closes the file                                  | `file.close()`                          |
| `flush()`          | Flushes the buffer to disk                       | `file.flush()`                          |
| `seek(offset)`     | Moves the file pointer to a specific location    | `file.seek(0)`                          |
| `tell()`           | Returns the current file pointer position        | `file.tell()`                           |
| `truncate([size])` | Resizes the file                                 | `file.truncate(10)`                     |

```python
# Create or overwrite a test file
with open("demo.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

# Open the file in read+write mode
with open("demo.txt", "r+") as f:
    print(" Reading entire content:")
    print(f.read())                    # read()

    f.seek(0)                          # Move cursor to start
    print("\n Reading line by line:")
    print(f.readline())               # readline()
    print(f.readline())

    f.seek(0)
    print("\n Reading all lines as list:")
    print(f.readlines())              # readlines()

    f.seek(0, 2)                       # Move to end of file
    print("\n Writing new line:")
    f.write("Line 4\n")               # write()

    print("\n Writing multiple lines:")
    f.writelines(["Line 5\n", "Line 6\n"])  # writelines()

    print("\n Current position (in bytes):", f.tell())  # tell()

    print("\n Truncating file to 20 bytes:")
    f.truncate(20)                    # truncate()

    f.flush()                         # flush()
    print(" File flushed to disk.")

# Check if file is closed
f = open("demo.txt")
print("\n Is file closed?", f.closed)
f.close()
print(" Is file closed after calling close()?", f.closed)
```

---

## 📚 Summary

* Files and directories are essential for data organization.
* Python offers built-in support for file handling.
* The `os` module provides powerful directory and file system interaction tools.
* Use appropriate file modes for reading and writing.
* Always close or manage file resources properly.

## Hands On Questions 

**1. Dynamic Log File Creator**
- Write a script that asks the user for a log message, then appends it with a timestamp to a file named app.log. 
- If the file doesn’t exist, it should create it automatically.

**2. File Content Analyzer**
Write a program that asks the user for a filename, reads the file, and prints:
- Total number of lines
- Total number of words
- Total number of characters
- Handle the case if the file doesn’t exist gracefully.

**3. CSV File Column Extractor**
- Input: A CSV file (e.g., records.csv) with multiple columns
- Task: Ask the user for a column name, then create a new file extracted_column.txt containing all the values of that column (one per line).


**5. Filter Log by Date**
- Input: A log file server.log with lines starting with dates in YYYY-MM-DD format
- Task: Ask the user to input a date (e.g., 2023-05-20). Create a new file filtered.log that contains only the lines from the original log that match the input date.

**4. Reverse Lines in File**
- Input: A text file (e.g., story.txt)
Task: Read the file and write a new file story_reversed.txt where the order of the lines is reversed (last line becomes first).

**5. Build a File Explorer Tool**
- Accept a folder name as input
- List all files and directories
- For each file, show size and creation date
- Let the user pick a file to view or delete

**6. Store User Data**
- Make a request to the endpoint: https://reqres.in/api/users?page=2
- Store the response from the request
- Parse the response as JSON and save it to a variable
- Create a file named users.txt
- Extract all usernames from the JSON data, formatting each as last_name, first_name
- Write all usernames and email into the users.csv file, one per line