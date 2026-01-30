import io
try:
    file_handler=open("sample.txt","rt")
    print("line1:",file_handler.readline())
    print("line2:",file_handler.readline())
except FileNotFoundError as er:
    print(er)
    
