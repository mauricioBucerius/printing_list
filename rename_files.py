import os


def get_int_key(string, key):
    for part in string.split('_'):
        if not part.find(key) == -1:        
            return int(part.replace(key, ''))
    return None
    
def change_key(string, key, value):
    splitted_string = string.split('_')
    for idx, part in enumerate(splitted_string):
        if not part.find(key) == -1: 
            splitted_string[idx] = f'{key}{value}'
    return '_'.join(splitted_string)

def rename_files(name, value, datatype):
    idx = 0
    for entry in os.listdir():
        if not entry.find(datatype) == -1:
            # print(entry, name, value)
            if not get_int_key(entry, name) == value:
                new_filename = change_key(entry, name, value)
                print(f'rename file {entry} to {new_filename}')
                os.rename(entry, new_filename)
                idx += 1
    
    if idx > 0:
        print(f'Renamed {idx} Files!')
    else:
        print('Nothing to rename...')
            # exit()
    
if __name__ == '__main__':
    KEY_1 = 'KEY NAME 1'
    KEY_VALUE_1 = 0
    
    rename_files(KEY_1, KEY_VALUE_1)
