from glob import glob
from os import rename

pattern = "sample_data/*.csv"
new_ext = 'txt'
dry_run = False
files = glob(pattern)

for file in files:
    name, ext = file.split('.')
    new_name = name + '.' + new_ext
    if not dry_run:
        rename(file, new_name)
    print(file, '->', new_name)
print("Koniec")
