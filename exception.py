# user defined Exception

class accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print("user defined exception: ", self.msg)
        
try:
    raise accident('crash between 2 cars')
except accident as e:
    e.print_exception()
        





# built in error
# try:
#     raise MemoryError('memory error')
# except MemoryError as e:
#     print(e)  
