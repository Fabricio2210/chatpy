from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def getVideoId(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.set_page_load_timeout(30)
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'img'))
        )
        driver.implicitly_wait(5)
        img_src_links = [img.get_attribute("src") for img in driver.find_elements(By.CSS_SELECTOR, 'img')]
        filtered_results = [el for el in img_src_links if el and 'hqdefault_live' in el]
        if len(filtered_results) > 0:
            anchors = driver.find_elements(By.CSS_SELECTOR, 'a#thumbnail')
            parsed_channel_id_string = anchors[1].get_attribute("href").split('v=')
            video_id = parsed_channel_id_string[1]
            return video_id
        else:
            return None
    finally:
        driver.quit()
