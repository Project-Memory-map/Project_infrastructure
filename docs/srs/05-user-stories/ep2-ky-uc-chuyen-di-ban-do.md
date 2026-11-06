[← Danh sách epic](README.md)

# 5.4 Epic EP2 – Ký ức, chuyến đi và bản đồ

## US-MEM-001 – Tạo ký ức bằng cách tìm địa điểm

> **Là một người dùng đã đăng nhập vừa đi du lịch về, muốn ghi lại kỷ niệm tại một địa điểm có tên, Tôi muốn nhập tên địa điểm rồi tạo ký ức với tiêu đề, nội dung và ngày, Để kỷ niệm được gắn đúng vị trí trên bản đồ để dễ tìm lại.**

| **Epic**     | **EP2 – Ký ức, chuyến đi và bản đồ** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.2, FR-2.3                       | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-ACC-002                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**                        |
|---------------------|--------------------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được                   |
| V – Valuable        | ✅ Giá trị rõ: kỷ niệm được gắn đúng vị trí trên bản đồ để dễ tìm lại          |
| E – Estimable       | ⚠️ Dịch vụ tìm địa điểm chưa chốt. Cần spike chọn dịch vụ trước khi ước lượng. |
| S – Small           | ✅ Hoàn thành trong một sprint                                                 |
| T – Testable        | ✅ Có 5 tiêu chí nghiệm thu đo được                                            |

### Tiêu chí nghiệm thu (5)

### AC1 – Tạo ký ức bằng địa điểm tìm được

| **Given** | **người dùng đang ở bản đồ của mình**                                                                                |
|-----------|----------------------------------------------------------------------------------------------------------------------|
| When      | người dùng nhập "Hồ Gươm", chọn kết quả đầu tiên, điền tiêu đề "Chiều thu Hà Nội", nội dung, ngày 12/10/2025 rồi lưu |
| Then      | ghim xuất hiện đúng vị trí Hồ Gươm trên bản đồ                                                                       |
| And       | ký ức ở chế độ riêng tư                                                                                              |
| And       | ngày hiển thị là 12/10/2025                                                                                          |

### AC2 – Câu chuyện dài

| **Given** | **người dùng đang tạo ký ức**                    |
|-----------|--------------------------------------------------|
| When      | người dùng nhập nội dung dài 20.000 ký tự và lưu |
| Then      | hệ thống lưu nguyên vẹn, không cắt bớt nội dung  |

### AC3 – Không tìm thấy địa điểm

| **Given** | **người dùng đang tạo ký ức**                                                                 |
|-----------|-----------------------------------------------------------------------------------------------|
| When      | người dùng nhập tên địa điểm "xyzxyz" không có kết quả                                        |
| Then      | hệ thống hiển thị "Không tìm thấy địa điểm. Hãy thử tên khác hoặc chọn trực tiếp trên bản đồ" |
| And       | không có ghim nào được tạo                                                                    |

### AC4 – Thiếu tiêu đề

| **Given** | **người dùng đã chọn địa điểm**           |
|-----------|-------------------------------------------|
| When      | người dùng để trống tiêu đề và lưu        |
| Then      | hệ thống hiển thị "Vui lòng nhập tiêu đề" |
| And       | ký ức không được lưu                      |

### AC5 – Ngày trong tương lai

| **Given** | **hôm nay là 02/11/2026**                       |
|-----------|-------------------------------------------------|
| When      | người dùng chọn ngày 03/11/2026 và lưu          |
| Then      | hệ thống hiển thị "Ngày không được ở tương lai" |
| And       | ký ức không được lưu                            |

**Ghi chú:** Sử dụng dịch vụ **Nominatim (OpenStreetMap API)** miễn phí để tìm tọa độ từ tên địa điểm. Hệ thống chỉ gửi yêu cầu khi người dùng nhấn Enter hoặc nút 'Tìm kiếm' (không gọi khi đang gõ, đúng chính sách sử dụng của Nominatim), gọi qua /geocode của backend có cache và giới hạn 1 yêu cầu/giây cho toàn hệ thống, kèm User-Agent ghi rõ tên ứng dụng (BR-19); kết hợp cơ chế chọn/ghim trực tiếp vị trí trên bản đồ (US-MEM-002) làm phương án dự phòng.

## US-MEM-002 – Tạo ký ức bằng cách chọn vị trí trên bản đồ

