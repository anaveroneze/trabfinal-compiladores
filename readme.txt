ELC 408 – Compiladores
Prof. Giovani Rubert Librelotto 
Aluna: Ana Luísa Veroneze Solórzano
-----------------------------
TRABALHO FINAL - Um Interpretador para Gramáticas Regulares

Este trabalho foi desenvolvido utilizando o Antlr para geração do Parser com suporte a Python.

O seguinte programa recebe como entrada a definição de uma Gramática e a valida como uma GRD,
apresentando erros. Em seguida, solicita ao usuário a entrada de uma palavra e a analisa, 
utilizando as produções definidas na gramática, verificando quais podem ser aplicadas para 
derivação da palavra, apresentando os  movimentos entre símbolos não-terminais. 
Caso a palavra de entrada consiga ser gerada por completo utilizando as produções, o programa 
a aceita. Caso contrário, o programa a rejeita e apresenta a localização do erro.

Para executar o programa em um ambiente Linux é necessário realizar as seguintes etapas:

------------------------------
1. Instalar Python (usada a versão 3.6.7), pip3 e pacote em Python para antlr:
$ apt-get install python3.6
$ apt install python3-pip
$ pip3 install antlr-python3-runtime

2. Compilar o programa gerando o parser para a GRD, com a flag "-visitor", que gera um arquivo .py 
com uma classe genérica para percorrer a árvore produzida pelo parser:
$ antlr4 -no-listener -visitor -Dlanguage=Python3 GramaticaRegular.g4

3. Executar o programa:
$ python main.py <arquivo-entrada>

-----------------------------
Observações:
- O caractere '#' é usado para representar vazio
- O caractere '$' é usado para representar final da palavra
- O <arquivo-entrada> deve conter a definição da gramática conforme exemplos de "entrada.txt" e "entrada2.txt"
- O arquivo GramaticaRegualr.g4, foi implementado para definir uma GRD, que será utilizado pelo Antlr para geração do parser.

-----------------------------
Erros tratados sobre a gramática:
- Produção com simbolos terminais não definidos na lista de terminais
- Produção com simbolos não terminais não definidos na lista de não terminais
- Produção com mais de um simbolo não terminal a esquerda
- Produção com simbolo não terminal a esquerda
- Simbolo duplicado na lista de terminais
- Simbolo duplicado na lista de não terminais
- Simbolo inicial não é um único elemento
- Simbolo inicial não declarado na lista de não terminais
- Simbolo inicial não está declarado