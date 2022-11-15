import os
currentPath = os.getcwd()
# print(currentPath)
# text_file_path = 'c:/Users/Topik Korea/Desktop/KS6HAD_/03/14.htm'
# text_file_path = '20/01.htm'
new_text_content = ''

chasi = 30
chapter = ['01', '02', '04', '06', '08', '10', '11', '12', '14']
src_path = []

for x in range(1, chasi+1):
    for y in chapter:
        src_path.append('{0:02d}/{1}.htm'.format(x, y))
# print(src_path)
for y in range(0, len(src_path),):
    with open(src_path[y], 'rt', encoding='utf-8') as f:
        print(src_path[y], y)
        lines = f.readlines()
        for i, l in enumerate(lines):
            if i == 85:
                new_string = '\t\t\turl1 = setContentPath(url1);\n\t\t\turl2 = setContentPath(url2);\n'
            else:
                new_string = l
            if new_string:
                new_text_content += new_string
            else:
                new_text_content += '\n'
        f.close()
    with open(src_path[y], 'w', encoding='utf-8') as f:
        f.write(new_text_content)
        f.close()
        new_text_content = ''
