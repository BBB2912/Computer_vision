#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt

names_list=[]
with open(r'./Input/Names/invited_names.txt','r') as file:
    names=file.readlines()
    for name in names:
        names_list.append(name.strip('\n'))
print(names)

#Replace the [name] placeholder with the actual name.

for name in names:
    with open(r'./Input/Letters/starting_letter.txt') as letter:
        letter_content=letter.read()
        replace_letter_content=letter_content.replace('[name]',name)
        new_letter_path=r'./Output/ReadyToSend/'
        new_letter_name=f'letter_for_{name}.txt'
        destination_path=new_letter_path+new_letter_name
        with open(destination_path,'w') as new_file:
            new_file.write(replace_letter_content)
            new_file.close()
#Save the letters in the folder "ReadyToSend".
