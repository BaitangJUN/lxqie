import time

def pomodoro_timer():
    # 设置专注时长和休息时长，这里以25分钟的专注时间和5分钟的休息时间为例
    focus_time = 25 * 60  # 专注时长，单位为秒
    rest_time = 5 * 60  # 休息时长，单位为秒
    
    while True:
        print("开始专注...")
        time.sleep(focus_time)  # 等待专注时长
        
        print("专注结束，开始休息...")
        time.sleep(rest_time)  # 等待休息时长

pomodoro_timer()
