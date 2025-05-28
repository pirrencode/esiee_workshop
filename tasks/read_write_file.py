# TASK: Write a code to read helloworld.txt and then write it back
# message: Hello world in French language
# Program title: read_write_file.py

try:
  with open('helloworld.txt', "r") as file:
    print(file.read())
  file.close()
  with open('helloworld.txt', "w") as file:
    file.write("Bonjour a tous!")
  file.close()
except FileNotFoundError as e:
  print("Missing file : {e}")
else:
  print('Succes')
finally:
  print('All operations are completed. Let's go for a break!')
  
