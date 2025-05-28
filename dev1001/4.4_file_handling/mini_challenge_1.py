diary_file = "diary_entry.txt"

# 1. Write two lines about your day (use 'w' mode)
with open(diary_file, 'w') as f:
  f.write("Dear\n")
  f.write("Diary\n")
    

# 2. Read and print content (use 'r' mode)
with open(diary_file, 'r') as f:
  for line in f:
    print(line.strip())
    # print(f.read())
