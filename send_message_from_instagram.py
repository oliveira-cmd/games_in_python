# importando modulos do python para usar no codigo
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# username no instagram de quem vai receber mensagem
user = ['rafaelwilhiam']
message_ = ("Mensagem enviada de um bot em python por Gabriel Oliveira")


class bot:
    def __init__(self, username, password, user, message):
        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/direct/inbox/'
        self.bot = driver
        self.login()

    def login(self):
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)

        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        # respondendo o primeiro pop-up
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(3)

        # respondendo o segundo pop-up
        self.bot.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(5)

        # clicando no botão do direct no instagram
        # self.bot.find_element_by_xpath('//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
        # time.sleep(3)

        # clicando no botão de procurar usuario no inbox
        self.bot.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]').click()
        time.sleep(5)
        for i in user:

            # inserindo o username na barra de busca
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
            time.sleep(2)

            # clicando no username
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div').click()
            time.sleep(2)

            # clicando em 'Avançar'
            self.bot.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[1]/div/div[2]/div/button/div').click()
            time.sleep(2)

            # clicando no input para inserir a mensagem
            send = self.bot.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

            # inserindo a mensagem
            send.send_keys(self.message)
            time.sleep(1)

            # enviando a mensagem
            send.send_keys(Keys.RETURN)
            time.sleep(2)

            # clicando na opção de procurar usuario no inbox novamente
            self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(2)
            if i == 'rafaelwilhiam':
                break


def init():
    # chamando a função 'bot' junto com os parametros
    bot('gabriel____2.1', '13040077', user, message_)

    # Mensagem exibida quando o script finalizar
    input('Mensagens Enviadas para {}'.format(user))


# Chamando a função Init
init()
