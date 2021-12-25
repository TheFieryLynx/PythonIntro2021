line = input()
systems = {}
while line:
    data = line.split()
    if len(data[0]) > 1:
        break
    systems[data[0]] = {}
    if len(data) > 2:
        systems[data[0]]["subsystems"] = [c for c in data[1]]
        systems[data[0]]["details"] = [c for c in data[2]]
    elif len(data) > 1:
        if data[1][:1].islower():
            systems[data[0]]["details"] = [c for c in data[1]]
        else:
            systems[data[0]]["subsystems"] = [c for c in data[1]]
    line = input()
code = ""
for key, system in systems.items():
    if "subsystems" in system:
        code += "class {0}(".format(key)
        for subsystem in system["subsystems"]:
            code += "{0},".format(subsystem)
        code = code[:-1]
        code += "):\n"
        if "details" in system:
            for detail in system["details"]:
                code += "\t{0} = \"{0}\"\n".format(detail)
        else:
            code += "\tpass\n"
    else:
        code += "class {0}:\n".format(key)
        if "details" in system:
            for detail in system["details"]:
                code += "\t{0} = \"{0}\"\n".format(detail)
        else:
            code += "\tpass\n"
code += "class pepela("
data = line.split()
for subsystem in data[0]:
    code += "{0},".format(subsystem)
code = code[:-1]
code += "):\n"
if len(data) > 2:
    for detail in data[1]:
        code += "\t{0} = \"{0}\"\n".format(detail)
# code += "\tprint(closure())\n"
code += "\tdef __init__(self):\n"
# code += "\t\tprint(dir(self))\n"
code += "\t\tvars = []\n"
code += "\t\tfor name in dir(self):\n"
code += "\t\t\tif \"__\" not in name:\n"
# code += "\t\t\t\tprint(name)\n"
code += "\t\t\t\tvars.append(name)\n"
code += "\t\tfor name in details:\n"
code += "\t\t\tif name not in vars:\n"
code += "\t\t\t\tprint(1 / 0)\n"
code += "pepela()"
print(code)
try:
    details = {}
    details["details"] = data[2] if len(data) > 2 else data[1]
    print(details)
    exec(code, details)
    print("Correct")
except Exception as ex:
    # print(ex)
    print("Incorrect")
    
#details = 'abcdef'
#class A:
#    a = "a"
#    b = "b"
#    c = "c"
#class B:
#    c = "c"
#    d = "d"
#    e = "e"
#class C(A):
#    f = "f"
#class D(A,B):
#    e = "e"
#class pepela(D,C):
#    e = "e"
#    def __init__(self):
#        vars = []
#        print(dir(self))
#        for name in dir(self):
#            if "__" not in name:
#                vars.append(name)
#                print(vars)
#        for name in details:
#            if name not in vars:
#                raise Exception
#    
#a = pepela()
    
#details = 'aby'
#class A:
#    a = "a"
#class B(A):
#    b = "b"
#class pepela(A,B):
#    y = "y"
#    def __init__(self):
#        vars = []
#        for name in dir(self):
#            if "__" not in name:
#                vars.append(name)
#        for name in details:
#            if name not in vars:
#                raise Exception
#class A:
#    a = 'a'
#class B:
#    b = 'b'
#class C(A,B):
#    c = 'c'
#class D(B,A):
#    d = 'd'
#class pepelaC3(C,A,B):
#    e = 'e'
#    def __init__(self):
#        print(dir(self))
#        for i in 'acbde':
#            if i not in dir(self):
#                raise Exception
#pepelaC3()