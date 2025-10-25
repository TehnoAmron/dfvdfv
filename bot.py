import telebot
from bot_logic import gen_pass
bot = telebot.TeleBot("8430119619:AAFXskyAu8oCHsEsnyG-b_Nu9rUroyb5G1g")


text_messages = {
    'welcome':
        u'Please welcome {name}!\n\n'
        u'This chat is intended for questions about and discussion of the pyTelegramBotAPI.\n'
        u'To enable group members to answer your questions fast and accurately, please make sure to study the '
        u'project\'s documentation (https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md) and the '
        u'examples (https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples) first.\n\n'
        u'I hope you enjoy your stay here!',

    'info':
        u"I am a TehnoBot that helps people.\n"
        u"Don't worry if the bot isn't 100% working yet.\n"
        u"Besides, I'm still in development.\n"
        u'Suggestions are also welcome, just leave them in the official MrTehno chat!',
        
    'wrong_chat':
        u'Hi there!\nThanks for trying me out. However, this bot can only be used in the pyTelegramAPI group chat.\n'
        u'Join us!\n\n'
        u'https://telegram.me/joinchat/067e22c60035523fda8f6025ee87e30b',

    'help':
        u'[Bot] List of commands:.\n'
        u'-/hello - Приветствие.\n'
        u'-/heh [Кол-во раз] - Пишет heh определенное кол-во раз.\n'
        u'-/ping - Ваш пинг.\n'
        u'-/pass [Длинна пароля] - Придумывает рандомный пароль.\n'
        u'-/bye - Прощание.\n'

    'ecohelp':
        u'Используйте многоразовые сумки, бутылки для воды и контейнеры вместо одноразовых пластиковых изделий.\n'
        u'Сортируйте отходы (пластик, стекло, бумагу, батарейки) и сдавайте их на переработку.\n'
        u'Выбирайте товары с минимумом упаковки или в перерабатываемой таре, а также продукты на развес.\n'
        u'Используйте старые вещи повторно или отдавайте их другим, а не выбрасывайте.\n'
        u'Не оставляйте мусор после пикников или прогулок. \n'
        u'Закрывайте кран, когда чистите зубы, и используйте воду рационально при мытье посуды или стирке.\n'
        u' Выключайте свет и бытовые приборы, когда они не нужны, и используйте энергосберегающие лампы.\n'
        u'Отказывайтесь от пакетированного чая и кофе «с собой», заменяя их на листовой чай и термокружку. \n'
        u'Чаще ходите пешком, ездите на велосипеде или пользуйтесь общественным транспортом.\n'
        u' Сажайте деревья и поддерживайте инициативы по озеленению вашего города. \n'
        u'Инвестируйте в «зеленую» энергетику или поддерживайте экологические организации. \n',

    'ecothing':
        u'Загрязнение происходит из-за антропогенной деятельности и природных процессов.\n'
        u'Основными виновниками являются промышленность, транспорт, сельское хозяйство и бытовая деятельность, которые выбрасывают в окружающую среду химические вещества (нефтепродукты, тяжелые металлы, пестициды, отходы), пластик, мусор и создают физические загрязнения (шум, тепло, радиация). \n'
        u'Выбросы заводов и электростанций (особенно работающих на ископаемом топливе) загрязняют воздух, воду и почву токсичными веществами, такими как тяжелые металлы и диоксиды.\n'
        u' Автомобильный транспорт является одним из главных источников загрязнения воздуха из-за сжигания топлива.\n'
        u'Вырубка лесов приводит к выбросу углерода в атмосферу и снижает способность природы поглощать углекислый газ.\n'
        u'Неправильная утилизация мусора, использование синтетических моющих средств и неэффективное управление отходами приводят к накоплению мусора и загрязнению окружающей среды.\n'
        u'Использование удобрений и пестицидов, а также отходы животноводческих комплексов загрязняют почву и водные ресурсы\n'
        u'Естественные явления, такие как извержения вулканов или естественные разливы нефти, также могут способствовать загрязнению.\n',

    'ecofacts':
        u'Ежегодно исчезает от 30 до 32 тысяч видов живых организмов.\n'
        u'К концу XXI века планета может лишиться половины своего биоразнообразия.\n'
        u'Ежегодно вырубается 11-12 миллионов гектаров тропических лесов, что в 10 раз больше, чем восстанавливается.\n'
        u'Леса, которые поглощают углекислый газ, занимают лишь 31% от общей площади лесов. \n'
        u'Загрязнение воздуха является причиной 7 миллионов смертей в год.\n'
        u'Неблагоприятные экологические факторы окружающей среды ответственны за 60% случаев острых респираторных заболеваний.\n'
        u'Уровень углекислого газа в атмосфере достиг максимума за последние 800 000 лет.\n'
        u'Пластиковые бутылки разлагаются более 500 лет.\n'
        u'Электроэнергия, потребляемая для отправки спама, эквивалентна выбросам \(3,5\) миллионов автомобилей в год.\n'
        u'Швеция импортирует мусор и перерабатывает 95% его отходов в энергию. \n'
        u'Ежедневно в природные водоемы попадает около 2–2,5 миллионов тонн человеческих отходов.\n',

    'ecoplast':
        u'Ежегодно в океан попадает миллионы тонн пластика, где он образует огромные мусорные пятна. Рыбы и другие морские обитатели заглатывают микропластик, ошибочно принимая его за пищу, что приводит к голоду и гибели.\n'
        u'Пластик просачивается в почву, отравляя ее и нарушая водный баланс. Это повреждает корни деревьев и уничтожает почвенные микроорганизмы.\n'
        u'Производство пластика требует большого количества энергии и является источником парниковых газов. \n'
        u'Животные могут запутываться в крупных пластиковых предметах, таких как пакеты или сетки, и гибнуть от удушья, удушения или голода.\n'
        u'Пластик, попадая в пищеварительную систему животных, не разлагается и может вызвать отравление токсичными веществами. \n'
        u'Пластик распадается на микрочастицы, которые попадают в организм человека через пищу, воду и воздух.\n'
        u'При повторном использовании пластиковой посуды или при сжигании пластика выделяются опасные вещества (например, фенол, формальдегид, диоксины), которые наносят вред здоровью. \n',

    'ecosort':
        u'Заведите отдельные контейнеры, коробки или пакеты для разных типов отходов. Это могут быть бумажные пакеты для макулатуры, отдельные емкости для пластика, стекла, металла и органики.\n'
        u'Ориентируйтесь на стандартные цвета контейнеров для вторсырья: синий для макулатуры, желтый для пластика, зеленый для стекла, черный для органики.\n'
        u'Очищайте упаковку от остатков пищи и жидкостей перед тем, как выбросить ее в контейнер для переработки.\n'
        u'Батарейки, ртутные лампы, градусники, бытовую химию и электронику нельзя выбрасывать в обычный мусор. Их следует сдавать в специальные пункты приема. \n'
        u'Многие города имеют пункты приема, куда можно сдать отсортированное вторсырье, такое как бумага, пластик, стекло и металл.\n'
        u'Батарейки, электроника, люминесцентные лампы и другие опасные отходы требуют сдачи в специально оборудованные места.\n'
        u'В некоторых регионах существуют специальные экобоксы или программы по сбору опасных отходов. \n'
        u'Современные заводы используют автоматические линии с оптическими, спектральными и другими датчиками, которые распознают и разделяют материалы с высокой точностью.\n'
}
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Still alive and kicking!")

