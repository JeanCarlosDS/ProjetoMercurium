# pip install selenium
# pip install webdriver-manager
# pip install packaging | Por motivos de bug do webdriver-manager, precisa instalar essa lib manualmente.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from os import system


def introducao():
    system('title TCC - Projeto Mercurium')
    system('color a')
    system('cls')
    print('-='*45,'\n')
    print(' '*35,'Projeto Mercurium\n')

    print(' '*24, '.@@@@@#           .  o@@@@@@@@@@@@@@@@@@')
    print(' '*24, '.@@@@@@*         @°  *@@@@@@@@@@@@@@@@@@')
    print(' '*24, '.@@@@@@@        O@.                  @@@')
    print(' '*24, '.@@@@@@@@      °@@°                  @@@')
    print(' '*24, '.@@@@@@@@@     @@@.       *@@@@@@@@@@@@@')
    print(' '*24, '.@@@@@@@@@*   @@@@°      O@@@@@@@@@@@@@@')
    print(' '*24, '.@@@@@#@@@@  #@@@@                @@@')
    print(' '*24, '.@@@@@ o@@@@*@@@@                .@@@')
    print(' '*24, '.@@@@@. @@@@@@@@*      *@@@@@@@@@@@@@')
    print(' '*24, '.@@@@@.  @@@@@@#      O@@@@@@@@@@@@@@')
    print(' '*24, '.@@@@@.  .@@@@@                @@@')
    print(' '*24, '.@@@@@.   o@@@                .@@@')
    print(' '*24, '.@@@@@.             *@@@@@@@@@@@@@')
    print(' '*24, '.@@@@@.            #@@@@@@@@@@@@@@')
    print(' '*24, '.@@@@@.                    °@@@')
    print(' '*24, '.@@@@@.                    °@@@')
    print(' '*24, '.@@@@@.       o@@@@@@@@@@@@@@@@')
    print(' '*24, '.@@@@@       #@@@@@@@@@@@@@@@@#\n')
    print(' '*4,'By: Jean Carlos, Sarah Messias, Fernando Oliveira, Nicolas Juliani e Adriel Ajala\n')
    print('-='*45)
    sleep(5)

def opcao_invalida():
    system('color 4')
    print('-='*30)
    print('Opção inválida! Tente novamente!\n')
    system('pause')

def acessar_site(Driver):
    Driver.get('https://empregacampinas.com.br/')
    Driver.switch_to.window(Driver.window_handles[1])
    Driver.close()
    Driver.switch_to.window(Driver.window_handles[0])
    Driver.maximize_window()

def remover_elemento(Driver, elementos):
    elementos = Driver.find_element(By.ID, elementos)
    Driver.execute_script('''
        var elementos = arguments[0];
        elementos.parentNode.removeChild(elementos);
        ''', elementos)

def pesquisar_vagas(Driver):
    classe_busca = Driver.find_element(By.CLASS_NAME, 'form-group')
    campo_comentario = classe_busca.find_element(By.CLASS_NAME, 'form-control')
    campo_comentario.click()
    campo_comentario.send_keys(vaga)

def agradecimentos():
    system('color b')
    system('cls')
    print('-='*30,'\n')
    print(' '*14,'Obrigado por usar o Mercurium!\n')
    print('-='*30)

    system('pause')


introducao()

while True:
    system('color a')
    system('cls')
    print('-='*30)
    vaga = input('Qual vaga deseja pesquisar? ').strip().capitalize()
    system('cls')

    if vaga in '':
        opcao_invalida()
        continue
    try:
        vaga = int(vaga)
    except:
        pass
    else:
        opcao_invalida()
        continue

    vaga_formatada = vaga.replace(' ','+')

    print('-='*30)
    quantidade = input('Para quantas vagas deseja pesquisar? ')
    system('cls')

    if quantidade in '':
        opcao_invalida()
        continue
    try:
        quantidade = int(quantidade)
    except:
        opcao_invalida()
        continue
    else:
        pass


    break

localizacao_adblock = r'C:\Users\aluno\Desktop\ProjetoMercurium\5.3.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + localizacao_adblock)

Driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
Driver.create_options()

system('cls')

acessar_site(Driver)


elementos = ('pum-2436769', 'pum-2416536', 'pum-2432453', 'pum-1657163', 'popmake-1657163', 'pum-content popmake-content', 'popup-maker-site-js-extra')
for i in range(len(elementos)):
    sleep(1)
    if len(Driver.find_elements(By.ID, elementos[i])) > 0:
        remover_elemento(Driver, elementos[i])
    else:
        print(f'O elemento {i} não pôde ser removido/encontrado.')


pesquisar_vagas(Driver)

sleep(1)
system('cls')

pagina = 1
vagas_por_pagina = 15 - 1 # →  Python começa a contar pelo 0.
# → While será responsável por permitir que o contador "i" seja resetado.
while True:
    i = 0
    quantidade -= vagas_por_pagina
    Driver.get(f'https://empregacampinas.com.br/page/{pagina}/?s={vaga_formatada}') # → Eu sei, eu sei... não precisa falar nada...
    sleep(3)
    
    # → Aqui será realizado o processo de coleta das informações das vagas.
    for i in range(quantidade + vagas_por_pagina):
        classe_vagas = Driver.find_element(By.CLASS_NAME, 'col-lg-8')
        vaga_emprego = classe_vagas.find_elements(By.CLASS_NAME, 'thumbnail')
        vaga_emprego[i].click()
        sleep(2)
        link = Driver.current_url
        classe_vaga_caracteristicas = Driver.find_element(By.CLASS_NAME, 'postie-post')
        campo_caracteristicas = classe_vaga_caracteristicas.find_elements(By.TAG_NAME, 'p')
        requisitos_vaga = campo_caracteristicas[3].text
        salario_vaga = campo_caracteristicas[4].text
        beneficios_vaga = campo_caracteristicas[5].text
        Driver.back()
        sleep(1)
        system('cls')
        

        # → Retorna em um arquivo o link para as vagas selecionadas junto às informações dela.
        with open(f'C:\\Users\\aluno\\Desktop\\ProjetoMercurium\\{vaga}.txt', 'a+', encoding='utf-8') as arquivo:
            arquivo.write('-='*10 + f'Vaga número {i + 1}° da {pagina}° página' + '-='*10 + f'\nLink: {link} \n\n{requisitos_vaga} \n\n{salario_vaga} \n\n{beneficios_vaga}' + '\n' + '-='*34 + '\n'*3)
        arquivo.close
        
        # → Verifica se existe uma próxima página e passa a seguinte se/quando necessário.
        if len(Driver.find_elements(By.CLASS_NAME, 'nextpostslink')) > 0:
            if i == vagas_por_pagina:
                pagina += 1
                break
            
    if quantidade < 1:
        break
    
    
Driver.close()

agradecimentos()
