# With this code it is possible to find file extension

name = input("File name: ")

if name.endswith(".gif"):
    print("image/gif")
elif name.endswith(".jpeg") or name.endswith(".jpg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
elif name.endswith(".pdf"):
    print("application/pdf")
elif name.endswith(".txt"):
    print("documnet/txt")
elif name.endswith(".zip"):
    print("documnets/zip")
else:
    print("application/octet-stream")    