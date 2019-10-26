// Hello World 是所有語言的第一步，在 terminal 上印出
console.log("Hello World");

// 第一個 Node.js 應用，使用 http.createServer() 創建服務器，並使用 listen() 監聽 8888 port，函數通過 request, response 兩個參數接收和回應 

// 使用 HTTP 模組建立 Web 應用前須用 require 載入此模組並指定一個變數接收傳回之 HTTP 物件
var http = require("http");

/* HTTP 物件主要的兩個屬性
   status_codes : 定義回應碼
   methods : 定義 get, post, deletc, update 等 HTTP 協定方法
   HTTP 回應碼常見為 200 (正常), 404 (網頁或資源不存在), 500 (伺服器內部錯誤) 等
   Node 將全部 HTTP 回應碼放在 http.status_codes 屬性中
*/

// createServer([callback])
// 建立 HTTP 伺服器, 傳回 Server 物件，callback = 監聽 HTTP 請求事件之回呼函數, 攜帶 2 個參數：ServerRequest (請求物件), ServerResponse (回應物件)
http.createServer(function(request, response){
    response.writeHead
}).listen(8888);

console.log('Server running at http://127.0.0.1:8888/');