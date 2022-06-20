def Filename_Extension(Filename):
    a=Filename.split(".")
    d={"py":"python","java":"java","c":"C program","c++":"C plus plus","c#":"C-Sharp or C-Hash","html":"html","css":"cascading-style-sheets","js":"javascript"}
    if a[-1] in d.keys():
        print(f"The extension of the file is : {d[a[-1]]}")
        
    else:
        print("It is not file type")
Filename=input("Input the Filename:")
Filename_Extension(Filename)