## Texto
We see three critical differences between programming and software engineering: time, scale, and the trade-offs at play. On a software engineering project, engineers need to be more concerned with the passage of time and the eventual need for change. In a software engineering organization, we need to be more concerned about scale and efficiency, both for the software we produce as well as for the organization that is producing it. Finally, as software engineers, we are asked to make more complex decisions with higher-stakes outcomes, often based on imprecise estimates of time and growth.

Within Google, we sometimes say, “Software engineering is programming integrated over time.” Programming is certainly a significant part of software engineering: after all, programming is how you generate new software in the first place. If you accept this distinction, it also becomes clear that we might need to delineate between programming tasks (development) and software engineering tasks (development, modification, maintenance). The addition of time adds an important new dimension to programming. Cubes aren’t squares, distance isn’t velocity. Software engineering isn’t programming.

## Comentário 
Engenheiros de software devem se preocupar em criar códigos que atendam as necessidades atuais e prever as necessidades futuras de um problema, levando em consideração as limitações da ferramenta ou plataforma utilizadas, dessa maneira criando códigos com a capacidade de serem atualizados conforme o escopo do projeto de modifica.
Sendo assim, engenharia de software é programação levando em consideração as perdas e os ganhos das opções disponeveis, principalmente em relação a requisitos não funcionais.

### Comparação de requisitos não funcionais (trade-offs) de 3 sistemas operacionais:
- As vantagens do MacOS estão atreladas ao fato de que o hardware da Apple está muito bem integrado ao sistema operacional, dessa maneira ele é mais optimizado e tem melhor desempenho. Porém, devido a isso, ele é menos flexível no quesito de personalização e é menos compatível com dispositivos não Apple.
- O Windows é compatível com uma vasta gama de hardwares e softwares, já que a maioria dos aplicativos comerciais e profissionais são desenvolvidos especificamente para Windows, contudo é menos eficiente já que roda vários serviços em segundo plano e também demanda um hardware mais potente.
- Já o Linux é geralmente mais eficiente e pode ser configurado para rodar em hardwares menos potentes, uma vez que ele pode ser amplamente customizado para atender às necessidades do usuário, porém ele demanda mais conhecimento técnico para operação e manutenção.

## Analise arquitetura do Airbnb
### Arquitetura inicial
Em sua primeira versão a aplicação foi desenvolvida utilizando Ruby-on-Rails dessa forma um único serviço era responsável tanto pelo client quanto para as funcionalidades server-side.
Como a empresa esta em seus estágios iniciais, a utilização dessa ferramenta para o desenvolvimento de seu sistema possuia algumas vantagens, sendo elas:
- Facilidade do desenvolvimento inicial
- Desenvolvimento ágil
- Complexidade baixa
Porem problemas quando seu time de desenvolvimento expandiu, uma vez que essa arquitetura era ruim para coordenar mudanças por vários desenvolvedores. Tornando todo processo mais lento e aumentando a quantidade de conflitos no código.

![Airbnb 1](https://github.com/user-attachments/assets/8267772e-ca03-4f49-9b04-cd6d2bb6cf95)

### Arquitetura posterior
Levando em conta os problemas da primeira versão, o Airbnb tomou a decisão de migrar da arquitetura monolítica para uma que utiliza microsserviços. No caso, a segunda versão era uma versão hibrida com elementos da arquitetura original, porem coexistindo com a nova arquitetura orientada a serviços (micro-serviços). E na terceira versão desenvolvida os elementos monolíticos da arquitetura inicial foram completamente removidos se baseando totalmente na arquitetura orientada a serviços.
Dessa forma tornando o sistema mais confiável e agora sendo escalável, uma vez que agora é possível alocar recursos para serviços específicos do sistema conforme a demanda. Contudo, com o aumento da complexidade do sistema a adição de novas features se tornou mais difícil, pois agora qualquer mudança pode envolver vários serviços e as dependências geradas pelas APIs gráficas dificultava fazer o debug de erros.

![Airbnb 3](https://github.com/user-attachments/assets/c7af5638-d1fd-4356-a2d2-3e6b87e7cd36)

Fonte: https://blog.bytebytego.com/p/a-brief-history-of-airbnbs-architecture?utm_source=publication-search



## Diagrama UML
Foi desenvolvido um diagrama UML para um sistema de rolagem de dados em RPG de mesa. Este ajuda a visualizar a interação entre as classes e os métodos envolvidos, facilitando a compreensão e a implementação do sistema.
![Diagrama](https://github.com/user-attachments/assets/66757ada-8d4f-4eaf-8817-5077192fb2fc)

### Classe Dice 
A classe Dice define a quantidade de lados do dado e possui métodos para gerar resultados aleatórios baseados nesses lados.
```
import java.util.Random;

public class Dice {
    private int diceFaces;

    public Dice(int diceFaces) {
        this.diceFaces = diceFaces;
    }

    public void setDiceFaces(int diceFaces) {
        this.diceFaces = diceFaces;
    }

    public int rollDice(){
        Random roll = new Random();
        int number = roll.nextInt(diceFaces);
        number += 1;
        return number;
    }
}
```

### Classe Action
A classe Action gerencia a rolagem de múltiplos dados e modificadores de dano, agregando os resultados conforme necessário. Ela possui um método que retorna uma string contendo o nome da ação e o dano final causado.
```
public class Action {
    private String actionName;
    private Dice diceUsed;
    private int numberOfDices;
    private int bonusToRoll;

    public Action(String actionName, Dice diceUsed, int numberOfDices, int bonusToRoll) {
        this.actionName = actionName;
        this.diceUsed = diceUsed;
        this.numberOfDices = numberOfDices;
        this.bonusToRoll = bonusToRoll;
    }

    public void setActionName(String actionName) {
        this.actionName = actionName;
    }

    public void setDiceUsed(Dice diceUsed) {
        this.diceUsed = diceUsed;
    }

    public void setNumberOfDices(int numberOfDices) {
        this.numberOfDices = numberOfDices;
    }

    public void setBonusToRoll(int bonusToRoll) {
        this.bonusToRoll = bonusToRoll;
    }

    public String actionRoll(){
        int temp;
        String text;
        temp = 0;
        for(int i = 0; i < numberOfDices; i++){
            temp += diceUsed.rollDice();
        }
        temp += bonusToRoll;
        text = this.actionName + " deals " + temp + " points of damage!";
        return text;
    }
}
```
### Classe Main
A classe Main configura valores e instâncias para testar o programa de rolagem de dados.
```
public class Main {
    public static void main(String[] args) {
        Dice d6 = new Dice(6);
        Action fireBolt = new Action("Fire Bolt",d6,2,4);

        System.out.println(d6.rollDice());
        System.out.println(fireBolt.actionRoll());
    }
}
```
