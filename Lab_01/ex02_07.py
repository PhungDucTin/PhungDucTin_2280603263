print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []  
while True:
    line = input()  
    if line.lower() == 'done':  
        break
    lines.append(line) 
print("\nCác dòng văn bảm bạn đã nhập là:")
for line in lines:
    print(line.upper())
