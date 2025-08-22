user_file = input("Enter the file path to be read: ")

try: 
  with open(user_file, 'r') as file:
    content = file.read()
    print("File content read successfully:")
    print(content)

except FileNotFoundError:
  print("The file was not found.")

except Exception as e:
  print(f"An error occurred: {e}")