from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import User, Users, TraditionalServer

with Diagram("docs/usecases", outformat="svg"):

    # Define actors
    business_customer = User("Бизнес-заказчик")
    ml_team = Users("МЛ команда")
    ml_service = TraditionalServer("Сервис ML Моделей")
    online_cinema = TraditionalServer("Онлайн-кинотеатр")

    # Define relations
    with Cluster("Use Cases"):
        business_customer >> Edge(color="black", style="dashed", label="Направляет гипотезы") >> ml_team
        business_customer >> Edge(color="black", style="dashed", label="Заказчик обращается к онлайн-кинотеатру для оценки эффекта") >> online_cinema
        ml_team >> Edge(color="black", style="dashed", label="Разработка и обучение ML моделей") >> ml_service
        ml_service >> Edge(color="black", style="dashed", label="Развертывание ML моделей в онлайн-кинотеатр") >> online_cinema
