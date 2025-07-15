from django.db import connection

def load_query(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()
    
def use_cursor(query: str, params: list[str] | None = None):
    with connection.cursor() as cursor:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        columns = [col[0] for col in cursor.description]  # type: ignore
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
def use_cursor_raw_fetchall(query, params: list[str] | None = None):
    with connection.cursor() as cursor:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()