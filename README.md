## 0. Markdown(MD)
  - MD언어: 설명, 정리 언어!
  - MD문법 존재(30분 공부)

## 1. 개발환경 구축
### 1-1. Anaconda
  - anaconda prompt 실행
  - conda env list : 가상환경 목록 보기
  - conda create -n llm python=3.11 : llm 가상환경 생성
  - conda activate llm : llm 가상환경 접속
  - pip list : 가상환경에 설치 된 라이브러리 목록 보기
  - pip install [라이브러리] : 라이브러리 설치
  - cls : 화면 청소
  - Anaconda는 편리하지만 매우 무거움... (컴퓨팅 자원을 많이씀)

### 1-2. 로컬 가상환경(다음 학기)
  - 불편하지만, 매우 가벼움
  - Python을 직접 설치 + 가상환경 직접 생성(venv)
  - python -m venv venv 가상환경 생성

### 1-3. Github
  - 버전관리도구
  - 코드를 관리해주는 웹 저장소
#### Repository 연결
  - Github는 프로젝트 단위로 Repository 생성
  - 팀장이 Repository를 생성하고 팀원들을 초대해서 협업
  - Github는 Git이라고 하는 버전관리도구를 손쉽게 사용할 수 있는 플랫폼(Git설치) / git -v cmd에서 (버전)확인 가능
  - 로컬(컴퓨터, 노트북)-글로벌(website)
  - Repository가 로컬, 글로벌에 존재해야함
#### 깃 상태 확인
  - git status : git Repository 현재 상태 확인
#### 새로운 환경 구축
  - git init . : git Repository 생성(로컬)
  - git remote -v : 원격 Repository 연결 상태 확인(글로벌)
  - git remote add origin [URL] : 로컬과 글로벌 Repository 연결(글로벌)
  - git branch -M main : Master branch → main branch 변경(github(글로벌)은 main, 로컬(컴퓨터)이 main에 맞춰야함)
#### 파일 버전관리목록(로컬) 추가
  - git add [file] : 해당 파일을 버전관리 목록 추가
  - git add . : 현재 경로의 모든 파일을 버전관리 목록 추가
  - git add ~는 commit에 포함할 파일들을 선택
  - git commit -m "내용" : 버전 생성
  - git add와 commit 로컬에서 행위(글로벌 변화 X)
  - git commit ~은 선택된 파일들을 확정적으로 저장소에 기록
#### 권한 추가
  - git config --global user.name [github 이름] (대괄호 제외)
  - git config --global user. email [github 이메일] (대괄호 제외)
#### 글로벌에 업로드
  - git push origin main : Local의 commit으로 생성한 버전을 글로벌에 업로드
#### 코드 내려받기
  - git pull origin main : 글로벌의 main 코드를 내려받기
