import serial
import time
import pandas as pd
import os

# 設置串口和波特率
ser = serial.Serial('COM6', 9600)  # 修改為你的Arduino所連接的串口，波特率與Arduino一致
time.sleep(2)  # 等待 Arduino 初始化

# 自動尋找當前目錄中的 CSV 檔案
def find_csv_file():
    for file in os.listdir():
        if file.endswith('.csv'):
            return file
    return None

# 尋找 CSV 檔案
csv_file = find_csv_file()

if csv_file is None:
    print("找不到任何 CSV 檔案")
    ser.close()
    exit()
else:
    print(f"找到 CSV 檔案: {csv_file}")

# 讀取CSV檔案
data = pd.read_csv(csv_file)

def send_command(command):
    ser.write(f"{command}\n".encode())  # 將命令發送給 Arduino
    time.sleep(1)  # 等待 Arduino 執行

try:
    for index, row in data.iterrows():
        time_sec = row['Time (sec)']  # 時間列
        prediction = row['Prediction']  # 預測列

        print(f"時間: {time_sec}, 預測: {prediction}")

        if prediction == 1.0:
            send_command(1)  # 發送 1 給 Arduino
            print("發送 1 給 Arduino")
        else:
            print("無需控制 Arduino")

        time.sleep(1)  # 每秒執行一次

except KeyboardInterrupt:
    print("程序停止")

finally:
    ser.close()
