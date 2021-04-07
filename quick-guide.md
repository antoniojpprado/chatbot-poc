#

<h1
    align="center">
    <img src="bot.png"
         title="Bot"
         width="100"
         style="vertical-align:middle"
    >

    Guia Rápido

</h1>


## ✅ Sobre

Este documento é uma guia rápido, para a implementação de alguns recursos, a seguir listados:
<br>
<br>

## ✅ Na transferência de canais de atendimento

- Os canais a serem acessados possuem suas configurações nas **actions**:
  - **handoff_config.yml** - Lista dos canais disponíveis.
  - **actions**
    - *ActionHandoffOptions* - Classe que apresenta as opções dos canais disponíveis.
    - *ActionHandoff* - Classe que realiza a transferência entre os canais.
- Em **rules.yml** temos as storys para quando ocorre uma transferência de canal, apresentação das opções e outras, tal como:
  - rule: A intencao de transferencia aciona a saudacao
  - rule: Provide handoff options
  - rule: Execute handoff
<br>
<br>

## ✅ Na utilização de formulário

- No **domain.yml** devem ser declaradas as seguints cláusulas:
  
  - **slots**: "campos"	dos formulários ou "variaveis" que irão armazenar as informações prestadas.
  
    Aqui são declarados os seus tipos e outras características dos "campos".
    
    Os respectivos nomes devem estar previamente declarados em *entities*.

  - **forms**: nesta cláusula são declarados os formulários e os "campos" que o compõe além de outros detalhes respectivos.
  
  - **actions**: se for o caso de haver validação dos dados informados, deve ser informado aqui o nome da action que realiza a validação.
  
- Em **actions.py** pode ser criado uma classe, tal como ***ValidateRegisterDatasForm***, para validar as informações do formulário, conforme são inputadas.
  
- Em **nlu.yml** deve ser criado uma intent, tal como ***request_register_datas***, com exemplos dos dados a serem informados e a sua ligação com os respectivos **slots**. A intent criada deve ser declarada em domain.yml na cláusula intents.
  
- Em **rules.yml** são criadas as stories para lidar com o submit e os informes do formulário, tal como em:
  - rule: submit form
  - rule: Inform datas
<br>
<br>

## ✅ Para integrar com mídias sociais
- Devem ser informados, no arquivo ***credentials.yml***, os dados necessários para autenticação e acesso ao canal desejado.


- Para o bot acessar uma mídia social, deve estar utlizando um servidor web. Localmente pode-se utlizar o **ngrok**. Veja no README os detalhes sobre sua ativação e aonde postar sua url.
<br>
<br>

## ✅ Fontes de referência:

- [Rasa docs](https://rasa.com/docs/)
