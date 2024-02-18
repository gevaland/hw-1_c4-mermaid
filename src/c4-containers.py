from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("../docs/c4-containers", direction="TB", 
             graph_attr=graph_attr, outformat="svg") as diagram:
    # customer = Person(name="Бизнес-заказчик", description="")
    user = Person(name="Пользователь")
    
    with SystemBoundary("ML конвейер"):
        hdp = Database(name="Витрина данных для моделей",
                       description="Данные в структурированном и быстродоступном формате для обучения/инференса ML моделей")
        models = Container(name="ML сервис",
                           description="Сервис для обучения/расчета ML моделей")
        


 
    with SystemBoundary("Онлайн кинотеатр"):
        front = Container(
            name="Фронтенд сервиса",
            technology="",
            description="",
        )
        back = Container(
            name="Бэкенд сервиса",
            technology="",
            description="Обрабатывает запросы пользователя и возвращает ответы микросервисов",
        )

    models << Relationship("Забирает результаты работы моделей") << back
    models >> Relationship("Сбор данных для обучения/инференса моделей") >> hdp
    hdp >> Relationship("Забирает данные для моделей") >> back

    user >> Relationship("Использует возможности онлайн-кинотеатра") >> front
    back >> Relationship("Принимает запросы пользователя") >> front
    front >> Relationship("Использует ответы микросервисов") >> back

diagram.render()  # Save diagram without opening it
