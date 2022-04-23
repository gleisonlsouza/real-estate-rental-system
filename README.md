# AP - Aluguel de Pobre

<p align="center">Real estate rental system / Sistema de aluguel de imóveis</p>
<p align="center">
<a href='#english'>English</a>
-
<a href='#português'>Português</a>
</p>


# English

## Intro

<p>Hello, my name is Gleison Souza, I'm 35 years old, I'm from Duque de Caxias, Rio de Janeiro. It is with great pleasure that I share with you my property rental system.

To see the system working <a href="http://alugueldepobre.com.br/" target="_blank"> click here.</a>
</p>

## Index:

* [About](#about)
* [Features](#features)
    * [Autocomplete](#autocomplete)
    * [User register](#user-register)
    * [User Login](#user-login)
    * [Password recovery](#password-recovery)
    * [Search by houses](#search-by-houses)
    * [Ad details](#ad-details)
    * [User panel](#user-panel)
* [Installation guide](#instalattion-guide)
* [Tools used](#tools-used)


<br>

# About
<p>The idea of Aluguel de Pobre came up after noticing the typical questions asked on social networks looking for
                 cheap real estate in middle-class neighborhoods.
                 Most rental sites are geared towards properly regularized properties, properties with
                 long months contract, but we middle class people are used to
                 rent a house with a "mouth contract" or as it is also known as a "drawer contract".
</p>
<p>But what about the name Aluguel de Pobre?</p>
<p>The site's name was strategically thought to cause a buzz, it's easy to stick, it's suggestive,
     can become a topic in the circle of friends even if I like "just kidding", but that with
     sure when thinking about renting a good and cheap house, the name Aluguel de Pobre will soon come to mind, this
     facilitate "word of mouth" dissemination.
</p>

<p>We know that a popular rental is usually dealt with directly with the owner (landlord) and that there is no
     a lot of bureaucracy, some charge a deposit which is a type of guarantee in case there is
     any damage to the residence after the tenant leaves, or if the tenant becomes unemployed,
     or if you decide to leave the property, so you will still have a few months already paid, in addition to
     we know that there are no rental sites that accept houses in communities, on our platform it is
     possible you register a property and inform the name of the community. Putting all these together
     questions I decided to develop this simple and effective platform that will help both those who are looking for
     cheap rent as those who are looking to advertise their properties.
</p>

<br>

# Features

## Autocomplete

<p>
The system has an autocomplete function that searches for information directly from the database
</p>

<p align="center">
    <img src="github/autocomplete.gif" />
</p>

<br>

## User register

### What's in the registry system

* Field validation
* Terms of use and privacy
* Google Recaptcha

<p align="center">
    <img src="github/register.gif" />
</p>

<br>

## User login

### What's in the login system

* Field validation
* Google Recaptcha

<p align="center">
    <img src="github/login.gif" />
</p>

<br>

## Password recovery

### What's in the pass recovery system

* Field validation
* Send link to email
* Google Recaptcha

<p align="center">
    <img src="github/passrecovery.gif" />
</p>

<br>

## Search by houses

### What's in the search system

<p>The initial search is simplified, after the first search the user can apply several filters to the search.</p>

<p>What filters are available?</p>

* Location
    * State
    * City
    * District
* Price range
    * Min
    * Max
* Additional fees
    * Deposit
    * Property tax
    * Fire tax
    * Pay for water
    * Pay for light
* Property dependencies
    * Number of bedrooms
    * Number of bathrooms
    * Number of parking spaces
    * If the house is independent
* Property restrictions
    * Accept pet
    * accept children
* Other information
    * Is it in community?
    * House roof type

<p align="center">
    <img src="github/search.gif" />
</p>

<br>

## Ad details

### What's in the detail system

* Full description of the property
* Larger size photos
* Field to send message to owner

<p align="center">
    <img src="github/addetail.gif" />
</p>

## User panel

### What's in the panel system

* My messages
    * Individual messages
    * All messages
* My properties
    * Show all
    * Add new
* Personal data
    * Edit
* Login data
    * Edit

<p align="center">
    <img src="github/userpanel.gif" />
</p>

<br>

## Installation guide

```python

# Download the project

# Extract the project to a folder

# Open the command prompt and go to the project folder

# Create your virtual environment

python -m venv venv

# Active your virtual environment

venv\Scripts\activate

# Install the requirements.txt

pip install -r requirements.txt

# Create database with migrate

py manage.py migrate

# !! VERY IMPORTANT !!
# Configure .env
# Copy .env-exemple and rename to .env
# Open .env 
# Fill in all required fields as requested

# Create your super user

python manage.py createsuperuser

# Collect static files

python manage.py collectstatic

# Run the projetct 

python manage.py runserver

``` 

<br>

## Tools used

<table  border="1">
<tr>
    <th> Name </th>
    <th> Version </th>    
    <th> Link </th>    
</tr>
<tr>
    <td> Python </td>
    <td> 3.10.2 </td>
    <td><a href="https://www.python.org/downloads/release/python-3102/" target="_blank" >View more</a></td>
</tr>
<tr>
    <td> Django </td>
    <td> 4.0.3 </td>
    <td> <a href="https://docs.djangoproject.com/en/4.0/releases/4.0.3/" target="_blank" >View more</a> </td>
</tr>
<tr>
    <td> BootStrap </td>
    <td> 5.1.0 </td>
    <td> <a href="https://getbootstrap.com/docs/5.1/getting-started/introduction/" target="_blank" >View more</a> </td>
</tr>
<tr>
    <td> HTML </td>
    <td> 5 </td>
    <td> - </td>
</tr>
<tr>
    <td> CSS </td>
    <td> 3 </td>
    <td> - </td>
</tr>
<tr>
    <td> JavaScript </td>
    <td> - </td>
    <td> - </td>
</tr>
<tr>
    <td> VScode </td>
    <td> 1.66.2 </td>
    <td> <a href="https://code.visualstudio.com/download" target="_blank" >View more</a>  </td>
</tr>
</table>

<br>
<br>
<br>

# Português

## Intro

<p>Olá, meu nome é Gleison Souza, tenho 35 anos, sou de Duque de Caxias, Rio de Janeiro. É com muito prazer que compartilho com vocês o meu sistema de locção de imóveis.

Para ver o sistema funcionando <a href="http://alugueldepobre.com.br/" target="_blank"> click aqui.</a>
</p>

## Índice:

* [Sobre](#sobre)
* [Recursos](#recursos)
    * [Autocompletar](#autocompletar)
    * [Cadastro de usuário](#cadastro-de-usuário)
    * [Login](#login)
    * [Recuperar senha](#recuperar-senha)
    * [Pesquise por casas](#pesquise-por-casas)
    * [Detalhes do anúncio](#detalhes-do-anúncio)
    * [Painel do usuário](#painel-do-usuário)
* [Guia de instalação](#guia-de-instalação)
* [Ferramentas utilizadas](#ferramentas-utilizadas)


<br>

# Sobre
<p>A idéia do Aluguel de Pobre surgiu após notar as perguntas típicas feitas em redes sociais a procura de
imóveis baratos em bairros de classe média.
A maioria dos sites de alugueis são voltados para imóveis devidamente regularizados, imóveis com
contrato de longos meses, porém nós da classe média estamos acostumados a
alugar casa com contrato de "boca" ou como também é conhecido "contrato de gaveta".
</p>

<p>Mas e o nome Aluguel de Pobre?</p>
<p>O nome do site foi estrategicamente pensado para causar um burburinho, é fácil de fixar, é sugestivo,
pode virar assunto na roda de amigos ainda que como "zueira", mas que com
certeza ao pensarem em alugar uma casa boa e barata logo virá em mente o nome Aluguel de Pobre, isso
facilitará a divulgação boca a boca.</p>

<p>Sabemos que um aluguel popular geralmente é tratado direto com o proprietário (senhorio) e que não tem lá
muita burocracia, alguns cobram um depósito que é um tipo de garantia caso haja
alguma avaria na residência após a saída do inquilino, ou se por ventura o inquilino ficar desempregado,
ou se resolver deixar o imóvel, assim ainda terá alguns meses já pagos, além disso
sabemos que não existe sites de alugueis que aceitem casas em comunidades, já em nossa plataforma é
possível você cadastrar um imóvel e informar o nome da comunidade. Juntando todos esses
quesitos resolvi desenvolver essa plataforma simples e eficaz que ajudará tanto quem está a procurar de
aluguel barato quanto quem está a procura de divulgar seus imóveis.
</p>

<br>

# Recursos

## Autocompletar

<p>
O sistema possui uma função de autocompletar que busca informações diretamente do banco de dados
</p>

<p align="center">
    <img src="github/autocomplete.gif" />
</p>

<br>

## Cadastro de usuário

### O que há no sistema de registro

* Validação de campo
* Termos de uso e privacidade
* Google Recaptcha

<p align="center">
    <img src="github/register.gif" />
</p>

<br>

## Login

### O que há no sistema de login

* Validação de campo
* Google Recaptcha

<p align="center">
    <img src="github/login.gif" />
</p>

<br>

## Recuperar senha

### O que há no sistema de recuperação de senha

* Validação de campo
* Enviar link para e-mail
* Google Recaptcha

<p align="center">
    <img src="github/passrecovery.gif" />
</p>

<br>

## Pesquise por casas

### O que há no sistema de pesquisa

<p>A pesquisa inicial é simplificada, após a primeira pesquisa o usuário pode aplicar vários filtros à pesquisa.</p>

<p>Quais filtros estão disponíveis?</p>

* Localização
     * Estado
     * Cidade
     * Bairro
* Faixa de preço
     * Mín.
     * Máx.
* Taxas adicionais
     * Depósito
     * IPTU
     * Taxa de incêndio
     * Paga água
     * Paga luz
* Dependências do imóvel
     * Numero de quartos
     * Número de banheiros
     * Número de vagas na garagem
     * Se a casa é independente
* Restrições do imóvel
     * Aceita animal de estimação
     * aceita crianças
* Outra informação
     * É na comunidade?
     * Tipo de telhado da casa

<p align="center">
    <img src="github/search.gif" />
</p>

<br>

## Detalhes do anúncio

### O que está no sistema de detalhes

* Descrição completa do imóvel
* Fotos em tamanho maior
* Campo para enviar mensagem ao proprietário

<p align="center">
    <img src="github/addetail.gif" />
</p>

## Painel do usuário

### O que há no sistema de painel

* Minhas mensagens
     * Mensagens individuais
     * Todas as mensagens
* Meus imóveis
     * Exibir todos
     * Adicionar novo
* Dados pessoais
     * Editar
*Dados login
     * Editar

<p align="center">
    <img src="github/userpanel.gif" />
</p>

<br>

## Guia de instalação

```python

# Faça download do projeto

# Extraia o projeto para uma pasta

# Abra o prompt de comando e vá para pasta do projeto

# Crie um ambiente virtual

python -m venv venv

# Ative seu ambiente virtual

venv\Scripts\activate

# Instale os requerimentos 

pip install -r requirements.txt

# Faça o migrate para criar a dabatase

py manage.py migrate

# !! MUITO IMPORTANTE !!
# Configure .env
# Copie .env-exemple e renomeie para .env
# Abra .env 
# Preencha os campos conforme solicitado

# Crie um super user

python manage.py createsuperuser

# Colete os arquivos estáticos

python manage.py collectstatic

# Execute o projeto 

python manage.py runserver

``` 

<br>

## Ferramentas utilizadas

<table  border="1">
<tr>
    <th> Nome </th>
    <th> Versão </th>    
    <th> Link </th>    
</tr>
<tr>
    <td> Python </td>
    <td> 3.10.2 </td>
    <td><a href="https://www.python.org/downloads/release/python-3102/" target="_blank" >Ver mais</a></td>
</tr>
<tr>
    <td> Django </td>
    <td> 4.0.3 </td>
    <td> <a href="https://docs.djangoproject.com/en/4.0/releases/4.0.3/" target="_blank" >Ver mais</a> </td>
</tr>
<tr>
    <td> BootStrap </td>
    <td> 5.1.0 </td>
    <td> <a href="https://getbootstrap.com/docs/5.1/getting-started/introduction/" target="_blank" >Ver mais</a> </td>
</tr>
<tr>
    <td> HTML </td>
    <td> 5 </td>
    <td> - </td>
</tr>
<tr>
    <td> CSS </td>
    <td> 3 </td>
    <td> - </td>
</tr>
<tr>
    <td> JavaScript </td>
    <td> - </td>
    <td> - </td>
</tr>
<tr>
    <td> VScode </td>
    <td> 1.66.2 </td>
    <td> <a href="https://code.visualstudio.com/download" target="_blank" >Ver mais</a>  </td>
</tr>
</table>

