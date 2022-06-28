word="Madam"
word= word.lower()
reverse_word=""
for char in word:
    reverse_word=reverse_word+char 
if reverse_word==word :
    print("Palindrome")
else:
    print("Not a palindrome")
    