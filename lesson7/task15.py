import sys


#'text2.txt'
#'text2.txt'

input_file = sys.argv[1]
output_file = sys.argv[2]
file_ = (open(input_file, 'rb')).read(1024)
open(output_file, 'wb').write(file_)
