class PerformanceMonitoring:
    def __init__(self):
        self.performance_data = []

    def add_performance_data(self, employee_id, amount, date, type_client):
        self.performance_data.append({
            'employee_id': employee_id,
            'amount': amount,
            'date': date,
            'type_client': type_client
        })

    def visualize_performance(self):
        # Логика визуализации данных (графики, диаграммы)
        pass
