# Тест для функции get_urls
import pytest

from crap import get_data, get_urls


def test_get_urls():
    raw_url = 'https://goldapple.ru/parfjumerija'
    start = 1
    end = 1
    urls = get_urls(raw_url, start, end)
    assert len(urls) > 0
    for url in urls:
        assert url.startswith('https://goldapple.ru')


# Тест для функции get_data
def test_get_data():
    urls = ['https://goldapple.ru/19760313110-78-vintage-green', 'https://goldapple.ru/19000191525-magnolia-bouquet']
    data = get_data(urls)
    assert len(data) == len(urls)
    for item in data:
        assert 'name' in item
        assert 'price' in item
        assert 'url' in item
        assert 'description' in item
        assert 'application' in item
        assert 'rating_value' in item
        assert 'rating_count' in item
        assert 'manufacturer_country' in item
        assert item['url'] in urls


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
