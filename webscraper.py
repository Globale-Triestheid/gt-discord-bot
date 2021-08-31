import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import os
import random

path = os.path.dirname(os.path.realpath('chromedriver.exe')) + "\chromedriver.exe"


class Fryer:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=path)

    def deepfry(self, image_url):
        self.driver.get("https://deepfriedmemes.com/")
        self.driver.find_element_by_xpath("//*[@id=\"qc-cmp2-ui\"]/div[2]/div/button[2]").click()
        self.driver.find_element_by_id("imageLoader").send_keys(image_url)
        # self.driver.find_element_by_id("imageLoader").click()

        canvas = self.driver.find_element_by_id("canvas")
        location = canvas.location
        size = canvas.size

        self.driver.save_screenshot("images/shot.png")

        x = location['x']
        y = location['y']
        w = size['width']
        h = size['height']
        width = x + w
        height = y + h

        im = Image.open('images/shot.png')
        im = im.crop((int(x), int(y), int(width), int(height)))
        im.save('images/deep_img.png')

        self.driver.close()


class NSFWWebscraper:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=path)

    # It's a sad day to be a dev
    def get_rule34(self, search_term):
        self.driver.get("https://rule34.xxx/index.php")
        search_bar = self.driver.find_element_by_xpath("//*[@id=\"tags\"]")
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.ENTER)

        parent = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[1]")
        element_list = parent.find_elements_by_tag_name("span")
        element = element_list[random.randrange(len(element_list) - 1)]
        new_url = element.find_element_by_tag_name("a").get_attribute("href")

        self.driver.get(new_url)

        try:
            return self.driver.find_element_by_xpath("//*[@id=\"gelcomVideoPlayer\"]/source").get_attribute("src"),\
                   self.driver.current_url
        except selenium.common.exceptions.NoSuchElementException:
            return self.driver.find_element_by_xpath("//*[@id=\"image\"]").get_attribute("src"), self.driver.current_url

        self.driver.close()

    def close_window(self):
        self.driver.close()
