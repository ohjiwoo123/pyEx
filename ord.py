def print_args(argc,*argv):
    for i in range(argc):
        print(argv[i])

print_args(args=3,"argv1","argv2","argv3")