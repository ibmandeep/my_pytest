with open('workfile.txt', 'r+') as f:
    # f.write("This is some data.....")
    read_data = f.read()
    print(read_data)
print(f.closed)
