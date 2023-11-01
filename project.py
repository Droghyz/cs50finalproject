from datetime import date
import csv

def main():
    start = True
    print("Greetings! Welcome to xyz, here is the new check in")
    while start:
      name = input("Insert guest Name,Surname: ").strip()
      first, last = check_name(name)
      message, days, c_in, c_out= check_in(first, last)
      print(message)
      save_file(first,last,c_in, c_out, days)
      start = is_ended()
      if start == False:
         print("No more guests to register, closing the program..")


def check_name(name):
   while True:
    if "," not in name:
        print("Name format is incorrect, please use Name,Surname format")
        name = input("Insert guest Name,Surname: ").strip()
    else:
        first, last = name.split(",")
        return first, last


def check_in(first, last):
    print(f"Insert the date of the arrival of the guest {last} {first} using YYYY-MM-DD format")
    check_in_date = input("Check-in date: ")
    check_out_date = input("Check-out date: ")
    while True:
      if "-" not in check_in_date: 
          print("Check in format not correct, please use YYYY-MM-DD format")
          check_in_date = input("Check-in date: ")
      elif "-" not in check_out_date:
          print("Check out format not correct, please use YYYY-MM-DD format")
          check_out_date = input("Check-out date: ")
      else:
        check_in_format = check_in_date.split("-")
        check_out_format = check_out_date.split("-")
        is_date_valid(check_in_format, check_out_format)
        new_check_in = date(int(check_in_format[0]), int(check_in_format[1]), int(check_in_format[2]))
        new_check_out = date(int(check_out_format[0]), int(check_out_format[1]), int(check_out_format[2]))
        total_stay = new_check_out-new_check_in
        days_stayed = total_stay.days
        negative_days(days_stayed)
        return (f"{last} {first} will stay here for {days_stayed} days"), days_stayed, new_check_in, new_check_out
    

def is_date_valid(c_in_format, c_out_format):
   if (int(c_in_format[1]) > 12) or (int(c_in_format[2]) > 31):
           raise ValueError("Check in dates are not valid")
   if (int(c_out_format[1]) > 12) or (int(c_out_format[2]) > 31):
           raise ValueError("Check out dates are not valid")
   
def negative_days(days):
   if days < 0:
      raise ValueError("Check-out must be after the date of arrival")
   

def is_ended():
  response = input("Would you like to register a new guest? (Y/N): ").lower()
  if response == "y":
    return True
  if response == "n":
     return False
  
def check_header():
  with open('guests.csv','r') as r:
    reader = csv.DictReader(r)
    fieldnames = ['Last Name', 'First Name', 'Check in', 'Check out']
    for row in reader:
      if fieldnames[0] in row:
        return False
      else:
        return True
      

def save_file(first,last,c_in, c_out, days):
   with open('guests.csv', 'a', newline='') as csvfile:
    fieldnames = ['Last Name', 'First Name', 'Check in', 'Check out', 'Duration of the Stay']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    is_header = check_header()
    if is_header == True or is_header == None:
      writer.writeheader()
      writer.writerow({'Last Name':last, 'First Name': first, 'Check in': c_in, 'Check out': c_out, 'Duration of the Stay': days})
    else:
       writer.writerow({'Last Name':last, 'First Name': first, 'Check in': c_in, 'Check out': c_out, 'Duration of the Stay': days})


if __name__ == "__main__":
    main()