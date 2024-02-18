from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("ai-screen-it-С4-container", direction="TB", graph_attr=graph_attr,
             outformat=["png", "svg"]):
    doctor = Person(
        name="Врач", description="Ведет переписку с пациентом. Создает карточку для пациента, "
                                 "а затем отвечает ему, учитывая рез-т ML моделей"
    )

    patient = Person(
        name="Пациент", description="Общается с врачом. Отправляет МРТ-снимок в Redmine. Получает ответ от врача"
    )

    with SystemBoundary("Decision Support System"):
        redmine = Container(name="Redmine",
                            technology="Redmine",
                            description="ПО для коммуникации врачей и пациентов")

        kafka = Container(
            name="Kafka",
            technology="Apache Kafka",
            description="Инструмент для передачи потоков данных в реальном времени"
        )

        spark = Container(
            name="Spark",
            technology="Apache Spark",
            description="Фреймворк для обработки больших объемов данных"
        )

        py_api = Container(
            name="Python API",
            technology="FastAPI",
            description="API для взаимодействия с Email System"
        )

        hadoop = Container(
            name='Hadoop',
            technology='Hadoop',
            description="Фреймворк для хранения больших объемов данных"
        )

        dwh = Database(
            name="Data WareHouse",
            technology="SQL",
            description="Хранение данных для аналитиков, Data Marts"
        )

    email = System(name="Email System",
                   description="Система уведомлений пользователей о новых сообщениях",
                   external=True)

    patient >> Relationship("Загружает МРТ-снимок") >> redmine
    doctor >> Relationship("Создает карточку для пациента") >> redmine
    email >> Relationship("Уведомляет пользователя о новом сообщении в переписке") >> [patient, doctor]

    redmine >> Relationship("Передает снимок на обработку") >> kafka
    kafka >> Relationship("Возвращает ответ моделей") >> redmine

    kafka >> Relationship("Передает снимок на обработку") >> spark
    spark >> Relationship("Возвращает ответ моделей") >> kafka

    kafka >> Relationship("Передает снимок в хранилище HDFS") >> hadoop
    kafka >> Relationship("Триггерит запуск рассылки") >> py_api

    py_api >> Relationship("Запускает рассылку") >> email

    spark >> Relationship("Сохраняет результаты моделей") >> dwh
    hadoop >> Relationship("Передает данные для витрин") >> dwh
