from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import User, Users, GenericDatabase, TraditionalServer

with Diagram("Use Case Diagram", show=True):

    # Define actors
    business_customer = User("Бизнес-заказчик")
    ml_team = Users("МЛ команда")
    data_storage = GenericDatabase("Хранилище данных")
    analytical_layer = TraditionalServer("Аналитический слой")

    # Define relations
    with Cluster("Отношения"):
        business_customer >> Edge(color="black", style="dashed", label="Направляет гипотезы") >> ml_team
        business_customer >> Edge(color="black", style="dashed", label="Заказчик обращается к аналитическому слою для оценки эффекта") >> analytical_layer
        ml_team >> Edge(color="black", style="dashed", label="Получение данных из хранилища") >> data_storage
        ml_team >> Edge(color="black", style="dashed", label="Разработка решений в аналитический слой") >> analytical_layer
        analytical_layer >> Edge(color="black", style="dashed", label="Получение данных из хранилища") >> data_storage
