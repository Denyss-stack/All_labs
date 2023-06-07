file_path = input("Enter file path: ")
def Total_lines():
    with open(file_path, "r") as myfile:
        count = len(myfile.readlines())
        print(f"Total line: {count}")
    
def CountEmptyLines():
    with open(file_path , "r") as myfile:
        empty_lines = 0
        for line in myfile:
            if line.isspace():
                empty_lines += 1
        print(f"Empty Lines: {empty_lines}")
   
def Lines_With_Z():
     with open(file_path , "r") as myfile:
         Lines_Z = 0
         for line in myfile:
             if "z" in line:
                 Lines_Z += 1
         print(f"Lines with Z: {Lines_Z}")
def Count_For_Z():
     with open(file_path , "r") as myfile:
         z_count = 0
         for line in myfile:
             z_count += line.count("z")
         print(f"z count: {z_count}" )
    
def Count_For_And():
     with open(file_path , "r") as myfile:
         Count_And = 0
         for line in myfile:
             if "and" in line:
                 Count_And += 1
         print(f"line with and: {Count_And}")
while True:
 Total_lines()
 CountEmptyLines()
 Lines_With_Z()
 Count_For_Z()
 Count_For_And()


 stop = input("Do you want to scan another file: (yes/no)")
 if stop() != "yes":
   break