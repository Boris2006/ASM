class MotivationCriteria:
    def __init__(self, sales_volume, closed_deals, retention_level, start_date, end_date):
        self.sales_volume = sales_volume
        self.closed_deals = closed_deals
        self.retention_level = retention_level
        self.start_date = start_date
        self.end_date = end_date

    def update_criteria(self, sales_volume, closed_deals, retention_level, start_date, end_date):
        self.sales_volume = sales_volume
        self.closed_deals = closed_deals
        self.retention_level = retention_level
        self.start_date = start_date
        self.end_date = end_date