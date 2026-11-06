[← Danh sách epic](README.md)

# 5.6 Epic EP4 – Quản trị nội dung

## US-ADM-001 – Ẩn và bỏ ẩn ký ức công khai vi phạm

> **Là một quản trị viên vận hành hệ thống, đã đăng nhập với vai trò quản trị, Tôi muốn ẩn một ký ức công khai vi phạm và bỏ ẩn khi cần, Để cộng đồng không nhìn thấy nội dung không phù hợp.**

| **Epic**     | **EP4 – Quản trị nội dung** | **Ưu tiên** | **Should**                      |
|--------------|-----------------------------|-------------|---------------------------------|
| FR liên quan | FR-4.6, FR-4.8, FR-4.9      | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-ACC-002                  | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**         |
|---------------------|-----------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được    |
| V – Valuable        | ✅ Giá trị rõ: cộng đồng không nhìn thấy nội dung không phù hợp |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                              |
| S – Small           | ✅ Hoàn thành trong một sprint                                  |
| T – Testable        | ✅ Có 5 tiêu chí nghiệm thu đo được                             |

### Tiêu chí nghiệm thu (5)

### AC1 – Ẩn kèm lý do

| **Given** | **quản trị viên đang xem ký ức công khai số 123**              |
|-----------|----------------------------------------------------------------|
| When      | quản trị viên chọn "Ẩn" và nhập lý do "Hình ảnh không phù hợp" |
| Then      | ký ức biến mất khỏi bản đồ công khai                           |
| And       | chủ ký ức thấy trạng thái "Đã bị quản trị viên ẩn"             |
| And       | hệ thống ghi nhật ký gồm người thao tác, thời điểm và lý do    |

### AC2 – Bỏ ẩn

| **Given** | **ký ức số 123 đang bị ẩn và vẫn ở chế độ công khai** |
|-----------|-------------------------------------------------------|
| When      | quản trị viên chọn "Bỏ ẩn"                            |
| Then      | ký ức xuất hiện lại trên bản đồ công khai             |

### AC3 – Thiếu lý do

| **Given** | **quản trị viên đang ẩn một ký ức**     |
|-----------|-----------------------------------------|
| When      | quản trị viên để trống lý do            |
| Then      | hệ thống hiển thị "Vui lòng nhập lý do" |
| And       | ký ức không bị ẩn                       |

### AC4 – Người dùng thường dùng chức năng quản trị

| **Given** | **một người dùng không phải quản trị viên**     |
|-----------|-------------------------------------------------|
| When      | người dùng cố mở trang quản trị                 |
| Then      | hệ thống hiển thị "Bạn không có quyền truy cập" |
| And       | không có thay đổi nào xảy ra                    |

### AC5 – Tìm kiếm ký ức công khai để duyệt

| **Given** | **quản trị viên đang ở trang quản trị nội dung**                                     |
|-----------|--------------------------------------------------------------------------------------|
| When      | quản trị viên nhập từ khóa tiêu đề hoặc tên tác giả vào ô tìm kiếm                   |
| Then      | danh sách chỉ hiển thị ký ức công khai khớp từ khóa, kèm trạng thái ẩn/hiện (FR-4.8) |

**Ghi chú:** Nội dung vi phạm bao gồm: Hình ảnh/video đồi trụy, bạo lực, kích động thù hận, thông tin sai sự thật, xúc phạm danh dự cá nhân/tổ chức, hoặc vi phạm bản quyền nghiêm trọng.

## US-ADM-002 – Xóa ký ức vi phạm nghiêm trọng

> **Là một quản trị viên vận hành hệ thống, đã đăng nhập với vai trò quản trị, Tôi muốn xóa hẳn một ký ức vi phạm nghiêm trọng, Để nội dung đó không còn tồn tại trong hệ thống.**

| **Epic**     | **EP4 – Quản trị nội dung** | **Ưu tiên** | **Should**                      |
|--------------|-----------------------------|-------------|---------------------------------|
| FR liên quan | FR-4.6, FR-4.9              | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-ADM-001                  | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: nội dung đó không còn tồn tại trong hệ thống  |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (4)

### AC1 – Xóa kèm lý do

