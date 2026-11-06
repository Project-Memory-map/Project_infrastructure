[← Mục lục SRS](README.md)

# 11. Quyết định đã chốt và vấn đề còn mở

## 11.1 Đã chốt trong bản 0.3 (không còn là \[TBD\])

1\. Phạm vi GĐ1 không gồm tương tác cộng đồng (thích, bình luận, "Muốn đi", theo dõi, báo cáo); FR-4.1–FR-4.5 giữ nhãn GĐ2, không có user story trong bản này (mục 4.4).

2\. Gắn hashtag bằng AI (Gemini) là tính năng tùy chọn, chỉ làm nếu nhóm hoàn thành sớm các chức năng cốt lõi; không bắt buộc cho GĐ1 (FR-3.6).

3\. "Khu vực" = cấp Tỉnh/Thành phố, danh mục cố định 34 tỉnh/thành (seed_regions.sql). Ánh xạ một ký ức vào tỉnh/thành dựa trên **tọa độ** đối chiếu ranh giới GeoJSON (thư viện shapely), không dựa vào tên tỉnh Nominatim trả về (xem US-EXP-003).

4\. Giới hạn chính thức: ảnh tối đa 10/ký ức, ≤ 5 MB/ảnh, định dạng .jpg/.jpeg/.png/.heic; video tối đa 1/ký ức, ≤ 50 MB, định dạng .mp4 hoặc .mov; hashtag tối đa 10/ký ức, tối đa 30 ký tự, chấp nhận chữ có dấu (BR-06).

5\. Chỉ hai mức riêng tư: riêng tư và công khai. Mức "chỉ bạn bè" nằm ngoài phạm vi GĐ1.

6\. Một ký ức có thể thuộc nhiều chuyến đi cùng lúc (trip_memories hỗ trợ quan hệ nhiều-nhiều). Chuyến đi không có chế độ chia sẻ công khai riêng ở GĐ1.

7\. Đăng ký email: chưa bắt buộc xác thực ngay để giảm phức tạp cho đồ án; nhưng liên kết tài khoản OAuth theo email trùng (BR-08) chỉ thực hiện khi email đã được xác thực, để tránh bị chiếm tài khoản (BR-18). Facebook không trả về email đã xác thực thì tạo tài khoản mới, không liên kết tự động. Tài khoản chỉ đăng nhập mạng xã hội có tùy chọn "Tạo mật khẩu" trong Hồ sơ cá nhân (US-ACC-007, AC4).

8\. Tài khoản bị quản trị viên khóa: toàn bộ ký ức công khai của tài khoản đó bị ẩn khỏi bản đồ cộng đồng tới khi mở khóa lại (BR-03).

9\. Dịch vụ tìm địa điểm: Nominatim (OpenStreetMap), gọi qua /geocode của backend có cache, tuân thủ đúng chính sách sử dụng (BR-19). Dịch vụ gửi email: Gmail SMTP (App Password) cho môi trường thật; Mailtrap cho môi trường phát triển/kiểm thử.

10\. Lưu trữ ảnh/video: thư mục cục bộ uploads/ khi demo; khi triển khai thật dùng Cloudflare R2 (free 10 GB, presigned URL, khớp BR-17). Dọn tệp mồ côi: định kỳ 1 lần/tháng (BR-13). Sao lưu CSDL: hàng tuần bằng mysqldump (NFR-R1).

11\. Chỉ tiêu hiệu năng: tối thiểu 100 người dùng đồng thời, phản hồi API \< 1 giây, trang chính tải ≤ 3 giây — chốt làm mục tiêu cho phạm vi đồ án (NFR-P1, NFR-P2).

## 11.2 Còn mở — ngoài phạm vi nội dung SRS

12\. Story point, sprint, người phụ trách, hạn nộp: điền trực tiếp trong Product Backlog (.xlsx) khi lập kế hoạch sprint. Đường găng gợi ý: Sprint 0 dựng khung dự án dùng chung (Core, get_current_user, map.js, API contract OpenAPI) trước, vì mọi story đều phụ thuộc Core và US-ACC-002.

13\. Mẫu SRS của giảng viên (nếu có) và phân công cụ thể 4 thành viên cho 4 phần — nhóm tự điền ngoài tài liệu này.
