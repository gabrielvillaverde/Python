# How many days there are for any given month and any given year?

# This function is_leap() return True if it is a leap year and return False if it is not a leap year.
# Leap year algorithm - # Flowchart to visualize the logic: https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Leap%20Algorithm#R7VpNc9owEP01HNuxJdmYY4CkzTTNdEpmmhyFrdhqhcXIIkB%2BfSUsY4wcQhqwC%2B0p0urDu29Xu08KHTiYLD4JPE2%2B8oiwDnCiRQcOOwC4CPjqj5Ysc0k3gLkgFjQyk0rBiD4TI3SMdEYjklUmSs6ZpNOqMORpSkJZkWEh%2BLw67ZGz6lenOCaWYBRiZkt/0EgmuTQA3VL%2BmdA4Kb7s%2Br18ZIKLycaSLMERn2%2BI4GUHDgTnMm9NFgPCNHgFLvm6qxdG14oJksp9FoDbYTJlQFxPomj0Jbzr4tT9YJTN5LIwmETKftPlQiY85ilml6W0L/gsjYje1VG9cs4N51MldJXwJ5FyaZyJZ5IrUSInzIwqhcXyXq//6BXdB7PdqjNcVHpL08t11Qq%2BCIERZXwmQrLD7iKUsIiJ3DEPrB2lIpzwCVH6qHWCMCzpU1UPbEItXs8rvaEaxiFvcI7Z9wmzmfnS6O7i%2B53lstIhGt15QiUZTfHK/rk6lVXwzZ5ESLLYDaNttlkAYE85brVoWZxWE%2BTz8oy4xRFONs4Hco6ElfePBjLYM5DhOwN5tfRCCLzcmDDlNJXZxs7ftKAMFLcLtgKlyOulq/M9S8evlfvzWPD/x8LOWHCdQwSD5W3kdre97W8d91w1s64Mg7fGFQLWl5qIK2Dl4%2BtMr9GahYzglGkjOsBnCv3%2BWKhWrFsRfaIZHas4A85YT0EdeGVn8YRPxrOsmQxe8Jcif3dr8jf07PwdHCt/QwvbW65xvSHK/HcVvEfK2IAzLlZr4WMQkjBU8kwK/otsjIwDD3nOYQB23SrA65PQWoHs1gBsAasMllX0MKNxqtqhMpwooPoaFqr48YUZmNAoyjMoyegzHq%2B20iiaQ6z29fodb6j3Ukkzy/PngeLYDSwm0rOBhjU4g2PhHFg4P5Ds5IGG/j5AoyaBdmErZX5B5X1RyFX7oaz4qlfWeN0pSvxfQA2KVPM6N2j3xhO06VP3XH2KWvWpcyjapG%2BZLRMn6IPX63pdvTkacXJtVnpwzhR5JIhQHWcKwBj6/oFIqVfFFtaR0kY5E2jnVeFESwzaMx2BVtMRaOd14ERLzL4%2BdXutlhh0qBKD2i8xyNum2rWJsI5rH6/I9M6lyHi9bXRRzUWm4TJjM6RzuDOi3hZXClq%2BMRYmnNcbCHS3I7oO6EbfQIDNSc8AaGQBDdt%2BbAL2s%2Bk5ZA47Sdch3WzusCnGST9QQ9RkHVTd8ocO%2Bb9jyp%2BLwMvf
  
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year")  
        return True
      else:
        print("Not leap year")
        return False
    else:
      print("Leap year") 
      return True
  else:
    print("Not leap year")  
    return False
  
def month_name_to_number(month_name):
    month_name = month_name.lower()
    month_dict = {
        'january': 1,
        'february': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'august': 8,
        'september': 9,
        'october': 10,
        'november': 11,
        'december': 12
    }
    # month_dict.get(key, default_value) is how it works .get
    return month_dict.get(month_name, None) # Looks up the value associated with the key month_name in the month_dict dictionary. If the key is present, it returns the corresponding value (i.e., the month number). If the key is not present, it returns None (the second provided argument).
    
def days_in_month(year, month):
    if is_leap(year) == False: # Not a leap year
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else: # Leap year
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return year, month, month_days[month - 1]
  
while True:
    year_input = input("Please, enter a year: ")
    if year_input.isdigit():
        year = int(year_input)
        if 1900 <= year <= 3000:
            break
        else:
            print("Invalid input. Please enter a year between 1900 and 3000.")
    else:
        print("Invalid input. Please enter a valid numeric year.")

while True:
    month_name = input("Please, enter the month name: ").lower()
    month = month_name_to_number(month_name)
    if month is not None:
        year, month, days = days_in_month(year, month)
        print(f"Year: {year} - Month: {month_name.capitalize()} - Days: {days}")
        break
    else:
        print("Invalid month name.")

