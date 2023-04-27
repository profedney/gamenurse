# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Andreia")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg quarto

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show andreia

    # These display lines of dialogue.

    a "Olá meu nome é Andreia, vamos jogar?"

    a "A enfermagem é uma profissão que tem como principal objetivo cuidar da saúde dos pacientes."

    menu:

        "Verdadeiro":
            jump verd1

        "Falso":
            jump falso1

    label verd1:

        a "Isso você acertou!"

        jump saida1

    label falso1:

        a "Não. Você errou"

        jump saida1

    label saida1:

        "Muito obrigado por ter jogado"
        "Jogo criado por Edney"


    return
