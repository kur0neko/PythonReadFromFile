#function decode take path argument file as input

def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
#It initializes an empty list decoded_message
#to store the words of the decoded message.
    decoded_message = []
    current_number = 1

#iterates through each line of the file
 #split the line into a number and a word
    for line in lines:
        line = line.strip()
        if line:
            Some_parts = line.split(' ')
#if size of string Some_parts is == 2 check to ensure that the split operation yields exactly two parts
#if both conditions are meet, proceed with unpacking number and word from Some_parts
            if len(Some_parts) == 2:
                number, word = Some_parts
                number = int(number)
                while current_number < number:
                    current_number += 1
                decoded_message.append(word)
# lastly,after check and processing every lines,
#  It will joins the words in decoded_message list into a single string
# which separated by spaces and returns it as finish product decoded message.

    return ' '.join(decoded_message)


decoded_message= decode('coding_qual_input.txt')
print(decoded_message)
