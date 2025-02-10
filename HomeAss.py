from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (Using Edge, can switch to Chrome)
driver = webdriver.Edge()
driver.maximize_window()

# Open the website
driver.get("https://www.saucedemo.com/")

# Wait for login elements
wait = WebDriverWait(driver, 10)

# Login
username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-test='username']")))
password = driver.find_element(By.XPATH, "//input[@data-test='password']")
login_button = driver.find_element(By.XPATH, "//input[@data-test='login-button']")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

# Wait for product page
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='inventory_list']")))

# Add item to cart
add_to_cart = driver.find_element(By.XPATH, "//button[contains(@id, 'add-to-cart')]")
add_to_cart.click()

# Go to cart
cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()

# Proceed to checkout
checkout = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']")))
checkout.click()

# Enter checkout details
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")

first_name.send_keys("Mobolaji")
last_name.send_keys("Major")
zip_code.send_keys("234")

# Continue checkout
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()

# Finish order
finish_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']")))
finish_button.click()

# Return to home
back_home_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='back-to-products']")))
back_home_button.click()

# Open menu and logout
menu_button = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu_button.click()

logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
logout_button.click()

# Close the browser
driver.quit()
