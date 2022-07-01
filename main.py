import requests
from bs4 import BeautifulSoup
from pprint import pp


def get_pmi_data(url: str) -> dict:
    response_pmi = requests.get(url)
    soup_pmi = BeautifulSoup(response_pmi.text, 'lxml')

    table_pmi = soup_pmi.tbody
    sum_pmi_tmp = table_pmi.find_all('td', class_='text-center')
    sum_pmi = list()
    for i in range(0, len(sum_pmi_tmp), 4):
        sum_pmi.append(int(sum_pmi_tmp[i].text))

    name_pmi_tmp = table_pmi.find_all('td')
    name_pmi = []

    for i in range(1, len(name_pmi_tmp), 8):
        name_pmi.append(name_pmi_tmp[i].text)

    pmi_dict = dict(zip(name_pmi, sum_pmi))

    return pmi_dict


def get_ivt_data(url: str) -> dict:
    response_ivt = requests.get(url)
    soup_ivt = BeautifulSoup(response_ivt.text, 'lxml')

    table_ivt = soup_ivt.tbody
    sum_ivt_tmp = table_ivt.find_all('td', class_='text-center')
    sum_ivt = list()
    for i in range(0, len(sum_ivt_tmp), 4):
        sum_ivt.append(int(sum_ivt_tmp[i].text))

    name_ivt_tmp = table_ivt.find_all('td')
    name_ivt = []

    for i in range(1, len(name_ivt_tmp), 8):
        name_ivt.append(name_ivt_tmp[i].text)

    ivt_dict = dict(zip(name_ivt, sum_ivt))

    return ivt_dict


def get_ist_data(url: str) -> dict:
    response_ist = requests.get(url)
    soup_ist = BeautifulSoup(response_ist.text, 'lxml')

    table_ist = soup_ist.tbody
    sum_ist_tmp = table_ist.find_all('td', class_='text-center')
    sum_ist = list()
    for i in range(0, len(sum_ist_tmp), 4):
        sum_ist.append(int(sum_ist_tmp[i].text))

    name_ist_tmp = table_ist.find_all('td')
    name_ist = []

    for i in range(1, len(name_ist_tmp), 8):
        name_ist.append(name_ist_tmp[i].text)

    ist_dict = dict(zip(name_ist, sum_ist))

    return ist_dict


def get_radio_data(url: str) -> dict:
    response_radio = requests.get(url)
    soup_radio = BeautifulSoup(response_radio.text, 'lxml')

    table_radio = soup_radio.tbody
    sum_radio_tmp = table_radio.find_all('td', class_='text-center')
    sum_radio = list()
    for i in range(0, len(sum_radio_tmp), 4):
        sum_radio.append(int(sum_radio_tmp[i].text))

    name_radio_tmp = table_radio.find_all('td')
    name_radio = []

    for i in range(1, len(name_radio_tmp), 8):
        name_radio.append(name_radio_tmp[i].text)

    radio_dict = dict(zip(name_radio, sum_radio))

    return radio_dict


url_pmi = "https://abitinfo.nntu.ru/bak/rating/" \
          "?learn_form_id=0&fac_id=281474976714124&specialization=&spec_id=281474976711240&commerce=1"
url_ivt = "https://abitinfo.nntu.ru/bak/rating/" \
          "?learn_form_id=0&fac_id=281474976714124&specialization=&spec_id=281474976711241&commerce=1"
url_ist = "https://abitinfo.nntu.ru/bak/rating/" \
          "?learn_form_id=0&fac_id=281474976714124&specialization=&spec_id=281474976711244&commerce=1"
url_radio = "https://abitinfo.nntu.ru/bak/rating/" \
            "?learn_form_id=0&fac_id=281474976714124&specialization=&spec_id=281474976711248&commerce=1"

print("ПМИ")
pp(get_pmi_data(url_pmi))
print("\n")
print("ИВТ")
pp(get_ivt_data(url_ivt))
print("\n")
print("ИСТ")
pp(get_ist_data(url_ist))
print("\n")
print("РАДИОТЕХ")
pp(get_radio_data(url_radio))

non_commercial = 40 + 93 + 125 + 35

pmi_names = get_pmi_data(url_pmi).keys()
ivt_names = get_ivt_data(url_ivt).keys()
ist_names = get_ist_data(url_ist).keys()
radio_names = get_radio_data(url_radio).keys()

print("\n")

print(f"radio_names: {list(pmi_names)}")
print(f"ivt_names: {list(ivt_names)}")
print(f" ist_names: {list(ist_names)}")
print(f"radio_names: {list(radio_names)}")
print("\n")

all_names = list(pmi_names) + list(ivt_names) + list(ist_names) + list(radio_names)
all_names_uniq = set(all_names)

# print(f"all names: {all_names}")
# print(f"uniq names: {all_names_uniq}")

# print(len(all_names))
print(f"занято заявлений на бюджет {len(all_names_uniq)} / {non_commercial}")
