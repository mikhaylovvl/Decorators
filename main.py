import datetime
import re
import requests
from bs4 import BeautifulSoup
from decorators import decorator_logger
from decorator_path_arg import decorator_logs
import os

BASE_PATH = os.getcwd()
LOGS_DIR_NAME = 'logs'
LOGS_FILE_NAME = 'logs.txt'


@decorator_logger
def make_log_datetime(dt, tm):
    return f"дата: {dt}, время вызова функции: {tm}"


def get_path():
    logs_directory = os.path.join(BASE_PATH, LOGS_DIR_NAME)
    if not os.path.exists(logs_directory):
        os.mkdir(logs_directory)
    path_to_log = os.path.join(BASE_PATH, LOGS_DIR_NAME, LOGS_FILE_NAME)
    return path_to_log


@decorator_logs(get_path())
def make_logs_dt(dt, tm):
    return f"дата: {dt}, время вызова функции: {tm}"


def get_news():
    BASE_LINK = "https://habr.com"
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome"
                        " / 102.0.5005.148 YaBrowser / 22.7.2.899 Yowser / 2.5 Safari / 537.36"
    }

    res = requests.get(url="https://habr.com/ru/all/", headers=headers).text
    soup = BeautifulSoup(res, "lxml")

    all_news = soup.findAll("div", class_="tm-article-snippet")

    pattern = r"[Дд]изайн|[Фф]ото|[Ww]eb|[Pp]ython|LINSTOR"
    for a_news in all_news:
        time_published_news = a_news.find("span", class_="tm-article-snippet__datetime-published").find("time"). \
            get("title")
        link_news = a_news.find("a", class_="tm-article-snippet__title-link").get("href")
        title_news = a_news.find("a", class_="tm-article-snippet__title-link").find("span").text
        result = re.findall(pattern, title_news)
        if result:
            print(f"<{time_published_news}> - <{title_news}"
                  f"> - <{BASE_LINK + link_news}>")

    make_log_datetime(datetime.date.today(), datetime.datetime.now().time())
    make_logs_dt(datetime.date.today(), datetime.datetime.now().time())


if __name__ == '__main__':
    get_news()
