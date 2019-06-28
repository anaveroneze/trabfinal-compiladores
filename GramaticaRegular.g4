grammar GramaticaRegular;

// regra para definir a definição formal da GR 
gram: 'V ' naoterminais 'T ' terminais 'P ' producoes 'S ' inicial EOF;

// definição símbolos possíveis terminais e não terminais
VAR : [A-Z]+;
VAR_T : [a-z]+;
VAZIO : '#' ;

// inicio das funções referentes a definição
naoterminais
        : '= [' simbolos ']';

terminais
        : '= [' simboloster ']';

simbolos
        : VAR ', ' simbolos
        | VAR
        ;

simboloster
        : VAR_T ', ' simboloster
        | VAR_T
        ;

inicial 
        : '= ' VAR;

producoes
        : '= [' producao ']';

producao
        : '(' VAR '>' transicao ')'
        | '(' VAR '>' transicao '), ' producao
        ;

// validação para ser uma gramática linear a direita (GLD)
transicao
        : VAR_T VAR '|' transicao
        | VAR_T VAR
        | VAZIO
        ;

WS  :   [ \t\n\r]+ -> skip ;