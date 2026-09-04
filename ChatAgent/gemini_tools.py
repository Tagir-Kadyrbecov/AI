import requests


class GeminiTools:
    @staticmethod
    def gemini_request_to_create_new_user(username: str, email: str, password: str):
        """
    Регистрирует нового пользователя в системе через REST API.

    Args:
        username: Полное имя пользователя (например, "Иван Иванов").
        email: почта.
        password: пароль.
        все они типа str
        """
        payload = {
            "username": username,
            "email": email,
            "password": password
        }
        response = requests.post("http://127.0.0.1:8000/user", json=payload)
        return response.text
