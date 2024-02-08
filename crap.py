import csv
import json
import time

import requests
from bs4 import BeautifulSoup
import logging

from tqdm import tqdm

# headers = {'Accept': 'text/html,application/xhtml+xml,application/json,*/*', 'Content-Type': 'application/json',
#            'User-Agent':
#                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0'}
# response = requests.get(url=products_url, headers=headers)
#
# Настройка логгирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def get_urls(raw_url, start, end):
    """
    Получение URL-адресов страниц с продуктами.

    Args:
        raw_url (str): Базовый URL-адрес страницы с продуктами.
        start (int): Номер первой страницы.
        end (int): Номер последней страницы.

    Returns:
        list: Список URL-адресов страниц с продуктами.
    """

    products_id = []
    for i in range(start, end + 1):
        products_url = f'{raw_url}?p={i}'
        page = requests.get(products_url)
        logging.debug(f"Requesting page: {products_url}")  # Вывод информации о запрашиваемой странице
        time.sleep(10)  # Добавление задержки в 1 секунду между запросами
        soup = BeautifulSoup(page.text, "lxml")
        elements = soup.find_all('div')
        for element in elements:
            for a in element.find_all('article'):
                for e in a.find_all('a'):
                    product_id = e.get('href')
                    logging.debug(
                        f"Found product ID: {product_id}")  # Вывод информации о найденном идентификаторе продукта
                    products_id.append(f'https://goldapple.ru{product_id}')

    return products_id


def get_data(urls):
    """
    Получение данных о продуктах.

    Args:
        urls (list): Список URL-адресов страниц с продуктами.

    Returns:
        list: Список словарей с данными о продуктах.
    """

    data_list = []
    rating_value = None
    rating_count = None
    application = None
    for url in urls[0:5]:
        # Загрузка страницы с информацией о товаре
        product_page = requests.get(url, verify=False)
        if product_page is None:
            continue
        else:
            logging.debug(f"Requesting product page: {url}")  # Логирование информации о запрашиваемой странице
            product_soup = BeautifulSoup(product_page.text, 'lxml')
            application_element = product_soup.find("div", {"text": "применение", "value": "Text_1"})
            if application_element is None:
                application = 'Нет информации'
            else:
                application = application_element.find("div", class_="owdA5")
                if application:
                    application = application.text
                else:
                    application = application_element.find("div", class_="_14lAW").text
            description_element = product_soup.find("div", {"text": "описание", "value": "Description_0"})
            description = description_element.find("div", {'itemprop': 'description'}).text.strip()
            name = product_soup.find("span", class_="qKFPx").text.strip()
            price = product_soup.find("meta", itemprop="price")["content"]
            country_of_origin = product_soup.find(string='страна происхождения')
            if country_of_origin:
                manufacturer_country = country_of_origin.find_next('br').next_element
            else:
                manufacturer_country = 'Нет информации'

        reviews_link = product_soup.find('a', class_='kFclw _6AiyG SEABh')
        if reviews_link is None:
            rating_value = '0'
            rating_count = '0'

        else:
            reviews_url = f'https://goldapple.ru{reviews_link.get("href")}'
            reviews_page = requests.get(reviews_url)
            logging.debug(f"Requesting reviews page: {reviews_url}")  # Логирование информации о запрашиваемой странице
            reviews_soup = BeautifulSoup(reviews_page.text, "lxml")
            if reviews_soup:
                rating_value = reviews_soup.find('div', {'itemprop': 'ratingValue'}).text.strip()
                rating_count = reviews_soup.find('div', class_='A2l87').text.strip()
            else:
                rating_value = '0'
                rating_count = '0'

        data = {
            'name': name,
            'price': price,
            'url': url,
            'description': description,
            'application': application,
            'rating_value': rating_value,
            'rating_count': rating_count,
            'manufacturer_country': manufacturer_country
        }
        print(data)

        # Добавление словаря в список
        data_list.append(data)

        time.sleep(5)  # Добавление задержки в 10 секунд между запросами

    return data_list


def write_to_csv(data_list, csv_file_path):
    """
    Запись данных в CSV-файл.

    Args:
        data_list (list): Список словарей с данными о продуктах.
        csv_file_path (str): Путь к CSV-файлу.

    Returns:
        str: Сообщение об успешной записи данных в CSV-файл.
    """

    fieldnames = ['name', 'price', 'url', 'description', 'application', 'rating_value', 'rating_count',
                  'manufacturer_country']

    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for data in data_list:
            # Запись данных в CSV-файл
            writer.writerow(data)
            logging.debug(f"Writing data to CSV: {data}")  # Логирование информации о записываемых данных

    return "Data has been written to CSV file with logging."


def main():
    """
    Основная функция программы.
    """
    # urls = get_urls('https://goldapple.ru/parfjumerija', 1, 1)
    # with open('urls.json', 'w') as f:
    #     json.dump(urls, f, indent=4)

    # Получение URL-адресов
    with open('urls.json', 'r') as file:
        urls = json.load(file)
        unique_urls = list(set(urls))  # Преобразование в список уникальных URL-адресов

    data_list = []  # Создание списка для хранения данных

    for url in tqdm(unique_urls, desc="Processing URLs", unit="URL"):
        try:
            data_list.extend(get_data([url]))  # Добавление данных к общему списку
            for _ in tqdm(write_to_csv(data_list, 'perfumes.csv'), desc="Writing to CSV", unit="item"):
                pass
        except Exception as e:
            print(f"An error occurred while processing {url}: {e}")


if __name__ == "__main__":
    main()
# print(f"Данные успешно записаны в файл {csv_file_path}")

