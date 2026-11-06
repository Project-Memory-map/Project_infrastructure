[← Danh sách epic](README.md)

# 5.3 Epic EP1 – Tài khoản và hồ sơ cá nhân

## US-ACC-001 – Đăng ký tài khoản bằng email

> **Là một người dùng mới chưa có tài khoản Bản đồ Ký ức, Tôi muốn tạo tài khoản bằng email và mật khẩu, Để có không gian riêng để lưu ký ức và quay lại sử dụng ở những lần sau.**

| **Epic**     | **EP1 – Tài khoản và hồ sơ cá nhân** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-1.1                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | Không có                             | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**                             |
|---------------------|-------------------------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được                        |
| V – Valuable        | ✅ Giá trị rõ: có không gian riêng để lưu ký ức và quay lại sử dụng ở những lần sau |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                                                  |
| S – Small           | ✅ Hoàn thành trong một sprint                                                      |
| T – Testable        | ✅ Có 5 tiêu chí nghiệm thu đo được                                                 |

### Tiêu chí nghiệm thu (5)

### AC1 – Đăng ký thành công

| **Given** | **khách đang ở trang đăng ký và email "an@example.com" chưa có tài khoản**          |
|-----------|-------------------------------------------------------------------------------------|
| When      | khách nhập tên hiển thị "An", email "an@example.com", mật khẩu "Matkhau123" rồi gửi |
| Then      | tài khoản mới được tạo với vai trò người dùng                                       |
| And       | khách được đăng nhập và chuyển tới bản đồ ký ức của mình                            |
| And       | hệ thống hiển thị thông báo "Đăng ký thành công"                                    |

### AC2 – Mật khẩu đúng độ dài tối thiểu

| **Given** | **khách đang ở trang đăng ký**                               |
|-----------|--------------------------------------------------------------|
| When      | khách nhập mật khẩu "Abcdef12" gồm đúng 8 ký tự có chữ và số |
| Then      | mật khẩu được chấp nhận và tài khoản được tạo                |

### AC3 – Mật khẩu quá ngắn

| **Given** | **khách đang ở trang đăng ký**                                     |
|-----------|--------------------------------------------------------------------|
| When      | khách nhập mật khẩu "Abc12" gồm 5 ký tự                            |
| Then      | hệ thống không tạo tài khoản                                       |
| And       | hệ thống hiển thị "Mật khẩu phải có ít nhất 8 ký tự gồm chữ và số" |

### AC4 – Email đã được đăng ký

| **Given** | **đã tồn tại tài khoản với email "an@example.com"** |
|-----------|-----------------------------------------------------|
| When      | khách đăng ký với email "an@example.com"            |
| Then      | hệ thống không tạo thêm tài khoản                   |
| And       | hệ thống hiển thị "Email này đã được đăng ký"       |

### AC5 – Email sai định dạng

| **Given** | **khách đang ở trang đăng ký**         |
|-----------|----------------------------------------|
| When      | khách nhập email "an@"                 |
| Then      | hệ thống hiển thị "Email không hợp lệ" |
| And       | không có tài khoản nào được tạo        |

**Ghi chú:** Trong GĐ1, hệ thống cho phép người dùng đăng nhập ngay sau khi đăng ký thành công mà chưa bắt buộc xác thực email ngay lập tức (chức năng gửi email kích hoạt đưa vào GĐ2 để giảm phức tạp).

## US-ACC-002 – Đăng nhập bằng email và mật khẩu

> **Là một người dùng đã đăng ký tài khoản bằng email, Tôi muốn đăng nhập bằng email và mật khẩu của mình, Để truy cập lại các ký ức và chuyến đi đã lưu.**

| **Epic**     | **EP1 – Tài khoản và hồ sơ cá nhân** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-1.2                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-ACC-001                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: truy cập lại các ký ức và chuyến đi đã lưu    |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 5 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (5)

### AC1 – Đăng nhập thành công

| **Given** | **tài khoản "an@example.com" đang hoạt động**       |
|-----------|-----------------------------------------------------|
| When      | người dùng nhập đúng email và mật khẩu              |
| Then      | người dùng được chuyển tới bản đồ ký ức của mình    |
| And       | tên hiển thị của người dùng xuất hiện trên màn hình |

### AC2 – Email không phân biệt hoa thường

| **Given** | **tài khoản đăng ký với email "an@example.com"**    |
|-----------|-----------------------------------------------------|
| When      | người dùng nhập "AN@Example.com" cùng mật khẩu đúng |
| Then      | người dùng đăng nhập thành công                     |

### AC3 – Sai mật khẩu

