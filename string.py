# Input string
s = input("Enter a string: ")

# Check if the string has at least 3 characters
if len(s) < 3:
    print("Input string should have at least 3 characters.")
else:
    # Calculate the index of the middle character(s)
    middle_index = len(s) // 2
    
    # Construct the new string
    new_str = s[0] + s[middle_index] + s[-1]
    
    # Print the new string
    print("New string:", new_str)
  
  ############

  # Input string
s = input("Enter a string: ")

# Check if the string has at least 3 characters
if len(s) < 3:
    print("Input string should have at least 3 characters.")
else:
    # Calculate the index of the middle character(s)
    middle_index = len(s) // 2
    
    # Construct the new string
    new_str = s[middle_index - 1:middle_index + 2]
    
    # Print the new string
    print("New string:", new_str)

################

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Calculate the midpoint of str1
midpoint = len(str1) // 2

# Create the new string by concatenating str1 up to the midpoint, then str2, then the rest of str1
str3 = str1[:midpoint] + str2 + str1[midpoint:]

print("The new string str3 is:", str3)

################

str1 = "P@#yn26at&i5ve"


letter_count = 0
digit_count = 0
special_count = 0


for char in str1:
    
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        letter_count += 1
   
    elif char.isdigit():
        digit_count += 1
    
    else:
        special_count += 1

print("Number of letters:", letter_count)
print("Number of digits:", digit_count)
print("Number of special symbols:", special_count)

###############
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Initialize an empty string to hold the result
s3 = ""

# Initialize indices for iterating through s1 and s2
index_s1 = 0
index_s2 = 0

# Loop until both strings are exhausted
while index_s1 < len(s1) and index_s2 < len(s2):
    # Append the first character from s2
    s3 += s2[index_s2]
    index_s2 += 1

    # Append the second character from s1
    s3 += s1[index_s1]
    index_s1 += 1

# If there are leftover characters in s2, append them
while index_s2 < len(s2):
    s3 += s2[index_s2]
    index_s2 += 1

# If there are leftover characters in s1, append them
while index_s1 < len(s1):
    s3 += s1[index_s1]
    index_s1 += 1

print("The new string s3 is:", s3)