> **Là một người dùng đã đăng nhập vừa đến một nơi không có tên trong danh mục địa điểm (một con suối, một đoạn đèo), Tôi muốn chọn trực tiếp vị trí trên bản đồ để tạo ký ức, Để ghim được cả những nơi tìm không ra bằng tên.**

| **Epic**     | **EP2 – Ký ức, chuyến đi và bản đồ** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.2                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-ACC-002                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: ghim được cả những nơi tìm không ra bằng tên  |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 3 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (3)

### AC1 – Chọn vị trí rồi tạo ký ức

| **Given** | **người dùng đang xem bản đồ**                                                                             |
|-----------|------------------------------------------------------------------------------------------------------------|
| When      | người dùng nhấp đúp (hoặc nhấn giữ trên điện thoại) vào một vị trí và điền tiêu đề, nội dung, ngày rồi lưu |
| Then      | ghim xuất hiện đúng vị trí đã chọn                                                                         |
| And       | ký ức ở chế độ riêng tư                                                                                    |

### AC2 – Vị trí ngoài danh mục khu vực

| **Given** | **người dùng chọn vị trí ở nước ngoài, ví dụ Paris** |
|-----------|------------------------------------------------------|
| When      | người dùng lưu ký ức                                 |
| Then      | ký ức vẫn được tạo                                   |
| And       | ký ức không gắn khu vực nào                          |

### AC3 – Khách chưa đăng nhập

| **Given** | **khách chưa đăng nhập đang xem bản đồ** |
|-----------|------------------------------------------|
| When      | khách nhấp đúp vào một vị trí            |
| Then      | hệ thống yêu cầu đăng nhập               |
| And       | không có ghim nào được tạo               |

**Ghi chú:** Máy tính dùng nhấp đúp, điện thoại dùng nhấn giữ. Tên địa điểm (place_name, bắt buộc) được điền tự động bằng reverse geocode qua Nominatim (/reverse) tại tọa độ vừa chọn; nếu không có kết quả hoặc lỗi mạng, hệ thống điền mặc định "Vị trí {lat}, {lng}" và cho người dùng tự sửa lại tên trước khi lưu.

## US-MEM-003 – Đính kèm ảnh vào ký ức

> **Là một người dùng đã đăng nhập đang tạo hoặc sửa một ký ức, Tôi muốn đính kèm nhiều ảnh vào ký ức, Để kỷ niệm có hình ảnh sinh động khi xem lại.**

| **Epic**     | **EP2 – Ký ức, chuyến đi và bản đồ** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.4                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-MEM-001                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: kỷ niệm có hình ảnh sinh động khi xem lại     |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 5 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (5)

### AC1 – Đính kèm 3 ảnh

| **Given** | **người dùng đang tạo ký ức**                    |
|-----------|--------------------------------------------------|
| When      | người dùng chọn 3 ảnh .jpg, mỗi ảnh 2 MB, và lưu |
| Then      | cả 3 ảnh được lưu theo thứ tự đã chọn            |
| And       | chi tiết ký ức hiển thị đủ 3 ảnh                 |

### AC2 – Đúng giới hạn tối đa

| **Given** | **người dùng đang tạo ký ức**             |
|-----------|-------------------------------------------|
| When      | người dùng chọn 10 ảnh, mỗi ảnh đúng 5 MB |
| Then      | hệ thống chấp nhận cả 10 ảnh              |

### AC3 – Vượt số lượng ảnh

| **Given** | **ký ức đã có 10 ảnh**                      |
|-----------|---------------------------------------------|
| When      | người dùng thêm ảnh thứ 11                  |
| Then      | hệ thống từ chối ảnh thứ 11                 |
| And       | hệ thống hiển thị "Mỗi ký ức tối đa 10 ảnh" |

### AC4 – Ảnh vượt dung lượng

| **Given** | **người dùng đang chọn ảnh**                         |
|-----------|------------------------------------------------------|
| When      | người dùng chọn ảnh 6 MB                             |
| Then      | hệ thống từ chối ảnh đó                              |
| And       | hệ thống hiển thị "Mỗi ảnh không được vượt quá 5 MB" |

### AC5 – Định dạng không hỗ trợ

| **Given** | **người dùng đang chọn ảnh**                        |
|-----------|-----------------------------------------------------|
| When      | người dùng chọn tệp "setup.exe"                     |
| Then      | hệ thống từ chối tệp                                |
| And       | hệ thống hiển thị "Định dạng tệp không được hỗ trợ" |

