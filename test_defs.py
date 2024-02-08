# # Тест для функции get_urls
# import pytest
#
# from crap import get_data, get_urls
#
#
# def test_get_urls():
#     raw_url = 'https://goldapple.ru/parfjumerija'
#     start = 1
#     end = 1
#     urls = get_urls(raw_url, start, end)
#     assert len(urls) > 0
#     for url in urls:
#         assert url.startswith('https://goldapple.ru')
#
#
# # Тест для функции get_data
# def test_get_data():
#     urls = ['https://goldapple.ru/19760313110-78-vintage-green', 'https://goldapple.ru/19000191525-magnolia-bouquet']
#     data = get_data(urls)
#     assert len(data) == len(urls)
#     for item in data:
#         assert 'name' in item
#         assert 'price' in item
#         assert 'url' in item
#         assert 'description' in item
#         assert 'application' in item
#         assert 'rating_value' in item
#         assert 'rating_count' in item
#         assert 'manufacturer_country' in item
#         assert item['url'] in urls
#
#
# # Запуск тестов
# if __name__ == "__main__":
#     pytest.main()
import csv

import pytest

from crap import get_urls, get_data, write_to_csv, main


@pytest.fixture
def urls():
    return ['https://goldapple.ru/7201000005-3-l-imperatrice',
            ]


@pytest.fixture
def data_list():
    return [
        {'name': 'L’Imperatrice Eau de Toilette', 'price': '10900',
         'url': 'https://goldapple.ru/7201000005-3-l-imperatrice',
         'description': "Туалетная вода L'Imperatrice от известного итальянского бренда DOLCE & GABBANA - воплощение женской чувственности, нежности и тайны, которую стремится узнать каждый мужчина.\nЭксклюзивная туалетная вода для роскошных дам\nОбраз, вдохновивший парфюмеров DOLCE & GABBANA на создание композиции L'Imperatrice  - это молодая, независимая и эффектная женщина, обладающая магнетическим шармом, прирожденным обаянием и очаровательной харизмой, перед которой невозможно устоять.\nАромат создает мягкую, но в то же время динамичную и интригующую атмосферу страсти и соблазна, завораживая и увлекая окружающих в мир сладких грез и фантазий. Туалетная вода L'Imperatrice от DOLCE&GABBAN универсальна. Она одинаково хорошо сочетается как с дневным, так и с вечерним нарядом, подчеркивая яркую индивидуальность, неотразимость и безупречное чувство стиля своей обладательницы.\nВерхние ноты аромата раскрываются в роскошном сочетании аккордов экзотических фруктов и розовых цветов. Затем в ансамбль плавно вступают гармоничные ноты сердца, которые проявляются в легком и свежем звучании спелого арбуза и ягод киви. Нежный и чарующий базовый шлейф, сотканный из цветочно-пряных розовых цикламенов и мускуса, наполнит утонченный аромат бодрым, весенним настроением.\nИдеальная гармония содержания и формы\nДля флакона аромата L'Imperatrice DOLCE & GABBANA парфюмеры избрали элегантную классическую форму. Флакон выполнен из прозрачного органического стекла, декорированного стильной надписью с названием композиции и бренда. Черный колпачок символизирует интригу и загадочность, которые сокрыты в бездонных глубинах женской души.",
         'application': 'Нет информации', 'rating_value': '0', 'rating_count': '0', 'manufacturer_country': 'ОАЭ'}
    ]


@pytest.fixture
def csv_file_path():
    return 'test.csv'