| **Given** | **tài khoản "an@example.com" đang hoạt động**      |
|-----------|----------------------------------------------------|
| When      | người dùng nhập mật khẩu sai                       |
| Then      | hệ thống hiển thị "Email hoặc mật khẩu không đúng" |
| And       | thông báo không cho biết email hay mật khẩu bị sai |

### AC4 – Tài khoản bị khóa

| **Given** | **tài khoản "an@example.com" đã bị quản trị viên khóa** |
|-----------|---------------------------------------------------------|
| When      | người dùng nhập đúng email và mật khẩu                  |
| Then      | hệ thống không cho đăng nhập                            |
| And       | hệ thống hiển thị "Tài khoản của bạn đã bị khóa"        |

### AC5 – Nhập sai nhiều lần liên tiếp

| **Given** | **người dùng đã nhập sai mật khẩu 5 lần liên tiếp trong 15 phút**               |
|-----------|---------------------------------------------------------------------------------|
| When      | người dùng nhập tiếp lần thứ 6, kể cả với mật khẩu đúng                         |
| Then      | hệ thống từ chối đăng nhập                                                      |
| And       | hệ thống hiển thị "Bạn đã nhập sai quá nhiều lần, vui lòng thử lại sau 15 phút" |

**Ghi chú:** Ngưỡng tạm khóa (5 lần sai trong 15 phút, khóa 15 phút) là đề xuất.

## US-ACC-003 – Đăng nhập bằng tài khoản Google

> **Là một người dùng có tài khoản Google, không muốn nhớ thêm mật khẩu, Tôi muốn đăng nhập bằng tài khoản Google, Để vào hệ thống nhanh mà không phải tạo mật khẩu riêng.**

| **Epic**     | **EP1 – Tài khoản và hồ sơ cá nhân** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-1.3, FR-1.9                       | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | Không có                             | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**                            |
|---------------------|------------------------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được                       |
| V – Valuable        | ✅ Giá trị rõ: vào hệ thống nhanh mà không phải tạo mật khẩu riêng                 |
| E – Estimable       | ⚠️ Phụ thuộc cấu hình ứng dụng Google bên ngoài. Nên làm spike 1 ngày để xác nhận. |
| S – Small           | ✅ Hoàn thành trong một sprint                                                     |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                                                |

### Tiêu chí nghiệm thu (4)

### AC1 – Đăng nhập Google lần đầu

| **Given** | **chưa có tài khoản nào dùng email Google "an@gmail.com"**  |
|-----------|-------------------------------------------------------------|
| When      | người dùng chọn "Đăng nhập bằng Google" và đồng ý cấp quyền |
| Then      | hệ thống tạo tài khoản mới với tên hiển thị lấy từ Google   |
| And       | người dùng được chuyển tới bản đồ ký ức của mình            |

### AC2 – Email Google trùng tài khoản email đã có

| **Given** | **đã có tài khoản đăng ký bằng email "an@gmail.com" và có 3 ký ức** |
|-----------|---------------------------------------------------------------------|
| When      | người dùng đăng nhập bằng Google với email "an@gmail.com"           |
| Then      | hệ thống liên kết vào tài khoản đã có, không tạo tài khoản thứ hai  |
| And       | người dùng thấy đủ 3 ký ức cũ của mình                              |

### AC3 – Người dùng từ chối cấp quyền

| **Given** | **người dùng đang ở màn hình xin quyền của Google** |
|-----------|-----------------------------------------------------|
| When      | người dùng chọn "Từ chối"                           |
| Then      | hệ thống đưa người dùng về trang đăng nhập          |
| And       | hệ thống hiển thị "Đăng nhập Google chưa hoàn tất"  |

### AC4 – Tài khoản bị khóa

| **Given** | **tài khoản liên kết với "an@gmail.com" đã bị khóa** |
|-----------|------------------------------------------------------|
| When      | người dùng đăng nhập bằng Google                     |
| Then      | hệ thống không cho đăng nhập                         |
| And       | hệ thống hiển thị "Tài khoản của bạn đã bị khóa"     |

**Ghi chú:** Cần đăng ký ứng dụng với Google trước khi làm. Nên chạy một spike ngắn để xác nhận cấu hình.

## US-ACC-004 – Đăng nhập bằng tài khoản Facebook

> **Là một người dùng có tài khoản Facebook, không muốn nhớ thêm mật khẩu, Tôi muốn đăng nhập bằng tài khoản Facebook, Để vào hệ thống nhanh mà không phải tạo mật khẩu riêng.**

