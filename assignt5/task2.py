import sys
my_text_file = sys.argv[1]
with open(my_txt_file, 'r') as f:
    f_cont = f.read()

print(f_cont)
