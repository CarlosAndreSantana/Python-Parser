# Python-Parser
### Tarefa dada:
    Construir   uma   ferramenta   para   encontrar   e   baixar   títulos   das   notícias   do   dia,   nos   principais   sites   de notícias. 
 
### Tarefa Concluída:
    Um Trabalho em  grupo desenvolvido em Pyton para Matéria de Programação Orientada Objetos Avançada da Universidade Federal de São Carlos.


### Class Open

###### Dentro da Class Open, temos uma função fun_sup que prepara a primeira pagina do site para coleta de noticías. 
###### O primeiro atributo é fp, que é usado para armazenar a url desejada
###### Em seguida temos html_doc que lê a url e decodifica em utf8
###### Após o uso, fp é fechado
###### E por fim, retornamos o sup com todo html da pagina ínical. 


### Class Writer

###### A Class Writer recebe o "Open"
###### Dentro da classe Writer temos uma função init, da qual estancia o Open para sua abertura. 
###### Temos Dentro da Class em questão uma Função Write, na qual recebe um site e um parser , que por padrão será sou.
###### Dentro da função Write, usamos a função open para pegar a data e o horário atual e criamos um arquivo csv ("csv.file").
###### Então é feito uma verificação, se o site é o do bol e o soup é o padrão ("parser").
###### Esta verificação serve para tratar exceções quando sites futuros forem adcionados. 
###### Dentro deste if, caso seja verdadeito, cria um writer par escrever no arquivo csv com um delimitador ( ";" ).
###### Cria um header dentro do mesmo, e então recebe o return da função fun_sup da Class Open.
###### Tendo estas informações na função Write, fazemos um para todo Title, ele vai buscar dentro do HTML um  class-thumb-title.
###### Após isso, vamos procurar usando laços de repetição o ("Pai de todos"), "highlights-headline".
###### Concluindo, depois de encontrar o pai de todos, teremos os titulos de nóticias principais.
###### É feito uma verificação, caso não tenha pai, é título principal. 
###### Descendo  a cadeia HTML, encontrámos os tópicos de cada título.
###### Escrevemos tudo no arquivo csv, seguindo o padrão, categoria, titulo, Url.


#### <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

### Integrantes da Equipe

#### Carlos Andre Costa Santana, 773370
#### Lucas Mathaeus Pereira, 726561
#### Sona Eveningstar Jorge Candeu, 769802

#### Ufscar - São Carlos - 2020

Println("FIM");

