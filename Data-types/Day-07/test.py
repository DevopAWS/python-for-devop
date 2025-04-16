import sys

type = sys.argv[1]

if type == "t2.micro":
    print(" yoou will charge 2 dollers per day")

elif type == "t3.medium":
    print("you will charge 4 dollers per day")

elif type == "t3.large":
    print ("you will charge 8 dollers per day")

else:
    print(" pleas provide a valid instance type")

    