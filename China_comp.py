from datetime import time, date, datetime, timedelta
import wait as wait
from selenium import webdriver
from pprint import pprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import json
#


start = datetime.today().replace(microsecond=0)
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get('https://chinatechmap.aspi.org.au/#/companies')

chrome_options = Options()
wait = WebDriverWait(driver, 20)

company_list = []

elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='company__link']")))  # ожидание
company_links = [x.get_attribute('href') for x in driver.find_elements(By.XPATH, "//a[@class='company__link']")] # ссылки на данные о комп (read more)


for item in company_links:
    # проваливаемся по ссылке на компанию. Собираем данные:
    # print(url_comp)
    driver.get(item) # переходим по ссылке на компанию.
    info_data = {}

    elem = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sidebar__header']")))
    # link = url_comp

    name = driver.find_element(By.XPATH, "//div[@class='sidebar__header']").text
    short_description = driver.find_element(By.XPATH, "//div[@class='sidebar__wrap']/p").text
    market_value = driver.find_element(By.XPATH, "//ul[@class='sidebar__info']/li").text.replace('Market value\n', '')
    founder = driver.find_elements(By.XPATH, "//ul[@class='sidebar__info']/li")[2].text.replace('Founder / CEO\n', '')
    type_company = driver.find_elements(By.XPATH, "//ul[@class='sidebar__info']/li")[1].text.replace('Type of company\n', '')
    ownership_structure = driver.find_elements(By.XPATH, "//ul[@class='sidebar__info']/li")[3].text.replace('Ownership structure\n', '')
    overview = driver.find_element(By.XPATH, "//section[@id='overview']").text
    areas_of_overseas = driver.find_element(By.XPATH, "//section[@id='areas-of-overseas-business']").text
    party_state = driver.find_element(By.XPATH, "//section[@id='party-state-activities']").text
    activities_in_xinjiang = driver.find_element(By.XPATH, "//section[@id='activities-in-xianjiang']").text
    privacy_policies = driver.find_element(By.XPATH, "//section[@id='privacy']").text
    covid19 = driver.find_element(By.XPATH, "//section[@id='covid']").text

    # info_data['link'] = link
    info_data['name'] = name
    info_data['short_description'] = short_description
    info_data['market_value'] = market_value
    info_data['founder'] = founder
    info_data['type_company'] = type_company
    info_data['ownership_structure'] = ownership_structure
    info_data['overview'] = overview
    info_data['areas_of_overseas'] = areas_of_overseas
    info_data['party_state'] = party_state
    info_data['activities_in_xinjiang'] = activities_in_xinjiang
    info_data['privacy_policies'] = privacy_policies
    info_data['covid19'] = covid19

    # заливаем в список компаний
    company_list.append(info_data)


driver.close()
pprint(f'Собраны данные по  {len(company_list)} компаниям')

#
# jsonString = json.dumps(list)
file_input = 'China.json'

with open(file_input, 'w') as f:
    json.dump(company_list, f)

# df = pd.DataFrame(company_list)
# file_name = 'Сtwitch_' + str(datetime.today().replace(microsecond=0)).replace(':','').replace(' ','_').replace('-','')
# df.to_excel(f'./{file_name}.xlsx', sheet_name=name_net, index=False)

stop = datetime.today().replace(microsecond=0)
print(f'Старт в {start}, стоп в  {stop}')
print(f'Продолжительность ==> {stop - start} сек')
print(f'Вывод осуществлен в файл  ==> {file_input} ')




