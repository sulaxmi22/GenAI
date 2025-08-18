1. System Setup

Python 3.10 
VSCode + Extensions – Python, Jupyter, Copilot.
Colab / Cursor / Firebase Studio – cloud & AI IDEs.

2. API Development

FastAPI (ASGI, async support)
Uvicorn (ASGI server)
Docs → /docs (Swagger), /redoc.
Pydantic → schema validation.

3. API Concepts

GET vs POST – GET = URL params, POST = secure body.
Decorator @app.get/post – endpoint exposure.
Curl/Postman – API testing.

4. Local to Global

Ngrok → expose localhost:
ngrok http 8000

Render → cloud deploy:
requirements.txt → pip freeze > requirements.txt

Start: uvicorn app:app --host 0.0.0.0 --port $PORT

5. Git
   
Git 2.50.1 – version control.
