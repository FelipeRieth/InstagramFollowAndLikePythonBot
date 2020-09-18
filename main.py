from selenium import webdriver
import time

#define as variaveis globais do webdriver e chromedriver
chrome = webdriver.ChromeOptions()
chrome.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
chrome_driver_binary = "C:/Users/Felipe/Desktop/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, options=chrome)

posts_quantity = 0
username = input("login: ")
password = input("senha: ")

def logar_no_instagram():
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)
    username_element = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
    username_element.send_keys(username)
    password_element = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
    password_element.send_keys(password)
    driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()

logar_no_instagram()

tags = []
n = int(input("Numero de tags: "))

for i in range(0, n):

    ele = input("Tag: ")

    tags.append(ele)  # adding the element




def exibir_quantidade_de_posts():
    posts_quantity = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span")
    print("Este perfil possui: ",posts_quantity.text, " posts")


def seguir_perfil():
    try:
        follow_button = driver.find_element_by_xpath("//button[@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']")
    except:
        print("Voce ja esta seguindo esta conta")
    else:
        if (follow_button.text == "Seguir" or follow_button.text == "Seguir de volta"):
            follow_button.click()



def curtir_post(postid):

    time.sleep(1)
    posts[postid].click()
    time.sleep(2)
    botao = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
    botao.click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()



time.sleep(2)
#
for j in range(0,len(tags)):
    driver.get("https://www.instagram.com/" + tags[j])
    time.sleep(1)
    exibir_quantidade_de_posts()
    seguir_perfil()
    time.sleep(0.5)
    posts = driver.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")
    time.sleep(0.5)
    if(len(posts) > 10):
        for i in range(0, 10):
            curtir_post(i)
    else:
        for i in range(0, len(posts)):
            curtir_post(i)