"""Simple instagram bot that make follows to other accounts"""


import random


from time import sleep


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Mixin:

    '''Class mixin, here you can change some configurations like amount of scrollbox pixels or Xpath(road to html element)'''

    f_photo = "//div[@class=\"v1Nh3 kIKUG  _bz0w\"]"
    btn_follow = "//button[contains(text(), 'Подписаться')]"
    check_close_acc = "//div[@class=\"QlxVY\"]"
    acc_exist = '//div[@class=\"                     Igw0E     IwRSH        YBx95       _4EzTm                                                                                         pwoi_            xUzvG         \"]'
    btn_like = '//span[@class=\"fr66n\"]'
    scroll_box = '/html/body/div[6]/div/div/div[2]'
    scroll_box_quit_button = '/html/body/div[6]/div/div/div[1]/div/div[2]/button/div'
    amount_of_scrollbox_pixels = '20000'


    def check_exist(self, link):
        try:
            self.driver.find_element_by_xpath(link)
        except NoSuchElementException:
            return False
        return True

    def rand_sleep(self):
        time = random.randint(2, 5)
        sleep(time)

class GetFollowersAccount(Mixin):

    '''Writing to the list of all account names using a scroll box, returns a list of accounts names.'''

    def _get_names(self, fn, follow_name):
        self.rand_sleep()
        self.driver.get("https://www.instagram.com/" + fn)
        self.rand_sleep()
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(follow_name)).click()
        self.rand_sleep()
        sugs = self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(follow_name))

        list_of_accounts = []

        #ScrollBox
        print(str(self.check_exist(self.scroll_box)) + 'Checking for the presence of a box with a scroll!')
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        self.rand_sleep()
        scroll_box = self.driver.find_element_by_xpath(self.scroll_box)
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script(f"""
                arguments[0].scrollTo(0, {self.amount_of_scrollbox_pixels});
                return arguments[0].scrollHeight;
                """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        print(links)
        names = [name.text for name in links if name.text != '']
        print(names)

        self.driver.find_element_by_xpath(self.scroll_box_quit_button).click()

        for name in names:
            print(name)
            list_of_accounts.append(name)

        print("Recorded data")
        return list_of_accounts


class MakeFollow(GetFollowersAccount, Mixin):

    '''Making follows with counts daily amount of follows and amount of iteration cycle follows for sleep time'''

    def get_follow(self, par1, par2, amount_by_hour, amount_by_cycle):
        amount = 0
        daily_amount = 0
        amount_already_followed = 0
        list_of_accounts = self._get_names(par1, par2)

        for name in list_of_accounts:
            self.rand_sleep()
            self.driver.get("https://www.instagram.com/" + name)
            print('Trying to like and subscribe to : ' + name)
            if self.check_exist(self.acc_exist) == False:
                print(str(self.check_exist(self.acc_exist)) + ' Page found')
                if self.check_exist("//button[contains(text(), 'Подписаться')]") == False:
                    print(str(self.check_exist("//button[contains(text(), 'Подписаться')]")) + ' This page has already been subscribed')
                    amount_already_followed += 1
                    print('Number of missed accounts : ' + str(amount_already_followed))
                    self.rand_sleep()
                    continue
                elif self.check_exist(self.check_close_acc) == True:
                    print(str(self.check_exist(self.check_close_acc)) + ' Closed page')
                    amount_already_followed += 1
                    print('Number of missed accounts : ' + str(amount_already_followed))
                    self.rand_sleep()
                    continue
                    self.rand_sleep()
                elif self.check_exist(self.f_photo) == False:
                    print(str(self.check_exist(self.f_photo)) + ' There are no photos on the page')
                    if self.check_exist(self.btn_follow) == True:
                        self.driver.find_element_by_xpath("//button[contains(text(), 'Подписаться')]").click()
                        self.rand_sleep()
                        amount += 1
                        daily_amount += 1
                        print('Number of subscriptions made : ' + str(daily_amount))
                        if amount >= int(amount_by_hour):
                            print('You need to rest for an hour, otherwise Instagram will be angry')
                            sleep(3600)
                            amount -= int(amount_by_hour)
                        self.rand_sleep()
                    else:
                        continue
                else:
                    if self.check_exist(self.f_photo) == True:
                        self.driver.find_element_by_xpath("//div[@class=\"v1Nh3 kIKUG  _bz0w\"]").click()
                        self.rand_sleep()
                    else:
                        self.driver.get("https://www.instagram.com/" + name)
                        self.driver.find_element_by_xpath("//div[@class=\"v1Nh3 kIKUG  _bz0w\"]").click()
                        self.rand_sleep()
                    if self.check_exist(self.btn_like) == True:
                        self.driver.find_element_by_xpath('//span[@class=\"fr66n\"]').click()
                        self.rand_sleep()
                        self.driver.get("https://www.instagram.com/" + name)
                        self.rand_sleep()
                    else:
                        self.driver.get("https://www.instagram.com/" + name)
                        self.rand_sleep()

                    self.rand_sleep()
                    if self.check_exist(self.btn_follow) == True:
                        self.driver.find_element_by_xpath("//button[contains(text(), 'Подписаться')]").click()
                        self.rand_sleep()
                        amount += 1
                        daily_amount += 1
                        print('Number of subscriptions made : ' + str(daily_amount))
                        if amount >= int(amount_by_hour):
                            print('You need to rest for an hour, otherwise Instagram will be angry')
                            sleep(3600)
                            amount -= int(amount_by_hour)
                        self.rand_sleep()
                    else:
                        print('Page not found')
                        continue
            else:
                continue
            if daily_amount >= int(amount_by_cycle):
                print('Everything for today, until tomorrow!')
                self.driver.quit()


class InstaBot(MakeFollow, Mixin):

    '''Main class that do authenication to instagram account, find your target for steal accounts name and running other function like get_follow'''

    def __init__(self, user_name, user_pw, fn, amount_by_hour, amount_by_cycle):
        self.driver = webdriver.Chrome()
        self.amount_by_hour = amount_by_hour
        self.amount_by_cycle = amount_by_cycle
        self.fn = fn
        self.follow_name = self.fn + '/followers/'
        self.driver.get("https://www.instagram.com/")
        self.rand_sleep()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(user_name)
        self.rand_sleep()
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(user_pw)
        self.rand_sleep()
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        self.rand_sleep()
        if self.check_exist("//button[contains(text(), 'Не сейчас')]") == True:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Не сейчас')]").click()
            self.rand_sleep()
        else:
            self.driver.get("https://www.instagram.com/" + user_name)
        if self.check_exist("//button[contains(text(), 'Не сейчас')]") == True:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Не сейчас')]").click()
            self.rand_sleep()
        else:
            self.driver.get("https://www.instagram.com/" + user_name)

    def get_followers(self):
        try:
            self.get_follow(self.fn, self.follow_name, self.amount_by_hour, self.amount_by_cycle)
        except:
            self.get_follow(self.fn, self.follow_name, self.amount_by_hour, self.amount_by_cycle)
    def quit(self):
        self.driver.quit()
        return print("exit")
