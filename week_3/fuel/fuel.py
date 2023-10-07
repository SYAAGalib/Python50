def main():
    fuel_percentage = cal_percent(get_input())
    print(fuel_percentage)


def get_input():
    while True:
        x = input("F: ")
        try:
            a, b = x.split("/")
            d = int(a) / int(b)
            if d <= 1:
                return d
        except:
            pass

def cal_percent(x):
    p = round(x * 100)
    return ("E" if p <= 1 else "F" if 99 <= p <= 100 else f"{p}%")

if __name__ == "__main__":
    main()