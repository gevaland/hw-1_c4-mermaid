from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("docs/c4-components", direction="TB", 
             graph_attr=graph_attr, outformat="svg") as diagram:
    user = Person(name="Пользователь")
    
    with SystemBoundary("ML конвейер"):
        with SystemBoundary("ML сервис"):
            spark = Container(name="Spark Applications", technology="Spark", description="Запуск ML моделей")
            airflow = Container(name="Airflow", technology="", description="Оркестрация ML конвейера")
            mlflow = Container(name="mlflow", technology="", description="Хранение ML моделей, метрик")
        hdp = Database(name="Витрина данных для моделей", 
                       technology="HDFS",
                       description="Данные в структурированном и быстродоступном формате для обучения/инференса ML моделей")
        



    with SystemBoundary("Онлайн кинотеатр"):
        front = Container(name="Фронтенд сервиса", 
                          description="")
        with SystemBoundary("Бэкенд сервиса"):
            back = Container(name="Бэкенд сервисы",
                            techology="Not specified",
                            description="")
            kafka = Container(name="Потоковая обработка данных", technology="Apache Kafka", description="Передает большие объемы данных (логи действий и т.д.) в хранилище")
            dwh = Database(name="DataLake", technology="Databricks Lakehouse", description="Данные сервиса в неструктурированном формате")

    user >> Relationship("Использует фронтенд") >> front
    back >> Relationship("Забирает данные с фронта") >> front
    front >> Relationship("Забирает результаты работы сервисов, моделей") >> back
    kafka >> Relationship("Переносит данные") >> back


    dwh >> Relationship("Сохраняет данные в Data Lake") >> kafka
    hdp >> Relationship("Переносит данные в HDFS") >> kafka
    back >> Relationship("Забирает нужные данные из хранилища") >> dwh

    spark << Relationship("Использует данные из витрины") << hdp
    # spark >> Relationship("Запускает spark приложения") >> airflow
    airflow >> Relationship("Запускает spark приложения") >> spark

    mlflow >> Relationship("Сохраняет обученные модели") >> spark
    spark >> Relationship("Использует ML модели из mlflow") >> mlflow


    # Add relationships to show the flow of results to downstream applications
    spark << Relationship("Сохраняет результаты в DataLake") << dwh

diagram.render()