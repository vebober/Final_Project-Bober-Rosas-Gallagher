from bs4 import BeautifulSoup as bs
import time
from urllib.request import urlopen
from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome("mac/chromedriver")

scrape_url = "https://myplace.cuyahogacounty.us/"

driver.maximize_window()
driver.get(scrape_url)
driver.find_element_by_id("Parcel").click()

headers = ('Parcel Id',
    'Bedrooms',
    'Bathrooms',
    'Living Area Total',
    'Total Value',
    'Half Bath',
    'Year Built',
    'Construction Quality',
    'Address 1',
    'Address 2',
    'Condition',
    'Garage Type',
    'Finished Basement'
    'Total Land',
    'Recent Sale Date'
    'Sell Price'
    'Second Sale Date'
    'Second Sale Price'
                  )

    
data = []
# 71001001-710011072 complete
for i in range(82201001,82500001,1000):
    for j in range(i, i+101):

        try:
            driver.find_element_by_xpath('//input[@name="Search"]').clear()
            driver.find_element_by_xpath('//input[@name="Search"]').send_keys(j)
            driver.find_element_by_id("btnSearch").click()
            driver.find_element_by_id("btnPropertyCardInfo").click()

            bedrooms = []
            bathrooms = []
            living_area = []
            total_value = []
            half_bath = []
            year_built = []
            constuction_quality = []
            address1 = []
            address2 = []
            condition = []
            garage_type = []
            finished_basement = []
            total_land = []
            sale_date = []
            sell_price = []
            second_sale_date =[]
            second_sale_price = []

            bedrooms_path ='//*[@id="dataBody"]/table[2]/tbody/tr[9]/td[4]'
            bathrooms_path ='//*[@id="dataBody"]/table[2]/tbody/tr[10]/td[2]'
            living_area_total_path ='//*[@id="dataBody"]/table[2]/tbody/tr[15]/td[2]'
            total_value_path ='//*[@id="dataBody"]/div[4]/div[2]/table/tbody/tr[4]/td[2]'
            half_bath_path ='//*[@id="dataBody"]/table[2]/tbody/tr[10]/td[4]'
            year_built_path ='//*[@id="dataBody"]/table[2]/tbody/tr[3]/td[2]'
            construction_quality_path ='//*[@id="dataBody"]/table[2]/tbody/tr[4]/td[4]'
            address1_path = '//*[@id="dataBody"]/table[1]/tbody/tr[2]/td[2]'
            address2_path = '//*[@id="dataBody"]/table[1]/tbody/tr[3]/td[2]'
            condition_path ='//*[@id="dataBody"]/table[2]/tbody/tr[4]/td[2]'
            garage_type_path ='//*[@id="dataBody"]/table[2]/tbody/tr[11]/td[2]'
            finished_basement_path ='//*[@id="dataBody"]/table[2]/tbody/tr[8]/td[4]'
            total_land_path ='//*[@id="dataBody"]/div[4]/div[1]/table/tbody/tr[2]/td[5]'
            sale_date_path ='//*[@id="dataBody"]/table[3]/tbody/tr[2]/td[1]'
            sell_price_path = '//*[@id="dataBody"]/table[3]/tbody/tr[2]/td[4]'
            second_sale_date_path = '//*[@id="dataBody"]/table[3]/tbody/tr[3]/td[1]'
            second_sale_price_path = '//*[@id="dataBody"]/table[3]/tbody/tr[3]/td[4]'


            bedrooms = driver.find_element_by_xpath(bedrooms_path)
            bathrooms = driver.find_element_by_xpath(bathrooms_path)
            living_area = driver.find_element_by_xpath(living_area_total_path)
            total_value = driver.find_element_by_xpath(total_value_path)
            half_bath = driver.find_element_by_xpath(half_bath_path)
            year_built = driver.find_element_by_xpath(year_built_path)
            construction_quality = driver.find_element_by_xpath(construction_quality_path)
            address1 = driver.find_element_by_xpath(address1_path)
            address2 = driver.find_element_by_xpath(address2_path)
            condition = driver.find_element_by_xpath(condition_path)
            garage_type = driver.find_element_by_xpath(garage_type_path)
            finished_basement = driver.find_element_by_xpath(finished_basement_path)
            total_land = driver.find_element_by_xpath(total_land_path)
            sale_date = driver.find_element_by_xpath(sale_date_path)
            sell_price = driver.find_element_by_xpath(sell_price_path)
            second_sale_date = driver.find_element_by_xpath(second_sale_date_path)
            second_sale_price = driver.find_element_by_xpath(second_sale_price_path)

            data.append([str(j),
            bedrooms.text,
            bathrooms.text,
            living_area.text,
            total_value.text,
            half_bath.text,
            year_built.text,
            construction_quality.text,
            address1.text,
            address2.text,
            condition.text,
            garage_type.text,
            finished_basement.text,
            total_land.text,
            sale_date.text,
            sell_price.text,
            second_sale_date.text,
            second_sale_price.text,
            ])
        except:
            driver.get(scrape_url)
            driver.find_element_by_id("Parcel").click()
            print("Fail")
            

        if j%50 ==0:
            df = pd.DataFrame(data)
            df.to_csv('housing_data2.csv', mode='a', header=False,index=False)
            data = []

    print(f'{j} Complete')

print(df)

driver.quit()