| **Epic**     | **EP1 – Tài khoản và hồ sơ cá nhân** | **Ưu tiên** | **Should**                      |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-1.4, FR-1.9                       | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | Không có                             | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**                           |
|---------------------|-----------------------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được                      |
| V – Valuable        | ✅ Giá trị rõ: vào hệ thống nhanh mà không phải tạo mật khẩu riêng                |
| E – Estimable       | ⚠️ Phụ thuộc cấu hình ứng dụng Facebook bên ngoài. Nên làm spike cùng US-ACC-003. |
| S – Small           | ✅ Hoàn thành trong một sprint                                                    |
| T – Testable        | ✅ Có 3 tiêu chí nghiệm thu đo được                                               |

### Tiêu chí nghiệm thu (3)

### AC1 – Đăng nhập Facebook lần đầu

| **Given** | **chưa có tài khoản nào liên kết với Facebook của người dùng** |
|-----------|----------------------------------------------------------------|
| When      | người dùng chọn "Đăng nhập bằng Facebook" và đồng ý cấp quyền  |
| Then      | hệ thống tạo tài khoản mới với tên hiển thị lấy từ Facebook    |
| And       | người dùng được chuyển tới bản đồ ký ức của mình               |

### AC2 – Facebook không cung cấp email

| **Given** | **tài khoản Facebook của người dùng không có email công khai**                     |
|-----------|------------------------------------------------------------------------------------|
| When      | người dùng đăng nhập bằng Facebook lần đầu                                         |
| Then      | hệ thống vẫn tạo tài khoản                                                         |
| And       | hệ thống nhắc người dùng bổ sung email trong hồ sơ để dùng chức năng quên mật khẩu |

### AC3 – Người dùng từ chối cấp quyền

| **Given** | **người dùng đang ở màn hình xin quyền của Facebook** |
|-----------|-------------------------------------------------------|
| When      | người dùng chọn "Hủy"                                 |
| Then      | hệ thống đưa người dùng về trang đăng nhập            |
| And       | hệ thống hiển thị "Đăng nhập Facebook chưa hoàn tất"  |

**Ghi chú:** Facebook có thể không trả về email đã xác thực; khi đó hệ thống không tự liên kết theo email mà luôn tạo tài khoản mới (BR-18). Cần đăng ký ứng dụng với Facebook trước khi làm.

## US-ACC-005 – Đặt lại mật khẩu khi quên

> **Là một người dùng đã đăng ký bằng email nhưng quên mật khẩu, Tôi muốn nhận liên kết đặt lại mật khẩu qua email, Để lấy lại quyền truy cập tài khoản mà không mất ký ức đã lưu.**

| **Epic**     | **EP1 – Tài khoản và hồ sơ cá nhân** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-1.5                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-ACC-001                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**                   |
|---------------------|---------------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được              |
| V – Valuable        | ✅ Giá trị rõ: lấy lại quyền truy cập tài khoản mà không mất ký ức đã lưu |
| E – Estimable       | ⚠️ Dịch vụ gửi email chưa chốt. Cần chốt trước khi ước lượng.             |
| S – Small           | ✅ Hoàn thành trong một sprint                                            |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                                       |

### Tiêu chí nghiệm thu (4)

### AC1 – Yêu cầu đặt lại với email đã đăng ký

| **Given** | **tài khoản "an@example.com" đang hoạt động**                                      |
|-----------|------------------------------------------------------------------------------------|
| When      | người dùng nhập "an@example.com" ở trang quên mật khẩu                             |
| Then      | hệ thống gửi email chứa liên kết đặt lại có hiệu lực 30 phút                       |
| And       | hệ thống hiển thị "Nếu email tồn tại, chúng tôi đã gửi hướng dẫn đặt lại mật khẩu" |

### AC2 – Email chưa đăng ký

| **Given** | **không có tài khoản nào dùng email "khong.co@example.com"**     |
|-----------|------------------------------------------------------------------|
| When      | người dùng nhập "khong.co@example.com" ở trang quên mật khẩu     |
| Then      | hệ thống hiển thị đúng thông báo như trường hợp email đã đăng ký |
| And       | hệ thống không gửi email nào                                     |

### AC3 – Đặt mật khẩu mới thành công

| **Given** | **người dùng mở liên kết đặt lại còn hiệu lực**          |
|-----------|----------------------------------------------------------|
| When      | người dùng nhập mật khẩu mới "Matkhaumoi9" hợp lệ và gửi |
| Then      | mật khẩu mới có hiệu lực                                 |
| And       | mật khẩu cũ không còn đăng nhập được                     |
| And       | liên kết đó không dùng lại được                          |

### AC4 – Liên kết hết hạn

