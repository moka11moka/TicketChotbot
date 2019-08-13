import requests
import json
import time
import re

attractions ={
'1 Altitude Gallery':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P11/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C5%3A1&locationId=294265',
'Adventure Cove Waterpark':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P4/tour_grades?tourDate=2019-8-11&attrdate=2019_8_11&ageBands=1%3A1%2C2%3A1&locationId=294265',
'Asain Civilisations Museum':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P69/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C5%3A1&locationId=294265',
'Cable Car Sky Pass':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P16/tour_grades?tourDate=2019-8-11&attrdate=2019_8_11&ageBands=1%3A1%2C2%3A1%2C3%3A0&locationId=294265',
'Gardens by the Bay':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P2/tour_grades?tourDate=2019-8-11&attrdate=2019_8_11&ageBands=1%3A2%2C2%3A0%2C3%3A0&locationId=294265',
'Grande Whisky Collection':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P86/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1&locationId=294265',
'HeadRock VR Sentosa Big 3':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/5594P40/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1&locationId=294265',
'Indian Heritage Centre':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P74/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C5%3A1&locationId=294265',
'Jurong Bird Park':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/62727P4/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1%2C3%3A0&locationId=294265',
'KidZania Singpore':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P5/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1&locationId=294265',
'Malay Heritage Centre':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P72/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C5%3A1&locationId=294265',
'Marina Bay Sands SkyPark':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P10/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1%2C3%3A0&locationId=294265',
'Mint Museum of Toys':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/59385P1/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1&locationId=294265',
'MOSH!':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/56640P1/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C5%3A1%2C2%3A1%2C3%3A0&locationId=294265',
'National Museum of Singapore':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P68/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C5%3A1&locationId=294265',
'National Orchid Garden':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P12/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1&locationId=294265',
'Night Safari':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/62727P2/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1%2C3%3A0&locationId=294265',
'Red Dot Design Museum':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/65615P1/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1&locationId=294265',
'River Safari':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/62727P3/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1%2C3%3A0&locationId=294265',
'S.E.A Aquarium':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P3/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1%2C3%3A0&locationId=294265',
'Sentosa 4D AdventureLand':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/21669P1/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1&locationId=294265',
'Singapore Zoo Rainforest Lumina':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/62727P5/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1%2C3%3A0&locationId=294265',
'Sun Yat Sen Nanyang Memorial Hall':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/57373P71/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C5%3A1%2C2%3A0&locationId=294265',
'Trick Eye Museum':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/7147P2/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C5%3A1%2C2%3A0&locationId=294265',
'Universal Studio':'https://www.tripadvisor.com.sg/AttractionBookingApi/product/3695UNIVERSAL/tour_grades?tourDate=2019-8-12&attrdate=2019_8_12&ageBands=1%3A1%2C2%3A1&locationId=294265'}

regex1 = re.compile(r"[A-Za-z]{3} [0-9]{1,2}, *[0-9]{4}")
regex2 = re.compile(r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}")
regex3 = re.compile(r"[0-9]{1,2}-[A-Za-z]{3}-[0-9]{4}")
regex4 = re.compile(r"[A-Za-z]{3,} [0-9]{1,2}, *[0-9]{4}")
regex5 = re.compile(r"[0-9]{4}\.[0-9]{1,2}\.[0-9]{1,2}")
regex6 = re.compile(r"[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}")
regex7 = re.compile(r"[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}")
regex8 = re.compile(r"[0-9]{8}")

monthMap = {"sep": "9", "oct": "10", "nov": "11", "dec": "12", "jan": "1", "feb": "2",
                "aug": "8", "jul": "7", "jun": "6", "may": "5", "apr": "4", "mar": "3"}
monthMap2 = {"september": "9", "october": "10", "november": "11", "december": "12",
                 "january": "1", "february": "2", "august": "8", "july": "7",
                 "june": "6", "may": "5", "april": "4", "march": "3"}
