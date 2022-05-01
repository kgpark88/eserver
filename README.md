# 에너지 빅데이터 분석 서비스 서버

## 1. 파이썬 가상환경 생성 및 실행
### Windows
- python –m venv venv 
- venv\Scripts\activate.bat
### MacOS/Linux
- python3 -m venv venv
- source venv/bin/activate

## 2. 서버프로그램 소스 다운로드
- git clone https://github.com/kgpark88/eserver

## 3. 파이썬 패키지 설치
- pip install pandas
- pip install matplotlib
- pip install seaborn
- pip install django 
- pip install djangorestframework 
- pip install drf-yasg 
- pip install django-import-export 
- pip install django-cors-headers
- pip install sklearn
- pip install tensorflow

## 4. 테이블 생성
- cd eserver
- python manage.py makemigrations energy
- python manage.py migrate 

## 5. 데이터베이스 관리자 계정 생성
- python manage.py createsuperuser

## 6. 백엔드 서버 실행
- python manage.py runserver

## 7. 백엔드 웹서비스 접속
- http://localhost:8000
