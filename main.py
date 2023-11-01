from plyer import notification

title = "Başlık"
message = "Bu bir bildirim mesajıdır 10 dakika icinde teslim olunuz."

notification.notify(
    title=title,
    message=message,
)