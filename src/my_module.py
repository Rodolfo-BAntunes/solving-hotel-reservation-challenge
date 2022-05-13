
import re
import numpy as np

def get_cheapest_hotel(data):   #DO NOT change the function's name
    cheapest_hotel = "cheapest_hotel_name"
    

####### tables ########
    days =  ['SUN','SAT']     #weekend days

    ## Dictionary with prices of each combination to Hotel, Category and Day
    prices_by_hotel = {
        'lakewood':{
        'weekend' :{
                   'regular':90,
                   'rewards':80
                   },
         'weekday' :{
                   'regular':110,
                   'rewards':80
                   }
         },
         'bridgewood':{
         'weekend' :{
                   'regular':60,
                   'rewards':50
                   },
         'weekday' :{
                   'regular':160,
                   'rewards':110
                   }
         },
         'ridgewood':{
         'weekend' :{
                   'regular':220,
                   'rewards':110
                   },
         'weekday' :{
                   'regular':150,
                   'rewards':40
                   }
         }
    }

    hotels = ['Lakewood','Bridgewood','Ridgewood']
    #########################

    def pickWeekday(date):
      #function to extract weekday of a given date on expected format

      RE = "\(.*?\)"  #regex to search anything inside parentesis
      result = re.findall(RE,date) 

      return(result[0][1:-1].upper()) #return weekday uppercased


    # Main function flow:
    # Ask the user for data;
    # Process to split the category and dates into two different variables;
    # Process date and category variables to check the cost for each date -> bill list variable;
    # Summatory of bills 
    
    ##print("Digite a categoria do hospede e as datas que ele irá se hospedar")
    ##entryData = input("Formato: Categoria: ddmmmaaaa(ddd), ddmmmaaaa(ddd), ddmmmaaaa(ddd),...") #expected format: DayMonthYear(Weekday)
    entryData = data
    ###### Regular Expressions ######

    RE_dates = '\d{2}\D{3}\d{4}\(\D*\)'
    RE_category = '\D*:'

    #################################

    category = re.findall(RE_category,entryData)[0][0:-1].lower()
    dates = re.findall(RE_dates,entryData)

    #rint(category,"\n",dates)

    bills = {
    'lakewood' : [],
    'bridgewood' : [],
    'ridgewood' : [],
    }
    for date in dates:
        weekday = pickWeekday(date)
        if weekday in days:           # Test for weekend
            bills['bridgewood'].append(prices_by_hotel.get('bridgewood').get('weekend').get(category))
            bills['lakewood'].append(prices_by_hotel.get('lakewood').get('weekend').get(category))
            bills['ridgewood'].append(prices_by_hotel.get('ridgewood').get('weekend').get(category))
        else:
            bills['bridgewood'].append(prices_by_hotel.get('bridgewood').get('weekday').get(category))
            bills['lakewood'].append(prices_by_hotel.get('lakewood').get('weekday').get(category))
            bills['ridgewood'].append(prices_by_hotel.get('ridgewood').get('weekday').get(category))
    total = {
    'lakewood' : np.sum(bills.get('lakewood')),
    'bridgewood' : np.sum(bills.get('bridgewood')),
    'ridgewood' : np.sum(bills.get('ridgewood')),
    }
    print(total)
    
    total = {
   'lakewood' : np.sum(bills.get('lakewood')),
   'bridgewood' : np.sum(bills.get('bridgewood')),
   'ridgewood' : np.sum(bills.get('ridgewood')),
   }
    cheaper_bill = np.min(list(total.values()))
    hotel_index = list(total.values()).index(cheaper_bill)
    cheapest_hotel = hotels[hotel_index]

        
    
    return cheapest_hotel


