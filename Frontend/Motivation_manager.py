class MotivationManager:
    def __init__(self):
        self.criteria_list = []

    def add_criteria(self, sales_volume, closed_deals, retention_level):
        criteria = MotivationCriteria(sales_volume, closed_deals, retention_level)
        self.criteria_list.append(criteria)

    def update_criteria(self, index, sales_volume, closed_deals, retention_level):
        if 0 <= index < len(self.criteria_list):
            self.criteria_list[index].update_criteria(sales_volume, closed_deals, retention_level)
