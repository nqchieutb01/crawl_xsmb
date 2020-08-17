import scrapy
import json
import calendar
from collections import OrderedDict

from datetime import datetime, timedelta
OUTPUT_FILE = 'C:/Users/ADMIN/PycharmProjects/Hamy/tutorial/tutorial/Output/nnsxmb.json'
markExistDate = OrderedDict()

class sxmb(scrapy.Spider):
    name = 'sxmb'
    start_urls = []
    start_date = datetime(2006,5,15)
    end_date = datetime(2007,8,15)
    while(start_date<=end_date):
        start_urls.append("https://xskt.com.vn/ngay/"+start_date.strftime('%d-%m-%Y'))

        month = start_date.month
        day = start_date.day
        year = start_date.year
        start_urls.append("https://xskt.com.vn/ngay/" + str(day) + "-" + str(month) + "-" + str(year))
        if(day<10):
            start_urls.append("https://xskt.com.vn/ngay/0"+str(day)+"-"+str(month)+"-"+str(year))
        if(month<10) :
            start_urls.append("https://xskt.com.vn/ngay/" + str(day) + "-0" + str(month) + "-" + str(year))

        start_date = start_date + timedelta(1)

    def parse(self, response):
        num = response.xpath("//table[@class='result']/tr[2]/td[2]/em/text()").get()
        a = response.url
        for c in a :
            if c =='/':
                a= a.replace(c,"-")
        a = a.split('-')
        date = str(int(a[-3]))+"-"+str(int(a[-2]))+"-"+a[-1]
        if num != "null":
            data = {
                'result_spe'  : num ,
                'date' : date,
            }

            with open(OUTPUT_FILE, 'a') as f:
                 if not date in markExistDate.keys() :
                    markExistDate.update({date:1})
                    f.write(json.dumps(data))
                    f.write(",")
                    f.write('\n')