from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/run_code")
async def run_code(code: str):
    # Создаем python файл с переданным кодом
    with open("user_code.py", "w") as file:
            file.write(code)

    # Запускаем python файл
    result = subprocess.run(['python', 'user_code.py'], capture_output=True, text=True)

    # Сравниваем результат выполнения с заранее предустановленным ответом
    expected_result = "" # получаем заданные преподавателем ответы
    if result.stdout.strip() == expected_result:
        return {"message": "Выполнение кода успешно и результат совпадает с ожидаемым"}
    else:
        return {"message": "Выполнение кода успешно, но результат не совпадает с ожидаемым"}