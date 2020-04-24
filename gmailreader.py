from selenium import webdriver #Do Install Selenium First
from time import sleep

email = ''    #Enter Your Gmail Email ID
pwd = ''      #Enter Your Gmail Password
path = ''     #Enter Your DriverPath (eg: 'Users/User/Desktop/Directory/geckodriver or chromedriver')
url = 'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f' #Router

driver = webdriver.Firefox(executable_path= path) #Firefox Driver
#driver = webdriver.Chrome(executable_path= path) Uncomment if using chrome driver

driver.get(url)

sleep(4)
signinbox = driver.find_element_by_class_name('s-btn__google').click()

emailbox = driver.find_element_by_id('identifierId')

emailbox.send_keys(email)

nextbox = driver.find_element_by_id('identifierNext')
sleep(2)
nextbox.click()
sleep(2)
passbox = driver.find_element_by_class_name('whsOnd').send_keys(pwd)

pasnextbox = driver.find_element_by_class_name('DL0QTb')
pasnextbox.click()

sleep(2)
driver.get('https://mail.google.com/mail/u/0/#inbox')
sleep(3)
checkbox = driver.find_element_by_class_name('G-as4')
checkbox.click()

tickbox = driver.find_element_by_class_name('m9').click()
sleep(3)
refresh = driver.find_element_by_class_name('gb_qe').click()
sleep(3)

while(1):
    sleep(4)
    checkbox.click()
    sleep(1)
    checkbox.click()
    tickbox = driver.find_element_by_class_name('m9').click()
    sleep(3)
    refresh = driver.find_element_by_class_name('gb_qe').click()
    sleep(3)

# driver.quit()
