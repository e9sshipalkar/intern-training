#using a built in context manager
with open ("eample.txt", "w") as file:
    file.write("hello python")
    print("file operation completed.")

