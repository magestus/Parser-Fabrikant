# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import premailer
import logging
import urllib.parse
import urllib.request


def get_html(url):
    response = urllib.request.urlopen(url)
    print()
    return response.read()#.decode('utf8')
 
 
def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    head = soup.find('head')
    table = soup.find('div', {"class": "Search-list"})

 
    result_html = premailer.Premailer('<html>' + str(head) + '<body>' + str(table) + '</body></html>',
                                      cssutils_logging_level=logging.CRITICAL, base_url='https://www.fabrikant.ru/').transform()
    with open('result.html', 'w') as f_obj_out:
        f_obj_out.write(result_html)

    #print(table)
 
    send_mail()
 
 
def send_mail():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
 
    fromaddr = "beatsoup4test@gmail.com"
    toaddr = "beatsoup4test@gmail.com"
    #   urllib.parse.quote
    mypass = "Potestim1111"
 
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = u"Данные с фабриканта"
 
    with open('result.html') as f_obj:
        body = f_obj.read()
 
    msg.attach(MIMEText(body, 'html'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
 
 
def main():
    search_text = input('Введите запрос: ').encode('utf8')

    parse(get_html('https://www.fabrikant.ru/trades/procedure/search/?type=1&query={}&procedure_stage=1&price_from=&price_to=&currency=0&date_type=date_publication&date_from=&date_to=&ensure=all&section_type%5B%5D=ds300&count_on_page=10&order_by=default&order_direction=1'.format(urllib.parse.quote(search_text))))


if __name__ == "__main__":
    main()
