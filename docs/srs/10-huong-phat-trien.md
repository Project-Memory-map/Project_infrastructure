[← Mục lục SRS](README.md)

# 10. Hướng phát triển (đề xuất cải tiến)

Các ý tưởng dưới đây tham khảo từ tài liệu góp ý nhóm thu thập. Chưa nằm trong phạm vi GĐ1; nhóm chọn ý nào thì mới chuyển thành yêu cầu và user story.

| **Ý tưởng**                             | **Mô tả ngắn**                                   | **Độ khó** | **Đề xuất**                     | **Tác động thiết kế**                              |
|-----------------------------------------|--------------------------------------------------|------------|---------------------------------|----------------------------------------------------|
| Thanh trượt thời gian (Timeline Slider) | Kéo qua các năm để ghim hiện/ẩn mượt trên bản đồ | Thấp       | Làm sớm                         | Dùng sẵn memory_date, không đổi CSDL               |
| Xuất dữ liệu (.zip, .pdf)               | Tải toàn bộ ảnh, bài viết về máy                 | Thấp-TB    | Làm sớm                         | Thêm API xuất; không đổi CSDL                      |
| Trang chi tiết kiểu nhật ký             | Ảnh toàn màn hình, chọn font chữ                 | Trung bình | Bản đơn giản                    | Có thể thêm cột font_style cho ký ức               |
| "Ngày này năm xưa"                      | Nhắc lại ký ức cùng ngày các năm trước           | Trung bình | GĐ2                             | Truy vấn theo ngày/tháng; email cần bảng thông báo |
| Hộp viên nang thời gian                 | Khóa ký ức tới ngày chỉ định                     | Trung bình | GĐ2                             | Thêm cột unlock_at cho ký ức                       |
| Nhạc nền theo ký ức                     | Gắn liên kết Spotify/YouTube vào ký ức           | Trung bình | GĐ2                             | Thêm cột music_url; chỉ nhúng liên kết             |
| Ghi âm giọng nói                        | Đính kèm bản ghi âm                              | TB-Cao     | GĐ2+                            | Thêm media_type = audio; tốn dung lượng            |
| Gắn thẻ người tham gia                  | Tìm ký ức theo người cùng đi                     | Cao        | GĐ2+                            | Thêm bảng người tham gia; cần cơ chế đồng ý        |
| Không gian ký ức dùng chung             | Bản đồ nhóm nhiều người cùng ghim                | Cao        | GĐ2+                            | Thêm bảng nhóm, thành viên, phân quyền             |
| Gắn hashtag bằng AI                     | Gemini gợi ý hashtag                             | Trung bình | Tùy chọn, làm nếu còn thời gian | memory_hashtags.source đã dự phòng                 |
