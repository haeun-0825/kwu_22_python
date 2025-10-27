# 라이브러리, 패키지, 모듈
# - 라이브러리 >= 패키지 >= 모듈 (라이브러리가 제일 큰 개념)

# 라이브러리: 여러 패키지와 모듈의 묶음(numpy, pandas 등...)
# 모듈: 이미 작성된 프로그램(일반적으로 *.py)
# 패키지: 특정 기능과 관련된 여러 모듈의 묶음(lecture, Solution=패키지)

# 내부: Python에서 기본적으로 제공
# 외부: 외부 개발자가 개발한 라이브러리
# 사용자: 직접 개발해서 사용하는 경우

# 외부 모듈
#   가정: requests 1,000개 모듈로 구성(그 중 1개가 get)
#   1. 다운로드 및 설치 → pip install [라이브러리]
#   2. 호출 → import 구문
#     ㄴ import requests             1,000개 모두 호출
#     ㄴ import requests as req      1,000개 모두 호출 (as = 별명 / req라는 별명을 붙여줌)
#     ㄴ from requests import get    get 1개만 호출 (requests라이브러리로부터 get을 가져오겠다)
#   3. 사용
#     ㄴ requests.get()
#     ㄴ req.get()
#     ㄴ get()