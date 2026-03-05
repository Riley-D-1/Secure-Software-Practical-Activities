def read_all_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # This reads the entire file into memory - inefficient for large files
    for line in lines:
        print(line.strip())

# Task:
# - Rewrite this function to process the file line-by-line instead of loading everything at once.
# - Use a generator or iterate directly over the file object for memory efficiency.