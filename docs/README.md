# Bod-detection app for VK

## Context

Система собирает информацию о пользователях из VK-Api, обучает одну из реализованных моделей и предсказывает аккаунты ботов в предоставленном наборе

Бизнес-цель: Уменьшить количество бот-трафика в VK, сделав его более безопасным местом с меньшим количеством политической пропаганды и другой активности.

Успех: Приложение позволяет обнаружить ботов в равном или более чем 80 % случаев.

# C4

<!-- ![](c4-context.svg) -->
```mermaid
C4Context
    accTitle: Bot-detection app
    accDescr: Context

    Person(person, "User", "Internet-user that wants to find out weather the people they are talking to are bots or not")

    System(web-app, "Web Application", "Realizes the logic of the application")

    System(dwh, "DWH", "Contains information about user-status and user-accounts in VKontakte")

    System(parser-app, "VK-parser", "Sends requests to VKAPI and processes recieved information")

    System(model-worker, "Model-worker", "Inferences selected models for future processing")

    
    Rel(person, web-app, "Uses")
    Rel(web-app, dwh, "TCP")
    Rel(parser-app, dwh, "TCP")
    Rel(model-worker, dwh, "TCP")
    Rel(web-app, parser-app, "HTTP")
    Rel(web-app, model-worker, "HTTP")
```

## Containers

```mermaid
C4Context
    accTitle: Bot-detection app Containers
    accDescr: Containers

    Person(person, "User", "Internet-user that wants to find out whether the people they are talking to are bots or not")

    System_Boundary(webApp, "Bot-detection app", "Realizes the logic of the application") {
        Container(frontend-app, "Web UI", "HTML", "Web UI allows users to upload account ids, train models and predict bots in VK")
        
        Container(backend-app, "Web API", "Python", "Realizes the logic of the application")
        
        ContainerDb(database, "Database", "PostgreSQL", "Contains information about user-status and user-accounts in VKontakte")

        Container(spark, "Spark", "Spark", "Processes data, involved in model training")

        Container(kafka, "Kafka", "Kafka", "Used to broker messages between containers")
        
        Container(parser-app, "VK-parser", "Python", "Sends requests to VKAPI and processes received information")
        
        Container(model-worker, "Model-worker", "Python", "Inferences selected models for future processing")
    }

    Rel(person, frontend-app, "Uses", "JSON-HTTP")
    Rel(frontend-app, backend-app, "JSON-HTTP")
    Rel(backend-app, database, "TCP")
    Rel(parser-app, database, "TCP")
    Rel(parser-app, kafka, "Writes to", "Kafka")
    Rel(kafka, spark, "Reads from", "Kafka")
    Rel(spark, database, "Writes to", "TCP")
    Rel(model-worker, database, "Reads and writes to","TCP")
    Rel(backend-app, parser-app, "Calls","HTTP")
    Rel(backend-app, model-worker, "Calls", "HTTP")

```
<!-- ![](c4-containers.svg) -->

## Components
```mermaid
C4Context
    accTitle: Bot-detection app Component
    accDescr: Components

    Person(person, "User", "Internet-user that wants to find out whether the people they are talking to are bots or not")

    Component(vkApi, "VKApi", "JSON", "vk.ru")

    ContainerDb(db, "PostgresDB", "PostgreSQL", "Stores user status and account data")
    Container(kafka, "Kafka", "Kafka", "Message broker")

    Container_Boundary(webApp, "Web App", "") {
        Component(baseApp, "Base", "HTML", "Base UI")
        Component(loadApp, "Load data", "HTML", "Upload user-data")
        Component(trainApp, "Train models", "HTML", "Choose and train model")
        Component(loadTestApp, "Load prediction data", "HTML", "Load user suspicious accounts")
        Component(predictApp, "Predict", "HTML", "Make predictions on user-accounts")
    }

    Container_Boundary(api, "Web API", "") {
        Component(modelLogic, "Models", "JSON", "Model routes")
        Component(dataLogic, "Data", "JSON", "Data routes[upload/download]")
    }

    Container_Boundary(parser, "VK API parser", "") {
        Component(getAccounts, "Get accounts", "JSON", "Request account information from VK API")
        Component(process, "Process data", "JSON", "Processes and packs user data")
        Component(producer, "Producer", "JSON", "Writes to Kafka")
    }

    Container_Boundary(spark, "Spark", "") {
        Component(read, "Read Data", "JSON", "Read Data")
        Component(processData, "Process Data", "JSON", "Process Data")
        Component(save, "Save data", "JSON", "Save Data to DB")
    }

    Container_Boundary(model-worker, "Model", "") {
        Component(model, "Model", "Python", "Model inference")
        Component(modelTrainer, "Model trainer", "Python", "Trains models")
    }

    Rel(person, baseApp, "Visits /", "HTTP")
    Rel(person, loadApp, "Visits /load", "HTTP")
    Rel(person, trainApp, "Visits /train", "HTTP")
    Rel(person, loadTestApp, "Visits /loadtest", "HTTP")
    Rel(person, predictApp, "Visits /predict", "HTTP")

    Rel(loadApp, dataLogic, "Calls", "JSON-HTTP")
    Rel(loadTestApp, dataLogic, "Calls", "JSON-HTTP")
    Rel(trainApp, modelLogic, "Calls", "JSON-HTTP")
    Rel(predictApp, modelLogic, "Calls", "JSON-HTTP")

    Rel(dataLogic, getAccounts, "Calls", "JSON-HTTP")
    Rel(modelLogic, modelTrainer, "Calls", "JSON-HTTP")
    Rel(modelLogic, model, "Calls", "JSON-HTTP")
    Rel(dataLogic, db, "Calls", "TCP")

    Rel(getAccounts, vkApi, "Calls", "JSON-HTTPS")
    Rel(producer, process, "Uses", "Python")
    Rel(process, getAccounts, "Uses", "Python")
    Rel(producer, kafka, "Writes to", "Kafka")

    Rel(read, kafka, "Reads from", "Kafka")

    Rel(processData, read, "Uses", "Spark")
    Rel(save, processData, "Uses", "Spark")
    Rel(save, db, "Writes to", "SQL")
    Rel(dataLogic, db, "Reads from", "SQL")
    
    Rel(model, db, "Writes to", "SQL")
```
<!-- ![](c4-components.svg) -->
## Use Cases

```mermaid
graph TD
    subgraph ide1 [Bot-detection App]
    create_session
    upload_data("Загрузить данные") -.-> |<< extend >>| control_session
    train("Обучить модели") -.-> |<< extend >>| control_session
    train -.-> |<< include >>| getData("Запустить обучение")
    choose("Выбрать модель") -.-> |<< extend >>| train
    run_comp("Запустить расчет по данным") -.-> |<< extend >>| control_session
    download_predictions("Загрузить предсказания") -.-> |<< extend >>| control_session
    drop_session("Удалить сессию") -.-> |<< extend >>| control_session
    end
    User("Пользователь") --- create_session("Создать сессию") 
    User --- control_session("Управлять сессией")
```


<!-- ![](uml-usecases.svg) -->
