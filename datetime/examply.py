import time
from datetime import datetime
# from pytz import timezone


def main() -> None:
    print(time.time()) #unix time seconds passed since start of standard unix time 1705058559.445794
    # simple dates
    some_date = datetime(2022, 10, 9, 18, 0, 0)
    print(some_date)  #2022-10-09 18:00:00

    # ISO 8601 parsing
    some_date = datetime.fromisoformat("2022-09-16T14:05:14")
    print(some_date)  #2022-09-16 14:05:14

    # get the present date
    today = datetime.now()
    print(today) #2024-01-12 11:22:39.445850

    # date comparison
    print(some_date < today)  #Bool


if __name__ == "__main__":
    main()