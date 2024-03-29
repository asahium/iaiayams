label night0_scene1:
    scene kitchen with dissolve
    play music "bestmusicever.mp3"
    show richard
    richard "Ешь."
    hide richard
    "Сегодня вечером Ричард приготовил блюдо, которое навеяло на меня болезненные воспоминания."
    "Я вспомнил, когда в последний раз ел это блюдо, оно заставило меня корчиться от боли из-за моей непереносимости острой пищи."
    "Я был полон решимости не повторять этот опыт, но от страха столкнуться с Ричардом по этому поводу у меня скрутило живот."
    "Я нерешительно смотрю на блюдо, вспоминая болезненный опыт прошлого раза."
    show richard
    richard "Ты не будешь?"
    alex "Я не могу это есть, меня от этого тошнит."
    richard "Ты просто придумываешь отговорки. Съешь это, иначе останешься голодным."
    "Я нервно перекладываю еду по тарелке."
    alex "Пожалуйста, я терпеть не могу острую пищу."
    richard "Перестань драматизировать. Это не так уж остро. Ты просто пытаешься привлечь к себе внимание."
    alex "Нет, это не так. Я правда не могу это есть."
    richard "Хватит! Если ты не будешь это есть, то, я думаю, тебе вообще не нужно есть."
    "Ричард вздыхает, бормочет что-то себе под нос и с силой хватает меня, таща к шкафу."
    alex "Нет, пожалуйста, я съем это, только не ставь меня туда снова."
    "Ричард закрывает дверь шкафа и запирает ее на ключ."
    
    hide richard
    jump night0_scene2

label night0_scene2:
    scene room with dissolve
    "В шкафу только небольшая щель для света, просачивающегося сквозь дверную раму, а иногда и вообще ничего. Я чувствую удушье, и мое сердце громко колотится в груди."
    "Тьма становится моим врагом, заключая меня в свои холодные, безжалостные объятия. Каждый раз, когда я оказываюсь в этом ужасном месте, мне так же страшно, как и в самый первый раз."
    "Я не могу не вспомнить бесчисленные случаи, когда Ричард обращался со мной подобным образом."
    "Это не первый раз, когда он издевается надо мной, но от этого это не становится менее пугающим."
    "Неуверенность в том, как долго он будет держать меня взаперти, наполняет меня ужасом, и я не могу избавиться от ощущения, что я совершенно один в этой темноте."
    play sound "click.mp3"
    stop music
    scene black
    "Когда Ричард с характерным щелчком выключает свет, шкаф погружается в полную темноту."
    "Накатывает паника, и я чувствую, как стены смыкаются надо мной. Мой разум начинает подшучивать надо мной, и я начинаю видеть жуткие очертания, скрывающиеся в темноте, искривленные и искаженный вид."
    "Малейший скрип или шорох заставляют мое сердце учащенно биться, и я не могу отделаться от ощущения, что вот-вот произойдет что-то ужасное."
    alex "Простите. Пожалуйста, выпустите меня."
    "Но ответа нет, только тишина, которая эхом отдается вокруг меня."
    "Видения в темноте становятся более яркими, дразня меня моими глубочайшими страхами."
    "Это похоже на кошмар, от которого я не могу проснуться, и я ловлю себя на том, что цепляюсь за надежду, что кто-нибудь, хоть кто-нибудь, придет спасти меня."
    "Посреди темноты я пытаюсь ухватиться за любое подобие комфорта, которое могу найти. Воспоминания о лучших временах мерцают в моем сознании, как далекие звезды на ночном небе."
    "Я помню тепло семьи, которой никогда не существовало. Но сейчас эти воспоминания кажутся такими далекими, омраченными жестокой реальностью моей жизни."
    "По мере того как минуты растягиваются, как мне кажется, в вечность, я изо всех сил стараюсь сохранять самообладание."
    "Слезы текут по моим щекам, и я обхватываю себя руками, отчаянно ища хоть какого-то утешения. Темнота, кажется, просачивается в самую мою душу, наполняя меня чувством безнадежности."
    alex "Я не позволю этой тьме поглотить меня."
    "Но это битва, которую я проигрываю. Страшные видения не проходят, и темнота ощущается как осязаемая сила, сокрушающая мой дух."
    "Я жажду, чтобы свет вернулся, чтобы кто-нибудь открыл дверь этого шкафа и спас меня от этого кошмара."
    "И все же, поскольку темнота продолжает держать меня в плену, я пытаюсь держаться за веру в то, что однажды, каким-то образом, я найду способ сбежать из этой бесконечной ночи."
    jump night0_scene3

