from Frontend.Motivation_criteria import MotivationCriteria


class MotivationManager:
    def __init__(self):
        self.criteria_list = []

    def add_criteria(self, sales_volume, closed_deals, retention_level):
        criteria = MotivationCriteria(sales_volume, closed_deals, retention_level)
        self.criteria_list.append(criteria)

    def update_criteria(self, index, sales_volume, closed_deals, retention_level):
        if 0 <= index < len(self.criteria_list):
            self.criteria_list[index].update_criteria(sales_volume, closed_deals, retention_level)
    
    def update_motivation_criteria():
        sales_volume = int(input("Введите объем продаж: "))
        closed_deals = int(input("Введите количество закрытых сделок: "))
        retention_level = input("Введите уровень удержания клиентов: ")
        start_date = input("Введите начальную дату (YYYY-MM-DD): ")
        end_date = input("Введите конечную дату (YYYY-MM-DD): ")
        
        if MotivationCriteria.set_criteria(sales_volume, closed_deals, retention_level, start_date, end_date):
            print("Критерии мотивации успешно обновлены")
        else:
            print("Не удалось обновить критерии мотивации")
