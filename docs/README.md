# Анализ этичности компаний на основании отзывов

Система будет собирать отзывы с сайтов, затем на основании отзывов будут ставится оценки компаниям.

# C4

## Context

```mermaid
C4Context
    accTitle: Shop
    accDescr: Context

    Person(person, "Customer", "Customer who is buying a product online")

    System(webApp, "Shop", "Allows customers to search, view and purchase products")
    System_Ext(emailPlatform, "Email Platform", "Email marketing platform")
    System_Ext(cdp, "Customer Data Platform", "Customer profiling")
    System(dwh, "Data Warehouse", "Reporting and data insights")

    Rel(person, webApp, "Search, view and purchase products", "JSON-RPC")
    Rel(webApp, cdp, "Send customer interaction and domain events to")
    Rel(cdp, emailPlatform, "Send email using")
    Rel(emailPlatform, person, "Sends email to", "SMTP")
    Rel(webApp, dwh, "Domain events", "Broker")
```

## Containers

```mermaid
C4Context
    accTitle: Shop System
    accDescr: Containers

    Person(person, "Customer", "Customer who is buying a product online")

    System_Boundary(webApp, "Shop", "Allows customers to search, view and purchase products") {
        Container(webApp, "Web Application", "HTML", "Web frontend for buying a product")
        Container(api, "API Application", "API Gateway", "API that manages product details")
        ContainerDb(db, "Database", "DynamoDB", "Tables to store product and customer data")

        Rel(webApp, api, "Makes calls to", "JSON-RPC")
        Rel(api, db, "Reads and writes to", "JSON-RPC")
    }

    Rel(person, webApp, "Visits", "JSON-RPC")
```

## Components
```mermaid
C4Context
    accTitle: Web Application Container
    accDescr: Components

    Person(person, "Customer", "Customer who is buying a product online")

    Container_Boundary(webApp, "Web Application", "") {
        Component(landingApp, "Homepage", "HTML", "Landing")
        Component(searchApp, "Search", "HTML", "Search")
        Component(productApp, "Product Details", "HTML", "Product Details")
        Component(orderApp, "Orders", "HTML", "Orders")
    }

    System_Ext(cms, "CMS", "Content Management System")
    Container(searchApi, "Search API", "API Gateway", "API that provides product filtering")
    Container(productApi, "Product API", "API Gateway", "API that manages product details")
    Container(orderApi, "Orders API", "API Gateway", "API that manages customer orders")

    Rel(person, landingApp, "Visits /", "HTTPS")
    Rel(landingApp, cms, "Makes calls to")
    Rel(person, searchApp, "Visits /search", "HTTPS")
    Rel(searchApp, searchApi, "Makes calls to", "JSON/HTTPS")
    Rel(person, productApp, "Visits /product/{id}", "HTTPS")
    Rel(productApp, productApi, "Makes calls to", "JSON/HTTPS")
    Rel(person, orderApp, "Visits /basket", "HTTPS")
    Rel(orderApp, orderApi, "Makes calls to", "JSON/HTTPS")
```


# UML UC + SysML REQ

## Use Cases

```mermaid
flowchart TD
    A[Customer] --> B(Go shopping)
```

## Requirements

```mermaid
requirementDiagram

    requirement Trading Requirement {
        id: 1
        text: Make online trading
        risk: high
        verifymethod: test
    }

    element Shop System {
        type: Software
    }

    Shop System - satisfies -> Trading Requirement
```