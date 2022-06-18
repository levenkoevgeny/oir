from django.db import migrations
from test_data.models import EmployeeKind, Subdivision, Faculty, Course, TestData, Question, Answer


def create_employee_kinds():
    employee_kinds = [
        {'employee_kind': 'Курсант'},
        {'employee_kind': 'Переменный состав'}
    ]

    EmployeeKind.objects.all().delete()

    for employee_kind in employee_kinds:
        EmployeeKind.objects.create(**employee_kind)


def create_faculties():
    faculties = [
        {'id': 1, 'faculty_name': 'ФКМ'},
        {'id': 2, 'faculty_name': 'ФМОБ'},
        {'id': 3, 'faculty_name': 'УИФ'},
        {'id': 4, 'faculty_name': 'СЭФ'}
    ]

    Faculty.objects.all().delete()

    for faculty in faculties:
        Faculty.objects.create(**faculty)


def create_courses():
    courses = [
        {'id': 1, 'course_name': '1'},
        {'id': 2, 'course_name': '2'},
        {'id': 3, 'course_name': '3'},
        {'id': 4, 'course_name': '4'}
    ]

    Course.objects.all().delete()

    for course in courses:
        Course.objects.create(**course)


def create_tests():
    TestData.objects.all().delete()
    test_data = [
        {'test_name': 'Тест № 1', 'extra_data': 'Первый тест', 'questions':
            [
                {'question_text': 'КАК ВЫ ОЦЕНИВАЕТЕ СВОЁ НАСТРОЕНИЕ В ПОСЛЕДНИЕ ДНИ?', 'has_multiple_choice': False,
                 'answers':
                     [
                         {
                             'answer_text': 'прекрасное настроение'
                         },
                         {
                             'answer_text': 'нормальное (обычное)'
                         },
                         {
                             'answer_text': 'испытываю напряжение, раздражение'
                         },
                         {
                             'answer_text': 'испытываю страх, тревогу'
                         },
                     ]
                 },
                {'question_text': 'КАК ИЗМЕНИЛАСЬ ЗА ПОСЛЕДНИЕ ПОЛ ГОДА ВАША ЖИЗНЬ?', 'has_multiple_choice': False,
                 'answers':
                     [
                         {
                             'answer_text': 'стала значительно лучше'
                         },
                         {
                             'answer_text': 'несколько улучшилась'
                         },
                         {
                             'answer_text': 'осталась на удовлетворительном уровне'
                         },
                         {
                             'answer_text': 'как было плохо, так и осталось'
                         },
                         {
                             'answer_text': 'несколько ухудшилась'
                         },
                         {
                             'answer_text': 'стала значительно хуже'
                         },
                     ]
                 },
                {'question_text': 'КАК БЫ ВЫ ОЦЕНИЛИ ЭКОНОМИЧЕСКОЕ ПОЛОЖЕНИЕ В СТРАНЕ?', 'has_multiple_choice': False,
                 'answers':
                     [
                         {
                             'answer_text': 'очень хорошее'
                         },
                         {
                             'answer_text': 'хорошее'
                         },
                         {
                             'answer_text': 'среднее'
                         },
                         {
                             'answer_text': 'плохое'
                         },
                         {
                             'answer_text': 'очень плохое'
                         },
                         {
                             'answer_text': 'затрудняюсь ответить'
                         },
                     ]
                 },
                {'question_text': 'КАК БЫ ВЫ ОЦЕНИЛИ СОЦИАЛЬНУЮ И ПОЛИТИЧЕСКУЮ ОБСТАНОВКУ В СТРАНЕ В ЦЕЛОМ?',
                 'has_multiple_choice': False,
                 'answers':
                     [
                         {
                             'answer_text': 'благополучная'
                         },
                         {
                             'answer_text': 'спокойная'
                         },
                         {
                             'answer_text': 'напряженная'
                         },
                         {
                             'answer_text': 'критическая, взрывоопасная'
                         },
                         {
                             'answer_text': 'затрудняюсь оценить'
                         },
                     ]
                 },
                {'question_text': 'КАК ВЫ СЧИТАЕТЕ, В ЦЕЛОМ СИТУАЦИЯ В СТРАНЕ ИЗМЕНЯЕТСЯ?',
                 'has_multiple_choice': False,
                 'answers':
                     [
                         {
                             'answer_text': 'безусловно улучшается'
                         },
                         {
                             'answer_text': 'скорее улучшается'
                         },
                         {
                             'answer_text': 'не изменяется'
                         },
                         {
                             'answer_text': 'скорее ухудшается'
                         },
                         {
                             'answer_text': 'безусловно, ухудшается'
                         },
                         {
                             'answer_text': 'затрудняюсь ответить'
                         },
                     ]
                 },
                {
                    'question_text': 'КАК ВЫ СЧИТАЕТЕ, В БЛИЖАЙШЕМ ГОДУ ВЫ (ВАШЕ ОКРУЖЕНИЕ) БУДЕТЕ ЖИТЬ ЛУЧШЕ ИЛИ ХУЖЕ, ЧЕМ СЕЙЧАС?',
                    'has_multiple_choice': False,
                    'answers':
                        [
                            {
                                'answer_text': 'значительно лучше'
                            },
                            {
                                'answer_text': 'несколько лучше'
                            },
                            {
                                'answer_text': 'ничего не поменяется'
                            },
                            {
                                'answer_text': 'несколько хуже'
                            },
                            {
                                'answer_text': 'значительно хуже'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'КАК ВЫ ДУМАЕТЕ, ЧТО ОЖИДАЕТ СТРАНУ В БЛИЖАЙШИЙ ГОД В ПОЛИТИЧЕСКОЙ СФЕРЕ?',
                    'has_multiple_choice': False,
                    'answers':
                        [
                            {
                                'answer_text': 'ситуация значительно улучшится'
                            },
                            {
                                'answer_text': 'некоторое улучшение ситуации'
                            },
                            {
                                'answer_text': 'ничего не изменится'
                            },
                            {
                                'answer_text': 'некоторое ухудшение ситуации'
                            },
                            {
                                'answer_text': 'ситуация значительно ухудшится'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'КАК ВЫ ДУМАЕТЕ, ЧТО ОЖИДАЕТ СТРАНУ В БЛИЖАЙШИЙ ГОД В ОБЛАСТИ ЭКОНОМИКИ?',
                    'has_multiple_choice': False,
                    'answers':
                        [
                            {
                                'answer_text': 'значительное улучшение ситуации'
                            },
                            {
                                'answer_text': 'некоторое улучшение ситуации'
                            },
                            {
                                'answer_text': 'ничего не изменится'
                            },
                            {
                                'answer_text': 'некоторое ухудшение ситуации'
                            },
                            {
                                'answer_text': 'значительное ухудшение ситуации'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'ЕСЛИ ГОВОРИТЬ В ЦЕЛОМ О СТРАНЕ, КАК ВЫ СЧИТАЕТЕ, В БЛИЖАЙШИЙ ГОД В СТРАНЕ БУДЕТ ЛУЧШЕ ИЛИ ХУЖЕ, ЧЕМ СЕЙЧАС?',
                    'has_multiple_choice': False,
                    'answers':
                        [
                            {
                                'answer_text': 'значительно лучше'
                            },
                            {
                                'answer_text': 'несколько лучше'
                            },
                            {
                                'answer_text': 'так же, как и сейчас'
                            },
                            {
                                'answer_text': 'несколько хуже'
                            },
                            {
                                'answer_text': 'значительно хуже'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'КАК ВЫ СЧИТАЕТЕ, КАКИЕ ИЗ СЛЕДУЮЩИХ ТЕМ НАИБОЛЕЕ ВАЖНЫ ДЛЯ ОБСУЖДЕНИЯ В ОБЩЕСТВЕ, СМИ? (предлагалось несколько вариантов выбора ответов)',
                    'has_multiple_choice': True,
                    'answers':
                        [
                            {
                                'answer_text': 'медицинской помощи и обслуживания'
                            },
                            {
                                'answer_text': 'гарантий свободы слова, доступности интернета, публикаций информации в социальных сетях;'
                            },
                            {
                                'answer_text': 'проблем алкоголизма, наркомании'
                            },
                            {
                                'answer_text': 'внесение изменений в Конституцию'
                            },
                            {
                                'answer_text': 'экологии, загрязнения окружающей среды'
                            },
                            {
                                'answer_text': 'сменяемости власти в стране'
                            },
                            {
                                'answer_text': 'вопросы социального обеспечения и гарантий'
                            },
                            {
                                'answer_text': 'коррупции в органах государственной власти'
                            },
                            {
                                'answer_text': 'состояния экономики страны'
                            },
                            {
                                'answer_text': 'действий правоохранительных органов'
                            },
                            {
                                'answer_text': 'популяризации здорового образа жизни'
                            },
                            {
                                'answer_text': 'домашнего насилия, насилия над женщинами, детьми'
                            },
                            {
                                'answer_text': 'привлечения к ответственности за участие в массовых беспорядках в 2020 г.'
                            },
                            {
                                'answer_text': 'санкционного давления коллективного запада в отношении Беларуси'
                            },
                            {
                                'answer_text': 'продвижения блока НАТО на восток'
                            },
                            {
                                'answer_text': 'военной напряженности и эскалации на границах Республики Беларусь'
                            },
                            {
                                'answer_text': 'иное'
                            },

                        ]
                },
                {
                    'question_text': 'ПОДДЕРЖИВАЕТЕ ЛИ ВЫ ДЕЙСТВИЯ СОТРУДНИКОВ ОРГАНОВ ВНУТРЕННИХ ДЕЛ ПО ПОДДЕРЖАНИЮ ОБЩЕСТВЕННОГО ПОРЯДКА В СТРАНЕ?',
                    'has_multiple_choice': False,
                    'answers':
                        [
                            {
                                'answer_text': 'да'
                            },
                            {
                                'answer_text': 'нет'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'ОТКУДА ВЫ УЗНАЕТЕ О ТЕХ ИЛИ ИНЫХ СОБЫТИЯХ, СВЯЗАННЫХ С ОБЩЕСТВЕННОЙ И ПОЛИТИЧЕСКОЙ ЖИЗНЬЮ В СТРАНЕ? (предлагалось несколько вариантов ответов)',
                    'has_multiple_choice': True,
                    'answers':
                        [
                            {
                                'answer_text': 'государственные телеканалы'
                            },
                            {
                                'answer_text': 'негосударственные телевизионные каналы'
                            },
                            {
                                'answer_text': 'новостные сайты государственных органов в сети Интернет'
                            },
                            {
                                'answer_text': 'новостные сайты негосударственных органов в сети Интернет'
                            },
                            {
                                'answer_text': 'социальные сети (VK, Telegram, Instagram, Facebook, Twitter и т.п.)'
                            },
                            {
                                'answer_text': 'YouTube-каналы, видеоблоги'
                            },
                            {
                                'answer_text': 'печатные СМИ (газеты)'
                            },
                            {
                                'answer_text': 'от руководства (инструктажи, совещания, информирование и т.д.)'
                            },
                            {
                                'answer_text': 'обсуждали в коллективе'
                            },
                            {
                                'answer_text': 'семья, друзья, соседи'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'НАСКОЛЬКО ВЫ УВЕРЕННЫ В СВОЕЙ ЛИЧНОЙ БЕЗОПАСНОСТИ В СВЯЗИ С ВЫПОЛНЕНИЕМ СВОИХ ОБЯЗАННОСТЕЙ ПО НЕСЕНИЮ СЛУЖБЫ, ОХРАНЕ ОБЩЕСТВЕННОГО ПОРЯДКА И Т. П.?',
                    'has_multiple_choice': False,
                    'answers':
                        [
                            {
                                'answer_text': 'уверен'
                            },
                            {
                                'answer_text': 'в основном уверен'
                            },
                            {
                                'answer_text': 'не очень уверен'
                            },
                            {
                                'answer_text': 'не уверен'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'НАСКОЛЬКО ВЫ УВЕРЕНЫ В БЕЗОПАСНОСТИ (ЗАЩИЩЕННОСТИ) ВАШИХ БЛИЗКИХ?',
                    'has_multiple_choice': False,
                    'answers':
                        [
                            {
                                'answer_text': 'уверен полностью'
                            },
                            {
                                'answer_text': 'в основном уверен'
                            },
                            {
                                'answer_text': 'не очень уверен'
                            },
                            {
                                'answer_text': 'не уверен'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'НАСКОЛЬКО ВЫ УВЕРЕНЫ В СВОЕЙ ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ (ЗАЩИЩЕННОСТИ ЛИЧНЫХ ДАННЫХ)?',
                    'has_multiple_choice': False,
                    'answers':
                        [
                            {
                                'answer_text': 'уверен полностью'
                            },
                            {
                                'answer_text': 'в основном уверен'
                            },
                            {
                                'answer_text': 'не очень уверен'
                            },
                            {
                                'answer_text': 'не уверен'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'КАК ВЫ ДУМАЕТЕ, ПРОИСХОДЯЩИЕ В СТРАНЕ СОБЫТИЯ СПОСОБСТВУЮТ ПОЛОЖИТЕЛЬНЫМ ИЗМЕНЕНИЯМ?',
                    'has_multiple_choice': False,
                    'answers':
                        [
                            {
                                'answer_text': 'да'
                            },
                            {
                                'answer_text': 'нет'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'ЗАДУМЫВАЛИСЬ ЛИ ВЫ НАД ТЕМ, ЧТОБЫ ОТЧИСЛИТЬСЯ И УВОЛИТЬСЯ ДО ИСТЕЧЕНИЯ СРОКА КОНТРАКТА?',
                    'has_multiple_choice': False,
                    'answers':
                        [
                            {
                                'answer_text': 'всегда'
                            },
                            {
                                'answer_text': 'часто'
                            },
                            {
                                'answer_text': 'редко'
                            },
                            {
                                'answer_text': 'никогда'
                            },
                            {
                                'answer_text': 'затрудняюсь ответить'
                            },
                        ]
                },
                {
                    'question_text': 'К ЧЬЕМУ МНЕНИЮ ВЫ В БОЛЬШЕЙ СТЕПЕНИ ПРИСЛУШИВАЕТЕСЬ ПРИ ФОРМИРОВАНИИ СОБСТВЕННЫХ ВЗГЛЯДОВ НА СОЦИАЛЬНО-ПОЛИТИЧЕСКИЕ ПРОЦЕССЫ И СИТУАЦИЮ В СТРАНЕ? (предлагалось несколько вариантов ответов)',
                    'has_multiple_choice': True,
                    'answers':
                        [
                            {
                                'answer_text': 'руководства Академии'
                            },
                            {
                                'answer_text': 'начальника факультета'
                            },
                            {
                                'answer_text': 'заместителя начальника факультета по работе с личным составом'
                            },
                            {
                                'answer_text': 'помощника начальника факультета по работе с молодежью'
                            },
                            {
                                'answer_text': 'начальника курса'
                            },
                            {
                                'answer_text': 'заместителя начальника курса'
                            },
                            {
                                'answer_text': 'старшины курса'
                            },
                            {
                                'answer_text': 'командира группы'
                            },
                            {
                                'answer_text': 'командира отделения'
                            },
                            {
                                'answer_text': 'профессорско-преподавательского состава'
                            },
                            {
                                'answer_text': 'однокурсников'
                            },
                            {
                                'answer_text': 'людей и новостных каналов из социальных сетей'
                            },
                            {
                                'answer_text': 'друзей и знакомых'
                            },
                            {
                                'answer_text': 'семьи'
                            },
                        ]
                },

            ]
         }
    ]

    for test in test_data:
        new_test = TestData.objects.create(test_name=test['test_name'], extra_data=test['extra_data'])

        questions = test['questions']

        for question in questions:
            new_question = Question.objects.create(question_text=question['question_text'],
                                                   has_multiple_choice=question['has_multiple_choice'],
                                                   test_data=new_test)
            answers = question['answers']
            for answer in answers:
                Answer.objects.create(answer_text=answer['answer_text'], question=new_question)


def init_db(apps, schema_editor):
    create_employee_kinds()
    create_faculties()
    create_courses()
    create_tests()


class Migration(migrations.Migration):
    dependencies = [
        ('test_data', '0004_employeekind_alter_questionarydata_employee_kind'),
    ]

    operations = [
        migrations.RunPython(init_db),
    ]
