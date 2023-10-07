# MM/DD/YYYY
# 9/8/1636 or August 9, 1636

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

year, day, month = 0, 0, 0
while True:
    try:
        date = input("Date: ").lower()

        # while date in "9/8/1636" this format
        if "/" in date:
            month, day, year = date.split("/")

        # while date in "August 9, 1636" this format
        elif "," in date:
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            if month in months:
                month = months.index(month) + 1
        print(f"\"{int(year)}-{int(month):02}-{int(day):02}\"")

    except ValueError:
        pass
