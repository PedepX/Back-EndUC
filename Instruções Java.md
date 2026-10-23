# Java - Anatomia do Código

## Arquivo com extensão `.java`

- Um arquivo Java tem extensão `.java`.
- A JVM executa o arquivo `.class`.

## Máquina Virtual Java (JVM)

- A JVM é responsável por executar o bytecode.
- O código Java é compilado para bytecode e depois executado pela JVM.

## Algoritmo

- Algoritmo = ações executadas em sequência.
- Ordem de execução: o programa é executado em ordem, linha por linha.

## Estrutura básica de uma classe Java

```java
public class BemVindo {
    public static void main(String[] args) {
        System.out.println("Bem Vindo à Programação em Java");
        System.out.println("Bem Vindo\"%s\"",args[1]);
    }
}
```

## Tipos primitivos

- `%d` → inteiro
- `%f` → real (6 casas por padrão)
- `%s` → String
- `%c` → caractere
- `%b` → booleano
- `%n` → nova linha

### Exemplos de tipos

- `byte` → inteiro (`-128 a 127`)
- `short` → inteiro (`-32.768 a 32.767`)
- `int` → inteiro (`± 2,1 bilhõ es`)
- `long` → inteiro (`± 9,2 x 10^18`)
- `float` → real (`~ 7 dígitos`)
- `double` → real (`~ 15 dígitos`)
- `char` → caractere
- `boolean` → booleano

## Operadores aritméticos

- `+` soma
- `-` subtração
- `*` multiplicação
- `/` divisão
- `%` módulo

## Conversão de tipos (cast)

```java
cast -> (double) soma / qt
```

- Serve para converter o valor de uma variável antes da operação.

## Sequência e formatação

- `\n` → nova linha
- `\t` → tabulação horizontal
- `\"` → aspas dentro da String
- `"` → aspas no texto da String

## Leitura de dados do teclado

Para ler entradas do usuário em Java, usamos a classe `Scanner`:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite algo:");
        String texto = sc.nextLine();
        System.out.println("Você digitou: " + texto);
    }
}
```

- `import java.util.Scanner;` → importa a classe para ler dados.
- `Scanner sc = new Scanner(System.in);` → cria o objeto leitor do teclado.
- `System.in` → representa a entrada do teclado.

## Observações gerais

- O programa começa na função `main`.
- A linguagem Java é orientada a objetos.
- O bytecode é gerado pela compilação do código Java e executado pela JVM.

## Resumo

Java é uma linguagem orientada a objetos, onde o código é escrito em arquivos `.java`, compilado para `.class` e executado pela JVM. A estrutura básica de um programa tem uma classe e um método `main`, e os tipos primitivos incluem `int`, `float`, `double`, `char`, `boolean`, entre outros.
