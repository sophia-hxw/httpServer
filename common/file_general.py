## 列出path下所有子目录名称（带路径）
def list_dir(path):
    import os

    list_name = []
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path): 
            list_name.append(file_path)
        else:  
            pass
    
    list_name.sort()
    return list_name

## 列出path下所有子文件名称（带路径）
def list_file(path):
    import os
    list_name = []
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if not os.path.isdir(file_path): 
            list_name.append(file_path)
        else:  
            pass
    
    list_name.sort()
    return list_name

## 列出path下所有后缀为ext的文件
def list_file_ext(path, ext=".jpg"):
    import os
    list_name = []
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)
        if os.path.splitext(file)[1]==ext:
            list_name.append(file_path)

    list_name.sort()   
    return list_name

## 读文本文件
def read_txt(txt_file):
    with open(txt_file, "r") as f:
        data = [x.strip() for x in f.readlines()]
        return data

## 写文本文件
def write_txt(str_words, fname, mod="a+"):
    with open(fname,mod) as f:
        f.write(str_words)
        f.write('\n')