n = int(input())
for i in range(n):
    size = list(map(str,input().split(" ")))
    if size[0][-1]=="L":
        if size[1][-1]== "M" or size[1][-1]=="S":
            print(">")
        elif size[1][-1] == "L":
            if size[0].count("X") > size[1].count("X"):
                print(">")
            elif size[0].count("X") < size[1].count("X"):
                print("<")
            elif size[0].count("X") == size[1].count("X"):
                print("=")
    elif size[0][-1]=="S":
        if size[1][-1]=="M" or size[1][-1]=="L":
            print("<")
        elif size[1][-1] == "S":
            if size[0].count("X") < size[1].count("X"):
                print(">")
            elif size[0].count("X") > size[1].count("X"):
                print("<")
            elif size[0].count("X") == size[1].count("X"):
                print("=")
    elif size[0][-1] == "M":
        if size[1][-1] == "L":
            print("<")
        elif size[1][-1] == "S":
            print(">")
        else:
            print("=")
