# Notas de Git :octocat:

## Comandos importantes
Resumo de alguns comandos que geralmente são mais utilizados no dia a dia.
### **git init**
Inicializa um repositório git na pasta atual.

### **git clone**
Puxa todos os dados commitados no repositório contido na url passada por parâmetro.
```sh
git clone url_do_repositório
```

### **git status**
Mostra o estado atual dos arquivos no repositório que estamos trabalhando. 

### **git log**
Mostra informações mais detalhadas sobre os commits feitos. Como por exemplo o nome do autor, a data do commit
e o código identificador do commit. Alguns exemplos de parâmetros para o comando git log:

Mostra o log simplificado:
```sh
git log --oneline
```

Mostra as alterações
```sh
git log -p
```
Mostra as alterações com uma filtragem de informações mostrando o hash e a mensagem do commit:
```sh
git log --pretty="format:%h %s"
```

Clicando [aqui](https://devhints.io/git-log) você encontra um site que resume o comando git log e mostra mais
opções de parâmetros a serem utilizados por esse comando.
### **git add**
Adiciona arquivos para serem monitorados pelo git. O exemplo abaixo adiciona todos os arquivos do diretório
atual.
```sh
git add .
```

### **git commit** 
Cria um "checkpoint" das nossas alterações após serem adicionados com o git add. Deve ser acompanhado pela 
flag ``-m`` para informar o que foi commitado. Um exemplo desse comando pode ser visto abaixo:

```sh
git commit -m "Initial Commit"
```
### **git remote**
Lista todos os repositórios remotoso que o projeto possui. Podemos adicionar repositórios a partir do comando ```git remote add```.

### **git push**
Envia as modificações para o repositório remoto.

### **git pull**
Recebe as modificações contidas no repositório remoto para o local.


## O arquivo git ignore
O .gitignore serve para ignorar (dã) alguns os arquivos e diretórios inseridos nele na hora de commitá-los. 
O exemplo abaixo mostra o .gitignore deste repositório:

```
me_ignore.py
*.java
/pasta_2
```
Estão sendo ignorados todos os arquivos com extensão ``.java``, todos os arquivos contidos em pasta_2 e
o arquivo ``me_ignore.py`` na raiz do projeto e o arquivo ``me_ignore_tambem.c`` na pasta_1.

## Branches
Branches são ramificações de um estado de trabalho, assim conseguimos diminuir conflitos. Podemos criar
uma branch a partir do comando ``git branch nome_da_branch`` e mudar para ela a partir do comando
``git checkout``. Clicando [aqui](http://git-school.github.io/visualizing-git/) você encontra uma aplicação
que faz a visualização de como as branches funcionam. 

O seguinte comando permite criar a branch e já mudar para ela:
```sh
git checkout -b nome_da_branch 
```

## Issues
Issues são sessões utilizadas para indicar que há algum problema, no entanto, hoje em dia 
existem outras diversas utilizades interessantes para essa feature. Podemos criar um [kambam](https://rockcontent.com/br/blog/kanban/)
ou uma to-do list por exemplo.Para resolver issues usuários de fora do projeto podemo utilizar ``pull requests``, ou seja, pedidos 
de alteração no código. Para isso o usuário realiza um ``fork``, altera o projeto e faz o ``pull request``.