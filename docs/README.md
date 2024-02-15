# Manuspect
Виртуальный помощник Manuspect, предназначенный для автоматизации повседневных задач, увеличения эффективности и продуктивности работы, а также оптимизации workflow. Целевая аудитория: фрилансеры, офисные работники, маркетологи, DS специалисты.

Успехом считается работающая модель process mining.

## Use Cases


```mermaid
graph TD
    user("Пользователь") -->|include| app("Приложение")
    app -->|include| comp("Сравнивать разные компании")
    app -->|include| models("Сравнивать разные модели")
    app -->|include| sources("Сравнивать разные источники")

    comp -->|include| get_comp_list("Получать список компаний")
    models -->|include| get_models("Получать модели")
    models -->|extend| add_models("Добавлять модели")
    sources -->|include| get_sources("Получать источники")
    sources -->|extend| add_sources("Добавлять источник")

    comp -->|include| analyze_reviews("Анализировать отзывы на компанию")
    analyze_reviews -->|include| get_text_analysis("Получить результат анализа текста")
    get_text_analysis -->|include| add_text_analysis("Добавить результат анализа текста")
    add_text_analysis -->|include| add_text("Добавить текст")

```


```mermaid
graph TD
    user("User") -->|include| app("Manuspect App")
    app -->|include| track("Task Tracking")
    track -->|include| define("Define Workflow")
    define -->|include| collectData("Collect Workflow Data")
    define -->|extend| formGraph("Form Workflow Graph")
    define -->|extend| decomposeGraph("Decompose Graph Into Tasks")
    track -->|include| measure("Measure Tasks")
    measure -->|include| assignResources("Assign Resources")
    track -->|include| analyze("Analyze Workflow")
    analyze -->|include| identifyOptimizations("Identify Optimizations")
    analyze -->|extend| planOptimizations("Plan Optimizations")
    analyze -->|include| accumulateResources("Accumulate Resources Statistics")
    
    app -->|include| improve("KPI Improvement")
    improve -->|include| delegate("Delegate Tasks")
    delegate -->|include| automateTasks("Automate Tasks")
    delegate -->|extend| handoverTasks("Hand Over Tasks")
    improve -->|include| improveWorkflow("Improve Workflow Based on AI Recommendations")
    
    app -->|include| control("Automation & KPI Control")
    control -->|include| deploy("Deploy Automations")
    control -->|include| manage("Manage Automations")
    control -->|include| controlKPIs("Control KPIs")
    control -->|extend| displayStats("Display Resource Statistics")
    control -->|extend| controlWorkflow("Control Workflow After Automations")
    controlWorkflow -->|include| interactiveUI("Interactive UI for Automations")

    app -->|include| assistant("Virtual Assistant")
    assistant -->|include| guide("Guide Through Processes")
    assistant -->|extend| recommend("Provide Recommendations")
    assistant -->|extend| analyzeUserFlow("Analyze UserFlow")
    assistant -->|extend| reduceRepetitiveProcesses("Help to Reduce Repetitive Processes")
```
# C4

## Context

```mermaid
C4Context
    accTitle: Manuspect service
    accDescr: Context
    
    Person(person, "Customer", "Customer who want to monitor and optimize workflow")
    System(crossPlatformApp, "Cross Platform App", "Allows customers to monitor and optimize workflow")
    System(ProcessMining, "ProcessMining", "Multiple independent services handling business features.")
    System(dwh, "Data Warehouse", "Databases for storing application data.")
    System(OpenAI, "OpenAI", "Underlying ML and AI technologies")

    Rel(person, crossPlatformApp, "Monitor and optimize workflow")
    Rel(crossPlatformApp, ProcessMining, "Utilizes Technology", "Broker")
    Rel(crossPlatformApp, OpenAI, "Utilizes Technology", "Broker")
    Rel(crossPlatformApp, dwh, "Stores/retrieves data", "Broker")
```

## Containers

```mermaid
C4Context
    accTitle: Manuspect service System
    accDescr: Containers

    Person(person, "Customer", "Customer who want to monitor and optimize workflow")

    System_Boundary(crossPlatformApp, "Cross Platform App", "Allows customers to monitor and optimize workflow") {
        Container(crossPlatformApp, "Cross Platform App", "FLutter", "Cross Platform App for buying a product")
        Container(api, "API Application", "API Gateway", "API that manages product details")
        ContainerDb(db, "Database", "PostgreSQL", "Tables to store product and customer data")
        Container(spark, "Spark", "Spark", "Data processing")
        Container(kafka, "Kafka", "Kafka", "Message broker")
        Container(microservices, "Microservices", "Python", "Multiple independent services handling business features.")
        Container(ProcessMining, "ProcessMining", "Multiple independent services handling business features.")
        Container(dwh, "Data Warehouse", "Databases for storing application data.")
        Container(OpenAI, "OpenAI", "Underlying ML and AI technologies")

        Rel(crossPlatformApp, api, "Makes calls to", "JSON-HTTP")
        Rel(api, microservices, "Interacts with", "Broker")
        Rel(microservices, kafka, "Writes to", "Kafka")
        Rel(microservices, db, "Reads and writes to", "SQL")
        Rel(kafka, microservices, "Writes to", "Kafka")
        Rel(microservices, ProcessMining, "Utilizes Technology", "Broker")
        Rel(microservices, OpenAI, "Utilizes Technology", "Broker")
        Rel(microservices, dwh, "Stores/retrieves data", "Broker")
        Rel(microservices, spark, "Reads from", "Kafka")
        Rel(spark, db, "Reads and writes to", "SQL")
    }

    Rel(person, crossPlatformApp, "Visits", "JSON-HTTP")
```

## Components
```mermaid
C4Context
    accTitle: Cross Platform App Container
    accDescr: Components

    Person(person, "Customer", "Customer who want to check ethcis of companies")

    Container_Boundary(crossPlatformApp, "Cross Platform App", "") {
        Component(reviewsStatsApp, "Reviews Stats", "Flutter", "Reviews Stats")
        Component(companiesEthicsApp, "Companies Ethics", "Flutter", "Companies Ethics")
    }
```