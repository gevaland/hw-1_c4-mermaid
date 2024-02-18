from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("../docs/c4-context", direction="TB", graph_attr=graph_attr):
    # customer = Person(name="Бизнес-заказчик", description="")
    user = Person(
        name="Пользователь"
    )
    ml_service = System(name="ML конвейер", 
                        description="Позволяет продуктивизировать  модели", 
                        external=False)
    
    mainframe = System(
        name="Онлайн кинотеатр",
        description="ПО, данные, инфраструктура онлайн-кинотеатра",
        external=True,
    )

    # customer >> Relationship("Направляет гипотезы/задачи для реализации") >> ml_service
    # ml_service >> Relationship("Предоставляет данные для оценки эффекта") >> customer

    ml_service >> Relationship("Использует данные кинотеатра для разработки моделей") >> mainframe
    mainframe >> Relationship("Использует результаты работы ML моделей") >> ml_service

    user >> Relationship("Использует возможности онлайн-кинотеатра") >> mainframe