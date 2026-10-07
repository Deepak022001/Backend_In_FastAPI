from fastapi import FastAPI
from fastapi import Request
import uvicorn

app=FastAPI(
    title="Swiggy Order Service",
    description=(
        "Internal Api for mangaing orders"
        "Handle creation,tracking of delivery systems"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@app.get("/")
def read_root():
    """Root endpoint - Health check"""
    # FastApi converts this dic to json automatically
    return {"message":"Welcome to swiggy order service",
            "status":"healthy"}

@app.get("/about")
def about():
    """Returns API metadata"""
    return{
        "service":"order-service",
        "team":"backend platform",
        "region":"ap-south-1"
    }

@app.get("/orders")
def list_orders():
    """List recent orders"""
    return{
        "orders":[
            {"id":1,"item":"Butter Chicken","status":"delivered"},
            {"id":2,"item":"Masala chicken","status":"preparing"},
            {"id":3,"item":"amul butter","status":"delivered"},
        ]
    }

@app.get("/orders/status")
def order_status():
    """GET order status"""
    return {
        "total_today":2_340_23,
        "top_city":"Bengaluru"
    }

@app.get("/debug/request-info")
async def request_info(request:Request):
    """Inspect the raw request object"""
    return {
        "method":request.method,
        "url":str(request.url),
        "headers":dict(request.headers),
        "path_params":request.path_params,
        "query":dict(request.query_params)
    }