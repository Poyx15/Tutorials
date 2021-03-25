from pathlib import Path

# Absolute path
# C:\Program Files\Microsoft
# /usr/local/bin

# Relative path

path = Path()
for file in path.glob("*.py"):  # search all .py files in current directory
    print(file)

# path.mkdir make directory
# path.rmdir remove directory
# visit pathlib document
