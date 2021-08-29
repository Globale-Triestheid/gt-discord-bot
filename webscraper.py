from selenium import webdriver
from PIL import Image
import os


class Fryer:

    def __init__(self):
        path = os.path.dirname(os.path.realpath('chromedriver.exe')) + "\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=path)

    def deepFry(self, image_url):
        self.driver.get("https://deepfriedmemes.com/")
        self.driver.find_element_by_xpath("//*[@id=\"qc-cmp2-ui\"]/div[2]/div/button[2]").click()
        self.driver.find_element_by_id("imageLoader").send_keys(image_url)
        # self.driver.find_element_by_id("imageLoader").click()

        canvas = self.driver.find_element_by_id("canvas")
        location = canvas.location
        size = canvas.size

        self.driver.save_screenshot("shot.png")

        x = location['x']
        y = location['y']
        w = size['width']
        h = size['height']
        width = x + w
        height = y + h

        im = Image.open('shot.png')
        im = im.crop((int(x), int(y), int(width), int(height)))
        im.save('deep_img.png')

        self.driver.close()