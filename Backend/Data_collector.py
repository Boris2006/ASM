class SalesDataCollector:
    def __init__(self):
        self.sales_data = []

    def collect_data(self, sale_record):
        self.sales_data.append(sale_record)

    def get_sales_data(self):
        return self.sales_data
