[← Mục lục SRS](README.md)

# Phụ lục A — Danh mục sơ đồ tham chiếu

Toàn bộ sơ đồ (use case, kiến trúc, ERD, luồng xử lý) nằm trong thư mục [so-do/](../so-do/README.md). Danh mục:

| **Hình** | **Nội dung**                                                             | **Tham chiếu**     |
|----------|--------------------------------------------------------------------------|--------------------|
| [Hình 1](../so-do/01-use-case.md) | Sơ đồ use case tổng quát (GĐ1)                                           | SRS §2.3           |
| [Hình 2](../so-do/02-kien-truc.md) | Sơ đồ kiến trúc tổng thể 3 lớp                                           | SDD §1             |
| [Hình 3](../so-do/02-kien-truc.md) | Sơ đồ phụ thuộc module (Core, M1-M4)                                     | SDD §2             |
| [Hình 4](../so-do/03-erd.md) | ERD - Module Tài khoản (USERS, OAUTH_ACCOUNTS, PASSWORD_RESET_TOKENS)    | SDD §3, schema.sql |
| [Hình 5](../so-do/03-erd.md) | ERD - Module Ký ức / Chuyến đi / Bản đồ (MEMORIES, MEDIA, TRIPS, ...)    | SDD §3, schema.sql |
| [Hình 6](../so-do/03-erd.md) | ERD - Module Quản trị (ADMIN_ACTIONS)                                    | SDD §3, schema.sql |
| [Hình 7](../so-do/04-luong-xu-ly.md) | Luồng tạo ký ức kèm ảnh (US-MEM-001, US-MEM-003)                         | SDD §2.4 luồng 1   |
| [Hình 8](../so-do/04-luong-xu-ly.md) | Luồng đăng nhập bằng Google (US-ACC-003)                                 | SRS US-ACC-003     |
| [Hình 9](../so-do/04-luong-xu-ly.md) | Luồng xem ghim công khai trong vùng nhìn bản đồ (US-EXP-001, US-EXP-002) | SRS US-EXP-001/002 |
