# Exception(오류)
#   - 프로그램을 개발하면서 예상하지 못한 상황
#      ㄴ 사용자 입력 오류

# 1. 예외 종류
#   - 예측 가능한 예외 → 예외 처리
#     ㄴ 핸드폰번호(숫자만)
#   - 예측 불가능한 예외
#     ㄴ 데이터센터 화재 → 미러 서버(차가 사고날 수 있으니 똑같은 차를 구매... => 자원 낭비)
#     ㄴ 정전 → UPS(자가 발전기)

# 2. 예외 기본 문법
# try:
#   - 예외가 발생할 수 있는 코드
# except:
#   - 예외를 처리하는 코드
# finally:
#   - 예외와 상관없이 무조건 실행되는 코드

# 예외 O: try → except → finally
# 예외 X: try → finally

# * 데이터베이스, 파일I(nput)/O(utput)의 경우는 반드시 예외 처리 필수! *

from urllib.request import urlopen, HTTPError
try:
    html = urlopen("http://www.naver.com")
except Exception as e:  # Exception 모든 예외 커버
    print(e)
finally:  # 도서관 자리를 비울 때 자리를 치운다(=자원반납. 그래야 다른 사람이 쓸 수 있음)
    # 사용한 자원을 반납할 때
    print("자원해제")

# except HTTPError as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)
