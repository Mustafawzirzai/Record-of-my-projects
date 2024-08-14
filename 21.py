class File_manager():
    def __init__(self,file_path):
        self.path=file_path

    def read_file(self):
        try:
            with open(self.path, 'r') as file:
                content=file.read()
            return content

        except:
            return "error file not found"

    def write_to_file(self,content,mode='w'):
        try:
            with open(self.path,mode) as file:
                file.write(content)
        except:
            return "error occurred"

    
f1=File_manager('example.txt')

write=f1.write_to_file("hello this abdullah")
print(f1.read_file())











