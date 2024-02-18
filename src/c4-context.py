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
