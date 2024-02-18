from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("ai-screen-it-С4-component", direction="TB", graph_attr=graph_attr,
             outformat=["png", "svg"]):
    doctor = Person(
        name="Врач", description="Ведет переписку с пациентом. Создает карточку для пациента, "
                                 "а затем отвечает ему, учитывая рез-т ML моделей"
    )

    patient = Person(
        name="Пациент", description="Общается с врачом. Отправляет МРТ-снимок в Redmine. Получает ответ от врача"
    )

    with SystemBoundary("Decision Support System"):
        with SystemBoundary("Redmine Container"):
            redmine_ui = Container(name="Redmine UI",
                                   technology="JavaScript",
                                   description="Пользоват.интерфейс Redmine")

            redmine_api = Container(name="Redmine API",
                                    technology="Redmine back-end",
                                    description="API Redmine")

        with SystemBoundary("Kafka Container"):
            brokers = Container(
                name="Brokers",
                technology="Apache Kafka Brokers",
                description="Серверы для потоковой передачи данных"
            )

        with SystemBoundary("Spark Container"):
            ml_models = Container(
                name="ML models",
                description="Сервис для инференса ML моделей"
            )

        py_api = Container(
            name="Python API",
            technology="FastAPI",
            description="API для взаимодействия с Email System"
        )

        with SystemBoundary("Hadoop Container"):
            hdfs = Container(
                name='HDFS',
                technology='HDFS',
                description="Файловая система для хранения больших данных"
            )

        dwh = Database(
            name="Data WareHouse",
            technology="SQL",
            description="Хранение данных для аналитиков, Data Marts"
        )

    email = System(name="Email System",
                   description="Система уведомлений пользователей о новых сообщениях",
                   external=True)

    patient >> Relationship("Загружает МРТ-снимок") >> redmine_ui
    doctor >> Relationship("Создает карточку для пациента") >> redmine_ui
    email >> Relationship("Уведомляет пользователя о новом сообщении в переписке") >> [patient, doctor]

    redmine_ui >> Relationship("Передает снимок из фронта на бек Redmine") >> redmine_api
    redmine_api >> Relationship("Возвращает ответ модели в UI") >> redmine_ui

    redmine_api >> Relationship("Передает снимок на обработку") >> brokers
    brokers >> Relationship("Возвращает ответ моделей") >> redmine_api

    brokers >> Relationship("Передает снимок на обработку") >> ml_models
    ml_models >> Relationship("Возвращает ответ моделей") >> brokers

    brokers >> Relationship("Передает снимок в хранилище HDFS") >> hdfs
    brokers >> Relationship("Триггерит запуск рассылки") >> py_api

    py_api >> Relationship("Запускает рассылку") >> email

    ml_models >> Relationship("Сохраняет результаты моделей") >> dwh
    hdfs >> Relationship("Передает данные для витрин") >> dwh
