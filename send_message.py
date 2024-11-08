import pandas as pd
import pywhatkit as kit
import time

clientes_df = pd.read_excel('celulares_python.xlsx')

# Mensagem padrão com placeholders para personalização
mensagem_template = """
Olá,

Meu nome é Carlos Nascimento, da Nexus Solutions, e ajudamos empresas a otimizar processos e reduzir custos com soluções personalizadas de automação.

Já ajudamos muitas empresas do setor de alimentos e ajudamos elas a melhorar seus processos ligados a tecnologia e tarefas repetitivas, e acredito que a Nexus pode ajudar a melhorar sua eficiência e reduzir os custos operacionais.

Gostaria de oferecer uma análise gratuita para identificar áreas em que a automação pode beneficiar o seu negócio. Posso te explicar como nossos serviços funcionam em uma breve conversa?

Agradeço o seu tempo e fico à disposição para conversarmos!

Segue o link do nosso site se quiser você conhecer mais sobre o nosso trabalho:
https://www.nexus-solutions.tech/

Atenciosamente,  
Carlos Nascimento  
Nexus Solutions
"""

# Função para enviar mensagens personalizadas
def enviar_mensagens():
    for index, cliente in clientes_df.iterrows():
        celular = str(cliente['celular'])  # Certifique-se de que o nome da coluna está correto e converta para string
        if not celular.startswith('+'):
            celular = '+' + celular  # Adiciona o '+' se não estiver presente
        
        # Personalizar a mensagem se necessário
        mensagem = mensagem_template
        
        try:
            # Enviar mensagem via WhatsApp
            kit.sendwhatmsg_instantly(celular, mensagem, 5, True)
            print(f"Mensagem enviada para ({celular})")
            time.sleep(2)  # Pausa para evitar problemas de sobrecarga
        except Exception as e:
            print(f"Erro ao enviar mensagem para {celular}: {str(e)}")

# Executar a função
enviar_mensagens()
