#import modules
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('chromedriver.exe')                        #set path for webdriver
driver.get('https://web.whatsapp.com/')                              #url link of whatsappweb

option=input("Please select option (textmsg/Attachement)")           #options for select to send messages or images to whatsapp
while True:
    if option=="textmsg":                                                #condition for set options textmsg or attachement

        input('Firstly scanning QR code and enter anything')             #Scan the QR Code of whatsappweb
    
        name = input('Enter the name of user or group : ')               #Enter the user or group name of whatsapp user

        msg=input("Enter message")                                       #Enter Message


        wuser = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))                 #give the xpath of title of user
        wuser.click()

        msg_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")   #Message Box input field
        msg_box.send_keys(msg)

        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()   #Button for sending the messages

        print("Messsage Send Succesfully")
    else:
        input('Firstly scanning QR code and enter anything')                        #Scan the QR Code of whatsappweb
    
        name = input('Enter the name of user or group : ')                          #Enter the user or group name of whatsapp user

        filepath = input('Enter your filepath (images/video): ')                    #Give the file path what you have to send image

        wuser = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))   #give the xpath of title of user
        wuser.click()

        attachment = driver.find_element_by_xpath('//div[@title = "Attach"]')   #give the Attachement option for send images
        attachment.click()

        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')  #It accepts images,videos,gif etc...
        image_box.send_keys(filepath)

        sleep(3)                                                                                                                                                   

        send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')      #send Button
        send_button.click()

        print("File Send Successfully")

