class Log():
    def __init__(self,file_name):
        self.file=file_name

    def write_error(self):
        with open(self.file,'a') as file:
            file.write("error! cannot open this file")
    with open('my_log_file.txt','r') as file:
        content=file.read()
        print(content)

log=Log('my_log_file.txt')
log.write_error()

