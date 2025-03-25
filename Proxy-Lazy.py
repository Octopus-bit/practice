class Server:
    def handle_request(self, request):
        # پردازش درخواست
        return f"Request '{request}' processed."

class LoggingProxy:
    def __init__(self, server):
        self._server = server

    def handle_request(self, request):
        # ثبت درخواست
        self.log_request(request)
        # پردازش درخواست از طرف سرور
        response = self._server.handle_request(request)
        # ثبت پاسخ
        self.log_response(response)
        return response

    def log_request(self, request):
        print(f"Logging request: {request}")

    def log_response(self, response):
        print(f"Logging response: {response}")

# مثال از استفاده
if __name__ == "__main__":
    # ایجاد سرور
    server = Server()
    
    # ایجاد Proxy
    proxy = LoggingProxy(server)
    
    # ارسال درخواست‌ها
    print(proxy.handle_request("Request 1"))  # این درخواست و پاسخ آن لاگ می‌شود
    print(proxy.handle_request("Request 2"))  # این درخواست و پاسخ آن لاگ می‌شود