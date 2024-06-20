# Projeto de extensão curricular


> Este projeto é um projeto de extensão curricular com a finalidade de conectar instituições à pessoas que precisam de apoio e ajuda humanitária.

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:
> Front:
- [x] Definir paleta de cores do projeto
- [x] Página de cadastro de voluntarios na pagina Home
- [ ] Página de doação[Home]
- [ ] Adicionar campo de pix cnpj e QRCODE (ficticio) [Home]
- [ ] Adicionar campo API PAYPAL [Home]
- [ ] remover demais páginas que não são home, dashboard do usuário, e login



> Back:
- [ ] Login
- [ ] Formulario de cadastro de voluntarios
- [ ] Formulario de doação
- [ ] criar blueprint de rotas
      

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão equivalente ao Python 3.10 e o instalador pip:
```
python --version
pip --version
```
- Sistema Operacional Linux ou Windows

## ☕ Criando variavel de ambiente [OPCIONAL]:

Crie uma variavel de ambiente:

No Windows:
```
python -m venv venv
venv\Scripts\activate
```

No Linux:
```
python3 -m venv venv
source venv/bin/activate
```

## 🚀 Instalando projeto_extensao_curricular

Para instalar o projeto_extensao_curricular, siga estas etapas:

Instale as dependencias:

```
pip install -r requirements.txt
```

Crie um arquivo .env e cole o seguinte código:

```
CONNECT_DB=postgres://db_extensao_user:pHnvKZYUWR8go7wLr2qqrjNHWwTYsejS@dpg-cp6m3pnsc6pc73cjbj9g-a/db_extensao
SECRET_KEY=admin
```

## ☕ Usando projeto_extensao_curricular

Para usar projeto_extensao_curricular, siga estas etapas:

```
flask run --debug
```

Adicione comandos de execução e exemplos que você acha que os usuários acharão úteis. Fornece uma referência de opções para pontos de bônus!

## 📫 Contribuindo para projeto_extensao_curricular

Para contribuir com projeto_extensao_curricular, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin projeto_extensao_curricular / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).



## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
