saturation_input = input('Enter saturation channel value: ')
# tt=""
# if len(saturation_input) > 0:
#     temp = saturation_input[0]
#     c = 0
#     for s in saturation_input:
#         if s == temp:
#             c += 1
#         else:
#             tt+=str(c)+temp
#             temp = s
#             c = 1
#     tt += str(c) + temp
#     print(tt)
#
# else:
#     print("No input provided")
#     print(tt)
# DECODING CODE (Decompression)
encoded_input = input('Enter encoded string: ')

# Fix: Remove brackets '(' and ')' if the user types them
clean_input = encoded_input.replace("(", "").replace(")", "")

decoded_output = ""
temp_count = ""

if len(clean_input) > 0:
    for char in clean_input:
        # If character is a digit, build the number (e.g., "1" then "2" becomes 12)
        if char.isdigit():
            temp_count += char
        else:
            # If character is a letter, print it 'temp_count' times
            if temp_count != "":
                count = int(temp_count)
                decoded_output += char * count
                temp_count = "" # Reset count for next letter
            else:
                # Handle case where string starts with a letter or has no number
                decoded_output += char

    print(decoded_output)

else:
    print("No input provided")