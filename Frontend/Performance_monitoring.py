from Backend.Data_users import connection_database_users


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
    
    @staticmethod
    def get_employee_rating(start_date, end_date):
        connection = connection_database_users()
        try:
            cursor = connection.cursor()
            query = """
            SELECT u.name, SUM(s.amount) as total_sales, SUM(r.motivation_bonus) as total_rewards
            FROM users u
            JOIN sales s ON u.id = s.id
            JOIN result_rewards r ON u.id = r.id
            WHERE s.date BETWEEN %s AND %s
            GROUP BY u.id, u.name
            ORDER BY total_sales DESC
            """
            cursor.execute(query, (start_date, end_date))
            results = cursor.fetchall()
            
            rating = []
            for row in results:
                rating.append({
                    'name': row[0],
                    'sales': row[1],
                    'rewards': row[2]
                })
            
            return rating
        except Exception as e:
            print(f"Ошибка при получении рейтинга сотрудников: {e}")
            return []
        finally:
            connection.close()
