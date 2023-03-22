import os
from rename_files import rename_files

PATH_REMOVE = 'Insert Path'
FOLDER = 'Insert Folder'

DELIMITER = 'Insert Delimiter'
DATATYPE = 'Insert Datatype'

KEY_NAME_1 = 'Insert Key Name 1'
KEY_NAME_2 = 'Insert Key Name 2'
START_KEY_1 = int(FOLDER.split(DELIMITER)[-1])
START_KEY_2 = 0

HEADER = 'BEGIN DSCRDATA\n% INDEX file\n' # for ADS

FILENAME = f"INSERT BASEFILENAME {os.path.basename(FOLDER).lower().replace(' ', '_')}.txt"


def get_int_key(string, key):
    for part in string.split('_'):
        if not part.find(key) == -1:        
            return int(part.replace(key, ''))
    return None
    
def get_file(file, idx, key):
    new_file_list = []
    for part in file.split('_'):
        if not part.find(key) == -1:
            new_file_list.append(f'{key}{idx}')
        else:
            new_file_list.append(part)
    return '_'.join(new_file_list)

def get_key(string):
    key_1 = get_int_key(string, KEY_NAME_1)
    key_2 = get_int_key(string, KEY_NAME_2)
    # print(string, key_1, key_2, key_1 == 0, key_2 != 0)
    if key_1 == START_KEY_1 and key_2 == START_KEY_2:
        return START_KEY_1
    elif key_1 != START_KEY_1 and key_2 == START_KEY_2:
        return key_1
    elif key_1 == START_KEY_1 and key_2 != START_KEY_2:
        return key_2
    else:
        return 0

def get_path(filename):
    wd = os.getcwd()
    if not wd.find('\\') == -1:
        wd = os.getcwd().replace('\\', '/')
    
    if len(PATH_REMOVE) > 0:
        path = wd.replace(PATH_REMOVE, '..')
        return f'{path}/{filename}'
    else:
        return wd

def main():
    files_key_1 = []
    files_key_2 = []
    idx_key_1 = START_KEY_1
    idx_key_2 = START_KEY_2
    cnt_miss = 0
    files_miss = []
    
    for entry in os.listdir():
        if entry.split('.')[-1].lower() == DATATYPE:
            
            if get_int_key(entry, KEY_NAME_1) > START_KEY_1:
                files_key_1.append(entry)
                                    
            elif get_int_key(entry, KEY_NAME_2) > START_KEY_2:
                files_key_2.append(entry)
                                    
            elif len(files_key_1) == 0 and len(files_key_2) == 0:
                files_key_1.append(entry)
                files_key_2.append(entry)
        
    files_key_1.sort(key=get_key)
    files_key_2.sort(key=get_key)
    
    print(f'Key 1 list entries: {len(files_key_1)} \t Key 2 list entries: {len(files_key_2)}')
    with open(FILENAME, 'w') as file:
        print(f'Opens File: {FILENAME}')
        file.write(HEADER)
        
        idx = 0
        if len(files_key_1) > 1:
            for entry in files_key_1:
                cur_idx_key_1 = get_int_key(entry, KEY_NAME_1)
                
                path = get_path(entry)
                print(f'Writes Line: {idx: <3}{path}')
                file.write(f'{idx: <4}{path}\n')
                idx += 1
                
                if cur_idx_key_1 == idx_key_1:
                    idx_key_1 += 1
                else:
                    file.write(f'{idx: <4}{path}\n')
                    idx += 1
                    files_miss.append(get_file(entry, idx_key_1, KEY_NAME_1))
                    idx_key_1 = cur_idx_key_1 + 1
                    cnt_miss += 1
                idx += 1
        else:
            files_key_1 = []
            
        if len(files_key_2) > 1:
            for entry in files_key_2:
                cur_idx_key_2 = get_int_key(entry, KEY_NAME_2)
                
                path = get_path(entry)
                print(f'Writes Line: {idx: <3}{path}')
                file.write(f'{idx: <4}{path}\n')
                idx += 1
                
                if cur_idx_key_2 == idx_key_2:
                    idx_key_2 += 1
                else:
                    file.write(f'{idx: <4}{path}\n')
                    idx += 1
                    files_miss.append(get_file(entry, idx_key_2, KEY_NAME_2))
                    idx_key_2 = cur_idx_key_2 + 1
                    cnt_miss += 1
        else:
            files_key_2 = []
                
        file.write('END')
    print(f'Done Writing {len(files_key_1)} elements in List 1 and {len(files_key_2)} in List 2')
    print(f'Writes {len(files_key_1) + len(files_key_2)} lines of paths\n')
    if cnt_miss > 0:
        print(f'{cnt_miss} files are missing:')
        
        for entry in files_miss:
            print(f'- {entry}')
    
if __name__ == '__main__':
    
    # changes
    if not os.path.basename(os.getcwd()) == os.path.basename(FOLDER):
        path = '\\'.join([os.getcwd(), FOLDER])
        os.chdir(path)
    # only have to rename, when the naming convention in the measureming fails
    # rename_files(KEY_NAME_1, START_KEY_1, DATATYPE)
    
    main()
