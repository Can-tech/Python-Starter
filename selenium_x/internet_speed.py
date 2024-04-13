from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class InternetSpeedTwitterBot:
    promissed_upload = 10
    promissed_download = 35

    def __init__(self, twitter_email, twitter_password, twitter_username) -> None:
        self.twitter_email=twitter_email
        self.twitter_password=twitter_password
        self.twitter_username=twitter_username
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.down=0
        self.up=0
    def get_internet_speed(self):
        #laod the speed page
        self.driver.get("https://www.speedtest.net/")
        #close the pop-up privacy
        sleep(3)
        self.driver.find_element(By.ID, value='onetrust-accept-btn-handler').click()
        self.driver.find_element(By.CLASS_NAME, value='start-text').click()
        sleep(40)
        self.down = self.driver.find_element(By.CLASS_NAME, value='download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, value='upload-speed').text
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        sleep(3)
        self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a').click()
        sleep(3)
        email = self.driver.find_element(By.NAME, "text")
        if email.text == "":
            email.click()
            sleep(1)
            email.send_keys(self.twitter_email)
        sleep(2)
        self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
        sleep(2)
        username = self.driver.find_element(By.CSS_SELECTOR, value='input')
        if username.text == "":
            username.click()
            username.send_keys(self.twitter_username)
        sleep(2)

        button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="ocfEnterTextNextButton"]').click()

        sleep(2)

        password = self.driver.find_element(By.NAME, value='password')
        if password.text == "":
            password.click()
            password.send_keys(self.twitter_password)
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, value='[data-testid="LoginForm_Login_Button"]').click()
        sleep(5)

        ##After Login
        tweet_textarea = self.driver.find_element(By.CSS_SELECTOR, value='[data-testid="tweetTextarea_0"]')
        tweet_textarea.click()
        sleep(1)
        tweet_textarea.send_keys(f"Hey why is my internet speed, {self.down}/{self.up}")
        sleep(1)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, value='[data-testid="tweetButtonInline"]')
        tweet_button.click()







bot1 = InternetSpeedTwitterBot("...", "...", "...")

bot1.get_internet_speed()
if(float(bot1.down) < bot1.promissed_download):
    bot1.tweet_at_provider()
# bot1.tweet_at_provider()

        