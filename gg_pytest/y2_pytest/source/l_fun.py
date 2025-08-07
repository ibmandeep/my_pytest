from subprocess import Popen, PIPE

# process = Popen(['ls', '-l'], stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()

# print("Output:", stdout.decode())
# print("Errors:", stderr.decode())


# process = Popen(['df', '-h'], stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()

# print("Output:", stdout.decode())
# print("Errors:", stderr.decode())



from black import format_str, FileMode

code = "def add(x,y):\n if x == 2:\n    return x+y"

formatted_code = format_str(code, mode=FileMode())

print(formatted_code)