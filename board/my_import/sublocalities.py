# -*- coding: utf-8 -*-
from board.models import BigSublocality, City
# городские районы и областные районы
sublocalities = (
    (u'Харьков', (
        (u'Центральный р-н', (
            u'Центр',
            u'Нагорный',
            u'Центральный рынок',
            u'Левада',
            u'пл. Руднева')),
        (u'Направление Н.Бавария', (
            u'Москалевка',
            u'Заиковка',
            u'Новожаново',
            u'Диканевка',
            u'Дудковка',
            u'Новая Бавария',
            u'Минутка',
            u'Липовая Роща',
            u'Ледное',
            u'Филипповка',
            u'Гуты',
            u'пос. Силикатный')),
        (u'Направление Хол.Гора', (
            u'ЮЖД',
            u'Панасовка',
            u'Гончаровка',
            u'Карповка',
            u'Холодная Гора',
            u'Лысая Гора',
            u'Гиевка',
            u'Лагерное',
            u'пос. Ленина',
            u'Красный Октябрь',
            u'Залютино',
            u'Новоселовка',
            u'Григоровка')),
        (u'Направление Аэропорт', (
            u'Качановка',
            u'Верещаковка',
            u'Добрые Пчелы',
            u'Одесская',
            u'Основа',
            u'пос. Герцена',
            u'Мерефянка',
            u'Аэропорт',
            u'Федорцы',
            u'Жихарь')),
        (u'Направление Рогань', (
            u'пл. Восстания',
            u'Красный Луч',
            u'Балашовка',
            u'Парк Артема',
            u'Селекционная',
            u'Новые Дома',
            u'Ново-Западный',
            u'Горбани',
            u'Павленки',
            u'ХТЗ',
            u'пос. Фрунзе',
            u'Заики',
            u'Затишье',
            u'Восточный',
            u'Рогань',
            u'Горизонт',
            u'пос. Докучаева')),  
        (u'Направление Салтовка', (
            u'Сабурова Дача',
            u'Рашкина Дача',
            u'Журавлевка',
            u'Тюринка',
            u'Шевченки',
            u'Лазьковка',
            u'Халтурина',
            u'Старая Салтовка',
            u'Салтовка',
            u'Северная Салтовка',
            u'Большая Даниловка',
            u'Немышля',
            u'Петренки',
            u'Кулиничи',
            u'пос. Кирова')),
        (u'Напр-е Белгородское', (
            u'Сокольники',
            u'Померки',
            u'пос. Жуковского',
            u'Шишковка',
            u'Роял Клаб',
            u'Парк Хаус',
            u'Пятихатки')), 
        (u'Направление Алексеевка', (
            u'Шатиловка',
            u'Сосновая горка',
            u'Павловка',
            u'Ивановка',
            u'Сортировка',
            u'Павлово поле',
            u'Алексеевка')),  
        (u'Пригород', (
            u'Малая Даниловка',
            u'Флоринка',
            u'Родичи',
            u'Черкасская Лозовая',
            u'Лесное',
            u'Циркуны',
            u'Рогань',
            u'Коммунист',
            u'Логачевка',
            u'Молчаны',
            u'Коммунар',
            u'Безлюдовка',
            u'Радгоспное',
            u'Бабаи',
            u'Покотиловка',
            u'Песочин',
            u'Подворки',
            u'Сиряки',
            u'Солоницевка')),
        (u'Область', (
            u'Балаклейский р-н',
            u'Барвенковский р-н',
            u'Близнюковский р-н',
            u'Богодуховский р-н',
            u'Боровской р-н',
            u'Валковский р-н',
            u'Великобурлукский р-н',
            u'Волчанский р-н',
            u'Двуречанский р-н',
            u'Дергачевский р-н',
            u'Зачепиловский р-н',
            u'Змиевской р-н',
            u'Золочевский р-н',
            u'Изюмский р-н',
            u'Кегичевский р-н',
            u'Коломакский р-н',
            u'Красноградский р-н',
            u'Краснокутский р-н',
            u'Купянский р-н',
            u'Лозовской р-н',
            u'Нововодолажский р-н',
            u'Первомайский р-н',
            u'Печенежский р-н',
            u'Сахновщинский р-н',
            u'Харьковский р-н',
            u'Чугуевский р-н',
            u'Шевченковский р-н')))),
    (u'Киев', (
        (u'Голосеевский р-н', (
            u'Голосеевский (центр)',
            u'Демeевка',
            u'Корчеватое',
            u'Саперная Слободка',
            u'Теремки',
            u'Теремки-2')),
        (u'Дарницкий р-н', (
            u'Бортничи',
            u'Новая Дарница',
            u'Осокорки',
            u'Позняки',
            u'Харьковский')),
        (u'Деснянский р-н', (
            u'Лесной',
            u'Троещина')),
        (u'Днепровский р-н', (
            u'Березняки',
            u'Воскресенка',
            u'ДВРЗ',
            u'Комсомольский',
            u'Левобережный',
            u'Никольская Слободка',
            u'Радужный',
            u'Русановка',
            u'Соцгород',
            u'Старая Дарница')),
        (u'Оболонский р-н', (
            u'Минский',
            u'Оазис-Оболонь',
            u'Оболонь')),
        (u'Печерский р-н', (
            u'Липки',
            u'Нижний Печерск',
            u'Печерск',
            u'Печерский (центр)')),
        (u'Подольский р-н', (
            u'Ветряные Горы',
            u'Виноградарь',
            u'Куреневка',
            u'Подол')),
        (u'Святошинский р-н', (
            u'Академгородок',
            u'Беличи',
            u'Борщаговка',
            u'Святошино')),
        (u'Соломенский р-н', (
            u'Александровская слободка',
            u'Отрадный',
            u'Соломенк',
            u'Соломенский (КПИ)',
            u'Чоколовка ',)),
        (u'Шевченковский р-н', (
            u'Лукьяновка',
            u'Нивки',
            u'Сырец',
            u'Татарка',
            u'Шевченковский (центр)',
            u'Шулявка ')),
        (u'Область', (
            u'Барышевский р-н',
            u'Белоцерковский р-н',
            u'Богуславский р-н',
            u'Бориспольский р-н',
            u'Бородянский р-н',
            u'Броварский р-н',
            u'Васильковский р-н',
            u'Володарский р-н',
            u'Вышгородский р-н',
            u'Згуровский р-н',
            u'Иванковский р-н',
            u'Кагарлыкский р-н',
            u'Киево-Святошинский р-н',
            u'Макаровский р-н',
            u'Мироновский р-н',
            u'Обуховский р-н',
            u'Переяслав-Хмельницкий р-н',
            u'Полесский р-н',
            u'Ракитнянский р-н',
            u'Сквирский р-н',
            u'Ставищенский р-н',
            u'Таращанский р-н',
            u'Тетиевский р-н',
            u'Фастовский р-н',
            u'Яготинский р-н')))),
    (u'Винница', (
        (u'Область', (
            u'Барский р-н',
            u'Бершадский р-н',
            u'Винницкий р-н',
            u'Гайсинский р-н',
            u'Жмеринский р-н',
            u'Ильинецкий р-н',
            u'Калиновский р-н',
            u'Казатинский р-н',
            u'Крыжопольский р-н',
            u'Липовецкий р-н',
            u'Литинский р-н',
            u'Могилёв-Подольский р-н',
            u'Мурованокуриловецкий р-н',
            u'Немировский р-н',
            u'Оратовский р-н',
            u'Песчанский р-н',
            u'Погребищенский р-н',
            u'Тепликский р-н',
            u'Томашпольский р-н',
            u'Тростянецкий р-н',
            u'Тульчинский р-н',
            u'Тывровский р-н',
            u'Хмельницкий р-н',
            u'Черневецкий р-н',
            u'Чечельницкий р-н',
            u'Шаргородский р-н',
            u'Ямпольский р-н')),)),
    (u'Днепропетровск', (
        (u'Область', (
            u'Апостоловский р-н',
            u'Васильковский р-н',
            u'Верхнеднепровский р-н',
            u'Днепропетровский р-н',
            u'Криворожский р-н',
            u'Криничанский р-н',
            u'Магдалиновский р-н',
            u'Межевский р-н',
            u'Никопольский р-н',
            u'Новомосковский р-н',
            u'Павлоградский р-н',
            u'Петриковский р-н',
            u'Петропавловский р-н',
            u'Покровский р-н',
            u'Пятихатский р-н',
            u'Синельниковский р-н',
            u'Солонянский р-н',
            u'Софиевский р-н',
            u'Томаковский р-н',
            u'Царичанский р-н',
            u'Широковский р-н',
            u'Юрьевский р-н')),)),
    (u'Донецк', (
        (u'Область', (
            u'Александровский р-н',
            u'Амвросиевский р-н',
            u'Артёмовский р-н',
            u'Великоновоселковский р-н',
            u'Волновахский р-н',
            u'Володарский р-н',
            u'Добропольский р-н',
            u'Константиновский р-н',
            u'Красноармейский р-н',
            u'Краснолиманский р-н',
            u'Новоазовский р-н',
            u'Марьинский р-н',
            u'Першотравневый р-н',
            u'Славянский р-н',
            u'Старобешевский р-н',
            u'Тельмановский р-н',
            u'Шахтёрский р-н',
            u'Ясиноватский р-н')),)),
    (u'Житомир', (
        (u'Область', (
            u'Андрушёвский р-н',
            u'Барановский р-н',
            u'Бердичевский р-н',
            u'Брусиловский р-н',
            u'Володарско-Волынский р-н',
            u'Емильчинский р-н',
            u'Житомирский р-н',
            u'Коростенский р-н',
            u'Коростышевский р-н',
            u'Лугинский р-н',
            u'Любарский р-н',
            u'Малинский р-н',
            u'Народичский р-н',
            u'Новоград-Волынский р-н',
            u'Овручский р-н',
            u'Олевский р-н',
            u'Попельнянский р-н',
            u'Радомышльский р-н',
            u'Романовский р-н', 
            u'Ружинский р-н',
            u'Червоноармейский р-н',
            u'Черняховский р-н',
            u'Чудновский р-н')),)),
    (u'Запорожье', (
        (u'Область', (
            u'Акимовский р-н',
            u'Бердянский р-н',
            u'Васильевский р-н',
            u'Великобелозёрский р-н',
            u'Весёловский р-н',
            u'Вольнянский р-н',
            u'Гуляйпольский р-н',
            u'Запорожский р-н',
            u'Каменско-Днепровский р-н',
            u'Куйбышевский р-н',
            u'Мелитопольский р-н',
            u'Михайловский р-н',
            u'Новониколаевский р-н',
            u'Ореховский р-н',
            u'Пологовский р-н',
            u'Приазовский р-н',
            u'Приморский р-н',
            u'Розовский р-н',
            u'Токмакский р-н',
            u'Черниговский р-н')),)),
    (u'Ивано-Франковск', (
        (u'Область', (
            u'Богородчанский р-н',
            u'Верховинский р-н',
            u'Галичский р-н',
            u'Городенковский р-н',
            u'Долинский р-н',
            u'Калушский р-н',
            u'Коломыйский р-н',
            u'Косовский р-н',
            u'Надворнянский р-н',
            u'Рогатинский р-н',
            u'Рожнятовский р-н',
            u'Снятынский р-н',
            u'Тысменицкий р-н',
            u'Тлумачский р-н')),)),
    (u'Кировоград', (
        (u'Область', (
            u'Александрийский р-н',
            u'Александровский р-н',
            u'Бобринецкий р-н',
            u'Гайворонский р-н',
            u'Голованевский р-н',
            u'Добровеличковский р-н',
            u'Долинский р-н',
            u'Знаменский р-н',
            u'Кировоградский р-н',
            u'Компанеевский р-н',
            u'Маловисковский р-н',
            u'Новгородковский р-н',
            u'Новоархангельский р-н',
            u'Новомиргородский р-н',
            u'Новоукраинский р-н',
            u'Ольшанский р-н',
            u'Онуфриевский р-н',
            u'Петровский р-н',
            u'Светловодский р-н',
            u'Ульяновский р-н',
            u'Устиновский р-н')),)),
    (u'Луганск', (
        (u'Область', (
            u'Антрацитовский р-н',
            u'Беловодский р-н',
            u'Белокуракинский р-н',
            u'Краснодонский р-н',
            u'Кременский р-н',
            u'Лутугинский р-н',
            u'Марковский р-н',
            u'Меловский р-н',
            u'Новоайдарский р-н',
            u'Новопсковский р-н',
            u'Перевальский р-н',
            u'Попаснянский р-н',
            u'Сватовский р-н',
            u'Свердловский р-н',
            u'Славяносербский р-н',
            u'Станично-Луганский р-н',
            u'Старобельский р-н',
            u'Троицкий р-н')),)),
    (u'Луцк', (
        (u'Область', (
            u'Владимир-Волынский р-н',
            u'Гороховский р-н',
            u'Иваничевский р-н',
            u'Киверцовский р-н',
            u'Ковельский р-н',
            u'Камень-Каширский р-н',
            u'Локачинский р-н',
            u'Луцкий р-н',
            u'Любешовский р-н',
            u'Любомльский р-н',
            u'Маневичский р-н',
            u'Ратновский р-н',
            u'Рожищенский р-н',
            u'Старовыжевский р-н',
            u'Турийский р-н',
            u'Шацкий р-н')),)),
    (u'Львов', (
        (u'Область', (
            u'Бродовский р-н',
            u'Бусский р-н',
            u'Городокский р-н',
            u'Дрогобычский р-н',
            u'Жидачовский р-н',
            u'Жолковский р-н',
            u'Золочевский р-н',
            u'Каменка-Бугский р-н',
            u'Николаевский р-н',
            u'Мостисский р-н',
            u'Перемышлянский р-н',
            u'Пустомытовский р-н',
            u'Радеховский р-н',
            u'Самборский р-н',
            u'Сколевский р-н',
            u'Сокальский р-н',
            u'Старосамборский р-н',
            u'Стрыйский р-н',
            u'Турковский р-н',
            u'Яворовский р-н')),)),
    (u'Николаев', (
        (u'Область', (
            u'Арбузинский р-н',
            u'Баштанский р-н',
            u'Березанский р-н',
            u'Березнеговатский р-н',
            u'Братский р-н',
            u'Веселиновский р-н',
            u'Вознесенский р-н',
            u'Врадиевский р-н',
            u'Доманёвский р-н',
            u'Еланецкий р-н',
            u'Жовтневый р-н',
            u'Казанковский р-н',
            u'Кривоозёрский р-н',
            u'Николаевский р-н',
            u'Новобугский р-н',
            u'Новоодесский р-н',
            u'Очаковский р-н',
            u'Первомайский р-н',
            u'Снигирёвский р-н')),)),
    (u'Одесса', (
        (u'Область', (
            u'Ананьевский р-н',
            u'Арцизский р-н',
            u'Балтский р-н',
            u'Березовский р-н',
            u'Белгород-Днестровский р-н',
            u'Беляевский р-н',
            u'Болградский р-н',
            u'Великомихайловский р-н',
            u'Ивановский р-н',
            u'Измаильский р-н',
            u'Килийский р-н',
            u'Кодымский р-н',
            u'Коминтерновский р-н',
            u'Котовский р-н',
            u'Красноокнянский р-н',
            u'Любашёвский р-н',
            u'Николаевский р-н',
            u'Овидиопольский р-н',
            u'Ренийский р-н',
            u'Раздельнянский р-н',
            u'Савранский р-н',
            u'Саратский р-н',
            u'Тарутинский р-н',
            u'Татарбунарский р-н',
            u'Фрунзовский р-н',
            u'Ширяевский р-н')),)),
    (u'Полтава', (
        (u'Область', (
            u'Великобагачанский р-н',
            u'Гадячский р-н',
            u'Глобинский р-н',
            u'Гребёнковский р-н',
            u'Диканьский р-н',
            u'Зеньковский р-н',
            u'Карловский р-н',
            u'Кобелякский р-н',
            u'Козельщинский р-н',
            u'Котелевский р-н',
            u'Кременчугский р-н',
            u'Лохвицкий р-н',
            u'Лубенский р-н',
            u'Машевский р-н',
            u'Миргородский р-н',
            u'Новосанжарский р-н',
            u'Оржицкий р-н',
            u'Пирятинский р-н',
            u'Полтавский р-н',
            u'Решетиловский р-н',
            u'Семёновский р-н',
            u'Хорольский р-н',
            u'Чернухинский р-н',
            u'Чутовский р-н',
            u'Шишацкий р-н')),)),
    (u'Ровно', (
        (u'Область', (
            u'Березновский р-н',
            u'Владимирецкий р-н',
            u'Гощанский р-н',
            u'Демидовский р-н',
            u'Дубенский р-н',
            u'Дубровицкий р-н',
            u'Заречненский р-н',
            u'Здолбуновский р-н',
            u'Корецкий р-н',
            u'Костопольский р-н',
            u'Млиновский р-н',
            u'Острожский р-н',
            u'Радивиловский р-н',
            u'Ровненский р-н',
            u'Рокитновский р-н',
            u'Сарненский р-н')),)),
    (u'Сумы', (
        (u'Область', (
            u'Ахтырский р-н',
            u'Белопольский р-н',
            u'Бурынский р-н',
            u'Великописаревский р-н',
            u'Глуховский р-н',
            u'Конотопский р-н',
            u'Краснопольский р-н',
            u'Кролевецкий р-н',
            u'Лебединский р-н',
            u'Липоводолинский р-н',
            u'Недригайловский р-н',
            u'Путивльский р-н',
            u'Роменский р-н',
            u'Середино-Будский р-н',
            u'Сумской р-н',
            u'Тростянецкий р-н',
            u'Шосткинский р-н',
            u'Ямпольский р-н')),)),
    (u'Тернополь', (
        (u'Область', (
            u'Бережанский р-н',
            u'Борщёвский р-н',
            u'Бучачский р-н',
            u'Гусятинский р-н',
            u'Залещицкий р-н',
            u'Збаражский р-н',
            u'Зборовский р-н',
            u'Козовский р-н',
            u'Кременецкий р-н',
            u'Лановецкий р-н',
            u'Монастырисский р-н',
            u'Подволочисский р-н',
            u'Подгаецкий р-н',
            u'Теребовлянский р-н',
            u'Тернопольский р-н',
            u'Чортковский р-н',
            u'Шумский р-н')),)),
    (u'Ужгород', (
        (u'Область', (
            u'Береговский р-н',
            u'Великоберезнянский р-н',
            u'Виноградовский р-н',
            u'Воловецкий р-н',
            u'Иршавский р-н',
            u'Межгорский р-н',
            u'Мукачевский р-н',
            u'Перечинский р-н',
            u'Раховский р-н',
            u'Свалявский р-н',
            u'Тячевский р-н',
            u'Ужгородский р-н',
            u'Хустский р-н')),)),
    (u'Херсон', (
        (u'Область', (
            u'Бериславский р-н',
            u'Белозёрский р-н',
            u'Великолепетихский р-н',
            u'Великоалександровский р-н',
            u'Верхнерогачикский р-н',
            u'Высокопольский р-н',
            u'Генический р-н',
            u'Голопристанский р-н',
            u'Горностаевский р-н',
            u'Ивановский р-н',
            u'Каланчакский р-н',
            u'Каховский р-н',
            u'Нижнесерогозский р-н',
            u'Нововоронцовский р-н',
            u'Новотроицкий р-н',
            u'Скадовский р-н',
            u'Цюрупинский р-н',
            u'Чаплинский р-н')),)),
    (u'Хмельницкий', (
        (u'Область', (
            u'Белогорский р-н',
            u'Виньковецкий р-н',
            u'Волочисский р-н',
            u'Городокский р-н',
            u'Деражнянский р-н',
            u'Дунаевецкий р-н',
            u'Изяславский р-н',
            u'Каменец-Подольский р-н',
            u'Красиловский р-н',
            u'Летичевский р-н',
            u'Новоушицкий р-н',
            u'Полонский р-н',
            u'Славутский р-н',
            u'Староконстантиновский р-н',
            u'Старосинявский р-н',
            u'Теофипольский р-н',
            u'Хмельницкий р-н',
            u'Чемеровецкий р-н',
            u'Шепетовский р-н',
            u'Ярмолинецкий р-н')),)),
    (u'Черкассы', (
        (u'Область', (
            u'Городищенский р-н',
            u'Драбовский р-н',
            u'Жашковский р-н',
            u'Звенигородский р-н',
            u'Золотоношский р-н',
            u'Каменский р-н',
            u'Каневский р-н',
            u'Катеринопольский р-н',
            u'Корсунь-Шевченковский р-н',
            u'Лысянский р-н',
            u'Маньковский р-н',
            u'Монастырищенский р-н',
            u'Смелянский р-н',
            u'Тальновский р-н',
            u'Уманский р-н',
            u'Христиновский р-н',
            u'Черкасский р-н',
            u'Чигиринский р-н',
            u'Чернобаевский р-н',
            u'Шполянский р-н')),)),
    (u'Чернигов', (
        (u'Область', (
            u'Бахмачский р-н',
            u'Бобровицкий р-н',
            u'Борзнянский р-н',
            u'Варвинский р-н',
            u'Городнянский р-н',
            u'Ичнянский р-н',
            u'Козелецкий р-н',
            u'Коропский р-н',
            u'Корюковский р-н',
            u'Куликовский р-н',
            u'Менский р-н',
            u'Нежинский р-н',
            u'Новгород-Северский р-н',
            u'Носовский р-н',
            u'Прилукский р-н',
            u'Репкинский р-н',
            u'Семёновский р-н',
            u'Сосницкий р-н',
            u'Сребнянский р-н',
            u'Талалаевский р-н',
            u'Черниговский р-н',
            u'Щорский р-н')),)),
    (u'Черновцы', (
        (u'Область', (
            u'Вижницкий р-н',
            u'Герцаевский р-н',
            u'Глыбокский р-н',
            u'Заставновский р-н',
            u'Кельменецкий р-н',
            u'Кицманский р-н',
            u'Новоселицкий р-н',
            u'Путильский р-н',
            u'Сокирянский р-н',
            u'Сторожинецкий р-н',
            u'Хотинский р-н')),)),
    (u'АР Крым', (
        (u'Область', ( 
            u'Алуштинский р-н',
            u'Армянский р-н',
            u'Бахчисарайский р-н',            
            u'Белогорский р-н',               
            u'Джанкойский р-н',               
            u'Евпаторийский р-н',
            u'Керченский р-н',
            u'Кировский р-н',                 
            u'Красногвардейский р-н',         
            u'Красноперекопский р-н',         
            u'Ленинский р-н',                 
            u'Нижнегорский р-н',              
            u'Первомайский р-н',              
            u'Раздольненский р-н',            
            u'Сакский р-н',                   
            u'Симферопольский р-н',              
            u'Советский р-н',            
            u'Судакский р-н',
            u'Феодосийский р-н',
            u'Черноморский р-н',
            u'Ялтинский р-н')),)),    
)


def import_data():
    for city_name, big_list in sublocalities:
        cc = City.objects.get(name=city_name)
        print city_name
        for big_name, subloc_list in big_list:
            if big_name == u'Область':
                for subloc_name in subloc_list:
                    bb = cc.sublocality_set.create(name=subloc_name, in_city=False)
                    bb.save()
            else:
                bg = BigSublocality.objects.get(name=big_name)
                for subloc_name in subloc_list:
                    bb = cc.sublocality_set.create(name=subloc_name, in_city=True)
                    bg.sublocality_set.add(bb)
    print 'Таблицы должны быть очищены перед импортом данных, иначе будет бяка'
