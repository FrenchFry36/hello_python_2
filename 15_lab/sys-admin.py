# import the os module
import os

# os.system() takes a string argument
os.system("ls")

# the more powerful subprocess.run() function, the full list of arguments for subprocess.run() looks like the following list: 
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

# import the subprocess module
import subprocess

# os.system() takes a string argument covered by square brackets
subprocess.run(["ls"])

# in Python, the square brackets are list data types, which means that run() can take a list of arguments.
# the "-l" is an argument that tells the ls command to use a long-listing format.
subprocess.run(["ls","-l"])

# the third argument will be a directory name 
subprocess.run(["ls","-l","README.md"])

# retrieving system information
command="uname" # the uname command to get system information
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# retrieving information about disk space,
# the df command to get disk information
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])