label night0_scene3:
    scene black with dissolve
    pause 1
    show text "2 года назад. Приют “Глори Хэвен”." with dissolve
    pause 1
    scene black with dissolve
    pause 1
    scene orphanage with dissolve
    play music "school.mp3"
    emanon "{i}Положи меня, как печать, на сердце твое, как перстень, на руку твою: ибо крепка, как смерть, любовь; люта, как преисподняя, ревность; стрелы ее — стрелы огненные; она пламень весьма сильный.{/i}"
    emanon "{i}Большие воды не могут погасить любви, и реки не зальют ее. Если бы кто давал богатство дома своего за любовь, то он был бы отвергнут с презреньем.{/i}"
    show boy1
    boy1 "Ха, посмотрите кто опять один."
    hide boy1
    show boy2
    boy2 "Алекс думает, что он умнее нас, вот и не разговаривает с нами."
    "Я изо всех сил стараюсь не обращать на них внимания и продолжаю читать."
    "Мальчик подходит ближе."
    hide boy2
    show boy1
    boy1 "О, я Алекс, и я тааакой умный."
    hide boy1
    show boy2
    boy2 "Ха-ха-ха"
    "Я опускаю голову, стараясь не показывать своих эмоций."
    hide boy2
    show boy1
    boy1 "Что случилось, Алекс?"
    "Он выдергивает книгу из моих рук."
    boy1 "Не можешь за себя постоять?"
    hide boy1
    menu:
        "Оставьте меня в покое, пожалуйста.":
            show boy2
            boy2 "Послушай его, он строит из себя крутого! Тебе здесь не место, Алекс."
        "Промолчать.":
            show boy2
            boy2 "Что ты молчишь? Язык проглотил?"
        "Отвалите от меня!":
            show boy2
            boy2 "Завали."
            stop music
            play sound "punch.mp3"
            scene black with vpunch
            play music "death.mp3"
            ""
            "Жизнь - это абсурд, пронизанный противоречиями путь, по которому мы все идем."
            "Искусственный свет, отражающийся от страниц мира, ослепляет нас, лишая возможности увидеть его истинное значение."
            "Вот маленький мальчик, беззащитное создание, которое случайно оказалось в неправильное время, в неподходящем месте."
            "Как глухий аккорд, разрывающий гармонию, таким же несуразным казался этот удар книгой, внезапный и жестокий."
            "Взгляни на книгу - символ мудрости и познания, и она становится орудием смерти, путающим логику и смысл."
            "Все прелести реальности, все сказки и мечты, все великие мысли и идеи, все они попираются этим одним несчастным ударом."
            "Мальчик, ничего не подозревая, погружен в свой мир, не подозревая о жестокой игре судьбы."
            "Он внезапно стал актером в этой трагедии без репетиции, без возможности повторить свою роль."
            "Его последние моменты наполнены шумом сокрушающихся иллюзий, когда жизнь и смерть переплетаются, смешиваются в странном танце."
            "Так бессмысленна и абсурдна смерть этого маленького мальчика, как и наш собственный путь."
            "Каждое дыхание, каждый шаг - проходит сквозь этот парадоксальный лабиринт смысла и бессмыслицы. В неведении, мы идем вперед, не зная, куда и зачем."
            "И, подобно тому, как книга стала причиной конца для малыша, так и наш собственный мир может обернуться против него."
            "Такое несовершенство бытия заставляет нас задуматься. Мы - ничтожество в бесконечной вселенной, мимолетная искра, горящая на краю бесконечности."
            "Мы должны найти смысл в этом беспорядке, создавая свои собственные иллюзии, заблуждаясь и стремясь к недостижимому."
            "Возможно, в этом и заключается ответ на наше существование."
            "Смерть маленького мальчика - лишь один из множества парадоксов нашего существования."
            "Жизнь продолжается, даже после таких потерь. Возможно, ответ не так важен, как вопросы, которые мы задаем, и сама борьба за смысл делает нас людьми."
            "Мы стремимся понять этот бесконечный круговорот, зная, что каждый удар может быть последним, и все же продолжаем идти вперед."
            jump death
    
    
    scene orphanage with vpunch
    play sound "punch.mp3"
    "Слезы наворачиваются на глаза, но я пытаюсь их скрыть."
    boy1 "Ты никому здесь не нужен. У тебя никогда не будет настоящей семьи."
    alex "Прекрати это... просто прекрати."
    boy2 "В чем дело, плакса? Теперь будешь плакать?"
    "Я еле сдерживаю слезы."
    alex "Я сказал, прекрати!"
    boy1 "О, посмотрите, никому не нужная плакса!"
    "Я пытаюсь встать, вытирая слезы."
    boy2 "Ты такой слабый. Неудивительно, что тебя никто не любит."
    boy1 "Эй, все, посмотрите на Алекса! Он совсем один, и никому до него нет дела!"
    alex "Я не одинок. У меня есть я сам."
    boy2 "О, бедный Алекс, он сам себе семья! Ха-ха!"
    alex "\*глубокий вдох.\*"
    alex "Мне не нужен ни ты, ни кто-либо другой, чтобы быть счастливым."
    boy1 "Значит тебе и книжка не нужна!"
    "Он вырывает страницы из книги."
    "Я смотрю вниз на порванную книжку с разбитым сердцем."

    scene room
    play sound "click.mp3"
    "Ричард вернулся через полтора часа. Он открыл дверцу шкафа, и потребовалось немало времени, чтобы выбрался наружу, из-за сильной дрожи."
    richard "Мне не доставляет удовольствия наказывать тебя. Итак, я надеюсь, ты усвоил свой урок."
    alex "Я усвоил свой урок."
    "Ложусь в просторную, не застеленную кровать. Я не выключал прикроватную лампу. Не мог оторвать взгляд от шкафа напротив себя."
    "Обхватив руками свое худощавое тело, я изо всех сил стараюсь притвориться, что моя боязливая интуиция хоть сколько-то уверена в том, что никто не смотрит на меня через замочную скважину."
    jump day1_scene1