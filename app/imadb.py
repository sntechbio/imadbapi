from app.controllers.imadb_all_controllers import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:controllers.imadb_all_controllers.app", reload=True)
