import requests
from bs4 import BeautifulSoup
import configparser

import telebot

config = configparser.ConfigParser()
config.read("settings.ini")
TOKEN = config['bot_settings']['token']

bot = telebot.TeleBot(TOKEN, parse_mode=None)


def get_table_data(url: str) -> dict:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    table_ = soup.tbody
    sum_tmp = table_.find_all('td', class_='text-center')
    sum_ = list()
    for i in range(0, len(sum_tmp), 4):
        sum_.append(int(sum_tmp[i].text))

    name_tmp = table_.find_all('td')
    name = []

    for i in range(1, len(name_tmp), 8):
        name.append(name_tmp[i].text)

    result_dict = dict(zip(name, sum_))

    return result_dict


@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.send_message(message.chat.id, f'Hello {message.chat.first_name}')


@bot.message_handler(commands=['docs'])
def send_doc_count(message):
    pmi_names_ = get_table_data(url_pmi).keys()
    ivt_names_ = get_table_data(url_ivt).keys()
    ist_names_ = get_table_data(url_ist).keys()
    radio_names_ = get_table_data(url_radio).keys()
    all_names = list(pmi_names_) + list(ivt_names_) + list(ist_names_) + list(radio_names_)
    all_names_uniq = set(all_names)
    bot.send_message(message.chat.id, f"занято заявлений на бюджет {len(all_names_uniq)} / {non_commercial}")


@bot.message_handler(commands=['pmi_list'])
def send_pmi_list(message):
    data = get_table_data(url_pmi)
    lst_ = []
    counter = 1
    for i, j in data.items():
        lst_.append(str(counter) + ': ' + str(i) + ' - ' + str(j))
        lst_.append('\n')
        counter += 1

    str_ = ''
    for i in lst_:
        str_ += i

    bot.send_message(message.chat.id, str_)


@bot.message_handler(commands=['ivt_list'])
def send_ivt_list(message):
    data = get_table_data(url_ivt)
    lst_ = []
    counter = 1
    for i, j in data.items():
        lst_.append(str(counter) + ': ' + str(i) + ' - ' + str(j))
        lst_.append('\n')
        counter += 1

    result = ''
    for i in lst_:
        result += i

    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=['ist_list'])
def send_ist_list(message):
    data = get_table_data(url_ist)
    lst_ = []
    counter = 1
    for i, j in data.items():
        lst_.append(str(counter) + ': ' + str(i) + ' - ' + str(j))
        lst_.append('\n')
        counter += 1

    result = ''
    for i in lst_:
        result += i

    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=['radio_list'])
def send_radio_list(message):
    data = get_table_data(url_radio)
    lst_ = []
    counter = 1
    for i, j in data.items():
        lst_.append(str(counter) + ': ' + str(i) + ' - ' + str(j))
        lst_.append('\n')
        counter += 1

    result = ''
    for i in lst_:
        result += i

    bot.send_message(message.chat.id, result)


print('bot_started')

url_pmi = "https://abitinfo.nntu.ru/bak/rating/" \
          "?learn_form_id=0&fac_id=281474976714124&specialization=&spec_id=281474976711240&commerce=1"
url_ivt = "https://abitinfo.nntu.ru/bak/rating/" \
          "?learn_form_id=0&fac_id=281474976714124&specialization=&spec_id=281474976711241&commerce=1"
url_ist = "https://abitinfo.nntu.ru/bak/rating/" \
          "?learn_form_id=0&fac_id=281474976714124&specialization=&spec_id=281474976711244&commerce=1"
url_radio = "https://abitinfo.nntu.ru/bak/rating/" \
            "?learn_form_id=0&fac_id=281474976714124&specialization=&spec_id=281474976711248&commerce=1"

non_commercial = 40 + 93 + 125 + 35

bot.polling(none_stop=True)