def test_get_urls(urls):
    raw_url = 'https://goldapple.ru/parfjumerija'
    start = 1
    end = 1
    expected_urls = ['https://goldapple.ru/28320100005-wild-roses',
                     'https://goldapple.ru/7431800005-eros-pour-femme',
                     'https://goldapple.ru/19760337211-bois-imperial-by-quentin-bisch',
                     'https://goldapple.ru/19000117858-porto-bello',
                     'https://goldapple.ru/19000240976-toy-2-pearl',
                     'https://goldapple.ru/19000161477-akasha-the-5th-element',
                     'https://goldapple.ru/19000183765-the-lovers',
                     'https://goldapple.ru/26370800004-white-suede',
                     'https://goldapple.ru/19000112931-eart',
                     'https://goldapple.ru/19000010695-les-eaux-d-un-instant-immense-peony',
                     'https://goldapple.ru/19000153568-unique-coffeeze',
                     'https://goldapple.ru/19760300420-901-muscade-amande-patchouli',
                     'https://goldapple.ru/19000181902-stay-home-relax',
                     'https://goldapple.ru/19000202658-aroma-candle',
                     'https://goldapple.ru/19000030981-douce-insomnie-verte-euphorie',
                     'https://goldapple.ru/19760300423-902-armagnac-tabac-blond-cannelle',
                     'https://goldapple.ru/19000195368-rattan-22-cm-3-mm',
                     'https://goldapple.ru/19000244593-deep-sweet-kiss',
                     'https://goldapple.ru/19000164098-urban-love',
                     'https://goldapple.ru/82510700003-amber-empire',
                     'https://goldapple.ru/19000109663-get-the-feeling',
                     'https://goldapple.ru/82860100001-eau-de-parfum',
                     'https://goldapple.ru/19000122590-quelque-chose-dans-l-air-s-c',
                     'https://goldapple.ru/19000153566-unique-cuirissime',
                     'https://goldapple.ru/28320100005-wild-roses',
                     'https://goldapple.ru/7431800005-eros-pour-femme',
                     'https://goldapple.ru/19760337211-bois-imperial-by-quentin-bisch',
                     'https://goldapple.ru/19000117858-porto-bello',
                     'https://goldapple.ru/19000240976-toy-2-pearl',
                     'https://goldapple.ru/19000161477-akasha-the-5th-element',
                     'https://goldapple.ru/19000183765-the-lovers',
                     'https://goldapple.ru/26370800004-white-suede',
                     'https://goldapple.ru/19000112931-eart',
                     'https://goldapple.ru/19000010695-les-eaux-d-un-instant-immense-peony',
                     'https://goldapple.ru/19000153568-unique-coffeeze',
                     'https://goldapple.ru/19760300420-901-muscade-amande-patchouli',
                     'https://goldapple.ru/19000181902-stay-home-relax',
                     'https://goldapple.ru/19000202658-aroma-candle',
                     'https://goldapple.ru/19000030981-douce-insomnie-verte-euphorie',
                     'https://goldapple.ru/19760300423-902-armagnac-tabac-blond-cannelle',
                     'https://goldapple.ru/19000195368-rattan-22-cm-3-mm',
                     'https://goldapple.ru/19000244593-deep-sweet-kiss',
                     'https://goldapple.ru/19000164098-urban-love',
                     'https://goldapple.ru/82510700003-amber-empire',
                     'https://goldapple.ru/19000109663-get-the-feeling',
                     'https://goldapple.ru/82860100001-eau-de-parfum',
                     'https://goldapple.ru/19000122590-quelque-chose-dans-l-air-s-c',
                     'https://goldapple.ru/19000153566-unique-cuirissime',
                     'https://goldapple.ru/28320100005-wild-roses',
                     'https://goldapple.ru/7431800005-eros-pour-femme',
                     'https://goldapple.ru/19760337211-bois-imperial-by-quentin-bisch',
                     'https://goldapple.ru/19000117858-porto-bello',
                     'https://goldapple.ru/19000240976-toy-2-pearl',
                     'https://goldapple.ru/19000161477-akasha-the-5th-element',
                     'https://goldapple.ru/19000183765-the-lovers',
                     'https://goldapple.ru/26370800004-white-suede',
                     'https://goldapple.ru/19000112931-eart',
                     'https://goldapple.ru/19000010695-les-eaux-d-un-instant-immense-peony',
                     'https://goldapple.ru/19000153568-unique-coffeeze',
                     'https://goldapple.ru/19760300420-901-muscade-amande-patchouli',
                     'https://goldapple.ru/19000181902-stay-home-relax',
                     'https://goldapple.ru/19000202658-aroma-candle',
                     'https://goldapple.ru/19000030981-douce-insomnie-verte-euphorie',
                     'https://goldapple.ru/19760300423-902-armagnac-tabac-blond-cannelle',
                     'https://goldapple.ru/19000195368-rattan-22-cm-3-mm',
                     'https://goldapple.ru/19000244593-deep-sweet-kiss',
                     'https://goldapple.ru/19000164098-urban-love',
                     'https://goldapple.ru/82510700003-amber-empire',
                     'https://goldapple.ru/19000109663-get-the-feeling',
                     'https://goldapple.ru/82860100001-eau-de-parfum',
                     'https://goldapple.ru/19000122590-quelque-chose-dans-l-air-s-c',
                     'https://goldapple.ru/19000153566-unique-cuirissime',
                     'https://goldapple.ru/28320100005-wild-roses',
                     'https://goldapple.ru/7431800005-eros-pour-femme',
                     'https://goldapple.ru/19760337211-bois-imperial-by-quentin-bisch',
                     'https://goldapple.ru/19000117858-porto-bello',
                     'https://goldapple.ru/19000240976-toy-2-pearl',
                     'https://goldapple.ru/19000161477-akasha-the-5th-element',
                     'https://goldapple.ru/19000183765-the-lovers',
                     'https://goldapple.ru/26370800004-white-suede',
                     'https://goldapple.ru/19000112931-eart',
                     'https://goldapple.ru/19000010695-les-eaux-d-un-instant-immense-peony',
                     'https://goldapple.ru/19000153568-unique-coffeeze',
                     'https://goldapple.ru/19760300420-901-muscade-amande-patchouli',
                     'https://goldapple.ru/19000181902-stay-home-relax',
                     'https://goldapple.ru/19000202658-aroma-candle',
                     'https://goldapple.ru/19000030981-douce-insomnie-verte-euphorie',
                     'https://goldapple.ru/19760300423-902-armagnac-tabac-blond-cannelle',
                     'https://goldapple.ru/19000195368-rattan-22-cm-3-mm',
                     'https://goldapple.ru/19000244593-deep-sweet-kiss',
                     'https://goldapple.ru/19000164098-urban-love',
                     'https://goldapple.ru/82510700003-amber-empire',
                     'https://goldapple.ru/19000109663-get-the-feeling',
                     'https://goldapple.ru/82860100001-eau-de-parfum',
                     'https://goldapple.ru/19000122590-quelque-chose-dans-l-air-s-c',
                     'https://goldapple.ru/19000153566-unique-cuirissime',
                     'https://goldapple.ru/28320100005-wild-roses',
                     'https://goldapple.ru/7431800005-eros-pour-femme',
                     'https://goldapple.ru/19760337211-bois-imperial-by-quentin-bisch',
                     'https://goldapple.ru/19000117858-porto-bello',
                     'https://goldapple.ru/19000240976-toy-2-pearl',
                     'https://goldapple.ru/19000161477-akasha-the-5th-element',
                     'https://goldapple.ru/19000183765-the-lovers',
                     'https://goldapple.ru/26370800004-white-suede',
                     'https://goldapple.ru/19000112931-eart',
                     'https://goldapple.ru/19000010695-les-eaux-d-un-instant-immense-peony',
                     'https://goldapple.ru/19000153568-unique-coffeeze',
                     'https://goldapple.ru/19760300420-901-muscade-amande-patchouli',
                     'https://goldapple.ru/19000181902-stay-home-relax',
                     'https://goldapple.ru/19000202658-aroma-candle',
                     'https://goldapple.ru/19000030981-douce-insomnie-verte-euphorie',
                     'https://goldapple.ru/19760300423-902-armagnac-tabac-blond-cannelle',
                     'https://goldapple.ru/19000195368-rattan-22-cm-3-mm',
                     'https://goldapple.ru/19000244593-deep-sweet-kiss',
                     'https://goldapple.ru/19000164098-urban-love',
                     'https://goldapple.ru/82510700003-amber-empire',
                     'https://goldapple.ru/19000109663-get-the-feeling',
                     'https://goldapple.ru/82860100001-eau-de-parfum',
                     'https://goldapple.ru/19000122590-quelque-chose-dans-l-air-s-c',
                     'https://goldapple.ru/19000153566-unique-cuirissime',
                     'https://goldapple.ru/28320100005-wild-roses',
                     'https://goldapple.ru/7431800005-eros-pour-femme',
                     'https://goldapple.ru/19760337211-bois-imperial-by-quentin-bisch',
                     'https://goldapple.ru/19000117858-porto-bello',
                     'https://goldapple.ru/19000240976-toy-2-pearl',
                     'https://goldapple.ru/19000161477-akasha-the-5th-element',
                     'https://goldapple.ru/19000183765-the-lovers',
                     'https://goldapple.ru/26370800004-white-suede',
                     'https://goldapple.ru/19000112931-eart',
                     'https://goldapple.ru/19000010695-les-eaux-d-un-instant-immense-peony',
                     'https://goldapple.ru/19000153568-unique-coffeeze',
                     'https://goldapple.ru/19760300420-901-muscade-amande-patchouli',
                     'https://goldapple.ru/19000181902-stay-home-relax',
                     'https://goldapple.ru/19000202658-aroma-candle',
                     'https://goldapple.ru/19000030981-douce-insomnie-verte-euphorie',
                     'https://goldapple.ru/19760300423-902-armagnac-tabac-blond-cannelle',
                     'https://goldapple.ru/19000195368-rattan-22-cm-3-mm',
                     'https://goldapple.ru/19000244593-deep-sweet-kiss',
                     'https://goldapple.ru/19000164098-urban-love',
                     'https://goldapple.ru/82510700003-amber-empire',
                     'https://goldapple.ru/19000109663-get-the-feeling',
                     'https://goldapple.ru/82860100001-eau-de-parfum',
                     'https://goldapple.ru/19000122590-quelque-chose-dans-l-air-s-c',
                     'https://goldapple.ru/19000153566-unique-cuirissime',
                     'https://goldapple.ru/28320100005-wild-roses',
                     'https://goldapple.ru/7431800005-eros-pour-femme',
                     'https://goldapple.ru/19760337211-bois-imperial-by-quentin-bisch',
                     'https://goldapple.ru/19000117858-porto-bello',
                     'https://goldapple.ru/19000240976-toy-2-pearl',
                     'https://goldapple.ru/19000161477-akasha-the-5th-element',
                     'https://goldapple.ru/19000183765-the-lovers',
                     'https://goldapple.ru/26370800004-white-suede',
                     'https://goldapple.ru/19000112931-eart',
                     'https://goldapple.ru/19000010695-les-eaux-d-un-instant-immense-peony',
                     'https://goldapple.ru/19000153568-unique-coffeeze',
                     'https://goldapple.ru/19760300420-901-muscade-amande-patchouli',
                     'https://goldapple.ru/19000181902-stay-home-relax',
                     'https://goldapple.ru/19000202658-aroma-candle',
                     'https://goldapple.ru/19000030981-douce-insomnie-verte-euphorie',
                     'https://goldapple.ru/19760300423-902-armagnac-tabac-blond-cannelle',
                     'https://goldapple.ru/19000195368-rattan-22-cm-3-mm',
                     'https://goldapple.ru/19000244593-deep-sweet-kiss',
                     'https://goldapple.ru/19000164098-urban-love',
                     'https://goldapple.ru/82510700003-amber-empire',
                     'https://goldapple.ru/19000109663-get-the-feeling',
                     'https://goldapple.ru/82860100001-eau-de-parfum',
                     'https://goldapple.ru/19000122590-quelque-chose-dans-l-air-s-c',
                     'https://goldapple.ru/19000153566-unique-cuirissime']
    actual_urls = get_urls(raw_url, start, end)
    assert expected_urls == actual_urls


