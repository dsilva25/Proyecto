#Login automatico en linkedin

from selenium import webdriver
import time
# Con esto abres el navegador
driver = webdriver.Firefox()
#driver = webdriver.Chrome('./chromedriver')

# Con esto navegas al sitio que desees
driver.get('https://www.linkedin.com/')

# Con esto localizas el input de usuario y contraseña
input_email = driver.find_element_by_id('login-email')
input_password = driver.find_element_by_id('login-password')

# Con esto introduces los datos de login
input_email.send_keys('user')
input_password.send_keys('pass')

# Para entrar puedes o bien hacer submit en algún campo del formulario o bien buscar el botón y hacer click
# 1 - Haciendo submit (Mi favorita)
input_password.submit()

time.sleep(10)

#input_search = driver.find_element_by_xpath( """//*[@id="ember1005"]/input""" )

#input_search.send_keys('Nombre a buscar')
#input_search.submit()
