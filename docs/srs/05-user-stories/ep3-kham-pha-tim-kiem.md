[← Danh sách epic](README.md)

# 5.5 Epic EP3 – Khám phá, bộ lọc và tìm kiếm

## US-EXP-001 – Xem bản đồ ký ức công khai

> **Là một khách du lịch chưa đăng nhập đang tìm cảnh đẹp để đi trải nghiệm, Tôi muốn xem các ghim ký ức công khai của cộng đồng trên bản đồ, Để chọn được điểm đến cho chuyến đi sắp tới.**

| **Epic**     | **EP3 – Khám phá, bộ lọc và tìm kiếm** | **Ưu tiên** | **Must**                        |
|--------------|----------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.1, FR-3.5                         | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | Không có                               | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: chọn được điểm đến cho chuyến đi sắp tới      |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (4)

### AC1 – Xem ghim công khai

| **Given** | **có 20 ký ức công khai trong vùng đang xem và 5 ký ức riêng tư của người khác** |
|-----------|----------------------------------------------------------------------------------|
| When      | khách mở bản đồ                                                                  |
| Then      | bản đồ hiển thị 20 ghim công khai                                                |
| And       | không hiển thị ký ức riêng tư                                                    |

### AC2 – Vùng chưa có ký ức

| **Given** | **vùng đang xem chưa có ký ức công khai nào**                 |
|-----------|---------------------------------------------------------------|
| When      | khách di chuyển bản đồ tới vùng đó                            |
| Then      | hệ thống hiển thị "Chưa có ký ức công khai trong khu vực này" |

### AC3 – Thông tin tác giả

| **Given** | **khách đang xem chi tiết một ký ức công khai** |
|-----------|-------------------------------------------------|
| When      | khách xem phần thông tin tác giả                |
| Then      | chỉ hiển thị tên hiển thị                       |
| And       | không hiển thị email của tác giả                |

### AC4 – Ký ức bị quản trị viên ẩn

| **Given** | **một ký ức công khai đã bị quản trị viên ẩn** |
|-----------|------------------------------------------------|
| When      | khách mở bản đồ                                |
| Then      | ký ức đó không xuất hiện                       |

**Ghi chú:** Chỉ tải ghim trong vùng bản đồ đang xem để giữ hiệu năng.

## US-EXP-002 – Lọc ký ức công khai theo hashtag

> **Là một bạn trẻ thích đi phượt, muốn tìm ký ức theo chủ đề, Tôi muốn lọc ký ức công khai theo hashtag, Để chỉ xem những ký ức đúng chủ đề mình quan tâm.**

| **Epic**     | **EP3 – Khám phá, bộ lọc và tìm kiếm** | **Ưu tiên** | **Must**                        |
|--------------|----------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-3.1, FR-3.4                         | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-EXP-001                             | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: chỉ xem những ký ức đúng chủ đề mình quan tâm |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (4)

### AC1 – Lọc theo một hashtag

| **Given** | **có 8 ký ức công khai gắn "dalat" và 12 ký ức khác** |
|-----------|-------------------------------------------------------|
| When      | người dùng chọn hashtag "dalat"                       |
| Then      | bản đồ và danh sách chỉ hiển thị 8 ký ức gắn "dalat"  |

### AC2 – Chọn nhiều hashtag

| **Given** | **có ký ức gắn "dalat" và ký ức gắn "phuot"**        |
|-----------|------------------------------------------------------|
| When      | người dùng chọn cả hai hashtag                       |
| Then      | hiển thị các ký ức gắn ít nhất một trong hai hashtag |

### AC3 – Hashtag chưa có ký ức

| **Given** | **chưa có ký ức công khai nào gắn "bienxanh"**        |
|-----------|-------------------------------------------------------|
| When      | người dùng chọn hashtag "bienxanh"                    |
| Then      | hệ thống hiển thị "Chưa có ký ức nào với hashtag này" |

### AC4 – Bỏ lọc

| **Given** | **người dùng đang lọc theo "dalat"**                            |
|-----------|-----------------------------------------------------------------|
| When      | người dùng bỏ chọn hashtag                                      |
| Then      | bản đồ hiển thị lại toàn bộ ký ức công khai trong vùng đang xem |