| **Given** | **liên kết đặt lại đã được gửi cách đây 31 phút**             |
|-----------|---------------------------------------------------------------|
| When      | người dùng mở liên kết                                        |
| Then      | hệ thống hiển thị "Liên kết đã hết hạn, vui lòng yêu cầu lại" |
| And       | mật khẩu không bị thay đổi                                    |

**Ghi chú:** Thời hạn liên kết 30 phút (đề xuất, đã chốt). Dịch vụ gửi email: Gmail SMTP (App Password) cho môi trường thật, Mailtrap cho môi trường phát triển/kiểm thử.

## US-ACC-006 – Cập nhật hồ sơ cá nhân

> **Là một người dùng đã đăng nhập muốn người khác nhận ra mình trên các ký ức công khai, Tôi muốn chỉnh sửa tên hiển thị, ảnh đại diện và giới thiệu ngắn, Để hồ sơ phản ánh đúng con người mình.**

| **Epic**     | **EP1 – Tài khoản và hồ sơ cá nhân** | **Ưu tiên** | **Should**                      |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-1.7, FR-1.8                       | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-ACC-002                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**      |
|---------------------|--------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được |
| V – Valuable        | ✅ Giá trị rõ: hồ sơ phản ánh đúng con người mình            |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                           |
| S – Small           | ✅ Hoàn thành trong một sprint                               |
| T – Testable        | ✅ Có 5 tiêu chí nghiệm thu đo được                          |

### Tiêu chí nghiệm thu (5)

### AC1 – Đổi tên hiển thị

| **Given** | **người dùng đang ở trang hồ sơ với tên "An"**          |
|-----------|---------------------------------------------------------|
| When      | người dùng đổi tên thành "Dread" và lưu                 |
| Then      | tên "Dread" được lưu                                    |
| And       | các ký ức công khai của người dùng hiển thị tên "Dread" |

### AC2 – Tên hiển thị đúng giới hạn

| **Given** | **người dùng đang ở trang hồ sơ**             |
|-----------|-----------------------------------------------|
| When      | người dùng nhập tên dài đúng 100 ký tự và lưu |
| Then      | hệ thống chấp nhận và lưu tên                 |

### AC3 – Tên hiển thị quá dài

| **Given** | **người dùng đang ở trang hồ sơ**                 |
|-----------|---------------------------------------------------|
| When      | người dùng nhập tên dài 101 ký tự và lưu          |
| Then      | hệ thống không lưu                                |
| And       | hệ thống hiển thị "Tên hiển thị tối đa 100 ký tự" |

### AC4 – Ảnh đại diện vượt dung lượng

| **Given** | **người dùng đang chọn ảnh đại diện**            |
|-----------|--------------------------------------------------|
| When      | người dùng chọn ảnh 6 MB                         |
| Then      | hệ thống từ chối ảnh                             |
| And       | hệ thống hiển thị "Ảnh không được vượt quá 5 MB" |

### AC5 – Tệp không phải ảnh

| **Given** | **người dùng đang chọn ảnh đại diện**               |
|-----------|-----------------------------------------------------|
| When      | người dùng chọn tệp "baocao.pdf"                    |
| Then      | hệ thống từ chối tệp                                |
| And       | hệ thống hiển thị "Định dạng tệp không được hỗ trợ" |

**Ghi chú:** Ảnh đại diện dùng chung giới hạn dung lượng ảnh (5 MB, đề xuất).

## US-ACC-007 – Đổi mật khẩu khi đang đăng nhập

> **Là một người dùng đã đăng nhập đăng ký bằng email và mật khẩu, Tôi muốn đổi mật khẩu hiện tại sang mật khẩu mới, Để giữ tài khoản an toàn khi nghi ngờ mật khẩu bị lộ.**

| **Epic**     | **EP1 – Tài khoản và hồ sơ cá nhân** | **Ưu tiên** | **Should**                      |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-1.6                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-ACC-002                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**          |
|---------------------|------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được     |
| V – Valuable        | ✅ Giá trị rõ: giữ tài khoản an toàn khi nghi ngờ mật khẩu bị lộ |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                               |
| S – Small           | ✅ Hoàn thành trong một sprint                                   |
| T – Testable        | ✅ Có 4 tiêu chí nghiệm thu đo được                              |

### Tiêu chí nghiệm thu (4)

### AC1 – Đổi mật khẩu thành công

| **Given** | **người dùng đang đăng nhập**                                               |
|-----------|-----------------------------------------------------------------------------|
| When      | người dùng nhập đúng mật khẩu hiện tại và mật khẩu mới "Matkhaumoi9" hợp lệ |
| Then      | mật khẩu mới có hiệu lực                                                    |
| And       | hệ thống hiển thị "Đổi mật khẩu thành công"                                 |

