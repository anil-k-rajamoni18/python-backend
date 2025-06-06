from pathlib import Path

# 1. Create a Path object (relative)
file_path = Path("demo_folder") / "example.txt"

print(file_path)

# # 2. Create a directory (if it doesn't exist)
file_path.parent.mkdir(exist_ok=True)
print(f"Created folder: {file_path.parent}")

# # 3. Write text to the file
file_path.write_text("Hello from pathlib!")
print(f"Written to file: {file_path}")

# # 4. Read the file content
content = file_path.read_text()
print("File content:", content)

# # 5. Check if the file and folder exist
print("File exists:", file_path.exists())
print("Is file:", file_path.is_file())
print("Is directory:", file_path.parent.is_dir())

# # 6. Show file parts
print("File name:", file_path.name)
print("File suffix (extension):", file_path.suffix)
print("File stem:", file_path.stem)
print("Parent directory:", file_path.parent.resolve())

# # 7. File metadata
print("File size:", file_path.stat().st_size, "bytes")

# # 8. List all .txt files in the folder
print("\nText files in folder:")
for txt in file_path.parent.glob("*.txt"):
    print("-", txt.name)

# # 9. Rename the file
new_file_path = file_path.with_name("renamed_example.txt")
file_path.rename(new_file_path)
print(f"\nFile renamed to: {new_file_path.name}")

# # 10. Create another file and write something
extra_file = file_path.parent / "extra.txt"
extra_file.write_text("Another file.")
print("Created extra file.")

# # 11. Recursively list all .txt files
# print("\nAll .txt files (recursive):")
# for txt in file_path.parent.rglob("*.txt"):
#     print("-", txt.relative_to(file_path.parent))

# # 12. Cleanup: Delete files and directory
extra_file.unlink()
new_file_path.unlink()
file_path.parent.rmdir()
print("\nCleanup complete.")
