import os
path = "wall_log.txt"
log_read = open(path, 'r')
#you have to open a file with a new file variable if you want to read it in a different way - otherwise it returns an empty string.

#log_string = log_read.read() #returns string of file contents, w/ \n for every new line
#print("log string:", log_string)

#log_line_1 = log_read.readline() #returns a string of the first line - every time this is called, it progresses to the next line
#print("log_line_1:", log_line_1)

#log_line_2 = log_read.readline() #returns a string of the second line - every time this is called, it progresses to the next line
#print("log_line_2:", log_line_2)

log_list = log_read.readlines() #returns a list of all lines - a new string for every new line
print("log_list:", log_list)
log_read.close()

title = 'Equation list:\n'

def create_file(filepath):
    filepath_end = []
    filepath_list = []
    folderpath = []
    filepath = filepath.replace("/", "\\")
    while "\\" in filepath:
        filepath_list = filepath.split("\\")
        print("line 27",filepath_list)
        while "" == filepath_list[0]:
            del filepath_list[0]
            print(filepath_list)

        folderpath = []
        folderpath.extend(filepath_list)
        del folderpath[-1]
        print("line 34:", folderpath)
        print("line 31:", "\\".join(folderpath))
        if os.path.isdir("\\".join(folderpath)) != True:
            make_folder("\\".join(folderpath))

        if "." in filepath_list[-1]:
            print("line 35:", filepath_list)
            filepath = "\\".join(folderpath)+"\\"+filepath_list[-1]
            break
                

    os.system("type nul > "+filepath)
    

def make_folder(foldername):
    os.system("mkdir "+foldername)
path = "boy/girl/hello/equation.txt"
create_file(path)
create_file("boy/girl/hello.txt")
create_file("/boy/hi.png")