**Ghi chú:** Khi người dùng chọn nhiều hashtag để lọc, hệ thống sẽ hiển thị các ký ức chứa **ít nhất một trong các hashtag đã chọn** (phép toán OR).

## US-EXP-003 – Lọc ký ức công khai theo khu vực

> **Là một khách du lịch muốn xem ký ức tại một tỉnh thành cụ thể, Tôi muốn lọc ký ức công khai theo khu vực, Để tìm nhanh các địa điểm quanh nơi mình sắp đến.**

| **Epic**     | **EP3 – Khám phá, bộ lọc và tìm kiếm** | **Ưu tiên** | **Must**                        |
|--------------|----------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-3.1                                 | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-EXP-001                             | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**                            |
|---------------------|------------------------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được                       |
| V – Valuable        | ✅ Giá trị rõ: tìm nhanh các địa điểm quanh nơi mình sắp đến                       |
| E – Estimable       | ⚠️ Định nghĩa khu vực và danh mục khu vực chưa chốt. Cần chốt trước khi ước lượng. |
| S – Small           | ✅ Hoàn thành trong một sprint                                                     |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                                                |

### Tiêu chí nghiệm thu (4)

### AC1 – Lọc theo khu vực

| **Given** | **có 6 ký ức công khai thuộc "Lâm Đồng" và 10 ký ức ở nơi khác** |
|-----------|------------------------------------------------------------------|
| When      | người dùng chọn khu vực "Lâm Đồng"                               |
| Then      | chỉ hiển thị 6 ký ức thuộc "Lâm Đồng"                            |

### AC2 – Ký ức chưa gắn khu vực

| **Given** | **có ký ức công khai không thuộc khu vực nào** |
|-----------|------------------------------------------------|
| When      | người dùng lọc theo một khu vực bất kỳ         |
| Then      | ký ức đó không xuất hiện trong kết quả lọc     |
| And       | ký ức đó vẫn xuất hiện khi không lọc khu vực   |

### AC3 – Kết hợp khu vực và hashtag

| **Given** | **có ký ức "Lâm Đồng" gắn "phuot" và ký ức "Lâm Đồng" không gắn hashtag nào** |
|-----------|-------------------------------------------------------------------------------|
| When      | người dùng chọn khu vực "Lâm Đồng" và hashtag "phuot"                         |
| Then      | chỉ hiển thị ký ức thỏa cả khu vực và hashtag                                 |

### AC4 – Khu vực chưa có ký ức

| **Given** | **khu vực "Cao Bằng" chưa có ký ức công khai**                |
|-----------|---------------------------------------------------------------|
| When      | người dùng chọn "Cao Bằng"                                    |
| Then      | hệ thống hiển thị "Chưa có ký ức công khai trong khu vực này" |

**Ghi chú:** "Định nghĩa 'khu vực' trong GĐ1 là cấp **Tỉnh/Thành phố**. Danh mục khu vực nạp sẵn từ tệp seed_regions.sql (34 tỉnh thành Việt Nam). Việc ánh xạ một ký ức vào tỉnh/thành nào dựa trên **tọa độ** (lat/lng) đối chiếu ranh giới GeoJSON của 34 tỉnh (thư viện shapely) — không dựa vào tên tỉnh mà Nominatim trả về, vì dữ liệu OSM có thể chưa cập nhật theo đợt sáp nhập tỉnh.

## US-EXP-004 – Tìm kiếm ký ức công khai theo từ khóa

> **Là một bạn trẻ muốn tìm nhanh ký ức về một địa danh cụ thể, Tôi muốn tìm ký ức công khai bằng từ khóa, Để đi thẳng tới nội dung mình cần mà không phải duyệt bản đồ.**

| **Epic**     | **EP3 – Khám phá, bộ lọc và tìm kiếm** | **Ưu tiên** | **Should**                      |
|--------------|----------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-3.2                                 | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-EXP-001                             | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**                  |
|---------------------|--------------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được             |
| V – Valuable        | ✅ Giá trị rõ: đi thẳng tới nội dung mình cần mà không phải duyệt bản đồ |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                                       |
| S – Small           | ✅ Hoàn thành trong một sprint                                           |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                                      |

