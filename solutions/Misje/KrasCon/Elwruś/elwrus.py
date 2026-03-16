#python

def decrypt_punchcard(file_name):
    with open(file_name, 'r') as file:
        data = file.read().strip()
        
    bajt_list = []
    x = 0
    y = 8
    while y <= len(data):
        bajt_list.append(data[x:y])
        x += 8
        y += 8
        
    message = ""
        
    for bajt in bajt_list:
        message += chr(int(bajt, 2))
        
    return message
        
