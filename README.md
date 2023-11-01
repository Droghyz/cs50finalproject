# PyHotel

## Video Demo: <https://www.youtube.com/watch?v=ysABsyQQDGs>

### Description:

PyHotel is a program that simulate few of the steps that Receptionist need to do when a customer arrives to the Hotel, asking the user for inputs and generating a CSV file with the collection of these inputs.

### What library do i use?:

I used `datatime` for managing the dates input and `csv` to create the CSV file

For the testing, i used the classic `pytest`

### How does it work?:

At the beginning, the usert is greeted with a greeting string before asking for the name and surname of the guest (comma separated e.g: `John,Doe`).

If the name does not respect this format, the program will ask again for the input.

After the name and surname is provided, the program will ask for the check in day (arrival day at the hotel) in `YYYY-MM-DD` format (e.g: `2023-10-30`), as well as the check out day (day of departure).

If one or both of the dates input is in a wrong format (not separated from a `"-"`), the program will ask again for the input otherwise, if the dates are totally wrong (e.g: `2023-40-50`) the program will raise a `ValueError` and close the program.

One more check is made, the program will check if the check out date is after the check in date, if is not, the program will raise a `ValueError` and exit the program.

Once the last check is done, the program will return a string to the user with the Surname and Name of the guest following the ammount of days that will stay in the hotel.

> The diplayed days indicate the nights in which the customer sleeps in the hotel. E.g: The guest arrives the 2023-01-01 and leaves the 2023-01-10 the displayed days would be 9, because 9 are the nights in which the customer sleeps in the hotel, the last day is intended as the check out date, therefore it is not considered.It's pretty common to say "9 nights and 10 days"

At this time the CSV file is generated and the following information are saved (Last Name, Name, Check In, Check Out, Days at Hotel)

In the end, the program will ask the user if he want to insert another guest (in case of multiple check in at the same time) or just exit the program.
