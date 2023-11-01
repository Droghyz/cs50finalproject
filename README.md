# PyHotel

    #### Video Demo:  <URL HERE>
    #### Description:
    PyHotel is a program that simulate few of the steps that Receptionist need to do when a customer arrives to the Hotel, asking the user for inputs and generating a CSV file with the collection of these inputs.
    At the beginning, the usert is greeted with a greeting string before asking for the name and surname of the guest (comma separated i.e: John,Doe).
    If the name does not respect this format, the program will ask again for the input.
    After the name and surname is provided, the program will ask for the check in day (arrival day at the hotel) in YYYY-MM-DD format (i.e: 2023-10-30), as well as the check out day (day of departure).
    If one or both of the dates input is in a wrong format (not separated from a "-"), the program will ask again for the input otherwise, if the dates are totally wrong (i.e: 2023-40-50) the program will raise a ValueError and close the program.
    One more check is made, the program will check if the check out date is after the check in date, if is not, the program will raise a ValueError and exit the program.
    Once the last check is done, the program will return a string to the user with the Surname and Name of the guest following the ammount of days that will stay in the hotel (The days are displayed as "night slept to the hotel", the day of departure in fact is not calculated).
    At this time the CSV file is generated and the following information are saved (Last Name, Name, Check In, Check Out, Days at Hotel)
    At the end, the program will ask the user if he want to insert another guest (in case of multiple check in at the same time) or just exit the program.
