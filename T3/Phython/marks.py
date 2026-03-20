Name=None
R_N=None
Branch=None
Batch=None
def details():
    global Name,R_N,Branch,Batch
    Name=input("Enter your Name")
    R_N=input("Enter your roll Number")
    Branch=input("Enter your branch name")
    Batch=input("Enter your Batch")
def marks():
    DE=[]
    Python=[]
    FSD=[]
    for i in range(4):
        de=int(input(f"Enter marks of DE of T{i+1}"))
        DE.append(de)
        py=int(input(f"Enter marks of Python of T{i+1}"))
        Python.append(py)
        fsd=int(input(f"Enter marks of FSD of T{i+1}"))
        FSD.append(fsd)
    return([DE,Python,FSD])
def SPI(Marks_in):
    global Name,R_N,Branch,Batch
    print(f"\n\n\nYour name is {Name}")
    print(f"\nYour Roll Number is {R_N}")
    print(f"\nYour Branch is {Branch}")
    print(f"\nYour Batch is {Batch}")
    print(f"\n\npercentage of each subject is   {(sum(Marks_in[0]))}")
    print(f"\npercentage of each subject is   {sum(Marks_in[1])}")
    print(f"\npercentage of each subject is   {sum(Marks_in[2])}")
    print(f"\nToatl percenatge    {((sum(Marks_in[0])+sum(Marks_in[1])+sum(Marks_in[2]))/300)*100}\n\n")
