def main():
    print("Greetings! Welcome to xyz, here is the new check in")
    name = input("Insert guest Name,Surname: ").strip()
    first, last = check_name(name)
    check_in(first, last)



def check_name(name):
    while True:
        if "," not in name:
          print("Name format is incorrect, please use Name,Surname format")
          name = input("Insert guest Name,Surname: ").strip()
        else:
          first, last = name.split(",")
          return first, last

def check_in(first, last):
    print(f"Insert the date of the arrival of the guest {last} {first}")



def save_file():
    ...


if __name__ == "__main__":
    main()