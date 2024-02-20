import webbrowser
import random
file_path = "D:/폐기/list.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    
url_list = content.split('\n')

choicelist = random.choice(url_list)

webbrowser.open_new(choicelist)