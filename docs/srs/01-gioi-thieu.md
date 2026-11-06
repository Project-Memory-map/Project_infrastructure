[← Mục lục SRS](README.md)

# 1. Giới thiệu

## 1.1 Mục đích

Tài liệu này mô tả các yêu cầu của hệ thống web **Bản đồ Ký ức**: một nhật ký trực tuyến cho phép người dùng lưu giữ kỷ niệm, câu chuyện, hình ảnh và video gắn với địa điểm trên bản đồ, đồng thời là nơi để cộng đồng, đặc biệt là các bạn trẻ thích đi đó đây, tham khảo và khám phá những địa điểm đẹp. Tài liệu là cơ sở để nhóm thiết kế, lập trình, kiểm thử và nghiệm thu.

## 1.2 Phạm vi

**Trong phạm vi (GĐ1)**: hệ thống web chạy trên máy tính và điện thoại, gồm:

- Quản lý tài khoản và hồ sơ cá nhân.

- Ghim ký ức lên bản đồ kèm câu chuyện, ảnh, video, ngày tháng, hashtag.

- Chuyến đi: gom các ký ức theo thời gian.

- Khám phá ký ức công khai của cộng đồng: lọc theo hashtag, khu vực; tìm kiếm; lọc ký ức cá nhân theo thời gian.

- Quản trị và kiểm duyệt nội dung ở mức cơ bản.

**Giai đoạn 2 (chưa làm trong bản này)**: tương tác cộng đồng gồm thích, bình luận, lưu "Muốn đi", theo dõi người dùng, báo cáo vi phạm.

**Ngoài phạm vi**: ứng dụng di động native, nhắn tin trực tiếp, thanh toán, tương tác cộng đồng (GĐ2, xem mục 11.1).

## 1.3 Định nghĩa và viết tắt

| **Thuật ngữ**        | **Ý nghĩa**                                                                                                        |
|----------------------|--------------------------------------------------------------------------------------------------------------------|
| Ký ức                | Một bản ghi gắn với một địa điểm, gồm tiêu đề, nội dung, ảnh/video, ngày tháng, hashtag, chế độ riêng tư/công khai |
| Ghim (pin)           | Điểm đánh dấu của một ký ức trên bản đồ                                                                            |
| Chuyến đi            | Tập hợp nhiều ký ức, sắp xếp theo thời gian                                                                        |
| Muốn đi              | Danh sách ký ức/địa điểm của người khác mà người dùng lưu lại để đi sau (GĐ2)                                      |
| Hashtag              | Nhãn chủ đề gắn với ký ức, dùng để lọc và tìm kiếm                                                                 |
| Khu vực              | Đơn vị địa lý để lọc ký ức; dùng cấp tỉnh/thành (34 tỉnh, xem mục 11.1)                                            |
| Riêng tư / Công khai | Riêng tư: chỉ chủ ký ức xem được. Công khai: mọi người, kể cả khách, xem được                                      |
| SRS / SDD            | Tài liệu đặc tả yêu cầu / Tài liệu thiết kế hệ thống                                                               |
| INVEST               | Tiêu chí kiểm tra user story: Independent, Negotiable, Valuable, Estimable, Small, Testable                        |
| Given-When-Then      | Cú pháp viết tiêu chí nghiệm thu (acceptance criteria) theo kịch bản                                               |
| MoSCoW               | Mức ưu tiên: Must (bắt buộc), Should (nên có), Could (có thể có), Won't (không làm lần này)                        |

## 1.4 Tài liệu liên quan

- Tài liệu Thiết kế hệ thống (SDD) v0.2: kiến trúc, module, cơ sở dữ liệu, API.

- schema.sql: lược đồ cơ sở dữ liệu MySQL.

- ProductBacklog_BanDoKyUc.xlsx: danh sách user story và tiêu chí nghiệm thu dạng bảng, dùng cho Scrum.

- Chuẩn tham khảo cấu trúc: IEEE 830 / ISO 29148.

## 1.5 Bố cục tài liệu

Mục 2 mô tả tổng quan. Mục 3 và 4 liệt kê yêu cầu chức năng theo 4 phần. Mục 5 chi tiết hóa bằng user story và tiêu chí nghiệm thu. Mục 6 và 7 nêu giao diện và yêu cầu phi chức năng. Mục 8 tập hợp quy tắc nghiệp vụ. Mục 9 là ma trận truy vết. Mục 10 và 11 nêu hướng phát triển và vấn đề còn mở.
