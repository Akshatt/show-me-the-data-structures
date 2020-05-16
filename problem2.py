import os

def find_files(suffix, path):
    if suffix == '' or not os.path.exists(path):
        return "Error:for {} files in {}\nFile/Directory does not exist".format(suffix,path) 
    
    path_entries = os.listdir(path)
    
    #base case
    if len(path_entries) == 0:
        return []
    
    #file_paths = [path+'/'+file for file in path_entries if file.endswith('.'+ suffix)]
    #sub_dir = [directory for directory in path_entries if '.' not in directory]
    sub_dir = []
    file_paths = []
    for entry in path_entries:
        if entry.endswith('.' + suffix):
            file_paths.append(path+'/'+entry)
        elif '.' not in entry:
            sub_dir.append(entry)
    
    for dir in sub_dir:
        file_paths.extend(find_files(suffix,path+'/'+dir))
        
    return file_paths


#testcase1 - has both .c files and sub directories containing .c files
print("testcase 1")
print(find_files('c', './testdir1'))


#testcase2 - has no .c files and only sub directories with other files so should return empty list
print("\ntestcase 2")
print(find_files('c', './testdir2'))

#testcase3 - path doesnt exist: should return with error msg
print("\ntestcase 3")
print(find_files('c', './testdir1/imaginary_directory'))

#testcase4 - suffix not provided: should return with error msg 
print("\ntestcase 4")
print(find_files('', './testdir2'))