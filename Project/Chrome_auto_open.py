import subprocess
import tkinter as tk
import os

# 전체 프로필이름 설정
profiles = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 9", "Profile 10"]

# subprocess를 이용하여 명령어 전달하는 메서드 작성
def open_chrome_windows():
    url = url_entry.get()       # tk.Entry 에서 입력한 값 반환
    for profile in profiles:
        subprocess.Popen(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--new-window", "--profile-directory=" + profile, url])

# os.system() 함수를 이용하여 터미널 끄는 메서드 작성
def close_terminal():
    app_name = "Terminal"
    os.system(f"pkill {app_name}")

# 터미널과 window 둘다 끄기
def on_close():
    close_terminal()
    window.destroy()

# tkinter로 window 생성, title 변경
window = tk.Tk()
window.title("My Window")

# Link label,입력창 생성 후 배치
url_label = tk.Label(window, text="링크:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# 크롬을 여는 버튼 생성 후 배치
button = tk.Button(window, text="열기", command=open_chrome_windows)
button.pack()

# window 사이즈 세팅
window_width = 200
window_height = 100
screen_width = window.winfo_screenwidth()    # winfo_screenwidth(), winfo_screenheight() : 모니터의 크기 픽셀로 반환
screen_height = window.winfo_screenheight()

# 모니터 정중앙에 window 배치를 위한  x축,y축 계산
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# window 사이즈와 첫 팝업위치 적용 ( '{가로축 사이즈}x{세로축 사이즈}+{첫 x축 위치}+{첫 y축 위치}' )
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))


# protocol()의 "WM_DELETE_WINDOW"을 이용하여 window의 x를 눌러 껐을때 on_close() 작동
window.protocol("WM_DELETE_WINDOW", on_close)

# 생성한 window가 닫히지 않도록 유지
window.mainloop()
