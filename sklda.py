saturation_input = input('Enter saturation channel value: ')
tt=""
if len(saturation_input) > 0:
    temp = saturation_input[0]
    c = 0
    for s in saturation_input:
        if s == temp:
            c += 1
        else:
            tt+=str(c)+temp
            temp = s
            c = 1
    tt += str(c) + temp
    print(tt)

else:
    print("No input provided")
    print(tt)

encoded_input = tt
decoded_output = ""
temp_count = ""

if len(encoded_input) > 0:
    for char in encoded_input:
        # Check if the character is a number (0-9)
        if char.isdigit():
            temp_count += char
        else:
            # We found a non-digit character, time to decode
            if temp_count != "":
                count = int(temp_count)
                decoded_output += char * count

                # Reset the count for the next group
                temp_count = ""
            else:
                # This handles cases where input might be malformed (e.g., starts with a letter)
                print("Error: Format incorrect. Expected number before character.")
                break

    print(decoded_output)

else:
    print("No input provided")