from jsonpath import jsonpath

data2 = {'code': 0, 'msg': 'OK',
         'data': {'id': 37646, 'leave_amount': 400000.0, 'mobile_phone': '18435132058', 'reg_name': '小柠檬',
                  'reg_time': '2023-03-21 21:03:06.0', 'type': 1,
                  'token_info': {'token_type': 'Bearer', 'expires_in': '2023-03-21 21:30:41',
                                 'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjM3NjQ2LCJleHAiOjE2Nzk0MDU0NDF9.TWZE6qrR-qbudcfHEy5GMyjGC6z4Aue93wPHsdZcB8pW9vF9SBbhku6WCXJvWxhJ_9mD0slv4aLWW8FB5sZTnA'}},
         'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
token = jsonpath(data2, "$..token")
member_id = jsonpath(data2,"$..mobile_phone")
print(token,member_id,sep='\n')
