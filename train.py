from ultralytics import YOLO
from params import train_params
import torch
from tqdm import tqdm  # 실시간 진행 상황 모니터링
from torchvision import transforms
from PIL import Image
import os

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
    train_metrics = results_train.results
    train_map50 = train_metrics['map50']
    train_map95 = train_metrics['map']
    train_precision = train_metrics['precision']
    train_recall = train_metrics['recall']
    train_iou = train_metrics['iou']
    
    print(f"Train Precision: {train_precision}, Train Recall: {train_recall}")
    print(f"Train mAP@0.5: {train_map50}, Train mAP@0.5:0.95: {train_map95}")
    print(f"Train IoU: {train_iou}")
    
    # 2. Validation step
    results_val = model.val(
        data=train_params.val_data,
        batch_size=train_params.batch_size,
        imgsz=train_params.img_size,
        device=device
    )
    
    # Validation 결과 출력
    val_metrics = results_val.results
    val_map50 = val_metrics['map50']
    val_map95 = val_metrics['map']
    val_precision = val_metrics['precision']
    val_recall = val_metrics['recall']
    val_iou = val_metrics['iou']
    
    print(f"Validation Precision: {val_precision}, Validation Recall: {val_recall}")
    print(f"Validation mAP@0.5: {val_map50}, Validation mAP@0.5:0.95: {val_map95}")
    print(f"Validation IoU: {val_iou}")

# 마지막 에포크 후 Test
results_test = model.val(
    data=train_params.test_data,
    batch_size=train_params.batch_size,
    imgsz=train_params.img_size,
    device=device
)

# Test 결과 출력
test_metrics = results_test.results
test_map50 = test_metrics['map50']
test_map95 = test_metrics['map']
test_precision = test_metrics['precision']
test_recall = test_metrics['recall']
test_iou = test_metrics['iou']

print(f"Test Precision: {test_precision}, Test Recall: {test_recall}")
print(f"Test mAP@0.5: {test_map50}, Test mAP@0.5:0.95: {test_map95}")
print(f"Test IoU: {test_iou}")

print("모델 학습 완료")
