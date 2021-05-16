str = 'X-DSPAM-Confidence:0.8475'
# extracting portion the string after the colon
first_index = str.find(':')
str_portion = str[first_index + 1:]
str_portion = float(str_portion)
print(str_portion)