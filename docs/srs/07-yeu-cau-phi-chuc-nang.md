[← Mục lục SRS](README.md)

# 7. Yêu cầu phi chức năng

## 7.1 Hiệu năng

| **Mã** | **Yêu cầu**                                                                                                                  | **Mức**                              |
|--------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| NFR-P1 | Tối ưu để tránh độ trễ và sập hệ thống khi nhiều người dùng truy cập. Trang chính tải trong ≤ 3 giây trên mạng thông thường. | (đề xuất)                            |
| NFR-P2 | Hỗ trợ tối thiểu **100 người dùng đồng thời** mà không có độ trễ lớn (thời gian phản hồi API \< 1 giây)                      | (đề xuất, đã chốt cho phạm vi đồ án) |
| NFR-P3 | Bản đồ chỉ tải ghim trong vùng đang xem, tối đa 500 ghim mỗi lần.                                                            | (đề xuất)                            |
| NFR-P4 | Danh sách phân trang, mỗi trang 20 mục; ảnh dùng bản thu nhỏ trong danh sách và tải ảnh gốc khi xem chi tiết.                | (đề xuất)                            |

## 7.2 Bảo mật

| **Mã** | **Yêu cầu**                                                                                                                                                                                                    | **Mức**  |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| NFR-S1 | Mật khẩu được mã hóa băm (ví dụ bcrypt), không lưu dạng thô.                                                                                                                                                   | Bắt buộc |
| NFR-S2 | Ảnh/video của ký ức riêng tư không truy cập được qua đường dẫn tĩnh công khai. Backend cấp URL có chữ ký số (HMAC) kèm thời hạn ngắn (vài phút), chỉ cấp cho người có quyền xem; xem BR-17.                    | Bắt buộc |
| NFR-S3 | Phiên đăng nhập dùng token có thời hạn (JWT hoặc tương đương). JWT mang kèm token_version; đổi/đặt lại mật khẩu tăng token_version để JWT cũ mất hiệu lực ngay, không chờ hết hạn; xem BR-20.                  | Bắt buộc |
| NFR-S4 | Dùng HTTPS khi triển khai.                                                                                                                                                                                     | Bắt buộc |
| NFR-S5 | Kiểm tra loại và dung lượng tệp tải lên ở phía máy chủ.                                                                                                                                                        | Bắt buộc |
| NFR-S6 | Chống các lỗi phổ biến: SQL injection (dùng ORM/tham số hóa truy vấn), XSS (chỉ gán dữ liệu người dùng bằng textContent, không dùng innerHTML/bindPopup với chuỗi HTML dựng từ dữ liệu người dùng); xem BR-21. | Bắt buộc |
| NFR-S7 | Khóa bí mật (API key, JWT secret, mật khẩu cơ sở dữ liệu) không đưa lên kho mã nguồn.                                                                                                                          | Bắt buộc |

## 7.3 Tính tương thích và dễ dùng

| **Mã** | **Yêu cầu**                                                               | **Mức**   |
|--------|---------------------------------------------------------------------------|-----------|
| NFR-U1 | Chạy được trên Chrome, Edge, Firefox, Safari trên máy tính và điện thoại. | Bắt buộc  |
| NFR-U2 | Giao diện hiển thị đúng trên màn hình rộng từ 360 px trở lên.             | (đề xuất) |
| NFR-U3 | Giao diện và thông báo lỗi bằng tiếng Việt.                               | Bắt buộc  |
| NFR-U4 | Ghim một ký ức hoàn thành trong vài bước thao tác.                        | (đề xuất) |

## 7.4 Độ tin cậy và bảo trì

| **Mã** | **Yêu cầu**                                                                                                                                   | **Mức**            |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| NFR-M1 | Mã nguồn chia module rõ ràng, tách riêng HTML, CSS, JS.                                                                                       | Bắt buộc           |
| NFR-M2 | Mỗi tiêu chí nghiệm thu ở mục 5 có thể chuyển thành một ca kiểm thử.                                                                          | Bắt buộc           |
| NFR-R1 | Sao lưu cơ sở dữ liệu MySQL định kỳ hàng tuần bằng lệnh mysqldump (hoặc export tự động của Aiven MySQL free), lưu trữ ngoài thư mục mã nguồn. | (đề xuất, đã chốt) |
