#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("./mail_merge/Input/Names/invited_names.txt") as file:
    names=file.readlines()
with open("./mail_merge/Input/Letters/starting_letter.txt") as file:
    letter=file.read()
    print(letter)
    for name in names:
        new_letter_text=letter.replace("[name]", name.strip())
        new_letter=open(f"./mail_merge/Output/ReadyToSend/letterTo{name.strip()}.txt","w")
        new_letter.write(new_letter_text)
        new_letter.close()