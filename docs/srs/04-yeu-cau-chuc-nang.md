[← Mục lục SRS](README.md)

# 4. Yêu cầu chức năng

## 4.1 Phần 1 – Tài khoản, xác thực và hồ sơ cá nhân

| **Mã** | **Yêu cầu**                                                                                                                                | **Giai đoạn** |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| FR-1.1 | Người dùng đăng ký tài khoản bằng email và mật khẩu; hệ thống kiểm tra email hợp lệ, chưa trùng, mật khẩu đủ mạnh.                         | GĐ1           |
| FR-1.2 | Người dùng đăng nhập bằng email và mật khẩu.                                                                                               | GĐ1           |
| FR-1.3 | Người dùng đăng nhập bằng tài khoản Google (Gmail).                                                                                        | GĐ1           |
| FR-1.4 | Người dùng đăng nhập bằng tài khoản Facebook.                                                                                              | GĐ1           |
| FR-1.5 | Quên mật khẩu: gửi liên kết đặt lại mật khẩu qua email, liên kết có thời hạn.                                                              | GĐ1           |
| FR-1.6 | Đăng xuất; đổi mật khẩu khi đang đăng nhập.                                                                                                | GĐ1           |
| FR-1.7 | Hồ sơ cá nhân: ảnh đại diện, tên hiển thị, giới thiệu ngắn; người dùng chỉnh sửa được.                                                     | GĐ1           |
| FR-1.8 | Trang cá nhân hiển thị các ký ức, chuyến đi của người dùng (lọc theo thời gian ở Phần 3).                                                  | GĐ1           |
| FR-1.9 | Khi đăng nhập lần đầu bằng Google/Facebook, hệ thống tự tạo tài khoản; nếu email trùng tài khoản đã có thì liên kết về cùng một tài khoản. | GĐ1           |

## 4.2 Phần 2 – Ký ức, chuyến đi và bản đồ

| **Mã** | **Yêu cầu**                                                                                                                                               | **Giai đoạn** |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| FR-2.1 | Hiển thị bản đồ toàn màn hình; ghim của người dùng màu xanh, ghim công khai của cộng đồng màu đỏ.                                                         | GĐ1           |
| FR-2.2 | Tạo ký ức bằng cách nhập tên địa điểm (hệ thống tìm và ghim lên bản đồ) hoặc nhấp đúp/nhấn giữ trên bản đồ để chọn vị trí.                                | GĐ1           |
| FR-2.3 | Mỗi ký ức gồm: tiêu đề, nội dung (mô tả ngắn hoặc câu chuyện dài), ảnh hoặc video, ngày tháng năm do người dùng chọn, hashtag, chế độ riêng tư/công khai. | GĐ1           |
| FR-2.4 | Đính kèm nhiều ảnh và video cho một ký ức. Giới hạn (đề xuất): tối đa 10 ảnh, mỗi ảnh ≤ 5 MB; tối đa 1 video, ≤ 50 MB.                                    | GĐ1           |
| FR-2.5 | Người dùng sửa, thêm bớt nội dung và xóa ký ức của mình; xóa phải có bước xác nhận.                                                                       | GĐ1           |
| FR-2.6 | Chuyển đổi chế độ riêng tư (chỉ mình tôi) / công khai (cộng đồng thấy) bất kỳ lúc nào.                                                                    | GĐ1           |
| FR-2.7 | Tạo chuyến đi và thêm các ký ức vào chuyến đi; các ký ức trong chuyến đi được sắp xếp theo thời gian.                                                     | GĐ1           |
| FR-2.8 | Nhấp vào ghim để xem chi tiết ký ức.                                                                                                                      | GĐ1           |
| FR-2.9 | Hashtag do người dùng nhập thủ công. Gắn hashtag tự động bằng AI: xem FR-3.6.                                                                             | GĐ1           |

## 4.3 Phần 3 – Khám phá, bộ lọc và tìm kiếm

| **Mã** | **Yêu cầu**                                                                                                                                                                                                                 | **Giai đoạn** |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| FR-3.1 | Trang cộng đồng: lọc ký ức công khai theo **khu vực** và theo **hashtag**.                                                                                                                                                  | GĐ1           |
| FR-3.2 | Tìm kiếm ký ức công khai theo từ khóa (tên địa điểm, tiêu đề).                                                                                                                                                              | GĐ1           |
| FR-3.3 | Trang cá nhân: lọc/tìm kiếm ký ức của mình theo **thời gian** (năm, tháng hoặc khoảng ngày).                                                                                                                                | GĐ1           |
| FR-3.4 | Thanh bên hiển thị danh sách chuyến đi và bộ lọc hashtag; kết quả lọc cập nhật đồng thời trên bản đồ.                                                                                                                       | GĐ1           |
| FR-3.5 | Kết quả danh sách phân trang hoặc tải dần để đảm bảo hiệu năng.                                                                                                                                                             | GĐ1           |
| FR-3.6 | \[Tùy chọn / Giai đoạn 2\] Gắn hashtag tự động bằng AI (dự kiến Google Gemini). Trong phạm vi GĐ1, người dùng nhập hashtag thủ công; tính năng gợi ý bằng AI sẽ được tích hợp nếu nhóm hoàn thành sớm các chức năng cốt lõi | Tùy chọn      |

## 4.4 Phần 4 – Quản trị và cộng đồng

| **Mã**  | **Yêu cầu**                                                                                                                                     | **Giai đoạn** |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| FR-4.1  | Thích (like) và bỏ thích một ký ức công khai.                                                                                                   | GĐ2           |
| FR-4.2  | Bình luận vào ký ức công khai; chủ bình luận xóa được bình luận của mình, chủ ký ức xóa được bình luận trong ký ức của mình.                    | GĐ2           |
| FR-4.3  | Lưu ký ức/địa điểm vào danh sách "Muốn đi"; xem và bỏ lưu.                                                                                      | GĐ2           |
| FR-4.4  | Theo dõi người dùng khác và xem ký ức công khai của họ.                                                                                         | GĐ2           |
| FR-4.5  | Báo cáo ký ức hoặc bình luận vi phạm, kèm lý do.                                                                                                | GĐ2           |
| FR-4.6  | Quản trị viên ẩn/bỏ ẩn hoặc xóa ký ức vi phạm, khóa/mở khóa tài khoản vi phạm. Xử lý hàng đợi báo cáo thuộc GĐ2.                                | GĐ1           |
| FR-4.7  | Chỉ người dùng đã đăng nhập mới được thích, bình luận, lưu, theo dõi, báo cáo.                                                                  | GĐ2           |
| FR-4.8  | Quản trị viên xem và tìm kiếm danh sách ký ức công khai để phát hiện nội dung vi phạm (bổ sung vì chưa có báo cáo vi phạm ở GĐ1). **(đề xuất)** | GĐ1           |
| FR-4.9  | Mọi thao tác ẩn/xóa/khóa của quản trị viên đều yêu cầu lý do và được ghi nhật ký (ai, lúc nào, làm gì, vì sao). **(đề xuất)**                   | GĐ1           |
| FR-4.10 | Quản trị viên tìm kiếm tài khoản theo email hoặc tên hiển thị để phục vụ khóa/mở khóa (US-ADM-003).                                             | GĐ1           |
