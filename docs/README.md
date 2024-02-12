# Анализ сентимента новостей в проекте difan.xyz

Проект является экспериментальной частью стартапа [difan.xyz](https://difan.xyz/).

Планируется интегрировать аналитику новостей по акциям компании в общий аналитический отчет (основной продукт), 
а также предоставлять доступ к данным студентам экономических ВУЗов (дополнительный продукт).

В аналитику новостей пока входит анализ сентимента и различные представления этих данных, суммаризация новостей. 
С точки зрения ML это NLP-задачи классификации и суммаризации текста.

Бизнес-цель: Дополнительная полезная информация, извлекаемая из новостного фона при помощи ML-моделей, 
позволит предоставлять более подробный анализ.

Успехом считается налаженный ETL-пайплайн получения и обработки данных, 
и проработанные endpoint'ы API для вывода результатов на сайт.

## Use Cases

```mermaid
graph
    user("User") --> app("Website")
    
    app -->|main product| main("Stock analytics")
    app -->|secondary product| hse("Data terminal")

    main -->|number| sentiment("Current sentiment")
    main -->|text| news("Latest news")

    hse --> single_company("Single company")
    hse --> sector_data("List of companies / Industry sector")

    main -->|summarization| summarized_content("Summarized info")
    single_company -->|summarization| summarized_content("Summarized info")

    single_company -->|raw data| raw_single_company("Stock news with sentiment")
    single_company -->|aggregation| analyze_reviews("Aggregated news (avg. sentiment over period)")
    
    sector_data --> |aggregation| analyze_reviews("Aggregated news (avg. sentiment over period)")
```


# C4

## Context

```mermaid
C4Context
    accTitle: difan.xyz
    accDescr: Context

    Person(person, "User", "Stock analyst / Fund manager")

    System(webApp, "Website", "Provides stock reports")
    System_Ext(webAppAuth, "User Authorization", "Confirms subscription tier to authorize access")
    System(dwh, "Data Warehouse", "Data source for compiling analytical reports")
    System(processing, "Data Processing", "T in ETL - processing, ML model inference, etc.")
    System_Ext(dataSources, "Data Providers", "APIs and Stock Exchange connectors")

    Rel(person, webApp, "Search, view and export analytical reports")
    Rel(person, webAppAuth, "Login and manage subscription")
    Rel(webApp, webAppAuth, "Check access level", "OAuth2")
    Rel(dwh, webApp, "get requested data", "GET / POST")
    Rel(processing, dwh, "load processed data")
    Rel(dataSources, processing, "get raw data", "GET")
```

## Containers

```mermaid
C4Context
    accTitle: difan.xyz
    accDescr: Containers

    Person(person, "User", "Stock analyst / Fund manager")

    System_Boundary(webApp, "Website", "Provides stock reports") {
        Container(webApp, "Web Application", "HTML, PHP", "Web frontend")
        Container(api, "FastAPI", "API Gateway", "API for interacting with DWH")
        ContainerDb(db, "DWH", "MySQL", "Data source for compiling analytical reports")

        Rel(webApp, api, "Makes calls to", "JSON/HTTPS")
        Rel(api, db, "Reads from", "JSON/HTTPS")
    }

    Rel(person, webApp, "Visits", "JSON/HTTPS")

```

## Components
```mermaid
C4Context
    accTitle: Web Application
    accDescr: Components

    Person(person, "User", "Stock analyst / Fund manager")

    Container_Boundary(webApp, "Web frontend", "") {
        Component(landingApp, "Homepage", "HTML", "Landing")
        Component(searchApp, "Company search", "HTML", "Search")
    }
    
    Container_Boundary(backend, "Backend", "") {
        
        Container_Boundary(intermediary, "API", "") {
            Component(api, "FastAPI", "JSON/HTTPS", "API for interacting with DWH")
            Component(ASGI, "Uvicorn webserver", "JSON/HTTPS", "webserver running Fastapi")
        }
    
        Component(dwh, "MySQL DWH", "SQL", "Data storage")
        Component(reportBackend, "Report compiler", "SQL / Python", "Compiles requested data into a report")
        Component(etlBackend, "ETL processes", "Python / SQL", "Updates DWH with new data")
    }
    

    Container(authModule, "User Authorization", "", "Confirms subscription tier to authorize access")
    Container(etlApi, "Data API", "API Gateway", "API that provides new data for DWH")

    Rel(person, landingApp, "Visits /", "HTTPS")
    Rel(person, searchApp, "Visits /", "HTTPS")
    
    Rel(ASGI, api, "Hosting")
    
    Rel(landingApp, api, "Visits /", "HTTPS")
    Rel(searchApp, api, "Visits /", "HTTPS")

    Rel(api, reportBackend, "Passes request args into a method",)
    Rel(reportBackend, dwh, "Reads data", "SQL")
    
    Rel(reportBackend, api, "Returns report data", "JSON/.xlsx")
    Rel(api, landingApp, "Update webpage", "HTTPS")
    
    Rel(etlApi, etlBackend, "New data", "HTTPS/JSON")
    Rel(etlBackend, dwh, "Load processed data", "SQL")
    
    
    

```
