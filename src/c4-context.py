from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("ai-screen-it-С4-context", direction="TB", graph_attr=graph_attr,
             outformat=["png", "svg"]):
    doctor = Person(
        name="Врач", description="Ведет переписку с пациентом. Создает карточку для пациента, "
                                 "а затем отвечает ему, учитывая рез-т ML моделей"
    )

    patient = Person(
        name="Пациент", description="Общается с врачом. Отправляет МРТ-снимок в Redmine. Получает ответ от врача"
    )

    redmine = System(
            name="Decision Support System",
            technology="Redmine",
            description="Инструмент для комм-ции врачей и пациентов",
        )

    email = System(name="Email System",
                   description="Система уведомлений пользователей о новых сообщениях",
                   external=True)

    patient >> Relationship("Загружает МРТ-снимок, ведет переписку с врачом") >> redmine
    doctor >> Relationship("Создает карточку для пациента, ведет переписку с пациентом") >> redmine
    email >> Relationship("Уведомляет пользователя о новом сообщении в переписке") >> [patient, doctor]
    redmine >> Relationship("Запускает рассылку") >> email
