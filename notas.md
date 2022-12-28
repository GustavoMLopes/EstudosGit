# Notas de Git

## Comandos importantes
Resumo de alguns comandos que geralmente são mais utilizados no dia a dia.
### **git init**
Inicializa um repositório git na pasta atual.

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

Clicando [aqui](https://devhints.io/git-log) você encontra um site que resume o comando git log e mostra mais opções de parâmetros a serem utilizados por esse comando.
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

## O arquivo git ignore
O .gitignore serve para ignorar (dã) alguns os arquivos e diretórios inseridos nele na hora de commitá-los.

