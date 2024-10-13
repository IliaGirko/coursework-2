import json
from abc import ABC, abstractmethod
from typing import Any


class JSON(ABC):
    """Абстрактный класс для взаимодействия с файлом в формате json"""

    @abstractmethod
    def dump_vacancies(self, result: list[dict[Any]], file_name: str = "vacancy") -> None:
        pass

    @abstractmethod
    def load_vacancies(self, file_name: str = "vacancy") -> list | list[dict[Any]]:
        pass

    @abstractmethod
    def del_vacancy(self, file_name: str = "vacancy") -> None:
        pass


class WorkToJSON(JSON):
    """Класс для работы с файлами типа json"""

    __slots__ = "result"

    def load_vacancies(self, file_name: str = "vacancy") -> list | list[dict[Any]]:
        """Метод чтения json файла"""
        try:
            with open(f"data/{file_name}.json", "r", encoding="UTF-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except Exception:
            return []

    def dump_vacancies(self, result: list[dict[Any]], file_name: str = "vacancy") -> None:
        """Загружает отфильтрованный и сортированный список вакансий в json файл,
        можно задать имя файла, или использовать стандартное"""
        try:
            self.__file_name = file_name
            data = self.load_vacancies(self.__file_name)
            data.extend(result)
            with open(f"data/{self.__file_name}.json", "w", encoding="UTF-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception:
            print("Введено не корректное имя для файла")

    def del_vacancy(self, file_name: str = "vacancy") -> None:
        """Метод очищает файл, но не удаляет его"""
        try:
            with open(f"data/{file_name}.json", "w"):
                pass
        except Exception as e:
            print(e)
