import requests
from bs4 import BeautifulSoup
import PySimpleGUI as ps

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    url = "https://www.ctrs.com.ua/?utm_source=google&utm_medium=cpc&gclid=CjwKCAiA_6yfBhBNEiwAkmXy51XNSv8D0-9TfHxFd6C0MBYp0Dmy-zV8KETGjfdPpU-Rb4uGPF-CQhoCXeYQAvD_BwE"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    print(soup)
    products = soup.findAll('div', class_='df fdc pr border-box br10 root-0-2-161 product-card')
    product = []
    prices = []
    imgs = []
    layout = []
    for prod1 in products:
        a = prod1.find('a', class_='link link-0-2-163')
        img = a.find("img", class_ = "img-0-2-162")['src']
        imgs.append(img)
        #print(img['src'])
        title = a.find('span', class_='line-clamp-2 break-word title-0-2-167').text
        product.append(title)
        price = prod1.find('div', class_='df fdc jcfe prices-0-2-166').find('div', class_='jcsb df aic priceNew-0-2-170')
        #price_product = price.find('span', class_='medium price-0-2-172')['data-price']
       # prices.append(price_product)
    menu = []
    for i in range(len(prices)):
        menu = [ps.Text(text=f'{product[i]}'), ps.Text(text=f'{prices[i]}')]

        layout.append(menu)/'mjohbuyfytfrydyrdyt'
        layout.append([ps.Push()])
        print(f'{product[i]} \t {prices[i]} \t {product[i]}')
    window = ps.Window('NoteBook', finalize=True).Layout([[ps.Column(
        layout, size=(630, 400), scrollable=True, element_justification="center", vertical_scroll_only=True,
        sbar_trough_color='black')]])
    while True:
        event, values = window.read()
        if event == ps.WIN_CLOSED or event == 'Cancel':
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
