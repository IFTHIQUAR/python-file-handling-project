import os
#CREATEING A FILE:
def create(file_name):
    try:
        with open(file_name,'x')as f:
            print(f"The File {file_name} created successfully")
    except FileExistsError:
        print(f"The file {file_name} already exists")
    except Exception as E:
        print("An Error Occurred")

#READING A FILE:
# read_file.py
#filename = "example.py"
def read(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


#WRITING A DATA INTO A FILE:
def write(file_name):
    try:
        with open(file_name,'w')as f:
            data=input("Enter data to write:")
            f.write(data)
            print("Your data written successfully")
    except Exception as E:
        print("An Error Occurred")

#UPDATING A DATA INTO A FILE:
def update(file_name):
    try:
        with open(file_name,'a')as f:
            data=input("Enter data to update:")
            f.write(data)
            print("Your data updated successfully")
    except FileNotFoundError:
        print(f"The file {file_name} Not Found")
    except Exception as E:
        print("An Error Occurred")
#DELETING A FILE:
def delete(file_name):
    try:
        os.remove(file_name)
        print(f"Your file {file_name} deleted successfully")
    except FileNotFoundError:
        print(f"The file {file_name} Not Found")
    except Exception as E:
        print("An Error Occurred")

#DISPLAYING A FILES:
def display():
    files=os.listdir()
    if not files:
        print("FILES NOT FOUND")
    else:
        for file in files:
            print(file)
def main():
    while True:
        print()
        print("### FILE MANAGEMENT SYSTEM ###")
        print("\n1.Create \n2.Read \n3.Write \n4.Update \n5.Delete\n6.Display\n7.Exit ")
        ch = int(input("ENTER YOUR CHOICE FOR FILE OPERATIONS:"))
        if ch == 1:
            file_name = input("Enter your file name:")
            create(file_name)
        elif ch == 2:
            file_name = input("Enter your file name:")
            read(file_name)
        elif ch == 3:
            file_name = input("Enter your file name:")
            write(file_name)
        elif ch == 4:
            file_name = input("Enter your file name:")
            update(file_name)
        elif ch == 5:
            file_name = input("Enter your file name:")
            delete(file_name)
        elif ch == 6:
            display()
        elif ch == 7:
            print("## APPLICATION CLOSED SUCCESSFULLY ##")
            break
        else:
            print("INVALID OPTIONS SELECTED")
if __name__=="__main__":
    main()
