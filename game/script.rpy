# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Joshua")
define e = Character("Eileen")
define m = Character("Mulher de branco")
define v = Character("Violet")
define s = Character("Sam")
define j = Character("???")
image flower:
    "bg flower.png"
    zoom 1.95

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene flower


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    s "O pai vai ficar bem?"
    "Seu irmão perguntava, em sua mão ele carregava uma chaleira com água quente."
    v "Sim, Sam, o papai vai melhorar."
    "Você falava sem muita emoção."
    s "Eu sinto falta da mamãe."
    "Você cerrava os punhos enquanto ajeitava uma bolsa d'água para despejar a água quente."
    "O silêncio se mantia."
    "Após encher a bolsa d'água, você levava ela até seu pai que estava de cama."
    p "O-obrigado"
    "Seu pai tossia, você conseguia ver o sangue sujando a mão dele, mas ele logo a escondia limpando a mesma. Você já sabia o motivo disso, era bem vísivel o sangue na boca dele sempre que tossia."
    v "Não precisa agradecer, pai."
    "Seu pai passava a mão pelo seu rosto, ajeitando seu cabelo para trás da orelha."
    p "Você já está com 14 anos Violet. O tempo passou muito rápido."
    p "Sam ainda é novo, não tem nem 1 mês que ele fez 7, você precisa ter paciência com ele."
    v "Eu sei, eu que tenho que cuidar dele agora, você já me disse isso quando a mãe morreu, não precisa me lembrar."
    p "Eu não queria que fosse assim. Deitado nessa cama, mal me levantando."
    v "Está tudo bem. Não precisa se preocupar."
    p "Como foi hoje na cidade? Conseguiu vender a colheita de batata?"
    v "Vendi um pouco. Temos dinheiro suficiente, não se preocupa."
    "Seu pai olhava para baixo, como quem procurava por algo."
    p "Filha..."
    p "Preciso conversar com você."
    p "Eu liguei para seus avós hoje, eles vem buscar vocês amanhã. Eu não consigo cuidar de vocês no meu estado."
    p "Vai ficar tudo bem. Eu consigo me virar..."
    v "..."
    "Algumas lagrimas começavam a se formar no seu rosto. Seu pai as enxugava com a mão."
    p "Não precisa chorar. Eu sei que tem sido difícil. Você tem lidado com tudo da casa."
    "Seu silência dominava o ar por alguns segundos."
    p "E ainda tem a questão dos seus pesadelos com o labirinto, mas tudo isso vai acabar quando você for morar com seus avós e estiver longe desse labirinto também."
    v "Tudo bem..."
    "As palavras saiam fracas de sua boca."
    p "Eu te amo, filhota."
    v "Eu também te amo, pai."
    p "Você fala para o Sam por mim? Não vou conseguir encarar ele."
    v "Claro."
    "Seu pai beijava sua testa e você deixava o quarto dele. Seu irmão estava na cozinha tomando um copo com leite."
    v "Sam, ajeita suas roupas, o vovô e a vovó vão buscar a gente amanhã."
    s "Eu não quero ficar com eles. A gente tem que cuidar do papai."
    v "Sam! Não é uma escolha. Papai precisa de descanso, o médico vai vir amanhã a tarde, lembra? Nós vamos ficar no vovô."
    s "Mas e se o médico não conseguir? A gente pode ir no labirinto. Lembra? Se a gente chegar no final, um desejo é realizado. Nós pode-"
    "Seu estresse já estava em um nível que não dava para segurar. Você soca a parede no mesmo momento para soltar a raiva."
    v "Cala a boca!"
    "No meio de sua raiva, você acabou quebrando o quadro da família. Os cacos acabaram cortando sua mão. Pegando um pano, você cobre os cortes."
    "Sam começa a correr para o quarto chorando."
    "O quadro no chão quebrado ainda mostrava a foto de vocês: Uma mulher de cabelos longos e pretos, ao seu lado um homem alto e forte, com cabelo curto e castanho, na frente, duas crianças, um garotinho parecido com o pai, e você, cabelo curto e de cara fechada."
    "Após encarar a foto, você a coloca na mesa. Terminando de limpar os cacos do chão, você vai para seu quarto."
    "Sam já está deitado, e não aparenta estar acordado."
    "Você o encara um pouco, mas logo após se deita para dormir também."
    j "Violet. Violet."
    "Você escuta uma voz te chamando durante a noite. Levantando no susto, você percebe que seu irmão não está na cama."
    "Levantando rápido da cama, você o enxerga de canto de olho pela janela. Ele estava indo em direção ao labirinto."
    "Você corre para fora, vendo ele entrar pelo portão."


    "Correndo atrás dele você encara o portão para o Labirinto das Flores."

    "Sua ansiedade se eleva após ter visto seu irmão tomando a primeira curva."
    
    "Falta apenas um passo para você entrar. O que você deseja fazer?"

    menu: 
        "Seguir seu irmão.":
            jump seguir_sim
            
        "Voltar para casa.":
            jump seguir_nao   

    label seguir_sim:  
        "Você se depara com seu irmão lá dentro olhando algumas flores, ele havia encontrado um caminho sem saída."
        "Suas mãos o sacode falando que ele não deveria sair de casa assim no meio da madrugada."
        "Então você o puxa de volta para retornar para casa, porém o caminho de volta se fechou."

        jump seguir_feito

    label seguir_nao:

        "Você retorna para a segurança de sua casa e seu corpo ainda tremia por conta do frio."
        "Você volta  para o quarto, e se deita na cama."      
        "Você acorda no outro dia. Sua cabeça ainda está meio zonza. Então você escuta a buzina."
        "Seus avós já estavam te esperando. Você passa pelo quadro quebrado e encara a foto uma ultima vez."
        "Nela estava você, seu pai e sua mãe."
        "Você a encara por mais alguns segundos como se algo faltasse. Você não consegue se lembrar o que poderia ser."
        "Seus avós te buscam, e você se muda com eles."
    return
    
    label seguir_feito:
        $ menu_tesoura = False
        $ sam = False
        $ sam_atacado = False

        "Apenas dois caminhos dos quais você não tinha visto antes estão disponiveis."
        "O caminho da esquerda possui um arco de rosas, já o da direita apenas a parede com folhas do labirinto."
        "Qual caminho você deseja?"
    
    menu:
        "Arco de rosas.":
            jump mulher

        "Parede com folhas":
            jump parede_folhas
    
    label parede_folhas:
        "Conforme você anda, você percebe que as rosas na parede são brancas."
        "Seu caminho segue com tranquilidade, seu irmão continua com você em silêncio."
        "Você vê mais dois caminhos: Um que segue reto, outro que vira a direita novamente. Você vai seguir ou vai para a direita?"

    menu: 
        "Seguir.":
            jump mao
        
        "Direita.":
            jump corpo

    label mao:
       
        "Você segue reto e se depara com uma tesoura sendo segurada por uma mão." 
        "Seu estomago se revira ao perceber que as rosas brancas ficavam vermelhas ao puxar o sangue daquela mão."

    menu:
        "Pega a tesoura.":
            jump tesoura_sim
        
        "Deixar a tesoura":
            jump tesoura_nao
    
    label tesoura_sim:
        $ menu_tesoura = True

        "Você percebe que a mão estava fria, provavelmente morta a um bom tempo."
        "Seu irmão vomita no chão ao ver você pegando a tesoura."
        "Assim que você retira a tesoura da mão, ela cai no chão, se soltando da parede. Um pouco de sangue ainda saia dela."
        "Sem caminho para seguir, você retorna a encruzilhada anterior."

        jump decisao_tesoura_feita

    label tesoura_nao:
        $ menu_tesoura = False

        "Você escolhe não pegar a tesoura. Sem caminho para seguir, você volta a encruzilhada anterior."

        jump decisao_tesoura_feita

    label decisao_tesoura_feita:
        "Você voltará ao começo, ou seguirá pelo caminho da direita?"    
    
    menu:
        "Começo":
            jump mulher

        "Direita":
            jump corpo

    label corpo:
        "Você se depara com as rosas da parede ficando mais vermelhas conforme você anda."
        "Até que você começa a enxergar partes de corpos pendurados nos espinhos das rosas."
        "No final do corredor, você enxerga um rosto ainda se mexendo entre as rosas."  
        "Você vai voltar ou fechar os olhos do seu irmão antes?"

    menu:
        "Fechar os olhos do seu irmão":
            jump sam_saudavel
        "Voltar para o começo":
            jump sam_traumatizado

    label sam_saudavel:
        $ sam = False

        "Sua mão tampa os olhos de seu irmão antes que ele possa ver algo. Você decide voltar para o começo." 
        jump mulher
    
    label sam_traumatizado:
        $ sam = True

        "Seu irmão consegue ver o corpo antes de vocês voltarem."
        "Ele trava por alguns segundos e o pânico domina seu rosto."
        "Você o puxa para voltar com você."
        jump mulher
    
    label mulher:
        $ menu_mulher_morta = False
        "Você atravessa o Arco de Flores"
        "Seguindo por ele você se depara com uma mulher de costas para você."
        "Ela ainda não tinha notado, mas ao se aproximar, você acaba por pisar em uma folha seca, que faz com que ela se vire para você"
        "A mulher possuia um vestido branco e sua voz era suave quando ela falava"
        m "Olá, tudo bem? Vocês estão perdidos?"
        "Ela se virava aos poucos e então, antes que você pudesse falar algo, você enxergava a boca dela."
        "Os labios daquela mulher eram vermelhos, não por conta de baton, ou da própria pele. Da sua boca escorria sangue."
        "Ela se aproximava a passos lentos após se virar, seus olhos eram apenas dois buracos sem luz que começavam a escorrer sangue junto da boca."
        "O vestido branco dela era tomado pela cor vermelha, e quando ela se movia a cor de seu vestido andava, como se fosse um liquido."
        "Ela começa a se mover em sua direção. O braço aparece por trás do vestido, ela tinha espinhos de rosa por todo braço e garras afiadas"

    menu:
        "Correr.":
            jump fugir
        "Conversar.":
            jump conversa  
        "Lutar.":
            jump atacar
    
    label atacar:
        if menu_tesoura:
            if sam:
                "Com a tesoura, você a ataca, cortando uma parte do vestido dela junto da pele. No local do corte, o vestido começava a sangrar e ficar branco onde havia sido cortado."
                "A mulher começava a tentar impedir o sangramento e corre de onde vocês estão."
                "Ao seu lado as rosas começavam a murchar e morrer, revelando um portão. Ao se aproximar você vê outra direção do labirinto."
                "Seu irmão estava em choque. Ele ficava parado sem conseguir se mexer. Você volta até ele e percebe que o mesmo está tremulo."
                "Você o pega pela mão e atravessa o portão com ele." 
                "Seu irmão está traumatizado."
                "Vocês continuam pelo labirinto. Assim que você atravessa uma voz começa a te guiar."
                "Alguns dias se passam até que vocês chegue ao final."
                "Vocês encaram um homem, ele era o jardineiro. Você o questiona sobre o desejo e ele a encara de volta."
                "Durante a conversa de vocês, você se distrai."
                "Ao perceber, Sam havia pegado a sua tesoura. Em um surto mental, ele cortava o próprio pescoço."
                "Horrorizada, você corre em direção ao corpo do seu irmão. Você o pega nos braços e começa a chorar."
                "O jardineiro a ajuda, e diz que o seu pai já estava melhor."
                "Ele te mostra a saida, e diz que enterrará seu irmão. Você larga o corpo dele, ainda chorando."
                "Você então sai do labirinto, retorna para sua casa e encontra seu em pé na cozinha com um sorriso no rosto."
                "Você o abraça e ele te abraça de volta. Ele havia melhorado."
                "Seu olhar fica triste ao se lembrar do seu irmão. Seu pai lhe questiona o porque da tristeza."
                "Uma mentira sai de sua boca, dizendo que não sabe onde o Sam está. Seu pai te encara confuso e pergunta. 'Quem é Sam?'"
                "Ninguém se lembra de seu irmão."
                return

            else:    
                $ menu_mulher_morta = True

                "Com a tesoura, você a ataca, cortando uma parte do vestido dela junto da pele. No local do corte, o vestido começava a sangrar e ficar branco onde havia sido cortado."
                "A mulher começava a tentar impedir o sangramento e corre de onde vocês estão. Ao seu lado as rosas começavam a murchar e morrer, revelando um portão. Ao se aproximar você vê outra direção do labirinto."
                jump portao
        
        else:
            "Você decide atacar a mulher para salvar seu irmão, porém algumas rosas se enrolam em sua perna a puxando para a parede."
            "Seu corpo começa a ser perfurado pelos espinhos enquanto você enxerga seu irmão sendo morto. Você desmaia no meio da dor."
            "Você encontra sua morte!"
            return

        label fugir:
                if sam:
                    "Seu irmão começa a vomitar e não consegue se mover, você tenta puxar ele, mas a mulher o alcança muito rápido."
                    "Ela pega seu irmão pelo pescoço e você o escuta se engasgando com o próprio vomito misturado com o sangue que escorre de seu pescoço."
                    "Você corre deixando seu irmão para trás ao ver ele perdendo a vida."
                    "Durante sua fuga, você encontra um portão que parece levar para outra área."
                    "Sua cabeça era tomada pela raiva e tristeza, o choque de perder seu irmão diante de seus olhos. Você soca a parede ao seu lado."
                    "Antes que você percebesse, espinhos se enrolaram em seus dedos, arrancando seu dedo anelar e mínimo. Você segura sua mão e atravessa o portão com o sangue escorrendo pelo seu dedo."
                    "Você continua pelo labirinto. Assim que você atravessa uma voz começa a te guiar."
                    "Alguns dias se passam até que você chegue ao final."
                    "Você encara um homem, ele era o jardineiro. Você o questiona sobre o desejo e ele a encara de volta."
                    "Ele abre caminho para você poder sair do labirinto e diz com calma que seu pai vai ficar bem."
                    "Você então sai do labirinto, retorna para sua casa e encontra seu em pé na cozinha com um sorriso no rosto."
                    "Você o abraça e ele te abraça de volta. Ele havia melhorado."
                    "Seu olhar fica triste ao se lembrar do seu irmão. Seu pai lhe questiona o porque da tristeza."
                    "Uma mentira sai de sua boca, dizendo que não sabe onde o Sam está. Seu pai te encara confuso e pergunta. 'Quem é Sam?'"
                    "Ninguém se lembra de seu irmão."
                    return

                else:

                    "Você puxa seu irmão pelo braço e sai correndo pelo caminho a sua direita."
                    "Algumas rosas vão em sua direção, tentando te prender em seus espinhos, porém você consegue se esquivar delas."
                    "Os passos da mulher começam a ficar para trás."
                    "Com sorte, você eventualmente chega em um portão. Você e seu irmão ofegantes decidem parar um pouco."
                    jump portao
                
        label conversa:
            "Antes que você conseguisse falar, a mulher avançava em você."
            "A pegando pelo pescoço, você sente varios espinhos te furando. Seus olhos vão fechando e você para de respirar."
            "Você encontra sua morte!"
            return
        
        label portao:
            "Você se sente nervosa e com raiva, seu pai sempre disse que você era a mais difícil de se controlar."
        menu:
            "Conversar":
                jump sam_conversar

            "Se acalmar":
                jump se_acalmar

        label sam_conversar:
            if menu_mulher_morta:
                v '"Sam! Que merda foi essa?" Você grita com seu irmão. "Por que você veio para cá?"'
                s '"P-porque o papai precisa melhorar. Aqui eles realizam desejos."'
                v '"Mas que merda? Eu já disse que isso é uma lenda. Agora estamos presos nisso."'
                s '"Desculpa, Violet. Eu queria ajudar o papai."'
                v '"Sabe a melhor forma de ajudar o pai? Não dando trabalho para ele!"'
                s "Sam parece estar triste, você solta um suspiro e o puxa pelo braço para atravessar o portão."
                "Você e seu irmão continuam pelo labirinto."
                "Alguns dias se passam até que vocês cheguem ao final."
                "Você e Sam encaram um homem, o jardineiro."
                "Sam grita pedindo para que seu pai seja curado."
                "Você o interrompe pedindo para que o jardineiro cure seu irmão."
                "O jardineiro encara vocês em silêncio e apenas faz um chá com uma flor que você nunca tinha visto antes."
                "Ele entrega para seu irmão tanto a flor, quanto o chá."
                "Ao tomar, seu irmão é curado dos ferimentos."
                "Vocês levam a flor para seu pai ao sair do labirinto. Fazem um chá para ele e ao tomar, ele se levanta em menos de 10 minutos."
                "Seu irmão acaba esquecendo sobre o labirinto."
                "Vocês continuam morando juntos."
                return


            else:
                v '"Sam! Que merda foi essa?" Você grita com seu irmão. "Por que você veio para cá?"'
                s '"P-porque o papai precisa melhorar. Aqui eles realizam desejos."'
                v '"Mas que merda? Eu já disse que isso é uma lenda. Agora estamos presos nisso."'
                "Você escuta o som de algumas plantas se mexendo. "
                "Por mais que estivesse atenta, é mais rápido do que você. A mulher havia alcançado vocês."
                "Seu irmão estava mais proximo dela. Ela o pega pelo braço e o puxa para perto. Algumas rosas se enrolam no rosto de Sam, furando ele."
                jump mulher2

        label se_acalmar:
            if menu_mulher_morta:
                "Você cerra seu punho e bate com força na parede de rosas. Você sente um espinho entrando na sua mão, doi um pouco."
                "Sam te olha com medo. Você balança sua mão e atravessa o portão com seu irmão."
                "Você e seu irmão continuam pelo labirinto."
                "Alguns dias se passam até que vocês cheguem ao final."
                "Você e Sam encaram um homem, o jardineiro."
                "Sam grita pedindo para que seu pai seja curado."
                "Você o interrompe apontando a tesoura para o jardineiro e pedindo para que ele cure seu irmão."
                "O jardineiro encara vocês em silêncio e apenas faz um chá com uma flor que você nunca tinha visto antes."
                "Ele entrega para seu irmão tanto a flor, quanto o chá."
                "Ao tomar, seu irmão é curado dos ferimentos."
                "Vocês levam a flor para seu pai ao sair do labirinto. Fazem um chá para ele e ao tomar, ele se levanta em menos de 10 minutos."
                "Vocês continuam morando juntos."
                return

            else:
                "Você cerra seu punho e bate com força na parede de rosas. Quando você percebe, os espinhos das rosas se enrolam nos seus dedos e os partem."
                "Seu dedo anelar e seu dedo mínimo estão decepados. Você atravessa o portão com a mão sangrando junto de seu irmão."
                "Você e seu irmão continuam pelo labirinto."
                "Alguns dias se passam até que vocês cheguem ao final."
                "Você e Sam encaram um homem, o jardineiro."
                "Sam grita pedindo para que seu pai seja curado."
                "Você o interrompe apontando a tesoura para o jardineiro e pedindo para que ele cure seu irmão."
                "O jardineiro encara vocês em silêncio e apenas faz um chá com uma flor que você nunca tinha visto antes."
                "Ele entrega para seu irmão tanto a flor, quanto o chá."
                "Ao tomar, seu irmão é curado dos ferimentos."
                "Vocês levam a flor para seu pai ao sair do labirinto. Fazem um chá para ele e ao tomar, ele se levanta em menos de 10 minutos."
                "Vocês continuam morando juntos."
                "Sua mão nunca se recuperou."
                return
            
            label mulher2:
            menu:
                "Correr.":
                    jump fugir2
                "Lutar.":
                    jump atacar2

            label atacar2:
                if menu_tesoura:
                    "Você usa a tesoura para atacar a mulher. Você atinge o vestido dela, que, ao ser rasgado, começa a escorrer sangue."
                    "Ela solta seu irmão e se afasta de vocês."
                    "Você não consegue mais segurar sua raiva e acaba socando a parede de rosas ao seu lado. Você sente um espinho entrando na sua mão, doi um pouco."
                    v '"Vamos embora"'
                    "Ao se virar para ver o rosto de seu irmão, você vê que seu olho havia sido arrancado. Você o abraça e atravessa o portão junto dele."
                    "Você e seu irmão continuam pelo labirinto."
                    "Alguns dias se passam até que vocês cheguem ao final."
                    "Você e Sam encaram um homem, o jardineiro."
                    "Sam grita pedindo para que seu pai seja curado."
                    "Você o interrompe apontando a tesoura para o jardineiro e pedindo para que ele cure seu irmão."
                    "O jardineiro encara vocês em silêncio e apenas faz um chá com uma flor que você nunca tinha visto antes."
                    "Ele entrega para seu irmão tanto a flor, quanto o chá."
                    "Ao tomar, seu irmão é curado dos ferimentos."
                    "Vocês levam a flor para seu pai ao sair do labirinto. Fazem um chá para ele e ao tomar, ele se levanta em menos de 10 minutos."
                    "Vocês continuam morando juntos."

                    return

                else:
                    "Você decide atacar a mulher para salvar seu irmão, porém algumas rosas se enrolam em sua perna a puxando para a parede."
                    "Seu corpo começa a ser perfurado pelos espinhos enquanto você enxerga seu irmão sendo morto. Você desmaia no meio da dor."
                    "Você encontra sua morte!"

                    return
            label fugir2:

                if menu_tesoura:

                    "Você deixa seu irmão para trás e atravessa a porta. Você ainda consegue escutar os gritos de seu irmão."
                    s "VIOLET! POR FAVOR, ME SALVA!"
                    "Você tampa seu ouvido para ignorar, até que em um momento os gritos param."
                    "Você atravessou o portão."
                    "Você continua pelo labirinto. Assim que você atravessa uma voz começa a te guiar."
                    "Alguns dias se passam até que você chegue ao final."
                    "Você encara um homem, ele era o jardineiro. Você o questiona sobre o desejo e ele a encara de volta."
                    "Ele abre caminho para você poder sair do labirinto e diz com calma que seu pai vai ficar bem."
                    "Você então sai do labirinto, retorna para sua casa e encontra seu em pé na cozinha com um sorriso no rosto."
                    "Você o abraça e ele te abraça de volta. Ele havia melhorado."
                    "Seu olhar fica triste ao se lembrar do seu irmão. Seu pai lhe questiona o porque da tristeza."
                    "Uma mentira sai de sua boca, dizendo que não sabe onde o Sam está. Seu pai te encara confuso e pergunta. 'Quem é Sam?'"
                    "Ninguém se lembra de seu irmão."

                    return

                else:
                    "Você deixa seu irmão para trás e atravessa a porta. Você ainda consegue escutar os gritos de seu irmão."
                    s "VIOLET! POR FAVOR, ME SALVA!"
                    "Você tampa seu ouvido para ignorar, até que em um momento os gritos param."
                    "Você atravessou o portão."
                    "A mulher de branco pega uma tesoura."
                    "Seu destino dentro do labirinto é incerto."

                return


    # This ends the game.
    
    return
