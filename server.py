from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class SimpleWebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
    # Отправляем успешный статус ответа
        self.send_response(200)

        # Меняем заголовок на text/html с указанием кодировки utf-8
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Читаем HTML-файл контактов
        filepath = os.path.join("templates", "04_contacts-page.html")
        # Убедись, что файл contacts.html лежит в той же папке, что и этот скрипт
        with open(filepath, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Отправляем содержимое клиенту, перекодировав строку в байты
        self.wfile.write(html_content.encode('utf-8'))

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleWebHandler)
    print(f"Сервер успешно запущен на http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")

if __name__ == '__main__':
 run_server()
