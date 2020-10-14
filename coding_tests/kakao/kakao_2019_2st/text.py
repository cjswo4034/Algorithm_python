'''
1. 데이터 전송 형태: requests -> 딕셔너리, urllib -> 인코딩 후 바이너리.
2. 요청 메소드(get, post): requests -> 요청 메소드 명시,  urllib -> 데이터의 여부에 따라 get과 post 요청을 구분
3. 없는 페이지 요청 에러 처리: requests -> 에러를 띄우지 않음, urllib -> 에러를 띄움
'''
a = 1
arr = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
arr = [e2 for e1 in arr for e2 in e1]
print(arr)