# tkinter 모듈과 pycoingecko 모듈을 가져옵니다.
import tkinter as tk
import pycoingecko

# pycoingecko 모듈의 CoinGeckoAPI() 클래스를 사용해 cg 객체를 생성합니다.
cg = pycoingecko.CoinGeckoAPI()

# 엔트리 위젯에서 엔터 키를 누르면 호출될 on_return_key 함수를 정의합니다.
def on_return_key(event):
    get_coin_price()

# 버튼을 누르면 호출될 get_coin_price 함수를 정의합니다.
def get_coin_price():
    # 모든 코인 리스트를 가져옵니다.
    coin_list = cg.get_coins_list()
    coin_id = None

    # 엔트리 위젯에서 입력된 코인 심볼을 가져옵니다.
    coin_symbol = entry.get()

    # 입력된 코인 심볼이 존재하는 코인인지 확인합니다.
    for coin in coin_list:
        if coin['symbol'] == coin_symbol:
            coin_id = coin['id']
            break
        else:
            coin_id = coin_symbol

    # 코인 ID를 사용하여 해당 코인의 시장 정보를 가져옵니다.
    coin_data = cg.get_coins_markets(ids=coin_id, vs_currency='usd')

    # 코인 정보가 존재하는 경우 해당 코인의 현재 가격과 24시간 동안 변동한 가격을 출력합니다.
    # 코인 정보가 존재하지 않는 경우 에러 메시지를 출력합니다.
    if coin_data is not None and len(coin_data) > 0:
        coin_price = coin_data[0]['current_price']
        coin_percentage_24h = round(coin_data[0]['price_change_percentage_24h'], 1)
        label.config(text=f"현재 가격은 ${coin_price} 입니다. 24시간동안 {coin_percentage_24h}% 변동했습니다.")
    else:
        label.config(text=f"{coin_id}라는 코인을 찾을수없습니다. 다시 확인하세요.")
        return

# 윈도우 창을 생성합니다.
window = tk.Tk()

# 윈도우 창의 크기와 타이틀을 설정합니다.
window_width = 400
window_height = 150
window.title('코인 가격(코인개코)')

# 코인 심볼을 입력할 수 있는 엔트리 위젯을 생성합니다.
label = tk.Label(window, text='원하는 코인 이름을 넣으세요.')
label.pack(pady=10)

# 코인 심볼을 입력할 수 있는 엔트리 위젯을 생성합니다.
entry = tk.Entry(window)
entry.pack(pady=10)
entry.bind('<Return>', on_return_key)

# 코인 가격을 조회하는 버튼을 생성합니다.
button = tk.Button(window, text='조회', command=get_coin_price)
button.pack(pady=10)

# 윈도우 창을 화면 중앙에 위치시킵니다.
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# 화면 중앙에 창을 배치하기 위한 x,y 좌표 계산
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# 창의 크기와 위치 설정
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# 창을 윈도우 모드로 실행하고 이벤트 루프 시작
window.mainloop()

