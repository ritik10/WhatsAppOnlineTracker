#!/usr/bin/python3.6
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pygame
import os
from datetime import datetime
import requests,time
# import gi
# gi.require_version("Notify","0.7")
# from gi.repository  import Notify
class WhatsappOnline:
    status = None
    login=True
    #Notify.init("App Name")
    search_bar_selector = '#side > div._2HS9r > div > label > input'
    message_input_selector = """#main > footer > div._2i7Ej.copyable-area > \
        div._13mgZ > div > div._3u328.copyable-text.selectable-text"""
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./media/person_online_notification.mp3')
        self.browser = webdriver.Safari()
        self.browser.get('https://web.whatsapp.com')
        print("\nWelcome to the whatsapp bot\n")


    def get_time(self):
         return (datetime.now().strftime("%H:%M:%S:%D"))

    def online_check(self,name):
        try:
            #_1Flk2
            search_bar = self.browser.find_element_by_class_name('_2_1wd')
                # self.search_bar_selector)
            search_bar.clear()
            search_bar.click()
            search_bar.send_keys(name)
            # press enter to search the person.
            search_bar.send_keys(u'\ue007')#YmixP fKfSX
            self.browser.minimize_window()
            online_flag=True
            offline_flag=True
            while(1):
                _status = self.browser.find_element_by_css_selector('#main > header')
                status = _status.text
                #print(status)
                if status.find('online') != -1 or status.find('typing…')!=-1:
                    self.status = 'online'
                    
                    if online_flag:
                        online_flag=False
                        offline_flag=True
                        if self.login:
                            os.system(f'say "{name} is already online."')
                            os.system('afplay /System/Library/Sounds/Glass.aiff')
                            self.login=False
                        else:    
                            os.system(f'say "{name} came online."')
                            os.system('afplay /System/Library/Sounds/Glass.aiff')
                            print(name.upper() +" came online at "+ self.get_time())

                else:
                    self.status = None

                if self.status is None:
                    if offline_flag:
                        online_flag=True
                        offline_flag=False
                        if self.login:
                            os.system(f'say "{name} is currently offline."')
                            os.system('afplay /System/Library/Sounds/Sosumi.aiff')
                            self.login=False
                        else:
                            os.system(f'say "{name} went offline."')
                            os.system('afplay /System/Library/Sounds/Sosumi.aiff')
                            print("{} {}".format(name.upper(), 'went offline at '+ self.get_time()))
                    
        
        finally:
            self.browser.close()

if __name__ == "__main__":
 

    user1 = WhatsappOnline()
    name = input("\nEnter the name of the person: ")

    
    user1.online_check(name)

