def gettime():
    import datetime
    return datetime.datetime.now()


def log():
    print("Choose your client")
    client = int(input("1. Harry \n2. Rohan \n3. Hammad"))
    con = 1 #Works exactly as True or False Stmt
    if client == 1:
        while con == 1:
            print("What do you want to log for Harry?")
            choice = int(input("1. Diet \n2. Activity\n"))
            if choice == 1:
                f = open("harry diet.txt", "a")
                data = input("Enter what has Harry Eaten?\n")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()

            else:
                f = open("harry exercise.txt", "a")
                data = input("How much time has Harry worked out?\n")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()
            con = int(input("Do you want to log more for Harry? \n1. Yes \n2. No\n"))

    elif client == 2:
        while con == 1:
            print("What do you want to log for Rohan?")
            choice = int(input("1. Diet \n2. Activity\n"))
            if choice == 1:
                f = open("rohan diet.txt", "a")
                data = input("Enter what has Rohan Eaten?\n")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()

            else:
                f = open("rohan exercise.txt", "a")
                data = input("How much time has Rohan worked out?\n")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()
            con = int(input("Do you want to log more for Rohan? \n1. Yes \n2. No\n"))

    elif client == 3:
        while con == 1:
            print("What do you want to log for Hammad?")
            choice = int(input("1. Diet \n2. Activity\n"))
            if choice == 1:
                f = open("hammad diet.txt", "a")
                data = input("Enter what has Hammad Eaten?\n")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()

            else:
                f = open("hammad exercise.txt", "a")
                data = input("How much time has Hammad worked out?\n")
                f.write(str([str(gettime())]) + "  " + data + "\n")
                f.close()
            con = int(input("Do you want to log more for Hammad? \n1. Yes \n2. No\n"))


def retrieve():
    con = 1
    while con == 1:
        print("Choose your client")
        client = int(input("1. Harry \n2. Rohan \n3. Hammad\n"))
        if client == 1:
            print("What do you want to retrieve for Harry?")
            choice = int(input("1. Diet \n2. Activity\n"))
            if choice == 1:
                f = open("harry diet.txt", "r")
                print(f.readlines())
                f.close()

            else:
                f = open("harry exercise.txt", "r")
                print(f.readlines())
                f.close()

        elif client == 2:
            print("What do you want to retrieve for Rohan?\n")
            choice = int(input("1. Diet \n2. Activity"))
            if choice == 1:
                f = open("rohan diet.txt", "r")
                print(f.readlines())
                f.close()

            else:
                f = open("rohan exercise.txt", "r")
                print(f.readlines())
                f.close()

        elif client == 3:
            print("What do you want to retrieve for Hammad?")
            choice = int(input("1. Diet \n2. Activity\n"))
            if choice == 1:
                f = open("hammad diet.txt", "r")
                print(f.readlines())
                f.close()

            else:
                f = open("hammad exercise.txt", "r")
                print(f.readlines())
                f.close()
        con = int(input("Do you want to retrieve any more details? \n1. Yes \n2. No\n"))


print("Welcome to HealthCare Management System")

while True:
    ch = int(input("What do you want to do? \n1. Log \n2. Retrieve\n3. Exit\n"))
    if ch == 1:
        log()
    elif ch == 2:
        retrieve()
    elif ch == 3:
        print("Thank You for using our HealthCare Management System!")
        break
    else:
        print("Wrong Input. Please try again.\n")