
# try:
#     file = open("a_file.txt")#will cause FileNotFound error
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["asdaf"])#will give KeyError
# except FileNotFoundError:
#     with open("a_file.txt","w") as file:
#         file.write("Hello")
# except KeyError as error_message:
#     print(f"KeyError:{error_message} does not exist!")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed!")
#     raise TypeError("This error was created by me :)")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters !")
    

bmi = weight / height ** 2
print(bmi)
