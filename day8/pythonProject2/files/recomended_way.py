# with open('allFiles/jabberwocky','r') as jabber:
#     for line in jabber:
#         print(line, end='')

# #not appropriate for large files as there may be memory limitations
# with open('allFiles/jabberwocky','r') as jabber:
#
#     lines = jabber.readlines()
# print(lines)
# op
# #['operation rolling thunder\n', 'joseph kurilal']

## we get an immutable string
# with open('allFiles/jabberwocky', 'r') as jabber:
#     text = jabber.read()
#
# print(text)

# read a file line by line
with open('allFiles/jabberwocky', 'r') as jabber:
    while True:
        line = jabber.readline()
        print(line)
        if 'jubjub' in line.casefold():
            break


print('*' * 80)