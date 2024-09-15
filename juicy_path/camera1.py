import cv2  # OpenCV 임포트
import threading
import time

# 카메라 열기
capture = cv2.VideoCapture(0)

# 카메라가 열리지 않으면 에러 메시지 출력
if not capture.isOpened():
    print("카메라를 열 수 없습니다.")
else:
    while True:
        ret, frame = capture.read()  # 카메라에서 프레임 읽기
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        # 프레임을 윈도우 창에 표시
        cv2.imshow('Camera Stream', frame)

        # 'q' 키를 누르면 루프를 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 카메라 리소스 해제 및 모든 창 닫기
capture.release()
cv2.destroyAllWindows()


