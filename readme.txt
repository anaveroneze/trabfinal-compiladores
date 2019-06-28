pip3 install antlr-python3-runtime
antlr4 -no-listener -visitor -Dlanguage=Python3 GramaticaRegular.g4
usada a flag "-visitor" para gerar .py com uma classe genérica para percorrer a árvore produzida
pela GramaticaRegular

caractere '#' usado para representar vazio

ERROS DA GRAMÁTICA:
- Produção com simbolos terminais não definidos na lista de terminais
- Produção com simbolos não terminais não definidos na lista de não terminais
- Produção com mais de um simbolo não terminal a esquerda
- Produção com simbolo não terminal a esquerda
- Simbolo duplicado na lista de terminais
- Simbolo duplicado na lista de não terminais
- Simbolo inicial não é um único elemento
- Simbolo inicial não declarado na lista de não terminais
- Simbolo inicial não está declarado

TO-DO:
enviar mensagem de erro, mostrando a posição da palavra a ser testada em que houve o problema.