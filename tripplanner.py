from amadeus import Client, ResponseError
import pandas as pd
import json
import datetime
from datetime import date, timedelta

amadeus = Client(
    client_id='xN5gQPJr5SvBwyamPW7s3UcEacp8Yy9j',
    client_secret='CFkVCJmrGBfEheLs'
)

def date_entry(dates):
	year, month, day = map(int, dates.split('-'))
	final_date = date(year, month, day)
	yield final_date

def date_range(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)


def flightsearch(startDate,endDate,duration,origin,destination):
	dateprice ={}
	for startDate in date_range(startDate, endDate):
	# for i in range(int(inputdate),int(enddate)):
	# 	x='2018-07-'+str(i)
	# 	y='2018-07-'+str(i+int(duration))
		startingDate = startDate.isoformat()
		returningDate =  (startDate + timedelta(int(duration))).isoformat()
		response = amadeus.shopping.flight_offers.get(origin=origin, destination=destination, departureDate=startingDate,returnDate=returningDate,max=1)
		#data = response.data[0].get('offerItems')[0].get('price')
		#print(data[0].get('offerItems')[0].get('price'))
		price = response.data[0].get('offerItems')[0].get('price')
		total = float(price.get('total')) + float(price.get('totalTaxes'))
		#print(total)
		dateprice[startingDate + '-' + returningDate]=total
	return dateprice
	

trips = int(input("How many trips do you want to make? "))
origin = input("Origin ")
destination= list(input("Destinations ").split(","))
#destination = input("Destination ")
origindate = input('Enter origin date in YYYY-MM-DD format ')
enddate = input("Return before in (YYYY-MM-DD format) ")
duration = input("Duration of stay at each place- ")
#destination = input()

flight_list={}
for i in range(0,trips):
	df= pd.Series(flightsearch(date_entry(origindate),date_entry(enddate),duration,origin,destination[i]))
	flight_list[origin +'--' + destination[i]]=df.sort_values().head()
	#print(df.sort_values().head(3))


#print(df)
#df = pd.Series(dateprice)
#print(df.sort_values().head(3))
print(flight_list)


