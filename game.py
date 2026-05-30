import time

# =========================
# CYBERSTRIKE HACKING GAME
# =========================

# ---------- REGISTER FUNCTION ----------

def register():

    username = input("Create Username: ")
    password = input("Create Password: ")

    try:
        file = open("users.txt", "a")
        file.write(username + "," + password + "\n")
        file.close()

        print("\nAccount Created Successfully!\n")

    except:
        print("Error while creating account!")


# ---------- LOGIN FUNCTION ----------

def login():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        file = open("users.txt", "r")
        data = file.readlines()
        file.close()

        for line in data:

            user_data = line.strip().split(",")

            if len(user_data) == 2:

                saved_user = user_data[0]
                saved_pass = user_data[1]

                if username == saved_user and password == saved_pass:
                    print("\nLOGIN SUCCESSFUL!\n")
                    return username

        print("\nInvalid Username or Password!\n")
        return None

    except FileNotFoundError:
        print("\nNo users registered yet!\n")
        return None


# ---------- HACKING GAME FUNCTION ----------

def hacking_game(password, points, mission_name):

    lives = 5
    hint_index = 1

    print("\nAccessing", mission_name, "...")
    time.sleep(1)

    print("Bypassing Firewall...")
    time.sleep(1)

    print("Decrypting Password...")
    time.sleep(1)

    while lives > 0:

        # Prevent hint index from exceeding password length
        if hint_index > len(password):
            hint_index = len(password)

        # Create password hint
        hint = password[:hint_index] + "*" * (len(password) - hint_index)

        print("\n==============================")
        print("MISSION:", mission_name)
        print("Password Hint:", hint)
        print("Password Length:", len(password))
        print("Lives Left:", lives)
        print("==============================")

        guess = input("Enter Password: ")

        # CORRECT PASSWORD
        if guess == password:

            print("\nACCESS GRANTED!")
            print(points, "POINTS ADDED!\n")

            return points

        # WRONG PASSWORD
        else:

            lives -= 1
            hint_index += 1

            print("\nWRONG PASSWORD!")

    print("\nACCESS DENIED!")
    print("Mission Failed!\n")

    return 0


# ---------- MISSIONS ----------

def hack_pc():
    password = "alpha"
    return hacking_game(password, 100, "PC SYSTEM")


def hack_bank():
    password = "bank123"
    return hacking_game(password, 150, "BANK SERVER")


def hack_organization():
    password = "net@456"
    return hacking_game(password, 200, "PRIVATE ORGANIZATION")


# ---------- MAIN MENU ----------

def game_menu():

    print("========== CYBERSTRIKE ==========")
    print("1. Hack PC")
    print("2. Hack Bank")
    print("3. Hack Organization")
    print("4. Check Score")
    print("5. Exit")
    print("=================================")


# ---------- START SCREEN ----------

print("""
██████╗██╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
╚██████╗   ██║   ██████╔╝███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
""")

print("====== WELCOME TO CYBERSTRIKE ======\n")


# ---------- LOGIN SYSTEM ----------

current_user = None

while current_user is None:

    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    # REGISTER
    if choice == "1":
        register()

    # LOGIN
    elif choice == "2":
        current_user = login()

    # EXIT
    elif choice == "3":
        print("\nExiting Game...")
        exit()

    else:
        print("\nInvalid Choice!\n")


# ---------- GAME LOOP ----------

score = 0

while True:

    game_menu()

    try:
        choice = int(input("Enter Choice: "))

        # HACK PC
        if choice == 1:
            score += hack_pc()

        # HACK BANK
        elif choice == 2:
            score += hack_bank()

        # HACK ORGANIZATION
        elif choice == 3:
            score += hack_organization()

        # CHECK SCORE
        elif choice == 4:
            print("\nCurrent User:", current_user)
            print("Your Score:", score, "\n")

        # EXIT
        elif choice == 5:

            print("\nSaving Data...")
            time.sleep(1)

            print("Exiting CYBERSTRIKE...")
            time.sleep(1)

            print("GOODBYE!\n")

            break

        # INVALID OPTION
        else:
            print("\nInvalid Choice!\n")

    except:
        print("\nPlease Enter Numbers Only!\n")
        