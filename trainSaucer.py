from ultralytics import YOLO
from params import train_params
import torch
from tqdm import tqdm  # 실시간 진행 상황 모니터링
from sklearn.metrics import accuracy_score, f1_score  # 추가된 메트릭 계산용 라이브러리

# CUDA 사용 여부 설정
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")

# 모델 로드 및 설정
model = YOLO(train_params.model).to(device)

# 사용자 정의 데이터셋으로 모델 학습
for epoch in tqdm(range(train_params.epochs), desc="Training YOLOv8s"):
    print(f"Epoch {epoch + 1}/{train_params.epochs}")
    
    # 1. Train step
    results_train = model.train(
        data=train_params.yaml_path,  # 데이터셋 설정
        epochs=1,  # 에포크는 1씩 반복
        imgsz=train_params.img_size,  # 이미지 크기
        batch=train_params.batch_size,  # 배치 크기
        project=train_params.project,  # 결과 저장 경로
        name=train_params.name,  # 결과 파일 이름
        save_period=train_params.save_period,  # 매 에포크마다 가중치 저장
        device=device
    )
    
    # Train 결과 출력
    train_loss = results_train['metrics/loss']  # 손실
    train_accuracy = accuracy_score(results_train['labels'], results_train['preds'])  # 정확도
    train_f1 = f1_score(results_train['labels'], results_train['preds'], average='weighted')  # F1 스코어
    print(f"Train Loss: {train_loss}, Train Accuracy: {train_accuracy}, Train F1: {train_f1}")
    
    # 2. Validation step
    results_val = model.val(
        data=train_params.val_data,
        batch_size=train_params.batch_size,
        imgsz=train_params.img_size,
        device=device
    )
    
    # Validation 결과 출력
    val_loss = results_val['metrics/loss']  # 손실
    val_accuracy = accuracy_score(results_val['labels'], results_val['preds'])  # 정확도
    val_f1 = f1_score(results_val['labels'], results_val['preds'], average='weighted')  # F1 스코어
    print(f"Validation Loss: {val_loss}, Validation Accuracy: {val_accuracy}, Validation F1: {val_f1}")

# 마지막 에포크 후 Test
results_test = model.val(
    data=train_params.test_data,
    batch_size=train_params.batch_size,
    imgsz=train_params.img_size,
    device=device
)

# Test 결과 출력
test_loss = results_test['metrics/loss']  # 손실
test_accuracy = accuracy_score(results_test['labels'], results_test['preds'])  # 정확도
test_f1 = f1_score(results_test['labels'], results_test['preds'], average='weighted')  # F1 스코어
print(f"Test Loss: {test_loss}, Test Accuracy: {test_accuracy}, Test F1: {test_f1}")

print("모델 학습 완료")