@bot.message_handler(commands=['info'])
def on_info(message):

    bot.reply_to(message, text_messages['info'])

@bot.message_handler(commands=['help'])
def on_ping(message):
    bot.reply_to(message, "")

@bot.message_handler(commands=['animal'])
def send_mem3(message):
    with open('images/anim_memee.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['animal2'])
def send_mem3(message):
    with open('images/anim_meme.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['animal3'])
def send_mem3(message):
    with open('images/anim_mem.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['animal4'])
def send_mem3(message):
    with open('images/anim_memm.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)    

@bot.message_handler(commands=['random_animal_mem'])
def send_random_mem(message):
    img_name = random.choice(os.listdir('imag'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['ecohelp'])
def on_ping(message):
    bot.reply_to(message, text_messages['ecohelp'])

@bot.message_handler(commands=['ecofacts'])
def on_ping(message):
    bot.reply_to(message, text_messages['ecofacts'])

@bot.message_handler(commands=['ecoplast'])
def on_ping(message):
    bot.reply_to(message, text_messages['ecoplast'])

@bot.message_handler(commands=['ecosort'])
def on_ping(message):
    bot.reply_to(message, text_messages['ecosort'])

@bot.message_handler(commands=['ecothing'])
def on_ping(message):
    bot.reply_to(message, text_messages['ecothing'])

@bot.message_handler(commands=['eco_zag1'])
def send_mem3(message):
    with open('images/eco_zag1.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['eco_zag2'])
def send_mem3(message):
    with open('images/eco-zag2.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['eco_zag3'])
def send_mem3(message):
    with open('images/eco-zag3.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['eco_zag4'])
def send_mem3(message):
    with open('images/animeco_zag4.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['eco'])
def send_random_mem(message):
    img_name = random.choice(os.listdir("ecophoto"))
    with open(f'ecophoto/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 


@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

bot.polling()
