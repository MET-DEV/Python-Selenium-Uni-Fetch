from selenium import webdriver
import time

driver=webdriver.Chrome();

file=open("uni.sql","w",encoding="utf-8")
file.close();

with open("uni.sql","a",encoding="utf-8") as f:
    f.write("insert into uni (name) values ")

driver.get("https://yokatlas.yok.gov.tr/universite.php")
time.sleep(3)
for i in range(1,204):
    uni_path=f"//*[@id='myUl']/li[{i}]/div/div[1]/h3"
    uni_name=driver.find_element_by_xpath(uni_path).text;
    with open("uni.sql","a",encoding="utf-8") as f:
        f.write(f"\n('{uni_name}'),")

    print(uni_name)

driver.close();



