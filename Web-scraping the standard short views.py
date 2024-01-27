from selenium import webdriver
from bs4 import BeautifulSoup
import time

def scrapblogs():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        url = "https://www.youtube.com/@TheSecretSauceTH/shorts"
        driver.get(url)
        time.sleep(5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        titles = soup.find_all('span', attrs={'class': 'inline-metadata-item style-scope ytd-video-meta-block'})

        for title in titles:
            print(title.text)

    finally:
        driver.quit()

scrapblogs()