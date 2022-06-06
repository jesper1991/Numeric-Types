
stock_prices = [('APPL',200),('GOOGL',400),('MSFT',100)]

# Tuple unpacking

for item in stock_prices:
    print(item)

for ticker, price in stock_prices:
    print(price+(0.1*price)) # För att se t.ex. 10% increase


work_hours = [('Abby', 100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
    # placeholders
    current_max = 0
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass


    return (employee_of_month,current_max)

employee_check(work_hours)
name,hours = employee_check(work_hours)
print(name,hours)
