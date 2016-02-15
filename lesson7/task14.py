import sys


catalog = sys.argv[1]
find_string = sys.argv[2]
file_ = (open(catalog, 'r')).readlines()
print(file_)
for i in range(len(file_)):
    if find_string in file_[i]:
        print(file_[i])
