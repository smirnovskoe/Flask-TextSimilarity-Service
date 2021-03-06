"""
Simple test
"""

import requests

text_water_tut = """Вода в районе пропала утром в воскресенье. Ремонтная бригада «Минскводоканала» причину обнаружила в тот же день — кто-то проник в колодец, перекрыл воду и срезал шпиндель вентиля, который отвечает за открытие и закрытие задвижки.
С редакцией связался сотрудник «Минскводоканала», пожелавший не озвучивать свое имя в печати. Он сообщил о новых и важных технических подробностях этой истории.
Он говорит, что шток задвижки (в статье мы ее называем шпинделем. — Прим. TUT.BY) был и в самом деле срезан, и сделано это было, скорее всего, болгаркой с аккумулятором (такой не требуется розетка). Но вот гайка, приваренная на шток, — дело рук совсем не злоумышленника. Это сделала бригада «Минскводоканала». Она приварила гайку после обнаружения проблемы. С помощью нее как бы нарастили обрезанный шток, и теперь с помощью ключа можно открыть задвижку, поворачивая гайку ключом. 
Сам маховик (вентиль) при этом уже не нужен.
Почему вода в Новой Боровой в воскресенье сначала появилась, а потом пропала до сегодняшнего утра? По словам собеседника, рабочие проверили работоспособность задвижки и открыли ее. За это время вода успела наполнить трубы. 
Но потом ее закрыли — «Минскводоканал» решил сделать анализ воды.
По информации обслуживающей компании «А-100 Комфорт», сотрудники «Минскводоканала» приехали сегодня примерно в три часа ночи — и вода появилась уже через час.
Теперь осталось выяснить, кто бы это мог спуститься в колодец и оставить целый район без воды. 
Следственные органы пока ничего не сообщали ни о проведении проверки, ни о заведенном деле.
Резонный вопрос — в Новой Боровой установлено много камер видеонаблюдения, неужели момент проникновения в колодец на них не попал? 
Как нам объяснили в обслуживающей компании «А-100 Комфорт», колодец расположен не на территории района, и там их камер нет. 
Предполагаемое время перекрытия воды — 6 утра воскресенья.
yandex.by/maps
Место, где расположен интересующий нас колодец. Скриншот: yandex.by/maps
Колодец находится примерно через дорогу от установленных биотуалетов. Они появились там в тот же день, когда пропала вода
Сейчас личность злоумышленника остается неизвестной. И все же ничего невозможного нет — колодец находится рядом с проезжей частью улицы Гинтовта (ориентировочно напротив дома № 1). Рядом припарковано много машин жителей района, колодец виден из окон домов напротив.
"""

text_water_onliner = """Вчера утром жители «Новой Боровой» стали жаловаться на отсутствие холодной и горячей воды. 
Добиться от «Минскводоканала» хоть какой-то информации было крайне сложно: одни диспетчеры заявляли, что всему виной авария, другие говорили, дело в некой загадочной задвижке, которую перекрыли неизвестные. 
Когда появится вода, никто сказать не мог. Пошли уже вторые сутки, а проблему так и не решили.
На въезде в «Новую Боровую» поставили несколько биотуалетов. Они уже прославились в соцсетях благодаря своей бело-красно-белой расцветке.
Да и в самом жилом комплексе на первый взгляд все очень буднично. Никто, как в Сухарево, с ведрами по району не мельтешит. Ажиотаж здесь скорее на детской площадке.
— У нас во втором доме на Леонардо да Винчи и вчера, и сегодня все хорошо. Только напор слабый, — пожимает плечами одна из молодых мам. 
Эту же информацию подтверждают и в «Булочной». Там тоже никаких проблем с водой не наблюдали.
— Вы вглубь района пройдите, там вода отсутствует. Я живу в 3-м доме на Авиационной, ее несколько раз то включали, то отключали. Повезло, что в 6 утра удалось помыться, — подсказывает нам еще одна местная жительница.
На Авиационной и правда попадаются люди, несущие в руках пятилитровые бутылки. Кто-то ходит за водой к соседям, кто-то к цистернам, которые пригнал «Минскводоканал». Одна из них припарковалась у детского сада «Карандаши». 
Его сотрудница еще утром писала нам, что там нечем вымыть посуду, провести влажную уборку, да даже руки ополоснуть!
— Детскому саду мы уже отгрузили много воды. Не знаю, сколько точно... Всего в бочке 5000 литров. 
Местные жители тоже подходят, правда, не очень много: рабочий день все-таки. Человек 100, может, и было, — щурится водитель цистерны.
— Живу в квартале «Форрест» уже девять месяцев и первый раз с таким столкнулась. Еще вчера в 7 вечера обещали, что «через два часа все исправят», но воды нет до сих пор. 
Хорошо, мы в магазине питьевую купили, но она уже закончилась. И туалет полностью заполнен... —  делится переживаниями Елена, пряча пятилитровик в детскую коляску.
И пока местные ищут ответ на вопрос, что же произошло, в своих дворовых чатах, в Telegram-канале «А-100 Комфорт» уже публикуют официальную версию: «Инженерный состав управляющей компании „А-100 Комфорт“ произвел полный осмотр центрального трубопровода водоснабжения, находящегося на балансе УП „Минскводоканал“. В результате осмотра было выявлено повреждение задвижки в одном из колодцев по магистрали от Гинтовта в НБ, из-за чего в районе „Новая Боровая“ отсутствует водоснабжение. 
Данные переданы в УП „Минскводоканал“ для устранения последствий».
Один из наших читателей дополняет эту информацию:
— Проблема с люком-заглушкой на Гинтовта. К нему пробрался кто-то посторонний: перекрыл воду и снес вентиль. Милиция сейчас разбирается. Там нет камер, установить личность сложно. Когда будет вода, неясно. Рассматриваем вариант подавать коллективную жалобу на «Минскводоканал».
А вот что пишет Telegram-канал «Минск.Официально» со ссылкой на «Минскводоканал»: «С целью максимально быстрого выявления причин аварии предприятием проведено обследование сетей. 
Выявлены неисправности запорной арматуры, в том числе рассматривается вариант умышленного повреждения. 
В настоящее время продолжается обследование, проводится мониторинг качества воды. 
Принимаются все необходимые меры для восстановления водоснабжения в максимально сжатые сроки»."""


result = requests.post('http://0.0.0.0:9999/api/ml', json={"text1": text_water_tut, "text2": text_water_onliner})

print(result.status_code)
print(result.content)