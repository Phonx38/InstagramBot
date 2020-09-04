

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC, ui

from selenium.webdriver.support.wait import WebDriverWait


class Instagram:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        print(self.driver.title)
        # self.assertEqual('Instagram',title,'Not Instagram')

    def login(self,u,p):
        username = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,'username')))
        username.clear()
        username.send_keys(u)

        sleep(1)

        password = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,'password')))
        password.clear()
        password.send_keys(p)

        logit = self.driver.find_element_by_tag_name('form')
        logit.submit()

    def goToHome(self):
        homebtn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a')))
        homebtn.click()
        ui.WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()


    def followFromUser(self,name,numOfFollowers):
        self.driver.get('https://www.instagram.com/'+name+'/')
        followingBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
        followingBtn.click()

        sleep(3)

        for i in range(1, numOfFollowers+1):
            followpeople = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[2]/ul/div/li[' + str(i) + ']/div/div[3]/button')
            followpeople.click()
            sleep(0.5)

        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()

    def unfollowFollowing(self,numOfUnfollow):
        navprofileXpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img'
        navprofile = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, navprofileXpath)))
        navprofile.click()
        sleep(1)

        profile = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]')
        profile.click()

        myfollowing = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')))
        myfollowing.click()

        for i in range(1,numOfUnfollow + 1):
            unfollowbtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[3]/button')))
            unfollowbtn.click()

            finalUnfollowBtn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[1]')))
            finalUnfollowBtn.click()

            sleep(1)

        closeBtn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button')
        closeBtn.click()

        self.goToHome()



    def logout(self):
        navprofileXpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img'
        navprofile = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, navprofileXpath)))
        navprofile.click()

        sleep(1)

        logout = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div')
        logout.click()






i = Instagram()

# sleep(5)
i.login('your Username','your password')
sleep(3)
i.unfollowFollowing(2)
i.followFromUser('account to follow user from',5)
sleep(2)
i.logout()