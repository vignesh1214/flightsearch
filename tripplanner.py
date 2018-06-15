from amadeus import Client, ResponseError
import pandas as pd
import json

amadeus = Client(
    client_id='xN5gQPJr5SvBwyamPW7s3UcEacp8Yy9j',
    client_secret='CFkVCJmrGBfEheLs'
)




def flightsearch(startDate,endDate,duration,origin,destination):
	dateprice ={}
	startDate= "2018-07-"+str(inputdate)
	endDate = "2018-07-"+str(enddate)
	for i in range(int(inputdate),int(enddate)):
		x='2018-07-'+str(i)
		y='2018-07-'+str(i+int(duration))
		response = amadeus.shopping.flight_offers.get(origin=origin, destination=destination, departureDate=x,returnDate=y,max=1)
		#data = response.data[0].get('offerItems')[0].get('price')
		#print(data[0].get('offerItems')[0].get('price'))
		price = response.data[0].get('offerItems')[0].get('price')
		total = float(price.get('total')) + float(price.get('totalTaxes'))
		#print(total)
		dateprice['2018:07:'+str(i)+'--'+'2018:07:'+str(i+int(duration))]=total
	return dateprice
	

trips = input("How many trips do you want to make? ")
origin = input("Origin ")
inputdate = input("Date of Travel starting range -- July? ")
enddate = input("Return before -- July? ")
duration = input("Duration of stay at each place- ")
destination= raw_input("Destination ").split(",")

for i in range(0,trips-1):
	df_1= pd.Series(flightsearch(inputdate,enddate,duration,origin,destination))



#print(df)
#df = pd.Series(dateprice)
print(df.sort_values().head(3))


# inputdate = input("Date of Travel starting range -- July? ")
# enddate = input("Return before -- July? ")
# duration = input("Duration of stay - ")
# startDate= "2018-07-"+str(inputdate)
# endDate = "2018-07-"+str(enddate)
# for i in range(int(inputdate),int(enddate)):
# 	x='2018-07-'+str(i)
# 	y='2018-07-'+str(i+int(duration))
# 	response = amadeus.shopping.flight_offers.get(origin='SFO', destination='LAX', departureDate=x,returnDate=y,max=1)
# 		#data = response.data[0].get('offerItems')[0].get('price')
# 		#print(data[0].get('offerItems')[0].get('price'))
# 	price = response.data[0].get('offerItems')[0].get('price')
# 	total = float(price.get('total')) + float(price.get('totalTaxes'))
# 	#print(total)
# 	dateprice['2018:07:'+str(i)+'--'+'2018:07:'+str(i+int(duration))]=total


# df = pd.Series(dateprice)
# print(df.sort_values().head(3))
#print(min(dateprice, key=dateprice.get))
# json.loads(response.data)

# print(response.data)
# data = response.data
# print(data[0].get('offerItems')[0].get('price'))
# price = data[0].get('offerItems')[0].get('price')
# total = float(price.get('total')) + float(price.get('totalTaxes'))
# print(total)
# print("total: " + price.get('total'))
# print("totalTaxes: " + price.get('totalTaxes'))


# data[]
# [
# 	{
# 		'type': 'flight-offer', 
# 		'id': '1528609857956-974646902', 
# 		'offerItems': [
# 			{
# 				'services': [
# 					{
# 						'segments': [
# 							{
# 								'flightSegment': 
# 									{
# 										'departure': {
# 											'iataCode': 'SFO', 
# 											'terminal': '2', 
# 											'at': '2018-07-20T06:00:00-07:00'
# 										}, 
# 										'arrival': {
# 											'iataCode': 'LAX', 
# 											'terminal': '0', 
# 											'at': '2018-07-20T07:28:00-07:00'
# 										}, 
# 										'carrierCode': 'AA', 
# 										'number': '6079', 
# 										'aircraft': {'code': 'E75'}, 
# 										'operating': {'carrierCode': 'AA', 'number': '6079'}, 
# 										'duration': '0DT1H28M'
# 									}, 
# 									'pricingDetailPerAdult': 
# 										{
# 											'travelClass': 'ECONOMY', 
# 											'fareClass': 'B', 
# 											'availability': 7, 
# 											'fareBasis': 'Q0ALZOB3'
# 										}
# 							}]
# 					}
# 				], 
# 				'price': {'total': '46.56', 'totalTaxes': '14.56'}, 
# 				'pricePerAdult': {'total': '46.56', 'totalTaxes': '14.56'}
# 			}
# 		]
# 	}
# ]