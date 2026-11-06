# Tài liệu đặc tả yêu cầu phần mềm (SRS) — Bản đồ Ký ức

[← Trang chính](../README.md) · Sơ đồ: [so-do/](../so-do/README.md)

| **Phiên bản**   | **0.3**                                                                          |
|-----------------|----------------------------------------------------------------------------------|
| Ngày            | 04/11/2026                                                                       |
| Nhóm thực hiện  | 4 thành viên                                                                     |
| Ngôn ngữ        | Tiếng Việt                                                                       |
| Tài liệu đi kèm | Thiết kế hệ thống (SDD) v0.2; schema.sql; Product Backlog (.xlsx); [so-do/](../so-do/README.md) |

**Lịch sử thay đổi**

| **Phiên bản** | **Ngày**   | **Nội dung**                                                                                                                                                                                                                                                                                                                             |
|---------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.1           | 01/11/2026 | Bản nháp đầu tiên, soạn từ các câu trả lời ban đầu của nhóm.                                                                                                                                                                                                                                                                             |
| 0.2           | 02/11/2026 | Cập nhật theo bản 0.1 nhóm đã chỉnh: CSDL là MySQL; tương tác cộng đồng (thích, bình luận, "Muốn đi", theo dõi, báo cáo vi phạm) chuyển sang Giai đoạn 2. Bổ sung: sơ đồ use case, 26 user story kèm tiêu chí nghiệm thu (INVEST, Given-When-Then), quy tắc nghiệp vụ, yêu cầu phi chức năng có mã, ma trận truy vết, hướng phát triển.  |
| 0.3           | 04/11/2026 | Chốt theo review kỹ thuật: thêm BR-17 đến BR-22 (vá 6 lỗ hổng mức P0: URL ảnh có chữ ký, chỉ gộp tài khoản OAuth khi email đã xác thực, giới hạn gọi Nominatim đúng chính sách, thu hồi JWT bằng token_version, chống XSS, xóa EXIF/GPS khi tải ảnh); chốt toàn bộ mục còn \[TBD\]; bổ sung tiêu chí còn thiếu; đồng bộ Product Backlog. |

## Mục lục

- [1. Giới thiệu](01-gioi-thieu.md)
  - 1.1 Mục đích
  - 1.2 Phạm vi
  - 1.3 Định nghĩa và viết tắt
  - 1.4 Tài liệu liên quan
  - 1.5 Bố cục tài liệu
- [2. Mô tả tổng quan](02-mo-ta-tong-quan.md)
  - 2.1 Bối cảnh sản phẩm
  - 2.2 Đối tượng và vai trò người dùng
  - 2.3 Sơ đồ use case tổng quát
  - 2.4 Môi trường vận hành và công nghệ
  - 2.5 Ràng buộc
  - 2.6 Giả định và phụ thuộc
- [3. Phân chia công việc theo 4 phần](03-phan-chia-cong-viec.md)
- [4. Yêu cầu chức năng](04-yeu-cau-chuc-nang.md)
  - 4.1 Phần 1 – Tài khoản, xác thực và hồ sơ cá nhân
  - 4.2 Phần 2 – Ký ức, chuyến đi và bản đồ
  - 4.3 Phần 3 – Khám phá, bộ lọc và tìm kiếm
  - 4.4 Phần 4 – Quản trị và cộng đồng
- [5. Đặc tả User Story và tiêu chí nghiệm thu](05-user-stories/README.md)
  - [5.3 Epic EP1 – Tài khoản và hồ sơ cá nhân](05-user-stories/ep1-tai-khoan.md)
  - [5.4 Epic EP2 – Ký ức, chuyến đi và bản đồ](05-user-stories/ep2-ky-uc-chuyen-di-ban-do.md)
  - [5.5 Epic EP3 – Khám phá, bộ lọc và tìm kiếm](05-user-stories/ep3-kham-pha-tim-kiem.md)
  - [5.6 Epic EP4 – Quản trị nội dung](05-user-stories/ep4-quan-tri.md)
- [6. Yêu cầu giao diện ngoài](06-yeu-cau-giao-dien-ngoai.md)
- [7. Yêu cầu phi chức năng](07-yeu-cau-phi-chuc-nang.md)
  - 7.1 Hiệu năng
  - 7.2 Bảo mật
  - 7.3 Tính tương thích và dễ dùng
  - 7.4 Độ tin cậy và bảo trì
- [8. Quy tắc nghiệp vụ](08-quy-tac-nghiep-vu.md)
- [9. Ma trận truy vết](09-ma-tran-truy-vet.md)
- [10. Hướng phát triển (đề xuất cải tiến)](10-huong-phat-trien.md)
- [11. Quyết định đã chốt và vấn đề còn mở](11-quyet-dinh-va-van-de-mo.md)
  - 11.1 Đã chốt trong bản 0.3 (không còn là \[TBD\])
  - 11.2 Còn mở — ngoài phạm vi nội dung SRS
- [Phụ lục A — Danh mục sơ đồ tham chiếu](phu-luc-a-danh-muc-so-do.md)

Quy ước: mục ghi **\[TBD\]** là nội dung nhóm chưa thống nhất. Mục ghi **(đề xuất)** là con số hoặc giải pháp do người soạn gợi ý, chưa được nhóm xác nhận. Nhãn **GĐ1** là phạm vi phiên bản này, **GĐ2** là giai đoạn sau.
