import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = os.path.basename(file_path)
        headers = {"Authorization": f"OAuth {self.token}"}
        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            headers=headers,
            params={"path": file_name, "overwrite": "true"},
        )
        response.raise_for_status()

        upload_url = response.json()["href"]
        with open(file_path, "rb") as f:
            upload_response = requests.put(upload_url, files={"file": f})
            print(upload_response)
            upload_response.raise_for_status()

        print(f"Файл {file_name} успешно загружен на Яндекс.Диск.")

if __name__ == '__main__':
    path_to_file = input("Введите путь к файлу: ")
    token = input("Введите ваш OAuth-токен: ")

    uploader = YaUploader(token)
    uploader.upload(path_to_file)