# Python-Parser
### Tarefa dada:
    Construir uma ferramenta para encontrar e baixar títulos das notícias do dia, nos principais sites de notícias. 
 
### Tarefa Concluída:
    Um Trabalho em grupo desenvolvido em Python para Matéria de Programação Orientada a Objetos Avançada da Universidade Federal de São Carlos.


### Classe Open

Dentro da classe Open, temos uma função fun_soup que prepara a página inicial do site para coleta de noticías. 
A variável fp armazena o site contido na url do código.
Em seguida temos o html_doc, que lê o html em binário e então decodifica em UTF-8.
E por fim, retornamos o soup com todo o html da página inicial. 


### Classe Writer

A classe Writer recebe como parâmetro no seu construtor um objeto Open.
Dentro da classe Writer temos um construtor, que declara um atributo chamado Open que recebe o objeto supracitado. 
Temos dentro da classe em questão um método write. Ele recebe uma url e o nome de um parser (a ser implementado).
Dentro da função write, usamos a função open para criar um arquivo .csv com a data e o horário atual.
Então é feita uma verificação, onde entra o princípio Open-Closed.
Esta serve para tratar exceções quando sites futuros forem adicionados. 
Caso o parser selecionado seja soup e o site seja o Bol, criamos um csv writer com delimitador ;.
Cria um header dentro do mesmo, e então recebe o soup da método fun_soup do objeto Open.
Tendo estas informações na função write, percorremos cada elemento html que tenha a classe "thumb-title", que chamamos de título.
Após isso, retornamos ao pai desse título cuja classe seja "highlights-headline".
Então, procuramos pela categoria nos filhos e, por último, coletamos o link da notícia.
É escrito no arquivo csv, seguindo o padrão de "categoria, titulo, link".

<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

### Integrantes da Equipe

#### Carlos Andre Costa Santana, 773370
#### Lucas Mathaeus Pereira, 726561
#### Sona Eveningstar Jorge Candeu, 769802

#### Universidade Federal de São Carlos - UFSCar
##### São Carlos
###### 2020