| **Given** | **quản trị viên đang xem ký ức số 123**               |
|-----------|-------------------------------------------------------|
| When      | quản trị viên chọn "Xóa", nhập lý do và xác nhận      |
| Then      | ký ức và ảnh, video của ký ức không còn truy cập được |
| And       | hệ thống ghi nhật ký thao tác kèm lý do               |

### AC2 – Thiếu lý do

| **Given** | **quản trị viên đang xóa một ký ức**    |
|-----------|-----------------------------------------|
| When      | quản trị viên để trống lý do            |
| Then      | hệ thống hiển thị "Vui lòng nhập lý do" |
| And       | ký ức không bị xóa                      |

### AC3 – Ký ức đã bị chủ xóa trước đó

| **Given** | **chủ ký ức số 123 đã xóa ký ức**       |
|-----------|-----------------------------------------|
| When      | quản trị viên mở ký ức số 123           |
| Then      | hệ thống hiển thị "Ký ức không tồn tại" |

### AC4 – Người dùng thường dùng chức năng quản trị

| **Given** | **một người dùng không phải quản trị viên**     |
|-----------|-------------------------------------------------|
| When      | người dùng cố xóa ký ức bằng chức năng quản trị |
| Then      | hệ thống từ chối                                |
| And       | ký ức không bị ảnh hưởng                        |

**Ghi chú:** Xóa theo cơ chế xóa mềm giống US-MEM-007; nhật ký thao tác vẫn được giữ.

## US-ADM-003 – Khóa và mở khóa tài khoản người dùng

> **Là một quản trị viên vận hành hệ thống, đã đăng nhập với vai trò quản trị, Tôi muốn khóa tài khoản vi phạm và mở khóa khi cần, Để ngăn người vi phạm tiếp tục sử dụng hệ thống.**

| **Epic**     | **EP4 – Quản trị nội dung** | **Ưu tiên** | **Should**                      |
|--------------|-----------------------------|-------------|---------------------------------|
| FR liên quan | FR-4.6, FR-4.9              | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-ACC-002                  | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: ngăn người vi phạm tiếp tục sử dụng hệ thống  |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 5 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (5)

### AC1 – Khóa tài khoản kèm lý do

| **Given** | **quản trị viên đang xem tài khoản "an@example.com"** |
|-----------|-------------------------------------------------------|
| When      | quản trị viên chọn "Khóa" và nhập lý do               |
| Then      | tài khoản không đăng nhập được                        |
| And       | hệ thống ghi nhật ký thao tác kèm lý do               |

### AC2 – Mở khóa tài khoản

| **Given** | **tài khoản "an@example.com" đang bị khóa**  |
|-----------|----------------------------------------------|
| When      | quản trị viên chọn "Mở khóa"                 |
| Then      | người dùng đăng nhập lại được                |
| And       | ký ức và chuyến đi của người dùng còn nguyên |

### AC3 – Quản trị viên tự khóa mình

| **Given** | **quản trị viên đang xem tài khoản của chính mình**             |
|-----------|-----------------------------------------------------------------|
| When      | quản trị viên chọn "Khóa"                                       |
| Then      | hệ thống từ chối                                                |
| And       | hệ thống hiển thị "Bạn không thể khóa chính tài khoản của mình" |

### AC4 – Người dùng thường dùng chức năng quản trị

| **Given** | **một người dùng không phải quản trị viên** |
|-----------|---------------------------------------------|
| When      | người dùng cố khóa một tài khoản khác       |
| Then      | hệ thống từ chối                            |
| And       | tài khoản kia không bị ảnh hưởng            |

### AC5 – Tìm kiếm tài khoản

| **Given** | **quản trị viên đang ở trang quản trị tài khoản**                                     |
|-----------|---------------------------------------------------------------------------------------|
| When      | quản trị viên nhập email hoặc tên hiển thị vào ô tìm kiếm                             |
| Then      | danh sách chỉ hiển thị tài khoản khớp từ khóa, kèm trạng thái active/locked (FR-4.10) |

**Ghi chú:** Khi tài khoản người dùng bị quản trị viên khóa, toàn bộ các ký ức công khai của tài khoản đó sẽ tự động bị ẩn khỏi bản đồ cộng đồng cho đến khi tài khoản được mở khóa trở lại.