def test_get_data(urls):
    expected_data_list = [
        {'name': 'L’Imperatrice Eau de Toilette', 'price': '10900',
         'url': 'https://goldapple.ru/7201000005-3-l-imperatrice',
         'description': "Туалетная вода L'Imperatrice от известного итальянского бренда DOLCE & GABBANA - воплощение женской чувственности, нежности и тайны, которую стремится узнать каждый мужчина.\nЭксклюзивная туалетная вода для роскошных дам\nОбраз, вдохновивший парфюмеров DOLCE & GABBANA на создание композиции L'Imperatrice  - это молодая, независимая и эффектная женщина, обладающая магнетическим шармом, прирожденным обаянием и очаровательной харизмой, перед которой невозможно устоять.\nАромат создает мягкую, но в то же время динамичную и интригующую атмосферу страсти и соблазна, завораживая и увлекая окружающих в мир сладких грез и фантазий. Туалетная вода L'Imperatrice от DOLCE&GABBAN универсальна. Она одинаково хорошо сочетается как с дневным, так и с вечерним нарядом, подчеркивая яркую индивидуальность, неотразимость и безупречное чувство стиля своей обладательницы.\nВерхние ноты аромата раскрываются в роскошном сочетании аккордов экзотических фруктов и розовых цветов. Затем в ансамбль плавно вступают гармоничные ноты сердца, которые проявляются в легком и свежем звучании спелого арбуза и ягод киви. Нежный и чарующий базовый шлейф, сотканный из цветочно-пряных розовых цикламенов и мускуса, наполнит утонченный аромат бодрым, весенним настроением.\nИдеальная гармония содержания и формы\nДля флакона аромата L'Imperatrice DOLCE & GABBANA парфюмеры избрали элегантную классическую форму. Флакон выполнен из прозрачного органического стекла, декорированного стильной надписью с названием композиции и бренда. Черный колпачок символизирует интригу и загадочность, которые сокрыты в бездонных глубинах женской души.",
         'application': 'Нет информации', 'rating_value': '0', 'rating_count': '0', 'manufacturer_country': 'ОАЭ'}
    ]
    actual_data_list = get_data(urls)
    assert expected_data_list == actual_data_list


def test_write_to_csv(data_list, csv_file_path):
    expected_message = "Data has been written to CSV file with logging."
    actual_message = write_to_csv(data_list, 'test.csv')
    assert expected_message == actual_message

    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        actual_data_list = list(reader)
    assert data_list == actual_data_list
