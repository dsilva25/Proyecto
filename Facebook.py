#Login automatico en facebook

from selenium import webdriver
import time


# Abrir navegador
driver = webdriver.Firefox()
#driver = webdriver.Chrome()

# Abrir sitio web
driver.get('https://www.facebook.com')

# Localizar el input de usuario y contraseña
input_email = driver.find_element_by_id('email')
input_password = driver.find_element_by_id('pass')

#introducir los datos de login
input_email.send_keys('User')
input_password.send_keys('pass')


input_password.submit()
time.sleep(10)

input_search = driver.find_element_by_name('q')
#('//*[@id="u_4_2"]/input[1]')

input_search.send_keys('Nombre a buscar')
input_search.submit()
