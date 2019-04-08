data_bmi = ['Quá Béo', 'Béo', 'Thừa cân', 'Bình Thường', 'Gầy']
name = input('Vui lòng nhập họ tên:')
weight = int(input('Vui lòng nhập cân nặng của bạn:'))
height = float(input('Vui lòng nhập chiều cao của bạn:'))
_bmi = weight / height ** 2
print("BMI của ", name, " :", _bmi)
if _bmi >= 35:
    print("Bạn đã", data_bmi[0], ". Đề nghị tập thể dục thường xuyên.")
elif _bmi >= 30:
    print("Bạn đã", data_bmi[1], ". Đề nghị tập thể dục thường xuyên.")
elif _bmi >= 25:
    print("Bạn đã", data_bmi[2], ". Đề nghị tập thể dục thường xuyên.")
elif _bmi >= 18.5:
    print("Bạn hoàn toàn", data_bmi[3], ". Vui lòng giữ sức khỏe nhiều hơn.")
else:
    print("Bạn đã", data_bmi[4], ". Đề nghị cần bổ sung thêm chất dinh dưỡng.")
