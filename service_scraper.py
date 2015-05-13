import scrapelib
import lxml.html
import re

s = scrapelib.Scraper()

result = s.get('https://servicerequest.cityofchicago.org/web_intake_chic/')

page = lxml.html.fromstring(result.text)

options = page.xpath("//option")

url = "https://servicerequest.cityofchicago.org/web_intake_chic/Controller?op=query&invSelect="


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