**Ghi chú:** Giới hạn 10 ảnh, mỗi ảnh tối đa 5 MB (đã chốt, xem BR-06). Định dạng nhận .jpg/.jpeg/.png/.heic; ảnh .heic (mặc định của iPhone) được tự động chuyển sang .jpg khi lưu (pillow-heif). Toàn bộ metadata EXIF, đặc biệt tọa độ GPS, bị xóa trước khi lưu (BR-22).

## US-MEM-004 – Đính kèm video vào ký ức

> **Là một người dùng đã đăng nhập có một đoạn video ngắn ghi lại khoảnh khắc đáng nhớ, Tôi muốn đính kèm một video vào ký ức, Để giữ lại cả động tác và âm thanh của khoảnh khắc đó.**

| **Epic**     | **EP2 – Ký ức, chuyến đi và bản đồ** | **Ưu tiên** | **Should**                      |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.4                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-MEM-001                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**           |
|---------------------|-------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được      |
| V – Valuable        | ✅ Giá trị rõ: giữ lại cả động tác và âm thanh của khoảnh khắc đó |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                                |
| S – Small           | ✅ Hoàn thành trong một sprint                                    |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                               |

### Tiêu chí nghiệm thu (4)

### AC1 – Đính kèm video hợp lệ

| **Given** | **người dùng đang tạo ký ức**                      |
|-----------|----------------------------------------------------|
| When      | người dùng chọn video .mp4 dung lượng 30 MB và lưu |
| Then      | video được lưu                                     |
| And       | chi tiết ký ức hiển thị video và phát được         |

### AC2 – Đúng dung lượng tối đa

| **Given** | **người dùng đang tạo ký ức**    |
|-----------|----------------------------------|
| When      | người dùng chọn video đúng 50 MB |
| Then      | hệ thống chấp nhận video         |

### AC3 – Video vượt dung lượng

| **Given** | **người dùng đang chọn video**                      |
|-----------|-----------------------------------------------------|
| When      | người dùng chọn video 60 MB                         |
| Then      | hệ thống từ chối video                              |
| And       | hệ thống hiển thị "Video không được vượt quá 50 MB" |

### AC4 – Thêm video thứ hai

| **Given** | **ký ức đã có 1 video**                      |
|-----------|----------------------------------------------|
| When      | người dùng thêm video thứ hai                |
| Then      | hệ thống từ chối                             |
| And       | hệ thống hiển thị "Mỗi ký ức chỉ có 1 video" |

**Ghi chú:** Mỗi ký ức cho phép tối đa 1 video (định dạng .mp4 hoặc .mov — .mov để nhận video quay thẳng bằng iPhone, dung lượng ≤ 50 MB). Trong giai đoạn demo, video lưu trực tiếp tại thư mục server uploads/{user_id}/{memory_id}/. Khi triển khai sản phẩm thật, video tải lên Cloudflare R2 (free 10 GB, không tính phí băng thông, có presigned URL — khớp cơ chế BR-17) thay vì AWS S3/Cloudinary.

## US-MEM-005 – Xem chi tiết một ký ức

> **Là một người dùng đã đăng nhập đang xem bản đồ, Tôi muốn nhấp vào một ghim để xem chi tiết ký ức, Để đọc lại câu chuyện và xem ảnh, video của chuyến đi.**

| **Epic**     | **EP2 – Ký ức, chuyến đi và bản đồ** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.8                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-MEM-001                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**           |
|---------------------|-------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được      |
| V – Valuable        | ✅ Giá trị rõ: đọc lại câu chuyện và xem ảnh, video của chuyến đi |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                                |
| S – Small           | ✅ Hoàn thành trong một sprint                                    |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                               |

### Tiêu chí nghiệm thu (4)

### AC1 – Xem ký ức của chính mình

| **Given** | **người dùng có ký ức "Chiều thu Hà Nội" ngày 12/10/2025 kèm 3 ảnh**                 |
|-----------|--------------------------------------------------------------------------------------|
| When      | người dùng nhấp vào ghim của ký ức đó                                                |
| Then      | chi tiết hiển thị tiêu đề, ngày 12/10/2025, tên địa điểm, nội dung, 3 ảnh và hashtag |
| And       | người dùng thấy lựa chọn sửa và xóa                                                  |

### AC2 – Xem ký ức công khai của người khác

| **Given** | **một người dùng khác có ký ức công khai**               |
|-----------|----------------------------------------------------------|
| When      | người dùng nhấp vào ghim của ký ức đó                    |
| Then      | người dùng xem được nội dung và tên hiển thị của tác giả |
| And       | không có lựa chọn sửa hay xóa                            |

