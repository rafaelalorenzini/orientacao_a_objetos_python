<h2>Orientação a Objetos em Python </h2>
Este repositório será voltado ao estudo de orientação a objetos (POO) em Python. 

Dados e funções relacionadas são encapsilados em um mesmo elemento denominado objeto.
A comunicação entre objetos é feito pelo envio e recebimento de mensagens.

<h4> Objetivo:</h4>
Desenhar um conjunto de classes que descrevem objetos semelhantes e que atendam as tarefas requeridas. 

<h4> Vantagens:</h4>
<ul>
<li> Maior índice de reaproveitamento de código;</li>
<li> Maior facilidade de manutenção;</li>
<li> Maior confiabilidade no código;</li>
<li> Maior facilidade de gerenciamento do código;</li>
<li> Maior robustez.</li>
</ul>

<h3> Objeto:</h3>
É uma entidade que formaliza o modo pelo qual compreendemos algo no domínio do problema. 
É a entidade o mais próxima possível das entidades do mundo real. Os objetos são os substantivos do problema.
<h4> O objeto tem:</h4>
<ul> 
<li> Estado: é definido pelas propriedades que ele possui e os valores que lhe são atribuídos;</li>
<li> Comportamento: definido pela forma como ele reage, em termos de mudança de seu estado e o relacionamento com os outros objetos;</li>
<li> Identidade: propriedade pela qual ele se distingue dos outros;</li>
</ul>

<h3> Classe:</h3>
Representação de qualquer coisa que sea necessária modelar para solucionar o problema. Pode ser visto como uma caixa-preta,
que expõe somente alguns dados e algumas funções. Descreve um conjunto de objetos semelhantes, isto é, atributos e métodos que resumem as características comuns de vários objetos.
A classe é uma abstração que define o que os objetos são e como se comportam.
Ex: Aluno, Professor, Cliente, Vendedor, Livro.

<h3> Classe x Objeto</h3>
<b>A classe define a estrutura, o objeto é a instância da classe</b>, a qual lhe são atribuídos valores.
O objeto é uma entidade concreta com tempo e espaço de existência, quanto a classe é apenas uma abstração.

<h4> Membros da Classe:</h4>
<ul> 
<li> Atributos (variáveis/data members/propriedades): São os dados que o objeto armazenará. Ao criar um objeto, se criará também o espaço de memória para todos os atributos dele. O estado do objeto é representado pelos valores de seus atributos;</li>
<li> Métodos (Funções/function members/Serviços): São as operações que podem ser executadas pelos objetos. Definem o comportamento do objeto.
São equivalentes às funções utilizadas na programação estruturada (C, Fortran). A diferença principal é que tem acesso direto a todos os atributos do objeto.</li>
</ul>

<h3> Pricípios Básicos de Orientação a Objetos</h3>
<h4> Abstração:</h4>
Consiste em identificar artefatos do software na modelagem de um domínio, ignorando aspectos nçao relevantes e concentrando-se nos assuntos proncipais do problema.
Classes são abstrações de conceitos.

<h4> Encapsulamento:</h4>
Esconder os detalhes da implementação de um objeto. A ideia é que o sistema não deve depender de sua implementação interna e sim de sua interface.
Em outras palavras, capacidade de um objeto possuir uma parte privada, acessível somente através dos métodos definidos na sua interface pública. 
Ex: não queremos que outro objeto possa alterar a média do aluno manualmente. Para garantir o princípio de encapsulamento:
Um objeto <b> não deve manipular diretamente os atributos</b> de um outro objeto. A manipulação deve ser feita via métods.

<h4> Modularidade:</h4>
Dividir o sistema em partes bem definidas.

<h4> Relacionamentos:</h4>
Os objetos se relacionam entre si:
<ul> 
<li> <b> Associação:</b> qualquer verbo pode ser utilizado;</li>
<li> <b> Composição/Agregação:</b> Parte-de. Composição: um depende de outro. Agregação: um não depende da existência do outro;</li>
<li> <b> Herança (generalização/especialização):</b> É-um. Permite a hierarquização das classes. Uma classe mais especializada
(sub-classe) herda métodos e atributos de uma classe mais geram (super-classe) e pode sobrescrever o comportamento de uma super-classe;</li>
<li> <b> Polimorfismo:</b> Possibilita que métodos diferentes, que estão em diferentes níveis da hierarquia de classes tenham o mesmo nome e apresentem diferentes comportamentos.
As sub-classes podem redefinir os comportamentos herdados de maneira diferente.</li>
<li> <b> Modularidade:</b> Capacidade de criar um conjunto de módulos, cada um contendo classes com idependência de funcionamento;</li>
<li> <b> Mensagem:</b> Objetos se comunicam por meio do envio e recebimento de mensagem.</li>
</ul>

<h3> O desenvolvimento de softaware</h3>
Há apenas diretrizes gerais que quando usadas levam em geral a um bom resultado. Além disso,
o desenvolvimento certamente é influenciado pelo ambiente computacional no qual será desenvolvido. A
linguagem de programação e o ambiente ou plataforma na qual será desenvolvido o sistema podem decidir o
modo, a estratégia e os passos que serão usados.
Podemos dividir o desenvolvimento de software em 3 etapas, independente da linguagem, sistema operacional
ou plataforma de desenvolvimento que será usada:
<ol>
<li> O projeto</li>
<li> A implementação</li>
<li> Os testes e depuração</li>
</ol>
O projeto é a parte mais importante. Nele são definidas as classes e a relação entre elas. Os princípios que
devem orientar a definição das classes são:
<ul>
<li>Responsabilidade de cada uma delas – quais problemas elas resolve;</li>
<li>Independência entre elas – se uma precisa da outra e vice-versa é melhor que sejam a mesma;</li>
<li>Comportamento – quais as entradas (parâmetros) e saídas (resultados) desta classe.
</li>
</ul>
Na fase de implementação, embora cada programador tenha seu estilo, é importante garantir a
compatibilidade dentro da sua parte e entre as partes dos vários programadores do mesmo sistema.
A fase de testes e depuração é a que consome mais tempo. Muitas vezes, é durante a fase de testes que se
descobre problemas do projeto e temos que retroceder à fase de projeto para corrigir e garantir a integridade
do sistema.


<h3>Referências:</h3>
<ul>
<li><a href="https://www.ime.usp.br/~mms/mac1222s2019/3%20-%20PDA%20-%20Python%20-%20introducao%20a%20programa%C3%A7%C3%A3o%20orientada%20a%20objetos.pdf">3 - PDA - Python - introducao a programação orientada a objetos - IME - USP.</a> </li>
<li><a href="https://www.youtube.com/watch?v=yhEqroz32Nk&t=223s">Programação Orientada a Objetos – Aula 01 - Introdução à orientação a objetos - Univesp - Universidade Virtual do Estado de São Paulo.</a> </li>
</ul>

