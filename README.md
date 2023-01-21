# WA_PDA_Check
 This is a bot that checks for availability of driving tests in Western Australia. It searches for driving tests at selected locations and notifies you via a [telegram bot](t.me/PDABookingsBot) message if there is a change in availability. You must have paid the driving test fee for the bot to begin searching for test slots.
 
 Libraries used: 
 - [Selenium](https://selenium-python.readthedocs.io/installation.html)
 - [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
 
 To begin:
 1. Clone or download this project onto your computer 
 2. In lines 21 and 22, replace code with your DotDirect username and password

      ```
      self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm:userId"]').send_keys('my_username')
      self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm:password"]').send_keys('my_password')
      ``` 
 3. Get your telegram chat id with [this telegram bot](https://t.me/rawdatabot?start=botostore)
 4. Replace code in line 58 with your chat id

       ```
       receiver_id = 999999999
       ```
 5. Modify code in lines 38, 39, and 40 to suit your desired driving test locations

      ```
      self.driver.find_element(by=By.XPATH, value='//*[@id="id2-searchBookingContainer:siteList_CAN"]').click()
      ```
 8. Open terminal/command promt, change directory to the project folder and install the following:

      ```
      cd xxx/WA_PDA_Checker
      ```
      ```
      pip install selenium
      pip install webdriver_manager
      pip install pyTelegramBotAPI
      ```
 7. Run the script!

      ```
      python main.py
      ```

The bot will begin refreshing the page at your desired interval (seconds) and you will be sent a screenshot of the available test slots when a change in availability is detected.

<img src="https://user-images.githubusercontent.com/99251110/213735947-eeb35860-2e3e-442e-a7d5-d386ac7de085.jpeg" alt="img" width="400"/>