### AC3 – Mở ký ức riêng tư của người khác

| **Given** | **ký ức số 123 là riêng tư và thuộc người khác** |
|-----------|--------------------------------------------------|
| When      | người dùng mở trực tiếp địa chỉ của ký ức số 123 |
| Then      | hệ thống hiển thị "Không tìm thấy ký ức"         |
| And       | không tiết lộ ký ức đó có tồn tại                |

### AC4 – Ký ức đã bị quản trị viên ẩn

| **Given** | **ký ức của người dùng đã bị quản trị viên ẩn**    |
|-----------|----------------------------------------------------|
| When      | chủ ký ức mở ký ức đó                              |
| Then      | chủ ký ức thấy trạng thái "Đã bị quản trị viên ẩn" |
| And       | người dùng khác không thấy ký ức đó                |

**Ghi chú:** Hình thức hiển thị (cửa sổ hay thanh bên) thuộc thiết kế giao diện, còn thương lượng.

## US-MEM-006 – Sửa nội dung ký ức

> **Là một người dùng đã đăng nhập muốn bổ sung chi tiết cho một kỷ niệm đã ghi, Tôi muốn sửa tiêu đề, nội dung, địa điểm, ngày, ảnh và video của ký ức, Để ký ức luôn đúng và đầy đủ theo thời gian.**

| **Epic**     | **EP2 – Ký ức, chuyến đi và bản đồ** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.5                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-MEM-001                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: ký ức luôn đúng và đầy đủ theo thời gian      |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (4)

### AC1 – Sửa tiêu đề và ảnh

| **Given** | **người dùng mở ký ức của mình có 3 ảnh**            |
|-----------|------------------------------------------------------|
| When      | người dùng đổi tiêu đề, thêm 1 ảnh, bỏ 1 ảnh rồi lưu |
| Then      | chi tiết ký ức hiển thị tiêu đề mới và 3 ảnh         |
| And       | thời điểm cập nhật được ghi lại                      |

### AC2 – Đổi địa điểm

| **Given** | **người dùng mở ký ức của mình tại Hà Nội**  |
|-----------|----------------------------------------------|
| When      | người dùng đổi địa điểm sang "Đà Lạt" và lưu |
| Then      | ghim di chuyển tới Đà Lạt                    |
| And       | khu vực của ký ức chuyển theo vị trí mới     |

### AC3 – Sửa ký ức của người khác

| **Given** | **ký ức số 123 thuộc người dùng khác**               |
|-----------|------------------------------------------------------|
| When      | người dùng cố sửa ký ức số 123                       |
| Then      | hệ thống từ chối                                     |
| And       | hệ thống hiển thị "Bạn không có quyền sửa ký ức này" |
| And       | nội dung ký ức không đổi                             |

### AC4 – Xóa trống tiêu đề khi sửa

| **Given** | **người dùng đang sửa ký ức của mình**    |
|-----------|-------------------------------------------|
| When      | người dùng xóa hết tiêu đề và lưu         |
| Then      | hệ thống hiển thị "Vui lòng nhập tiêu đề" |
| And       | ký ức giữ nguyên nội dung cũ              |

**Ghi chú:** Người dùng chỉ sửa được ký ức của mình.

## US-MEM-007 – Xóa ký ức

> **Là một người dùng đã đăng nhập muốn bỏ một ký ức không còn muốn lưu, Tôi muốn xóa ký ức của mình, Để kiểm soát những gì được lưu trong nhật ký.**

| **Epic**     | **EP2 – Ký ức, chuyến đi và bản đồ** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.5                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-MEM-001                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: kiểm soát những gì được lưu trong nhật ký     |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (4)

### AC1 – Xóa sau khi xác nhận

| **Given** | **người dùng mở ký ức của mình có ảnh và hashtag** |
|-----------|----------------------------------------------------|
| When      | người dùng chọn "Xóa" rồi xác nhận                 |
| Then      | ký ức biến mất khỏi bản đồ và danh sách            |
| And       | ảnh và video của ký ức không còn truy cập được     |

### AC2 – Hủy ở bước xác nhận

| **Given** | **người dùng chọn "Xóa" một ký ức**  |
|-----------|--------------------------------------|
| When      | người dùng chọn "Hủy" ở hộp xác nhận |
| Then      | ký ức vẫn còn nguyên                 |

### AC3 – Xóa ký ức thuộc một chuyến đi

