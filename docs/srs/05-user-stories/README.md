[← Mục lục SRS](../README.md)

# 5. Đặc tả User Story và tiêu chí nghiệm thu

## 5.1 Cách đọc

- Mỗi user story theo mẫu "Là một \[người dùng\], Tôi muốn \[hành động\], Để \[lợi ích\]".

- Mỗi story được tự kiểm tra theo 6 tiêu chí INVEST. Dấu ✅ là đạt, ⚠️ là cần lưu ý kèm lý do.

- Tiêu chí nghiệm thu viết theo Given-When-Then, có kịch bản thành công, trường hợp biên và trường hợp lỗi.

- Ước lượng (story point) do nhóm thực hiện khi lập kế hoạch sprint, nên để trống ở đây.

- Số liệu giới hạn (độ dài, dung lượng, thời hạn) lấy theo mục 4 và mục 8; những số ghi (đề xuất) cần nhóm xác nhận.

## 5.2 Danh sách epic và story

| **Mã**     | **Tiêu đề**                                  | **Epic** | **Ưu tiên** | **FR liên quan**       |
|------------|----------------------------------------------|----------|-------------|------------------------|
| US-ACC-001 | Đăng ký tài khoản bằng email                 | EP1      | Must        | FR-1.1                 |
| US-ACC-002 | Đăng nhập bằng email và mật khẩu             | EP1      | Must        | FR-1.2                 |
| US-ACC-003 | Đăng nhập bằng tài khoản Google              | EP1      | Must        | FR-1.3, FR-1.9         |
| US-ACC-004 | Đăng nhập bằng tài khoản Facebook            | EP1      | Should      | FR-1.4, FR-1.9         |
| US-ACC-005 | Đặt lại mật khẩu khi quên                    | EP1      | Must        | FR-1.5                 |
| US-ACC-006 | Cập nhật hồ sơ cá nhân                       | EP1      | Should      | FR-1.7, FR-1.8         |
| US-ACC-007 | Đổi mật khẩu khi đang đăng nhập              | EP1      | Should      | FR-1.6                 |
| US-ACC-008 | Đăng xuất khỏi hệ thống                      | EP1      | Must        | FR-1.6                 |
| US-MEM-001 | Tạo ký ức bằng cách tìm địa điểm             | EP2      | Must        | FR-2.2, FR-2.3         |
| US-MEM-002 | Tạo ký ức bằng cách chọn vị trí trên bản đồ  | EP2      | Must        | FR-2.2                 |
| US-MEM-003 | Đính kèm ảnh vào ký ức                       | EP2      | Must        | FR-2.4                 |
| US-MEM-004 | Đính kèm video vào ký ức                     | EP2      | Should      | FR-2.4                 |
| US-MEM-005 | Xem chi tiết một ký ức                       | EP2      | Must        | FR-2.8                 |
| US-MEM-006 | Sửa nội dung ký ức                           | EP2      | Must        | FR-2.5                 |
| US-MEM-007 | Xóa ký ức                                    | EP2      | Must        | FR-2.5                 |
| US-MEM-008 | Đổi chế độ riêng tư hoặc công khai của ký ức | EP2      | Must        | FR-2.6                 |
| US-MEM-009 | Tạo chuyến đi và thêm ký ức vào chuyến đi    | EP2      | Must        | FR-2.7                 |
| US-MEM-010 | Gắn hashtag cho ký ức                        | EP2      | Must        | FR-2.9                 |
| US-EXP-001 | Xem bản đồ ký ức công khai                   | EP3      | Must        | FR-2.1, FR-3.5         |
| US-EXP-002 | Lọc ký ức công khai theo hashtag             | EP3      | Must        | FR-3.1, FR-3.4         |
| US-EXP-003 | Lọc ký ức công khai theo khu vực             | EP3      | Must        | FR-3.1                 |
| US-EXP-004 | Tìm kiếm ký ức công khai theo từ khóa        | EP3      | Should      | FR-3.2                 |
| US-EXP-005 | Lọc ký ức cá nhân theo thời gian             | EP3      | Must        | FR-3.3                 |
| US-ADM-001 | Ẩn và bỏ ẩn ký ức công khai vi phạm          | EP4      | Should      | FR-4.6, FR-4.8, FR-4.9 |
| US-ADM-002 | Xóa ký ức vi phạm nghiêm trọng               | EP4      | Should      | FR-4.6, FR-4.9         |
| US-ADM-003 | Khóa và mở khóa tài khoản người dùng         | EP4      | Should      | FR-4.6, FR-4.9         |

Epic: EP1 = Tài khoản và hồ sơ cá nhân; EP2 = Ký ức, chuyến đi và bản đồ; EP3 = Khám phá, bộ lọc và tìm kiếm; EP4 = Quản trị nội dung.

## Các file theo epic

- [5.3 Epic EP1 – Tài khoản và hồ sơ cá nhân](ep1-tai-khoan.md) — 8 story
- [5.4 Epic EP2 – Ký ức, chuyến đi và bản đồ](ep2-ky-uc-chuyen-di-ban-do.md) — 10 story
- [5.5 Epic EP3 – Khám phá, bộ lọc và tìm kiếm](ep3-kham-pha-tim-kiem.md) — 5 story
- [5.6 Epic EP4 – Quản trị nội dung](ep4-quan-tri.md) — 3 story
