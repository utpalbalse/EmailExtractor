
#Program to extact all emails from a copied text and store it in a txt file in the same folder.

#Importing the 're' module for regular expressions and 'pyperclip' module for getting text from clipboard.
import re, pyperclip

#Creating a variable to find all emails of the type example@example.com
EmailDump = re.compile(r'[A-Z1-z0-9_.]+@[A-Z1-z0-9_.]+') 

#Storing copied text from clipboard in copiedText
copiedText = pyperclip.paste()

#Extracting emails from the text and storing in EmailExtract
EmailExtract = EmailDump.findall(copiedText)

#Storing and indenting emails in Emails
Emails= '\n'.join(EmailExtract)

#Creating(or overwriting) a emails.txt file to store all emails
EmailFile = open('emails.txt', 'w')
EmailFile.write(Emails)
EmailFile.close()


