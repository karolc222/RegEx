import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'https?://(www\.)?')

matches = pattern.finditer(emails)

for match in matches:
    print(match)