def getIndices(symbol,dateString):
    return [i for i,s in enumerate(dateString) if s==symbol]
# change the date to the normal format
def changeToDate(dateString):
    # Mar 06, 2007
    if regex1.match(dateString) is not None:
        month = monthMap[dateString[:dateString.index(' ')].lower()]
        day = dateString[dateString.index(' ')+1:dateString.index(',')]
        if day == '10' or day == '20' or day == '30':
            day = day
        else:
            day = day.replace('0', '')
        year = dateString[-4:]
        tourDate = year + '-' + month + '-' + day
        attrDate = year + '_' + month + '_' + day
        return tourDate,attrDate
    # 03/06/2007
    elif regex2.match(dateString) is not None:
        firstIndex = getIndices('/',dateString)[0]
        secondIndex = getIndices('/',dateString)[1]
        month = dateString[0:firstIndex]
        if month != '10':
            month = month.replace('0', '')
        day = dateString[firstIndex+1:secondIndex]
        if day == '10' or day == '20' or day == '30':
            day = day
        else:
            day = day.replace('0', '')
        year = dateString[secondIndex+1:]
        tourDate = year + '-' + month + '-' + day
        attrDate = year + '_' + month + '_' + day
        return tourDate, attrDate
    # 06-Mar-2007
    elif regex3.match(dateString) is not None:
        firstIndex = getIndices('-',dateString)[0]
        secondIndex = getIndices('-',dateString)[1]
        month = monthMap[dateString[firstIndex+1:secondIndex].lower()].replace('0','')
        if month != '10':
            month = month.replace('0', '')
        day = dateString[0:firstIndex]
        if day == '10' or day == '20' or day == '30':
            day = day
        else:
            day = day.replace('0', '')
        year = dateString[secondIndex+1:]
        tourDate = year + '-' + month + '-' + day
        attrDate = year + '_' + month + '_' + day
        return tourDate, attrDate
    # March 06, 2007
    elif regex4.match(dateString) is not None:
        month = monthMap2[dateString[:dateString.index(' ')].lower()]
        if month != '10':
            month = month.replace('0','')
        day = dateString[dateString.index(' ') + 1:dateString.index(',')]
        if day == '10' or day == '20' or day == '30':
            day = day
        else:
            day = day.replace('0', '')
        year = dateString[-4:]
        tourDate = year + '-' + month + '-' + day
        attrDate = year + '_' + month + '_' + day
        return tourDate, attrDate
    # 2018/02/01
    elif regex6.match(dateString) is not None:
        firstIndex = getIndices('/', dateString)[0]
        secondIndex = getIndices('/', dateString)[1]
        day = dateString[secondIndex + 1:]
        if day == '10' or day == '20' or day == '30':
            day = day
        else:
            day = day.replace('0', '')
        month = dateString[firstIndex + 1:secondIndex]
        if month != '10':
            month = month.replace('0', '')
        year = dateString[:firstIndex]
        tourDate = year + '-' + month + '-' + day
        attrDate = year + '_' + month + '_' + day
        return tourDate, attrDate
    # 2018.04.02
    elif regex5.match(dateString) is not None:
        firstIndex = getIndices('.', dateString)[0]

        secondIndex = getIndices('.', dateString)[1]
        day = dateString[secondIndex + 1:]
        if day == '10' or day == '20' or day == '30':
            day = day
        else:
            day = day.replace('0', '')
        month = dateString[firstIndex + 1:secondIndex]
        if month != '10':
            month = month.replace('0', '')
        year = dateString[:4]
        tourDate = year + '-' + month + '-' + day
        attrDate = year + '_' + month + '_' + day
        return tourDate, attrDate
    # 2018-01-02
    elif regex7.match(dateString) is not None:
        firstIndex = getIndices('-', dateString)[0]
        secondIndex = getIndices('-', dateString)[1]
        day = dateString[secondIndex + 1:]
        if day == '10' or day == '20' or day == '30':
            day = day
        else:
            day = day.replace('0', '')
        month = dateString[firstIndex + 1:secondIndex]
        if month != '10':
            month = month.replace('0', '')
        year = dateString[:firstIndex]
        tourDate = year + '-' + month + '-' + day
        attrDate = year + '_' + month + '_' + day
        return tourDate, attrDate
    # 20180102
    elif regex8.match(dateString) is not None:
        year = dateString[0:4]
        month = dateString[4:6]
        day = dateString[6:]
        if day == '10' or day == '20' or day == '30':
            day = day
        else:
            day = day.replace('0', '')
        if month != '10':
            month = month.replace('0', '')
        tourDate = year + '-' + month + '-' + day
        attrDate = year + '_' + month + '_' + day
        return tourDate, attrDate
    else:
        return 'Sorry, do not recognise the format of the date you input!'

