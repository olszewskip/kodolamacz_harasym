import datetime as dt

pre_data_1 = 'April 12, 1961 2:07 local time'
pre_data_2 = '07/21/69 2:56:15 AM UTC'
data_1 = dt.datetime.strptime(pre_data_1, '%B %d, %Y %H:%M local time')
data_2 = dt.datetime.strptime(pre_data_2, '%m/%d/%y %I:%M:%S AM %Z')

YEAR = 365
MONTH = 30
difference = data_2 - data_1
years = difference.days / YEAR
months = difference.days / MONTH

future_moment = dt.datetime.now() + difference
future_date = future_moment.date()

my_birth = dt.date(1989, 8, 14)
moje_lata = (future_date - my_birth).days / YEAR

print(data_1.isoformat())
print(data_2.isoformat())
print(difference, years, months)
print(future_moment)
print(future_date)
print(moje_lata)