#

<h1
    align="center">
    <img src="../poc/chatroom/bot.png"
         title="Bot"
         width="100"
         style="vertical-align:middle"
    >

    poc-bot

</h1>

## ✅ Sobre o projeto

Este projeto tem por objetivo realizar exercícios e demonstrar o uso dos recursos de um bot  para que com o conhecimento e domínio da técnica possa se fazer o uso em casos reais.

## ✅ Tecnologias

As seguintes ferramentas foram, as principais, usadas na construção do projeto:

- IA [Rasa](https://rasa.com/),
- Backend [Python](https://www.python.org/),
- Frontend [React](https://reactjs.org/)
- ...

## ✅ Começando

As instruções a seguir fornecerão uma cópia do projeto em sua máquina local para fins de desenvolvimento e teste.

Crie um diretório, conforme desejar, acesse o diretório e clone o projeto:

```shell
git clone https://github.com/antoniojpprado/poc-bot.git
```

### Pré-requisitos

É necessário que tenha instalado em sua máquina, os recursos listados abaixo. Se não tiver, instale-os, antes de continuar.

- [python](https://www.python.org/)
- [pip3](https://pypi.org/project/pip/)

### Instalando

Acesse o diretório que criou e crie um [ambiente virtual](https://docs.python.org/pt-br/3/library/venv.html) para o projeto:

```bash
python3 -m venv venv
```

Ative o ambiente virtual

```bash
source venv/bin/activate
```

Clone a projeto:

```bash
git clone https://github.com/antoniojpprado/poc-bot.git
```

Acesse o diretório do projeto:

```bash
cd poc-bot
```

Instale as dependências do projeto:

```bash
pip3 install -r requirements.txt
```

## ✅ Uso

### Ngrok

Caso queira que os bots rodem em um aplicativo de midia social, tal qual o [Telegram](https://telegram.org/), será necessário ativarmos o servidor web [ngrok](https://ngrok.com/), se não for o caso, pode saltar este tópico.
Para isto, ative o ngrok, com o seguinte comando:

```bash
ngrok http 5005
```

**Notas:**
- A porta sugerida neste comando, é a mesma porta utilizada para o bot HelpDesk, conforme acima instruído.

- Após estar rodando, faz-se necessário obtermos o endereço que o servidor ativou para o acesso. É o **https informado na última linha** dos dados da conexão, conforme abaixo ilustrado:

    ```bash
    Session Status                online
    Session Expired               Restart ngrok or upgrade: ngrok.com/upgrade
    Update                        update available (version 2.3.38, Ctrl-U to update)
    Version                       2.3.35
    Region                        United States(us)
    Web Interface                 http://127.0.0.1:4040
    Forwarding                    http://c4d51974bc0a.ngrok.io -> http://localhost:5005
    Forwarding                    https://c4d51974bc0a.ngrok.io -> http://localhost:5005
    ```

- Este endereço deve ser colocado nos arquivos ***credentials.yml*** de cada um dos bots, conforme abaixo demonstrado, na parâmetro ***webhook_url***
  
    ```yml
    telegram:
    access_token: "1600431576:AAGmtA9Wz06vTKckDQ39XgnvLb1Kr3yYx3A"
    verify: "pocrun_bot"
    webhook_url: "https://c4d51974bc0a.ngrok.io/webhooks/telegram/webhook"
    ```

### Bots

Teremos que executar os 3 bots, cada um em uma porta diferente, assim como as respectivas actions, também em portas diferentes.
Sendo o primeiro acesso, após a clonagem do projeto, faz-se necessário realizarmos o treinamentos dos bots.
Para isto, acessaremos cada um dos 3 diretórios dos Bots e os levantaremos individualmente.

### Bot HelpDesk

Estando no diretório raiz do projeto, acesse o diretório do bot Helpdesk, realize o treinamento e ative ele definindo uma porta específica:

```bash
cd helpdesk_bot
rasa train
rasa run -m models --enable-api --cors "*" --port 5005 --debug
```

Abra outro terminal, neste mesmo diretório e suba as actions:

```bash
rasa run actions --port 5055 --debug
```

### Bot Financeiro

Estando no diretório raiz do projeto, acesse o diretório do bot Financeiro, realize o treinamento e ative ele definindo uma porta específica:

```bash
cd fin_bot
rasa train
rasa run -m models --enable-api --cors "*" --port 5006 --debug
```

Abra outro terminal, neste mesmo diretório e suba as actions:

```bash
rasa run actions --port 5056 --debug
```

### Bot Administrativo

Estando no diretório raiz do projeto, acesse o diretório do bot Administrativo, realize o treinamento e ative ele definindo uma porta específica:

```bash
cd adm_bot
rasa train
rasa run -m models --enable-api --cors "*" --port 5007 --debug
```

Abra outro terminal, neste mesmo diretório e suba as actions:

```bash
rasa run actions --port 5057 --debug
```

### FrontEnd

Estando no diretório raiz do projeto, acesse o diretório do Frontend.

Sendo o primeiro acesso/execução, deve primeiramente iniciar o projeto React.

```bash
cd chatroom
yarn install
```

Em seguida, inicie o projeto:

```bash
yarn serve
```

## ✅ Contribuindo

- Faça um fork do projeto.
  
- Crie uma nova branch com as suas alterações:
  
  git checkout -b my-feature

- Salve as alterações e crie uma mensagem de commit contando o que você fez:
  
  git commit -m "feature: My new feature"

- Envie as suas alterações:
  
  git push origin my-feature

Caso tenha sugestões, <a href="mailto:antoniojpprado@gmail.com">entre em contato</a>.

## ✅ Licença

Todos os arquivos são cobertos pela GNU - Licença Pública Geral, consulte LICENSE.
