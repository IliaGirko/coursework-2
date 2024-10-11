from abc import ABC, abstractmethod
from typing import Any

import requests


class ImportAPI(ABC):
    """Абстрактный класс импорта с использованием API"""

    @abstractmethod
    # """Абстрактный метод получения ответа от API"""
    def _ImportAPI__get_vacancies(self, keyword: str) -> dict[list[dict[Any]]]:
        pass

    @abstractmethod
    # """Абстрактный метод преобразование ответа от API в json формат"""
    def json_list(self, keyword: str) -> list[dict[Any]]:
        pass


class HeadHunterAPI(ImportAPI):
    """Класс работы с API head hunter"""

    def __init__(self):
        self.__url: str = "https://api.hh.ru/vacancies"
        self.__params: dict[str | int] = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: list = []

    def _ImportAPI__get_vacancies(self, keyword: str) -> dict[Any | list[dict[Any]]]:
        """В методе получаются данные с сайта HH.ru'"""
        if isinstance(keyword, str):
            self.__params["text"] = keyword
            response: dict[Any | list[dict[Any]]] = requests.get(self.__url, params=self.__params)
            if response.status_code == 200:
                return response
            else:
                raise Exception("Не удалось подключиться к API HH")
        else:
            raise AttributeError("Введен не корретный запрос")

    def json_list(self, keyword) -> list[dict[Any]]:
        """В методе происходит фильтрация данных полученных с сайта HH.ru по ключу 'items'"""
        return self._ImportAPI__get_vacancies(keyword).json().get("items")
