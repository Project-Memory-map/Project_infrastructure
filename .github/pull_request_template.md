## Story

US-XXX-000 — tên story

## Đã làm

-

## Kiểm thử theo tiêu chí nghiệm thu

- [ ] AC1 —
- [ ] AC2 —

## Kiểm tra trước khi xin duyệt

- [ ] Nhánh đặt tên đúng `feature/<module>-<mã-story>-<mô-tả>` và đã rebase theo `develop`
- [ ] Chỉ sửa trong `app/modules/<module của mình>/` (nếu sửa `core/`, `shared/` hoặc `schema.sql` thì đã báo nhóm)
- [ ] Đổi đường dẫn hoặc trường API thì đã cập nhật bảng API trong README
- [ ] `uvicorn app.main:app` chạy được ở thư mục gốc, `/api/health` trả 200
- [ ] Dữ liệu người dùng hiển thị ở frontend chỉ dùng `textContent` (BR-21)
- [ ] Không commit `.env`, `uploads/`, khóa bí mật

## Ảnh chụp màn hình (nếu có giao diện)
