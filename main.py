from src.interaction_with_api import HeadHunterAPI
from src.interaction_to_json_file import WorkToJSON
from src.vacancy import FilterVacancy, FilterVacancySalary
from src.answers_vacancy import answer

from typing import Any

def main() -> None:
    """Функция взаимодействия с пользователем"""
    try:
        search_query = input("Введите поисковый запрос: ")# Пример: Python
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ") # Пример: Python
        salary_range_from = int(input("Введите диапазон зарплаты от: "))  # Пример: 100000
        top_n = int(input("Введите топ сколько вакансий вывести: ")) # Пример: 5
        file_name = input("Введите название для файла в который сохранить результат поиска: \n")  # Пример: "vacancy"

        hh_api = HeadHunterAPI()
        data_load = WorkToJSON()
        filter_hh = FilterVacancy()
        filter_salary_hh = FilterVacancySalary()

        json_answer: list[dict[Any]] = hh_api.json_list(search_query)
        if file_name == "":
            data_load.dump_vacancies(json_answer)
        else:
            data_load.dump_vacancies(json_answer, file_name)
        sorted_list: list[dict[Any]] = filter_hh._Vacancy__filter_vacancies(filter_words, json_answer)
        result_list: list[dict[Any]] = filter_salary_hh._VacancySalary__salary_range(sorted_list, salary_range_from)
        result_end = answer(result_list, top_n)
        if result_end == []:
            print("По заданным критериям не найдено ни одной вакансии для отображения")

        if file_name == "":
            data_load.dump_vacancies(result_end)
        else:
            data_load.dump_vacancies(result_end, file_name)

        user_answer = input("Хотите удалить вакансии?\nВведите: да или нет ").lower()

        if user_answer == "Да" and file_name == "":
            data_load.del_vacancy()
        elif user_answer == "Да":
            data_load.del_vacancy(file_name)
    except Exception:
        print("Введены некорректные данные")

if __name__ == "__main__":
    main()
