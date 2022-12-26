def file_generator(filename):
    with open(filename+'.txt', 'r') as f:
        for line in f:
            yield line

def type_line(line):
    space_splited = line.replace("\n", "").split(" ")
    data = {}
    if space_splited[0] == "$":
        data["what"] = "command"
        data["action"] = space_splited[1:]
    elif space_splited[0] != "dir":
        data["what"] = "file"
        data["size"] = int(space_splited[0])
    else:
        data["what"] = "dir"
    return data

def generate_pwd(pwd):
    str_pwd = ""
    for folder in pwd:
        str_pwd+=folder+"/"
#     print(str_pwd[1:])
    return str_pwd[1:]

def add_size_recursive(pwd_size, pwd, size):
    folder = []
    for i in range(len(pwd)-1):
        folder.append(pwd[i])
#         print(i, folder)
        pwd_size[generate_pwd(folder)] += size    
    
pwd = []
size = 0
pwd_size = {}
first_cmd = False
for line in file_generator("day7"):
    data = type_line(line)
    if data["what"] == "command":
        if first_cmd:
            first_cmd = False
            pwd_size[generate_pwd(pwd)] = size
            add_size_recursive(pwd_size, pwd, size)
        cmd = data["action"][0]
        if cmd == "ls":
            size = 0
        elif cmd == "cd":
            if data["action"][1] == "..":
                del pwd[-1]
            else:
                pwd.append(data["action"][-1])
    else:
        first_cmd = True
    if data["what"] == "file":
        size += data["size"]
pwd_size[generate_pwd(pwd)] = size
add_size_recursive(pwd_size, pwd, size)

total_space_disk = 70000000
total_use_disk = pwd_size['/']
total_free_disk = total_space_disk-total_use_disk
minimal_space_need = 30000000
folder_delete = ""
folder_minimal_space = total_use_disk
for pwd in pwd_size:
    size = total_free_disk+pwd_size[pwd]
#     print("\n",total_free_disk+pwd_size[pwd], end="")
    if size >= minimal_space_need:
#         print("  okay !", end="")
        if pwd_size[pwd] < folder_minimal_space:
            folder_minimal_space = pwd_size[pwd]
            folder_delete = pwd
            
print("folder to delete :")
print(folder_delete, "size:",folder_minimal_space)
print("space free after :",total_space_disk-(total_use_disk-folder_minimal_space))