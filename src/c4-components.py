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
