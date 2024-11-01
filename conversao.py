#!/usr/bin/env python
# coding: utf-8

# In[131]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# In[132]:


navegador = webdriver.Chrome()


# In[133]:


navegador.get('https://www.google.com.br')


# In[134]:


campo_busca = navegador.find_element(By.NAME, 'q')


# In[135]:


campo_busca.send_keys('Banco Central do Brasil')


# In[136]:


time.sleep(5)


# In[137]:


botao = WebDriverWait(navegador, 5).until( EC.element_to_be_clickable((By.NAME, 'btnK')))
botao.click()


# In[138]:


navegador.find_element(By.CLASS_NAME, 'LC20lb').click()


# In[139]:


time.sleep(5)


# In[140]:


try:
        cookie_button = WebDriverWait(navegador, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Aceitar') or contains(text(),'Prosseguir')]"))
        )
        cookie_button.click()
        print("Notificação de cookies fechada.")
except Exception as e:
        print("Não foi possível fechar a notificação de cookies ou ela não apareceu.")


# In[141]:


time.sleep(5)


# In[142]:


navegador.get("https://www.bcb.gov.br/conversao")


# In[143]:


time.sleep(5)


# In[144]:


valor_a_converter = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="valorBRL"]'))
    )
valor_a_converter.send_keys('10000')
    


# In[145]:


time.sleep(5)


# In[146]:


moeda_origem = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, 'button-converter-de'))
    )
moeda_origem.click()


# In[147]:


time.sleep(5)


# In[148]:


opcao_real = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Real (BRL)')]"))
    )
opcao_real.click()


# In[149]:


moeda_destino = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, 'button-converter-para'))
    )
moeda_destino.click()


# In[150]:


time.sleep(5)


# In[151]:


opcao_dolar = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Dólar dos Estados Unidos (USD)')]"))
    )
opcao_dolar.click()


# In[152]:


botao_converter = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='refresh']"))
    )
botao_converter.click()


# In[153]:


time.sleep(5)


# In[154]:


resultado_elemento = WebDriverWait(navegador, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'card-body') and contains(., 'Resultado da conversão:')]"))
)



# In[ ]:


print(f"RESULTADO DA CONVERSÃO: {resultado_elemento.text}")


# In[156]:


resultado_elemento.screenshot('elemento.png')


# In[157]:


navegador.get_screenshot_as_file('captura_tela.png')


# In[158]:


navegador.quit()
    