### AC2 – Sai mật khẩu hiện tại

| **Given** | **người dùng đang đăng nhập**                    |
|-----------|--------------------------------------------------|
| When      | người dùng nhập sai mật khẩu hiện tại            |
| Then      | mật khẩu không bị đổi                            |
| And       | hệ thống hiển thị "Mật khẩu hiện tại không đúng" |

### AC3 – Mật khẩu mới không hợp lệ

| **Given** | **người dùng đang đăng nhập**                                      |
|-----------|--------------------------------------------------------------------|
| When      | người dùng nhập mật khẩu mới "abc" gồm 3 ký tự                     |
| Then      | mật khẩu không bị đổi                                              |
| And       | hệ thống hiển thị "Mật khẩu phải có ít nhất 8 ký tự gồm chữ và số" |

### AC4 – Tạo mật khẩu cho tài khoản chỉ đăng nhập mạng xã hội

| **Given** | **người dùng đăng nhập bằng Google, chưa từng đặt mật khẩu (password_hash rỗng)** |
|-----------|-----------------------------------------------------------------------------------|
| When      | người dùng vào Hồ sơ cá nhân, chọn "Tạo mật khẩu" và nhập mật khẩu hợp lệ         |
| Then      | hệ thống lưu mật khẩu mới                                                         |
| And       | từ đó người dùng đăng nhập được bằng email và mật khẩu, bên cạnh đăng nhập Google |

**Ghi chú:** Đối với tài khoản chỉ đăng nhập bằng Google/Facebook (chưa có mật khẩu), trong trang Hồ sơ cá nhân có tùy chọn 'Tạo mật khẩu' (AC4) để người dùng có thể đăng nhập bằng email khi cần.

## US-ACC-008 – Đăng xuất khỏi hệ thống

> **Là một người dùng đã đăng nhập đang dùng máy tính dùng chung, Tôi muốn đăng xuất khi dùng xong, Để người khác không xem được ký ức riêng tư của mình.**

| **Epic**     | **EP1 – Tài khoản và hồ sơ cá nhân** | **Ưu tiên** | **Must**                        |
|--------------|--------------------------------------|-------------|---------------------------------|
| FR liên quan | FR-1.6                               | Ước lượng   | Nhóm ước lượng khi lập kế hoạch |
| Phụ thuộc    | US-ACC-002                           | Trạng thái  | Backlog                         |

### Tự kiểm tra INVEST

| **I – Independent** | **✅ Chỉ phụ thuộc điều kiện đã nêu ở mục "Phụ thuộc"**          |
|---------------------|------------------------------------------------------------------|
| N – Negotiable      | ✅ Cách hiển thị và chi tiết giao diện còn thương lượng được     |
| V – Valuable        | ✅ Giá trị rõ: người khác không xem được ký ức riêng tư của mình |
| E – Estimable       | ✅ Phạm vi rõ, nhóm ước lượng được                               |
| S – Small           | ✅ Hoàn thành trong một sprint                                   |
| T – Testable        | ✅ Có 3 tiêu chí nghiệm thu đo được                              |

### Tiêu chí nghiệm thu (3)

### AC1 – Đăng xuất thành công

| **Given** | **người dùng đang đăng nhập**                                   |
|-----------|-----------------------------------------------------------------|
| When      | người dùng chọn "Đăng xuất"                                     |
| Then      | người dùng được chuyển về trang đăng nhập hoặc bản đồ công khai |
| And       | các thông tin cá nhân không còn hiển thị                        |

### AC2 – Mở lại trang riêng tư sau khi đăng xuất

| **Given** | **người dùng vừa đăng xuất**          |
|-----------|---------------------------------------|
| When      | người dùng mở lại trang hồ sơ cá nhân |
| Then      | hệ thống yêu cầu đăng nhập            |
| And       | ký ức riêng tư không hiển thị         |

### AC3 – Quay lại bằng nút trở về của trình duyệt

| **Given** | **người dùng vừa đăng xuất**                              |
|-----------|-----------------------------------------------------------|
| When      | người dùng nhấn nút trở về của trình duyệt                |
| Then      | trang hiển thị yêu cầu đăng nhập thay vì nội dung cá nhân |

**Ghi chú:** Bản GĐ1 thực hiện thu hồi phiên phía trình duyệt (xóa JWT khỏi localStorage/sessionStorage) kết hợp đặt thời gian sống của token ngắn (ví dụ: 60 phút) để đảm bảo an toàn cơ bản.
