import os

'''Create A Folder'''
os.mkdir("Sahil")
print("Folder Created Successfully !")

'''Delete A Folder'''
os.rmdir("Sahil")
print("Folder deleted Successfully !")


'''Get Current Working Directory / Location'''
Location = os.getcwd()
print(f"Current Working Path = {Location}")


'''Remove a Particular Thing From this''' 
rm = os.remove("Sahil.jpg")
print("File Remove Successfully !")


'''Exit The Program Immediately'''
print("Exit From The Program")
os._exit(0)