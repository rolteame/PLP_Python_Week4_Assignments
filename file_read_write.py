try:
  with open('week4/newFileWrite.txt', 'w') as file:
    file.write('This is a new file created for writing.\n')
    file.write('It contains multiple lines of text.\n')
    file.write('This is the third line.\n')

  with open('week4/newFileWrite.txt', 'r') as file:
    content = file.read()
    print("File content read successfully:")
    
  with open('week4/newFileRead.txt', 'w') as file:
    file.write(content.upper())
    print("File content written to newFileRead.txt in uppercase.")

except FileNotFoundError:
  print("The file was not found.")

except Exception as e:
  print(f"An error occurred: {e}")

finally:
  print("Execution completed.")