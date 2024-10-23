from Backend.Data_users import connection_database_users


class ReportGenerator:
    def analyze_max_min_sales(self, criteria):
        # Логика формирования результата по наибольшему объёму продаж
        pass

    def analyze_sales_by_product(self, products_id):
        # Анализ по продуктам
        pass

    def analyze_type_of_client(self, retention_levels):
        # Анализ по типам клиентов
        pass

    def analyze_volume_of_bonuses(self, bonuses):
        # Анализ по количеству бонусов за год
        pass

    @staticmethod
    def generate_report(start_date, end_date):
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
            
            report = f"Отчет о мотивационных выплатах с {start_date} по {end_date}:\n\n"
            for row in results:
                report += f"Сотрудник: {row[0]}\n"
                report += f"Общие продажи: {row[1]}\n"
                report += f"Общие выплаты: {row[2]}\n\n"
            
            return report
        except Exception as e:
            print(f"Ошибка при генерации отчета: {e}")
            return "Не удалось сгенерировать отчет"
        finally:
            connection.close()
