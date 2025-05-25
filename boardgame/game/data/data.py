import random

event = [
    "Người được bạn bè yêu quý nhất?",
    "Người thông minh nhất?",
    "Người chơi game giỏi nhất?",
    "Người có ngoại hình đẹp nhất?",
    "Người hiền nhất?",
    "Người được các thầy cô quý mến nhất?",
    "Người được việc nhất?",
    "Người phân biệt vùng miền nhất?",
    "Người chơi thể thao giỏi nhất?",
    "Người có thể sẽ hay ăn trộm nhất?",
    "Người ngoại ngữ giỏi nhất?",
    "Người hát hay nhất?",
    "Người trẻ trâu nhất?",
    "Người wibu nhất?",
    "Hãy tạo ra ý tưởng của riêng bạn",
    "Người có khả năng nói dối khi làm bản biểm điểm",
    "Người có khả năng chạy quá tốc độ",
    "Hãy tạo ra ý tưởng của rieeng bạn",
    "Người đã vi phạm luật lệ quan trọng mà không bị phát hiện",
    "Người it có khả năng làm ____",
    "Người có khả năng làm ____ nhiều nhất",
    "Người sẽ làm mọi thứ vì tiền",
    "Người có thể sẽ gian lận thi cử",
    "Người nói mình ốm trong khi thực tế thì không",
    "Người có thể bán linh hồn vì tiền",
    "Người bí mật ăn mặc sai luật khi đến trường",
    "Người sẽ bị bắt đầu tiên trong một phim kinh dị",
    "Người sẽ không bao giờ từ chỗi ____",
    "Người được coi là tàng hình",
    "Người sẽ trả bất cứ giá nào để được điều mong muốn",
    "Người sẽ dùng crack thay vì mua bản quyền",



]


nameList = [
    "Đặng Đức Anh",
    "Lê Duy Anh",
    "Lê Đức Anh",
    "Lê Phương Anh",
    "Nguyễn Thảo Anh",
    "Cù Gia Chí Bách",
    "Vũ Trần Quốc Bảo",
    "Phạm Bảo Châu",
    "Trần Hương Chi",
    "Trần Trí Dũng",
    "Nguyễn Lê Đức Duy",
    "Trần Anh Đạt",
    "Hồ Hải Đăng",
    "Nguyễn Hương Giang",
    "Khổng Mạnh Hải",
    "Nghiêm Bảo Hân",
    "Đỗ Thanh Hiền",
    "Giáp Hoàng Hiếu",
    "Ngô Gia Huy",
    "Trương Công Gia Huy",
    "Phan Nam Khánh",
    "Vũ Trần Khoa",
    "Nguyễn Trung Kiệt",
    "Đào Hiểu Lam",
    "Trương Sỹ Lân",
    "Đào Hoàng Linh",
    "Phạm Hà Linh",
    "Bùi Huy Minh",
    "Nguyễn Duy Minh",
    "Nguyễn Văn Minh",
    "Nguyễn Minh Nghĩa",
    "Nguyễn Danh Ngọc",
    "Văn Bích Ngọc",
    "Phạm Gia Phát",
    "Đỗ Hồng Quang",
    "Lê Minh Quý",
    "Phạm Hồng Sơn",
    "Trương Nguyễn Đình Thái",
    "Trần Viết Thành",
    "Vũ Đặng Anh Thư",
    "Nguyễn Đức Triệu",
    "Vũ Đình Trung",
    "Đinh Thanh Tùng",
    "Lưu Minh Vũ",
    "Đặng Hải Nam",
    "Kiều Chấn Hưng",
    "Nghiêm Hoàng Minh",
    "Nguyễn Hoàng Minh",
    "Trương Thành Nam"
]




def randomChoice():
    anyplayers = random.choice(nameList)
    return anyplayers
