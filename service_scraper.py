import scrapelib
import lxml.html
import re

s = scrapelib.Scraper()

result = s.get('https://servicerequest.cityofchicago.org/web_intake_chic/')

page = lxml.html.fromstring(result.text)

options = page.xpath("//option")

url = "https://servicerequest.cityofchicago.org/web_intake_chic/Controller?op=query&invSelect="

base_url = "https://servicerequest.cityofchicago.org/web_intake_chic/"

for option in options :
    text = option.text
    service_code = option.attrib['value']
    if service_code == '' :
        continue
    
    service_url = url + service_code
    print service_url


    result2 = s.get(service_url)

    page2 = lxml.html.fromstring(result2.text)

    print page2.xpath('.//p[child::b[contains(text(), "Usage Notes")]]')[0].text_content()

    request_url = base_url + page2.xpath('.//a[child::i[contains(text(), "Request this Service")]]')[0].attrib['href']

    print request_url

    result3 = s.get(request_url)
    
    #import pdb
    #pdb.set_trace()
    page3 = lxml.html.fromstring(result3.text)
    for row in page3.xpath('.//form')[0].xpath('.//table')[0].xpath('.//tr[.//input|.//select]'):
        print row.xpath('.//td')[0].text_content()
        input_one = row.xpath('.//td')[0].xpath('.//input')
        if input_one:
            print input_one[0].values()
        else:
            print row.xpath('.//td')[0].xpath('.//select')[0].values()

        input_two = row.xpath('.//td')[1].xpath('.//input')

        if input_two:
            print input_two[0].values()
        else:
            print row.xpath('.//td')[1].xpath('.//select')[0].values()


    break
        
        
    