def deal_info(info):
    price_info = info['tour_grades'][0]['age_bands']
    result = " "
    for i in range(len(price_info)):
        result += price_info[i]['band_summary'] + "\t"
    return result

# normalize the date
def changeToUrl(dateString,attraction_name):
    url = attractions[attraction_name]
    equalSymbol = getIndices('=',url)
    andSymbol = getIndices('&',url)
    indices = []
    for i,j in zip(equalSymbol[:len(andSymbol)],andSymbol):
        indices.append(i)
        indices.append(j)
    days = changeToDate(dateString)
    url = url[:indices[0]+1]+days[0]+url[indices[1]:indices[2]+1]+days[1]+url[indices[3]:]
    return url

# get the info of price
def getPrice(dateString,attraction_name):
    url = changeToUrl(dateString,attraction_name)
    resp = requests.get(url)
    info = json.loads(resp.text)
    result = ""
    if info['polling_state'] == "IN_PROGRESS":
        resp = requests.get(url)
        info = json.loads(resp.text)
        count = 0
        while info['polling_state'] == "IN_PROGRESS":
            resp = requests.get(url)
            #print(url)
            count += 1
            info = json.loads(resp.text)
            if info['polling_state'] != "IN_PROGRESS":
                if info['tour_grades'][0]['price_formatted'] is None:
                    return attraction_name + '\t' + ' has been old out...'
                else:
                    return attraction_name + '\t' + deal_info(info)
            # if count == 10:
            #     return None
    elif info['polling_state'] == 'COMPLETE':
        if info['tour_grades'][0]['price_formatted'] is None:
            return attraction_name+'\t'+' has been old out...'
        else:
            return attraction_name+'\t'+deal_info(info)
    else:
        return attraction_name+'\t'+' has been old out...'

# get the final price
def getFinalPrice(dateString,attraction_name,senior_num,adult_num,child_num):
    people = ['senior','adult','child']
    info = getPrice(dateString,attraction_name)
    senior_price, adult_price, child_price = 0, 0, 0
    for i in info.split('\t')[1:]:
        for index,person in enumerate(people):
            if person in i.lower():
                if index == 0:
                    senior_price = senior_num * float(i[i.index('$')+1:])
                elif index == 1:
                    adult_price = adult_num * float(i[i.index('$')+1:])
                else:
                    child_price = child_num * float(i[i.index('$')+1:])

    total_price = "{:.2f}".format(senior_price + adult_price + child_price)
    result = {'status': 'available',
              'date': dateString,
              'attractionName': attraction_name,
              'seniorNum': senior_num,
              'seniorPrice': "{:.2f}".format(senior_price),
              'adultNum': adult_num,
              'adultPrice': "{:.2f}".format(adult_price),
              'childNum': child_num,
              'childPrice': "{:.2f}".format(child_price),
              'totalPrice': "{:.2f}".format(senior_price + adult_price + child_price)}
    if total_price == '0.00':
        result['status'] = 'unavailable'
    return json.dumps(result)

if __name__ == '__main__':
    dateString = '20190814'
    for attraction_name in attractions:
        print(getFinalPrice(dateString, attraction_name,1,2,1))
        time.sleep(0.3)
