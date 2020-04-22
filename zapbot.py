
     
     
      #<span dir="auto" title="Bloco do eu sozinho" class="_1wjpf _3NFp9 _3FXB1">Bloco do eu sozinho</span>
      # <div tabindex="-1" class="_1Plpp"> 
      # <span data-icon="send" class=""> 

import time
from selenium import webdriver

class WhatsappBot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "Oi eu sou o Jeremias, Bot da Lari tchau :)"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["Bloco do eu sozinho"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
            self.driver.get('https://web.whatsapp.com')
            time.sleep(5)

           
            for grupo_ou_pessoa in self.grupos_ou_pessoas:
              campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element_by_class_name('_1Plpp')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot= WhatsappBot()
bot.EnviarMensagens()