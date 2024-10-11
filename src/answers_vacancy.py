from typing import Any

from src.vacancy import SortedVacancyTop


def answer(result_list, top_n):
    svt = SortedVacancyTop()
    try:
        result: list[dict[Any]] = svt._VacancyTop__sorted_top_n(result_list, top_n)
        for i in result:
            print(
                f"Вакансия: \n{i["Вакансия"]}"
                f"\nСсылка на вакансию: \n{i["Ссылка на вакансию"]}"
                f"\nЗарплата: \nот {i["Зарплата"]["от"]} до {i["Зарплата"]["до"]}"
                f"\nТребование опыта работы: \n{i["Опыт работы"]}\n"
                )
        return result
    except Exception as e:
        print(e)
        return []