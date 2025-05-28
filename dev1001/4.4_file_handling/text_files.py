file = open('my_file.txt', 'a') # default is read
file.write("Hello\n")
file.close()

# Read
# 'with' automatically closes the file when it ends
with open('my_file.txt') as f:
  # files internally track their current position
  # all_content = f.read(3)
  # print(all_content) # reads 3 characters
  first_line = f.readline()
  print(first_line.strip())
  second_line = f.readline()
  print(second_line)

  
