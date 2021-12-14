import random
import json

from faker import Faker

from conf import MODEL

faker = Faker()


def books_gen(pk=1):
    pk = pk
    while True:
        yield {
            "model": MODEL,
            "pk": pk,
            "fields": {
                "title": title(),
                "year": year(),
                "pages": pages(),
                "isbn13": isbn13(),
                "rating": get_rating(),
                "price": get_price(),
                "author": get_authors()
            }
        }
        pk = pk + 1


def title():
    with open('books', encoding='utf-8') as f:
        for line in f:
            return line.strip()


def year(start_year=1900, end_year=2022):
    """

    :param start_year:
    :param end_year:
    :return:
    """
    year_cur = random.randint(start_year, end_year)
    return year_cur

def pages():
    pages_q = random.randint(1, 1000)
    return pages_q

def isbn13():
    isbn13_in = faker.isbn13()
    return isbn13_in

def get_rating():
    return random.uniform(0.0, 5.0)

def get_authors():
    return faker.name()

def get_price():
    price_cur = random.uniform(5.0, 1000.0)
    return price_cur

def main():
    gen = books_gen()
    list_ = [next(gen) for _ in range(100)]
    final_result = "final_result_1.txt"
    with open(final_result, "w", encoding='utf-8') as f:
        json.dump(list_, f, indent=4)  # fixme ensure_ascii


if __name__ == "__main__":
    main()
