#!/usr/bin/env python
# coding: utf-8

# INSTRUÇÕES:
#
# - resolva os exercícios colocando suas respostas no lugar dos XXX
#
# - o XXX pode aparecer na linha de entrada (>>>) ou na saída
#
# - siga a ordem, pois em geral os primeiros são mais fáceis
#
# - se você executar os testes, o doctest vai entregar muitas respostas ao 
#   exibir a linha de saída esperada para cada teste; portanto deixe para 
#   executar depois de ter respondido a maioria dos testes
#
# - os XXX nas linhas de entrada são um desafio maior, porque o doctest
#   não vai entregar a resposta, e muitas vezes existem várias respostas
#   possíveis que produzem a mesma saída; procure fornecer a resposta mais
#   simples que satisfaça o exemplo
#
# - a opção REPORT_ONLY_FIRST_FAILURE faz aparecer apenas o primeiro 
#   exercício não resolvido no relatório de testes
#
# - se quiser deixar um exercício para depois, coloque o comentário 
#   "# doctest: +SKIP" na linha de entrada, por exemplo:
#
#   >>> 2 ** 100 # doctest: +SKIP
#   XXX

'''
1. Operações com sequências
-----------------------------

Para estes exercícios, usaremos estes exemplos de sequências::

    >>> v = [7, 2, 8, 3, 1, 5]     # list
    >>> s = 'brasileiro'           # str
    >>> t = ('uva', 'ave', 'ovo')  # tuple
    
1.1. Acessando elementos::

    >>> v[2]
    8
    >>> s[-1]
    'o'
    >>> t[0]
    'uva'
    >>> s[3]
    's'
    
1.2. Acesso pelo fim::

    >>> v[-1]
    5
    >>> t[-2]
    'ave'
    >>> s[-4]
    'e'
    
1.3. Fatiamento::

    >>> s[1:4]
    'ras'
    >>> v[:3]
    [7, 2, 8]
    >>> s[:-4]
    'brasil'
    >>> s[6:]
    'eiro'
    
1.4. Passos::

    >>> m = range(10)
    >>> m
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> m[1:6]
    [1, 2, 3, 4, 5]
    >>> m[1:6:2] # errei porque tinha esquecido dos espacos depois da virgula
    [1, 3, 5]
    >>> s[::2]
    'baier'
    >>> m[::-2]
    [9, 7, 5, 3, 1]
    >>> s[::-3]
    'oesb'
    
1.5. Operadores::

    >>> 8 in v
    True
    >>> 9 in v
    False
    >>> 'a' in t
    False
    >>> 'ave' in t
    True
    >>> 'a' in s
    True
    >>> 'y' not in s # errei, tinha esquecido das aspas
    True
    
1.6. Funções::
    
    >>> max(v)
    8
    >>> min(s)
    'a'
    >>> min(v[:4]) # errei tambem, nao tinha visto o 2 e botei o 3
    2
    >>> max(t) # esse eu nao sabia se ele comparava primeira letra ou num de characters, tive que conferir no interativo
    'uva'
    >>> len(v)                           
    6

'''

if __name__=='__main__':
    import doctest
    opcoes = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(optionflags = opcoes)

