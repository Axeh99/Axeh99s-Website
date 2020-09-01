from app import create_app

app = create_app()

if __name__ == "__main__":
    print("DEVELOPMENT MODE")
    app.run(port=80, debug=True)