### Tiêu chí nghiệm thu (4)

### AC1 – Tìm theo địa danh

| **Given** | **có 5 ký ức công khai có tiêu đề hoặc tên địa điểm chứa "Hồ Gươm"** |
|-----------|----------------------------------------------------------------------|
| When      | người dùng tìm "Hồ Gươm"                                             |
| Then      | hiển thị 5 ký ức, ký ức mới nhất ở đầu danh sách                     |

### AC2 – Không phân biệt hoa thường

| **Given** | **có ký ức tên địa điểm "Hồ Gươm"** |
|-----------|-------------------------------------|
| When      | người dùng tìm "hồ gươm"            |
| Then      | kết quả giống khi tìm "Hồ Gươm"     |

### AC3 – Từ khóa quá ngắn

| **Given** | **người dùng đang ở ô tìm kiếm**         |
|-----------|------------------------------------------|
| When      | người dùng nhập 1 ký tự và tìm           |
| Then      | hệ thống hiển thị "Nhập ít nhất 2 ký tự" |

### AC4 – Không có kết quả

| **Given** | **không ký ức công khai nào khớp "xyzxyz"**           |
|-----------|-------------------------------------------------------|
| When      | người dùng tìm "xyzxyz"                               |
| Then      | hệ thống hiển thị "Không tìm thấy kết quả cho xyzxyz" |

**Ghi chú:** Tìm kiếm **không phân biệt dấu và hoa-thường** (collation ai_ci của MySQL 8.0, ví dụ gõ "ha noi" vẫn ra "Hà Nội") — đã chốt, khác đề xuất ban đầu "khớp chính xác có dấu". Dùng FULLTEXT ngram ở **BOOLEAN MODE** với cụm từ trong ngoặc kép (tránh NATURAL MODE trả về quá nhiều kết quả không liên quan), sắp xếp theo mức liên quan trước, rồi theo "mới nhất" = memory_date giảm dần (ngày của kỷ niệm, không phải ngày tạo bản ghi).

## US-EXP-005 – Lọc ký ức cá nhân theo thời gian

> **Là một người dùng đã đăng nhập muốn xem lại hành trình của mình theo từng năm, Tôi muốn lọc ký ức của mình theo năm, tháng hoặc khoảng ngày, Để xem lại kỷ niệm của một giai đoạn cụ thể.**

| **Epic**     | **EP3 – Khám phá, bộ lọc và tìm kiếm** | **Ưu tiên** | **Must**                        |
|--------------|----------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-3.3                                 | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-MEM-001                             | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: xem lại kỷ niệm của một giai đoạn cụ thể      |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (4)

### AC1 – Lọc theo năm

| **Given** | **người dùng có 4 ký ức năm 2024 và 3 ký ức năm 2025** |
|-----------|--------------------------------------------------------|
| When      | người dùng chọn năm 2024                               |
| Then      | chỉ hiển thị 4 ký ức năm 2024, ngày cũ trước ngày mới  |
| And       | bao gồm cả ký ức riêng tư và công khai                 |

### AC2 – Khoảng ngày gồm cả hai đầu

| **Given** | **người dùng có ký ức ngày 01/03/2025 và 31/03/2025** |
|-----------|-------------------------------------------------------|
| When      | người dùng chọn từ 01/03/2025 đến 31/03/2025          |
| Then      | cả hai ký ức đều xuất hiện                            |

### AC3 – Ngày bắt đầu sau ngày kết thúc

| **Given** | **người dùng đang chọn khoảng ngày**                                |
|-----------|---------------------------------------------------------------------|
| When      | người dùng chọn từ 31/03/2025 đến 01/03/2025                        |
| Then      | hệ thống hiển thị "Ngày bắt đầu phải trước hoặc bằng ngày kết thúc" |

### AC4 – Không có ký ức trong khoảng

| **Given** | **người dùng không có ký ức nào năm 2020**                           |
|-----------|----------------------------------------------------------------------|
| When      | người dùng chọn năm 2020                                             |
| Then      | hệ thống hiển thị "Bạn chưa có ký ức nào trong khoảng thời gian này" |

**Ghi chú:** Áp dụng cho cả ký ức riêng tư và công khai của chính người dùng.