| **Given** | **ký ức nằm trong chuyến đi "Đà Lạt tháng 10" cùng 2 ký ức khác** |
|-----------|-------------------------------------------------------------------|
| When      | người dùng xóa ký ức đó                                           |
| Then      | chuyến đi vẫn còn với 2 ký ức còn lại                             |

### AC4 – Xóa ký ức của người khác

| **Given** | **ký ức số 123 thuộc người dùng khác** |
|-----------|----------------------------------------|
| When      | người dùng cố xóa ký ức số 123         |
| Then      | hệ thống từ chối                       |
| And       | ký ức số 123 không bị ảnh hưởng        |

**Ghi chú:** Xóa ký ức là xóa mềm (deleted_at IS NOT NULL). Tệp ảnh/video trên ổ đĩa được dọn dẹp vật lý định kỳ bằng script tự động (cron job/APScheduler chạy 1 lần/tháng vào ngày đầu tháng), xóa tệp của ký ức đã xóa mềm quá 30 ngày (khớp BR-13).

## US-MEM-008 – Đổi chế độ riêng tư hoặc công khai của ký ức

> **Là một người dùng đã đăng nhập muốn chia sẻ một số kỷ niệm với cộng đồng và giữ kín số còn lại, Tôi muốn chuyển ký ức giữa chế độ riêng tư và công khai, Để quyết định ai được xem kỷ niệm của mình.**

| **Epic**     | **EP2 – Ký ức, chuyến đi và bản đồ** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.6                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-MEM-001                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: quyết định ai được xem kỷ niệm của mình       |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 3 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (3)

### AC1 – Chuyển sang công khai

| **Given** | **ký ức của người dùng đang riêng tư**                  |
|-----------|---------------------------------------------------------|
| When      | người dùng chuyển sang công khai                        |
| Then      | ký ức xuất hiện trên bản đồ công khai ở lần tải kế tiếp |
| And       | khách xem được nội dung và ảnh của ký ức                |

### AC2 – Chuyển về riêng tư

| **Given** | **ký ức của người dùng đang công khai**                                      |
|-----------|------------------------------------------------------------------------------|
| When      | người dùng chuyển về riêng tư                                                |
| Then      | ký ức biến mất khỏi bản đồ công khai                                         |
| And       | người khác mở đường dẫn ảnh của ký ức nhận thông báo không có quyền truy cập |

### AC3 – Người không phải chủ đổi chế độ

| **Given** | **ký ức số 123 thuộc người dùng khác**    |
|-----------|-------------------------------------------|
| When      | người dùng cố đổi chế độ của ký ức số 123 |
| Then      | hệ thống từ chối                          |
| And       | chế độ của ký ức không đổi                |

**Ghi chú:** Chỉ hai mức riêng tư: riêng tư và công khai (đã chốt). Mức "chỉ bạn bè" nằm ngoài phạm vi GĐ1.

## US-MEM-009 – Tạo chuyến đi và thêm ký ức vào chuyến đi

> **Là một người dùng đã đăng nhập vừa đi chuyến "Đà Lạt tháng 10" và ghi nhiều ký ức, Tôi muốn gom các ký ức của một chuyến đi lại với nhau, Để xem lại hành trình theo đúng thứ tự thời gian.**

| **Epic**     | **EP2 – Ký ức, chuyến đi và bản đồ** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.7                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-MEM-001                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: xem lại hành trình theo đúng thứ tự thời gian |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 5 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (5)

### AC1 – Tạo chuyến đi và thêm ký ức

| **Given** | **người dùng có 3 ký ức ngày 10/10, 11/10, 12/10/2025**       |
|-----------|---------------------------------------------------------------|
| When      | người dùng tạo chuyến đi "Đà Lạt tháng 10" và thêm cả 3 ký ức |
| Then      | chuyến đi hiển thị 3 ký ức theo thứ tự ngày tăng dần          |

### AC2 – Hai ký ức cùng ngày

| **Given** | **chuyến đi có hai ký ức cùng ngày 11/10/2025** |
|-----------|-------------------------------------------------|
| When      | người dùng mở chuyến đi                         |
| Then      | ký ức tạo trước hiển thị trước                  |

### AC3 – Thêm ký ức của người khác

| **Given** | **ký ức số 123 thuộc người dùng khác**                 |
|-----------|--------------------------------------------------------|
| When      | người dùng cố thêm ký ức số 123 vào chuyến đi của mình |
| Then      | hệ thống từ chối                                       |
| And       | hệ thống hiển thị "Chỉ thêm được ký ức của bạn"        |

