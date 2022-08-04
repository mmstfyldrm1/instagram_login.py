 
from instagramUserInfo import username , password
from selenium import webdriver 
import time
from selenium.webdriver.common.keys import Keys

class Instagram : 
     def __init__(self,username,password):
         self.username = username
         self.password = password 
         self.browser = webdriver.Firefox()

     def sıgnIn(self):
         self.browser.get("https://www.instagram.com/accounts/login/?hl=tr")

         time.sleep(1)

         emailInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
         passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

         emailInput.send_keys(self.username)
         passwordInput.send_keys(self.password)
         passwordInput.send_keys(Keys.ENTER)

         time.sleep(3)

     def getFollowers(self):
         self.browser.get(f'https://www.instagram.com/{self.username}')
         time.sleep(2)
         self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").click()
         time.sleep(2)



         dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
         userA = dialog.find_elements_by_css_selector("li")
         followerCaount = len(dialog.find_elements_by_css_selector("li"))
         print(f'takipçi sayısı :{followerCaount}')


         action = webdriver.ActionChains(self.browser)

         while True :

             dialog.click()
             action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
             time.sleep(1)
             newCaount = len(dialog.find_elements_by_css_selector("li"))


             

             if  followerCaount != newCaount :
                 followerCaount = newCaount
                 print(f'YENİ SAYI {newCaount}')
                 time.sleep(3)
             else :
                   break   
        
         followerCaounta =  dialog.find_elements_by_css_selector("li")      
 
         for user in followerCaounta :
             link = user.find_element_by_css_selector("a").get_attribute("href")
             print(link)




     def takip(self):
         self.browser.get("https://www.instagram.com/neueglence/?hl=tr")
         time.sleep(2)

         followButton = self.browser.find_element_by_tag_name("button")
         
         if followButton.text == "Takip Et":
             time.sleep(2)
             followButton.click()
         else :
             print("zaten takiptesin ")
        


instagram = Instagram(username, password)

instagram.sıgnIn()
instagram.getFollowers()

#instagram.takip()



