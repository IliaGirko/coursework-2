from abc import ABC, abstractmethod
from typing import Any


class Vacancy(ABC):
    """Абстрактный класс получения отфильтрованной информации о вакансии"""

    @abstractmethod
    def _Vacancy__filter_vacancies(self, filter_words: str, json_answer: list[dict[Any]]) -> list[dict[Any]]:
        pass


class FilterVacancy(Vacancy):
    """Класс фильтрации(ответа с сайта) в читаемый вид"""

    __slots__ = ("filter_words", "json_answer")

    def _Vacancy__filter_vacancies(self, filter_words: str, json_answer: list[dict[Any]]) -> list[dict[Any]]:
        self.result_list: list = []
        try:
            if isinstance(filter_words, str):
                sorted_data: list[dict[Any]] = [x for x in json_answer if filter_words in x.get("name")]
                for data in sorted_data:
                    result_dict: dict[str | dict[Any]] = {
                        "Вакансия": data.get("name"),
                        "Ссылка на вакансию": data.get("alternate_url"),
                        "Зарплата": {"от": "", "до": ""},
                        "Опыт работы": data.get("experience").get("name"),
                    }
                    if not data.get("salary"):
                        result_dict["Зарплата"]["от"] = "Зарплата не указана"
                        result_dict["Зарплата"]["до"] = "Зарплата не указана"
                    elif not isinstance(data.get("salary").get("from"), int):
                        result_dict["Зарплата"]["от"] = 0
                        result_dict["Зарплата"]["до"] = data.get("salary").get("to")
                    elif not isinstance(data.get("salary").get("to"), int):
                        result_dict["Зарплата"]["от"] = data.get("salary").get("from")
                        result_dict["Зарплата"]["до"] = "Максимальный порог не указан"
                    else:
                        result_dict["Зарплата"]["от"] = data.get("salary").get("from")
                        result_dict["Зарплата"]["до"] = data.get("salary").get("to")
                    self.result_list.append(result_dict)
                return self.result_list
            else:
                return []
        except Exception as e:
            print(e)
            return []


class VacancySalary(ABC):
    """Абстрактный класс сортировки списка ваканчий по значению зарплаты ОТ"""

    @abstractmethod
    def _VacancySalary__salary_range(self, sorted_list: list[dict[Any]], user_from: int) -> list[dict[Any]] | list:
        pass


class FilterVacancySalary(VacancySalary):
    """Класс фильтрации вакансий по зарплате, значение ОТ получаем от пользователя"""

    __slots__ = ("sorted_list", "user_from")

    def _VacancySalary__salary_range(self, sorted_list: list[dict[Any]], user_from: int = 0) -> list[dict[Any]] | list:
        self.result: list = []
        try:
            for data in sorted_list:
                if data.get("Зарплата").get("от") == "Зарплата не указана":
                    continue
                elif data.get("Зарплата").get("от") >= user_from or data.get("Зарплата").get("от") == 0:
                    self.result.append(data)
            return self.result
        except Exception as e:
            print(e)
            return []

class VacancyTop(ABC):
    """Абстрактный класс сортировки списка вакансий"""

    @abstractmethod
    def _VacancyTop__sorted_top_n(self, sorted_data: list[dict[Any]], top_n: int) -> list[dict[Any]] | list:
        pass


class SortedVacancyTop(VacancyTop):
    """Класс сортирует список вакансий по убыванию"""

    __slots__ = ("sorted_data", "top_n")

    def _VacancyTop__sorted_top_n(self, sorted_data: list[dict[Any]], top_n: int = 5) -> list[dict[Any]] | list:
        try:
            result: list[dict[Any]] = sorted(sorted_data, key=lambda i: i["Зарплата"]["от"], reverse=True)
            return result[:top_n]
        except Exception as e:
            print(e)
            return []