### AC4 – Chuyến đi thiếu tên

| **Given** | **người dùng đang tạo chuyến đi**               |
|-----------|-------------------------------------------------|
| When      | người dùng để trống tên và lưu                  |
| Then      | hệ thống hiển thị "Vui lòng nhập tên chuyến đi" |
| And       | chuyến đi không được tạo                        |

### AC5 – Sửa, xóa chuyến đi và bỏ một ký ức khỏi chuyến đi

| **Given** | **người dùng có chuyến đi "Đà Lạt tháng 10" với 3 ký ức**                                                   |
|-----------|-------------------------------------------------------------------------------------------------------------|
| When      | người dùng đổi tên chuyến đi, bỏ một ký ức khỏi chuyến đi (ký ức vẫn còn trong hệ thống), rồi xóa chuyến đi |
| Then      | tên chuyến đi được cập nhật trước khi xóa                                                                   |
| And       | ký ức bị bỏ không còn nằm trong chuyến đi nhưng vẫn tồn tại độc lập                                         |
| And       | sau khi xóa, chuyến đi không còn xuất hiện nhưng các ký ức thuộc chuyến đi vẫn còn nguyên                   |

**Ghi chú:** Cho phép một ký ức có thể thuộc về nhiều chuyến đi khác nhau (ví dụ: chuyến đi 'Miền Trung 2025' và chuyến đi 'Đà Nẵng' có thể chứa chung một ký ức về cầu Rồng).

## US-MEM-010 – Gắn hashtag cho ký ức

> **Là một người dùng đã đăng nhập muốn ký ức của mình dễ được tìm thấy theo chủ đề, Tôi muốn gắn các hashtag như \#dalat, \#phuot vào ký ức, Để ký ức xuất hiện khi người khác lọc theo chủ đề.**

| **Epic**     | **EP2 – Ký ức, chuyến đi và bản đồ** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-2.9                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-MEM-001                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**       |
|---------------------|---------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được  |
| V – Valuable        | ✅ Giá trị rõ: ký ức xuất hiện khi người khác lọc theo chủ đề |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                            |
| S – Small           | ✅ Hoàn thành trong một sprint                                |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                           |

### Tiêu chí nghiệm thu (4)

### AC1 – Gắn hai hashtag

| **Given** | **người dùng đang tạo ký ức**                |
|-----------|----------------------------------------------|
| When      | người dùng nhập "#dalat" và "#phuot" rồi lưu |
| Then      | ký ức có hai hashtag "dalat" và "phuot"      |
| And       | chi tiết ký ức hiển thị cả hai               |

### AC2 – Không phân biệt hoa thường

| **Given** | **hashtag "dalat" đã tồn tại**                             |
|-----------|------------------------------------------------------------|
| When      | người dùng nhập "#DaLat" cho ký ức khác                    |
| Then      | hệ thống dùng chung hashtag "dalat", không tạo hashtag mới |

### AC3 – Hashtag có ký tự không hợp lệ

| **Given** | **người dùng đang nhập hashtag**                                             |
|-----------|------------------------------------------------------------------------------|
| When      | người dùng nhập "#đà lạt!"                                                   |
| Then      | hệ thống từ chối                                                             |
| And       | hệ thống hiển thị "Hashtag chỉ gồm chữ, số, dấu gạch dưới (tối đa 30 ký tự)" |

### AC4 – Quá số lượng hashtag

| **Given** | **ký ức đã có 10 hashtag**                      |
|-----------|-------------------------------------------------|
| When      | người dùng thêm hashtag thứ 11                  |
| Then      | hệ thống từ chối                                |
| And       | hệ thống hiển thị "Mỗi ký ức tối đa 10 hashtag" |

**Ghi chú:** Mỗi ký ức gắn tối đa 10 hashtag. Quy tắc định dạng (đã chốt): chỉ chứa chữ cái — **kể cả chữ có dấu tiếng Việt** (ví dụ "đàlạt" hợp lệ, không cần bỏ dấu), chữ số và dấu gạch dưới (\_), **không khoảng trắng**, tối đa 30 ký tự, không phân biệt hoa thường (khớp collation utf8mb4_0900_as_ci, cột hashtags.name VARCHAR(30)). Trong GĐ1, người dùng nhập hashtag **thủ công** (source = 'manual'); gợi ý tự động bằng AI Gemini (source = 'ai') là tính năng tùy chọn, chỉ làm nếu nhóm hoàn thành sớm tiến độ (FR-3.6).
