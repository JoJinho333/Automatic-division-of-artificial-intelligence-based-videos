# 바운딩 박스 11개 적용되는 코딩

import json
import cv2

# 바꿔줘야 하는것
# json 파일 위치, 이름
# 메인코드 영상 위치, 이름
# 영상과 사진 비율 고려해야함

# json 파일 읽어오기
with open('C:\data\GOODDAY_Mple+210706+2+CAM2JSON.json', 'r', encoding='UTF-8') as f:
    json_data = json.load(f)
print(json.dumps(json_data, indent='\t'))

'''
경우의 수
person 밑에 들어있는 값의 길이가 2면
    그리고 person 안에 두번째 값의 eyes1 값의 길이가 0이 아니라면
        두번째 값에 대한 리스트를 생성
        그 안에 바운딩 박스 좌표를 넣기

    person 안에 두번째 값의 eyes1 값의 길이가 0이라면
        리스트를 생성
        그 안에 1로된 좌표 넣기

    person 안에 첫번째 값의 eyes1 값의 길이가 0이 아니라면
        첫번째 값에 대한 리스트를 생성
        그 안에 바운딩 박스 좌표를 넣기

    person 안에 첫번째 값의 eyes1 값의 길이가 0이라면
        리스트를 생성
        그 안에 1로된 좌표 넣기

==============================================================

person 밑에 들어있는 값의 길이가 1이면        
    person 안에 첫번째 값의 eyes1 값의 길이가 0이 아니라면
        첫번째 값에 대한 리스트를 생성
        그 안에 바운딩 박스 좌표를 넣기

        리스트를 생성
        두번째 바운딩 박스에 대한 빈공간을 만들었기 때문에 그 안에 1로된 좌표 넣기

    person 안에 첫번째 값의 eyes1 값의 길이가 0이면
        리스트를 생성
        그 안에 1로된 좌표 넣기

==============================================================
person 밑에 들어있는 값의 길이가 0이면 
    리스트를 생성
    첫번째와 두번째 바운딩 박스에 대한 값으로 그 안에 1로된 좌표 넣기

=> 이걸 사람 수에 따라 바운딩 박스 적용되는 코드로 바꾸면 좋음
'''

eye1_list = []
eye1_list_2 = []
eye1_list_3 = []
eye1_list_4 = []
eye1_list_5 = []
eye1_list_6 = []
eye1_list_7 = []
eye1_list_8 = []
eye1_list_9 = []
eye1_list_10 = []
eye1_list_11 = []

eyes1 = range(0, len(json_data[0]['data']))

for i in eyes1:
    if len(json_data[0]['data'][i]['person']) == 11:
        if len(json_data[0]['data'][i]['person'][10]['eyes1']) != 0:
            eye1_a_11 = json_data[0]['data'][i]['person'][10]['eyes1']
            line = []
            for j in range(4):
                eye1_b_11 = eye1_a_11.split(',')[j]
                eye1_c_11 = float(eye1_b_11)
                eye1_d_11 = eye1_c_11
                eye1_e_11 = round(eye1_d_11)
                line.append(eye1_e_11)
            eye1_list_11.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][9]['eyes1']) != 0:
            eye1_a_10 = json_data[0]['data'][i]['person'][9]['eyes1']
            line = []
            for j in range(4):
                eye1_b_10 = eye1_a_10.split(',')[j]
                eye1_c_10 = float(eye1_b_10)
                eye1_d_10 = eye1_c_10
                eye1_e_10 = round(eye1_d_10)
                line.append(eye1_e_10)
            eye1_list_10.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_10.append(line)

        if len(json_data[0]['data'][i]['person'][8]['eyes1']) != 0:
            eye1_a_9 = json_data[0]['data'][i]['person'][8]['eyes1']
            line = []
            for j in range(4):
                eye1_b_9 = eye1_a_9.split(',')[j]
                eye1_c_9 = float(eye1_b_9)
                eye1_d_9 = eye1_c_9
                eye1_e_9 = round(eye1_d_9)
                line.append(eye1_e_9)
            eye1_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['eyes1']) != 0:
            eye1_a_8 = json_data[0]['data'][i]['person'][7]['eyes1']
            line = []
            for j in range(4):
                eye1_b_8 = eye1_a_8.split(',')[j]
                eye1_c_8 = float(eye1_b_8)
                eye1_d_8 = eye1_c_8
                eye1_e_8 = round(eye1_d_8)
                line.append(eye1_e_8)
            eye1_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['eyes1']) != 0:
            eye1_a_7 = json_data[0]['data'][i]['person'][6]['eyes1']
            line = []
            for j in range(4):
                eye1_b_7 = eye1_a_7.split(',')[j]
                eye1_c_7 = float(eye1_b_7)
                eye1_d_7 = eye1_c_7
                eye1_e_7 = round(eye1_d_7)
                line.append(eye1_e_7)
            eye1_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes1']) != 0:
            eye1_a_6 = json_data[0]['data'][i]['person'][5]['eyes1']
            line = []
            for j in range(4):
                eye1_b_6 = eye1_a_6.split(',')[j]
                eye1_c_6 = float(eye1_b_6)
                eye1_d_6 = eye1_c_6
                eye1_e_6 = round(eye1_d_6)
                line.append(eye1_e_6)
            eye1_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes1']) != 0:
            eye1_a_5 = json_data[0]['data'][i]['person'][4]['eyes1']
            line = []
            for j in range(4):
                eye1_b_5 = eye1_a_5.split(',')[j]
                eye1_c_5 = float(eye1_b_5)
                eye1_d_5 = eye1_c_5
                eye1_e_5 = round(eye1_d_5)
                line.append(eye1_e_5)
            eye1_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes1']) != 0:
            eye1_a_4 = json_data[0]['data'][i]['person'][3]['eyes1']
            line = []
            for j in range(4):
                eye1_b_4 = eye1_a_4.split(',')[j]
                eye1_c_4 = float(eye1_b_4)
                eye1_d_4 = eye1_c_4
                eye1_e_4 = round(eye1_d_4)
                line.append(eye1_e_4)
            eye1_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes1']) != 0:
            eye1_a_3 = json_data[0]['data'][i]['person'][2]['eyes1']
            line = []
            for j in range(4):
                eye1_b_3 = eye1_a_3.split(',')[j]
                eye1_c_3 = float(eye1_b_3)
                eye1_d_3 = eye1_c_3
                eye1_e_3 = round(eye1_d_3)
                line.append(eye1_e_3)
            eye1_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes1']) != 0:
            eye1_a_2 = json_data[0]['data'][i]['person'][1]['eyes1']
            line = []
            for j in range(4):
                eye1_b_2 = eye1_a_2.split(',')[j]
                eye1_c_2 = float(eye1_b_2)
                eye1_d_2 = eye1_c_2
                eye1_e_2 = round(eye1_d_2)
                line.append(eye1_e_2)
            eye1_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 10:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][9]['eyes1']) != 0:
            eye1_a_10 = json_data[0]['data'][i]['person'][9]['eyes1']
            line = []
            for j in range(4):
                eye1_b_10 = eye1_a_10.split(',')[j]
                eye1_c_10 = float(eye1_b_10)
                eye1_d_10 = eye1_c_10
                eye1_e_10 = round(eye1_d_10)
                line.append(eye1_e_10)
            eye1_list_10.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_10.append(line)

        if len(json_data[0]['data'][i]['person'][8]['eyes1']) != 0:
            eye1_a_9 = json_data[0]['data'][i]['person'][8]['eyes1']
            line = []
            for j in range(4):
                eye1_b_9 = eye1_a_9.split(',')[j]
                eye1_c_9 = float(eye1_b_9)
                eye1_d_9 = eye1_c_9
                eye1_e_9 = round(eye1_d_9)
                line.append(eye1_e_9)
            eye1_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['eyes1']) != 0:
            eye1_a_8 = json_data[0]['data'][i]['person'][7]['eyes1']
            line = []
            for j in range(4):
                eye1_b_8 = eye1_a_8.split(',')[j]
                eye1_c_8 = float(eye1_b_8)
                eye1_d_8 = eye1_c_8
                eye1_e_8 = round(eye1_d_8)
                line.append(eye1_e_8)
            eye1_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['eyes1']) != 0:
            eye1_a_7 = json_data[0]['data'][i]['person'][6]['eyes1']
            line = []
            for j in range(4):
                eye1_b_7 = eye1_a_7.split(',')[j]
                eye1_c_7 = float(eye1_b_7)
                eye1_d_7 = eye1_c_7
                eye1_e_7 = round(eye1_d_7)
                line.append(eye1_e_7)
            eye1_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes1']) != 0:
            eye1_a_6 = json_data[0]['data'][i]['person'][5]['eyes1']
            line = []
            for j in range(4):
                eye1_b_6 = eye1_a_6.split(',')[j]
                eye1_c_6 = float(eye1_b_6)
                eye1_d_6 = eye1_c_6
                eye1_e_6 = round(eye1_d_6)
                line.append(eye1_e_6)
            eye1_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes1']) != 0:
            eye1_a_5 = json_data[0]['data'][i]['person'][4]['eyes1']
            line = []
            for j in range(4):
                eye1_b_5 = eye1_a_5.split(',')[j]
                eye1_c_5 = float(eye1_b_5)
                eye1_d_5 = eye1_c_5
                eye1_e_5 = round(eye1_d_5)
                line.append(eye1_e_5)
            eye1_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes1']) != 0:
            eye1_a_4 = json_data[0]['data'][i]['person'][3]['eyes1']
            line = []
            for j in range(4):
                eye1_b_4 = eye1_a_4.split(',')[j]
                eye1_c_4 = float(eye1_b_4)
                eye1_d_4 = eye1_c_4
                eye1_e_4 = round(eye1_d_4)
                line.append(eye1_e_4)
            eye1_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes1']) != 0:
            eye1_a_3 = json_data[0]['data'][i]['person'][2]['eyes1']
            line = []
            for j in range(4):
                eye1_b_3 = eye1_a_3.split(',')[j]
                eye1_c_3 = float(eye1_b_3)
                eye1_d_3 = eye1_c_3
                eye1_e_3 = round(eye1_d_3)
                line.append(eye1_e_3)
            eye1_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes1']) != 0:
            eye1_a_2 = json_data[0]['data'][i]['person'][1]['eyes1']
            line = []
            for j in range(4):
                eye1_b_2 = eye1_a_2.split(',')[j]
                eye1_c_2 = float(eye1_b_2)
                eye1_d_2 = eye1_c_2
                eye1_e_2 = round(eye1_d_2)
                line.append(eye1_e_2)
            eye1_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 9:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list_10.append(line)
        eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][8]['eyes1']) != 0:
            eye1_a_9 = json_data[0]['data'][i]['person'][8]['eyes1']
            line = []
            for j in range(4):
                eye1_b_9 = eye1_a_9.split(',')[j]
                eye1_c_9 = float(eye1_b_9)
                eye1_d_9 = eye1_c_9
                eye1_e_9 = round(eye1_d_9)
                line.append(eye1_e_9)
            eye1_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['eyes1']) != 0:
            eye1_a_8 = json_data[0]['data'][i]['person'][7]['eyes1']
            line = []
            for j in range(4):
                eye1_b_8 = eye1_a_8.split(',')[j]
                eye1_c_8 = float(eye1_b_8)
                eye1_d_8 = eye1_c_8
                eye1_e_8 = round(eye1_d_8)
                line.append(eye1_e_8)
            eye1_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['eyes1']) != 0:
            eye1_a_7 = json_data[0]['data'][i]['person'][6]['eyes1']
            line = []
            for j in range(4):
                eye1_b_7 = eye1_a_7.split(',')[j]
                eye1_c_7 = float(eye1_b_7)
                eye1_d_7 = eye1_c_7
                eye1_e_7 = round(eye1_d_7)
                line.append(eye1_e_7)
            eye1_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes1']) != 0:
            eye1_a_6 = json_data[0]['data'][i]['person'][5]['eyes1']
            line = []
            for j in range(4):
                eye1_b_6 = eye1_a_6.split(',')[j]
                eye1_c_6 = float(eye1_b_6)
                eye1_d_6 = eye1_c_6
                eye1_e_6 = round(eye1_d_6)
                line.append(eye1_e_6)
            eye1_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes1']) != 0:
            eye1_a_5 = json_data[0]['data'][i]['person'][4]['eyes1']
            line = []
            for j in range(4):
                eye1_b_5 = eye1_a_5.split(',')[j]
                eye1_c_5 = float(eye1_b_5)
                eye1_d_5 = eye1_c_5
                eye1_e_5 = round(eye1_d_5)
                line.append(eye1_e_5)
            eye1_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes1']) != 0:
            eye1_a_4 = json_data[0]['data'][i]['person'][3]['eyes1']
            line = []
            for j in range(4):
                eye1_b_4 = eye1_a_4.split(',')[j]
                eye1_c_4 = float(eye1_b_4)
                eye1_d_4 = eye1_c_4
                eye1_e_4 = round(eye1_d_4)
                line.append(eye1_e_4)
            eye1_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes1']) != 0:
            eye1_a_3 = json_data[0]['data'][i]['person'][2]['eyes1']
            line = []
            for j in range(4):
                eye1_b_3 = eye1_a_3.split(',')[j]
                eye1_c_3 = float(eye1_b_3)
                eye1_d_3 = eye1_c_3
                eye1_e_3 = round(eye1_d_3)
                line.append(eye1_e_3)
            eye1_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes1']) != 0:
            eye1_a_2 = json_data[0]['data'][i]['person'][1]['eyes1']
            line = []
            for j in range(4):
                eye1_b_2 = eye1_a_2.split(',')[j]
                eye1_c_2 = float(eye1_b_2)
                eye1_d_2 = eye1_c_2
                eye1_e_2 = round(eye1_d_2)
                line.append(eye1_e_2)
            eye1_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 8:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list_9.append(line)
        eye1_list_10.append(line)
        eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][7]['eyes1']) != 0:
            eye1_a_8 = json_data[0]['data'][i]['person'][7]['eyes1']
            line = []
            for j in range(4):
                eye1_b_8 = eye1_a_8.split(',')[j]
                eye1_c_8 = float(eye1_b_8)
                eye1_d_8 = eye1_c_8
                eye1_e_8 = round(eye1_d_8)
                line.append(eye1_e_8)
            eye1_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['eyes1']) != 0:
            eye1_a_7 = json_data[0]['data'][i]['person'][6]['eyes1']
            line = []
            for j in range(4):
                eye1_b_7 = eye1_a_7.split(',')[j]
                eye1_c_7 = float(eye1_b_7)
                eye1_d_7 = eye1_c_7
                eye1_e_7 = round(eye1_d_7)
                line.append(eye1_e_7)
            eye1_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes1']) != 0:
            eye1_a_6 = json_data[0]['data'][i]['person'][5]['eyes1']
            line = []
            for j in range(4):
                eye1_b_6 = eye1_a_6.split(',')[j]
                eye1_c_6 = float(eye1_b_6)
                eye1_d_6 = eye1_c_6
                eye1_e_6 = round(eye1_d_6)
                line.append(eye1_e_6)
            eye1_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes1']) != 0:
            eye1_a_5 = json_data[0]['data'][i]['person'][4]['eyes1']
            line = []
            for j in range(4):
                eye1_b_5 = eye1_a_5.split(',')[j]
                eye1_c_5 = float(eye1_b_5)
                eye1_d_5 = eye1_c_5
                eye1_e_5 = round(eye1_d_5)
                line.append(eye1_e_5)
            eye1_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes1']) != 0:
            eye1_a_4 = json_data[0]['data'][i]['person'][3]['eyes1']
            line = []
            for j in range(4):
                eye1_b_4 = eye1_a_4.split(',')[j]
                eye1_c_4 = float(eye1_b_4)
                eye1_d_4 = eye1_c_4
                eye1_e_4 = round(eye1_d_4)
                line.append(eye1_e_4)
            eye1_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes1']) != 0:
            eye1_a_3 = json_data[0]['data'][i]['person'][2]['eyes1']
            line = []
            for j in range(4):
                eye1_b_3 = eye1_a_3.split(',')[j]
                eye1_c_3 = float(eye1_b_3)
                eye1_d_3 = eye1_c_3
                eye1_e_3 = round(eye1_d_3)
                line.append(eye1_e_3)
            eye1_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes1']) != 0:
            eye1_a_2 = json_data[0]['data'][i]['person'][1]['eyes1']
            line = []
            for j in range(4):
                eye1_b_2 = eye1_a_2.split(',')[j]
                eye1_c_2 = float(eye1_b_2)
                eye1_d_2 = eye1_c_2
                eye1_e_2 = round(eye1_d_2)
                line.append(eye1_e_2)
            eye1_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 7:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list_8.append(line)
        eye1_list_9.append(line)
        eye1_list_10.append(line)
        eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][6]['eyes1']) != 0:
            eye1_a_7 = json_data[0]['data'][i]['person'][6]['eyes1']
            line = []
            for j in range(4):
                eye1_b_7 = eye1_a_7.split(',')[j]
                eye1_c_7 = float(eye1_b_7)
                eye1_d_7 = eye1_c_7
                eye1_e_7 = round(eye1_d_7)
                line.append(eye1_e_7)
            eye1_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes1']) != 0:
            eye1_a_6 = json_data[0]['data'][i]['person'][5]['eyes1']
            line = []
            for j in range(4):
                eye1_b_6 = eye1_a_6.split(',')[j]
                eye1_c_6 = float(eye1_b_6)
                eye1_d_6 = eye1_c_6
                eye1_e_6 = round(eye1_d_6)
                line.append(eye1_e_6)
            eye1_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes1']) != 0:
            eye1_a_5 = json_data[0]['data'][i]['person'][4]['eyes1']
            line = []
            for j in range(4):
                eye1_b_5 = eye1_a_5.split(',')[j]
                eye1_c_5 = float(eye1_b_5)
                eye1_d_5 = eye1_c_5
                eye1_e_5 = round(eye1_d_5)
                line.append(eye1_e_5)
            eye1_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes1']) != 0:
            eye1_a_4 = json_data[0]['data'][i]['person'][3]['eyes1']
            line = []
            for j in range(4):
                eye1_b_4 = eye1_a_4.split(',')[j]
                eye1_c_4 = float(eye1_b_4)
                eye1_d_4 = eye1_c_4
                eye1_e_4 = round(eye1_d_4)
                line.append(eye1_e_4)
            eye1_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes1']) != 0:
            eye1_a_3 = json_data[0]['data'][i]['person'][2]['eyes1']
            line = []
            for j in range(4):
                eye1_b_3 = eye1_a_3.split(',')[j]
                eye1_c_3 = float(eye1_b_3)
                eye1_d_3 = eye1_c_3
                eye1_e_3 = round(eye1_d_3)
                line.append(eye1_e_3)
            eye1_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes1']) != 0:
            eye1_a_2 = json_data[0]['data'][i]['person'][1]['eyes1']
            line = []
            for j in range(4):
                eye1_b_2 = eye1_a_2.split(',')[j]
                eye1_c_2 = float(eye1_b_2)
                eye1_d_2 = eye1_c_2
                eye1_e_2 = round(eye1_d_2)
                line.append(eye1_e_2)
            eye1_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 6:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list_7.append(line)
        eye1_list_8.append(line)
        eye1_list_9.append(line)
        eye1_list_10.append(line)
        eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes1']) != 0:
            eye1_a_6 = json_data[0]['data'][i]['person'][5]['eyes1']
            line = []
            for j in range(4):
                eye1_b_6 = eye1_a_6.split(',')[j]
                eye1_c_6 = float(eye1_b_6)
                eye1_d_6 = eye1_c_6
                eye1_e_6 = round(eye1_d_6)
                line.append(eye1_e_6)
            eye1_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes1']) != 0:
            eye1_a_5 = json_data[0]['data'][i]['person'][4]['eyes1']
            line = []
            for j in range(4):
                eye1_b_5 = eye1_a_5.split(',')[j]
                eye1_c_5 = float(eye1_b_5)
                eye1_d_5 = eye1_c_5
                eye1_e_5 = round(eye1_d_5)
                line.append(eye1_e_5)
            eye1_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes1']) != 0:
            eye1_a_4 = json_data[0]['data'][i]['person'][3]['eyes1']
            line = []
            for j in range(4):
                eye1_b_4 = eye1_a_4.split(',')[j]
                eye1_c_4 = float(eye1_b_4)
                eye1_d_4 = eye1_c_4
                eye1_e_4 = round(eye1_d_4)
                line.append(eye1_e_4)
            eye1_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes1']) != 0:
            eye1_a_3 = json_data[0]['data'][i]['person'][2]['eyes1']
            line = []
            for j in range(4):
                eye1_b_3 = eye1_a_3.split(',')[j]
                eye1_c_3 = float(eye1_b_3)
                eye1_d_3 = eye1_c_3
                eye1_e_3 = round(eye1_d_3)
                line.append(eye1_e_3)
            eye1_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes1']) != 0:
            eye1_a_2 = json_data[0]['data'][i]['person'][1]['eyes1']
            line = []
            for j in range(4):
                eye1_b_2 = eye1_a_2.split(',')[j]
                eye1_c_2 = float(eye1_b_2)
                eye1_d_2 = eye1_c_2
                eye1_e_2 = round(eye1_d_2)
                line.append(eye1_e_2)
            eye1_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 5:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list_6.append(line)
        eye1_list_7.append(line)
        eye1_list_8.append(line)
        eye1_list_9.append(line)
        eye1_list_10.append(line)
        eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes1']) != 0:
            eye1_a_5 = json_data[0]['data'][i]['person'][4]['eyes1']
            line = []
            for j in range(4):
                eye1_b_5 = eye1_a_5.split(',')[j]
                eye1_c_5 = float(eye1_b_5)
                eye1_d_5 = eye1_c_5
                eye1_e_5 = round(eye1_d_5)
                line.append(eye1_e_5)
            eye1_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes1']) != 0:
            eye1_a_4 = json_data[0]['data'][i]['person'][3]['eyes1']
            line = []
            for j in range(4):
                eye1_b_4 = eye1_a_4.split(',')[j]
                eye1_c_4 = float(eye1_b_4)
                eye1_d_4 = eye1_c_4
                eye1_e_4 = round(eye1_d_4)
                line.append(eye1_e_4)
            eye1_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes1']) != 0:
            eye1_a_3 = json_data[0]['data'][i]['person'][2]['eyes1']
            line = []
            for j in range(4):
                eye1_b_3 = eye1_a_3.split(',')[j]
                eye1_c_3 = float(eye1_b_3)
                eye1_d_3 = eye1_c_3
                eye1_e_3 = round(eye1_d_3)
                line.append(eye1_e_3)
            eye1_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes1']) != 0:
            eye1_a_2 = json_data[0]['data'][i]['person'][1]['eyes1']
            line = []
            for j in range(4):
                eye1_b_2 = eye1_a_2.split(',')[j]
                eye1_c_2 = float(eye1_b_2)
                eye1_d_2 = eye1_c_2
                eye1_e_2 = round(eye1_d_2)
                line.append(eye1_e_2)
            eye1_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 4:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list_5.append(line)
        eye1_list_6.append(line)
        eye1_list_7.append(line)
        eye1_list_8.append(line)
        eye1_list_9.append(line)
        eye1_list_10.append(line)
        eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes1']) != 0:
            eye1_a_4 = json_data[0]['data'][i]['person'][3]['eyes1']
            line = []
            for j in range(4):
                eye1_b_4 = eye1_a_4.split(',')[j]
                eye1_c_4 = float(eye1_b_4)
                eye1_d_4 = eye1_c_4
                eye1_e_4 = round(eye1_d_4)
                line.append(eye1_e_4)
            eye1_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes1']) != 0:
            eye1_a_3 = json_data[0]['data'][i]['person'][2]['eyes1']
            line = []
            for j in range(4):
                eye1_b_3 = eye1_a_3.split(',')[j]
                eye1_c_3 = float(eye1_b_3)
                eye1_d_3 = eye1_c_3
                eye1_e_3 = round(eye1_d_3)
                line.append(eye1_e_3)
            eye1_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes1']) != 0:
            eye1_a_2 = json_data[0]['data'][i]['person'][1]['eyes1']
            line = []
            for j in range(4):
                eye1_b_2 = eye1_a_2.split(',')[j]
                eye1_c_2 = float(eye1_b_2)
                eye1_d_2 = eye1_c_2
                eye1_e_2 = round(eye1_d_2)
                line.append(eye1_e_2)
            eye1_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 3:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list_4.append(line)
        eye1_list_5.append(line)
        eye1_list_6.append(line)
        eye1_list_7.append(line)
        eye1_list_8.append(line)
        eye1_list_9.append(line)
        eye1_list_10.append(line)
        eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes1']) != 0:
            eye1_a_3 = json_data[0]['data'][i]['person'][2]['eyes1']
            line = []
            for j in range(4):
                eye1_b_3 = eye1_a_3.split(',')[j]
                eye1_c_3 = float(eye1_b_3)
                eye1_d_3 = eye1_c_3
                eye1_e_3 = round(eye1_d_3)
                line.append(eye1_e_3)
            eye1_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes1']) != 0:
            eye1_a_2 = json_data[0]['data'][i]['person'][1]['eyes1']
            line = []
            for j in range(4):
                eye1_b_2 = eye1_a_2.split(',')[j]
                eye1_c_2 = float(eye1_b_2)
                eye1_d_2 = eye1_c_2
                eye1_e_2 = round(eye1_d_2)
                line.append(eye1_e_2)
            eye1_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 2:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list_3.append(line)
        eye1_list_4.append(line)
        eye1_list_5.append(line)
        eye1_list_6.append(line)
        eye1_list_7.append(line)
        eye1_list_8.append(line)
        eye1_list_9.append(line)
        eye1_list_10.append(line)
        eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes1']) != 0:
            eye1_a_2 = json_data[0]['data'][i]['person'][1]['eyes1']
            line = []
            for j in range(4):
                eye1_b_2 = eye1_a_2.split(',')[j]
                eye1_c_2 = float(eye1_b_2)
                eye1_d_2 = eye1_c_2
                eye1_e_2 = round(eye1_d_2)
                line.append(eye1_e_2)
            eye1_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 1:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list_2.append(line)
        eye1_list_3.append(line)
        eye1_list_4.append(line)
        eye1_list_5.append(line)
        eye1_list_6.append(line)
        eye1_list_7.append(line)
        eye1_list_8.append(line)
        eye1_list_9.append(line)
        eye1_list_10.append(line)
        eye1_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes1']) != 0:
            eye1_a = json_data[0]['data'][i]['person'][0]['eyes1']
            line = []
            for j in range(4):
                eye1_b = eye1_a.split(',')[j]
                eye1_c = float(eye1_b)
                eye1_d = eye1_c
                eye1_e = round(eye1_d)
                line.append(eye1_e)
            eye1_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye1_list.append(line)

    else:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye1_list.append(line)
        eye1_list_2.append(line)
        eye1_list_3.append(line)
        eye1_list_4.append(line)
        eye1_list_5.append(line)
        eye1_list_6.append(line)
        eye1_list_7.append(line)
        eye1_list_8.append(line)
        eye1_list_9.append(line)
        eye1_list_10.append(line)
        eye1_list_11.append(line)

print(eye1_list)
print(eye1_list_2)
print(len(eye1_list_2))

# bounding box eye2 좌표 리스트로 빼기

eye2_list = []
eye2_list_2 = []
eye2_list_3 = []
eye2_list_4 = []
eye2_list_5 = []
eye2_list_6 = []
eye2_list_7 = []
eye2_list_8 = []
eye2_list_9 = []
eye2_list_10 = []
eye2_list_11 = []

eyes2 = range(0, len(json_data[0]['data']))

for i in eyes2:
    if len(json_data[0]['data'][i]['person']) == 11:
        if len(json_data[0]['data'][i]['person'][10]['eyes2']) != 0:
            eye2_a_11 = json_data[0]['data'][i]['person'][10]['eyes2']
            line = []
            for j in range(4):
                eye2_b_11 = eye2_a_11.split(',')[j]
                eye2_c_11 = float(eye2_b_11)
                eye2_d_11 = eye2_c_11
                eye2_e_11 = round(eye2_d_11)
                line.append(eye2_e_11)
            eye2_list_11.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][9]['eyes2']) != 0:
            eye2_a_10 = json_data[0]['data'][i]['person'][9]['eyes2']
            line = []
            for j in range(4):
                eye2_b_10 = eye2_a_10.split(',')[j]
                eye2_c_10 = float(eye2_b_10)
                eye2_d_10 = eye2_c_10
                eye2_e_10 = round(eye2_d_10)
                line.append(eye2_e_10)
            eye2_list_10.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_10.append(line)

        if len(json_data[0]['data'][i]['person'][8]['eyes2']) != 0:
            eye2_a_9 = json_data[0]['data'][i]['person'][8]['eyes2']
            line = []
            for j in range(4):
                eye2_b_9 = eye2_a_9.split(',')[j]
                eye2_c_9 = float(eye2_b_9)
                eye2_d_9 = eye2_c_9
                eye2_e_9 = round(eye2_d_9)
                line.append(eye2_e_9)
            eye2_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['eyes2']) != 0:
            eye2_a_8 = json_data[0]['data'][i]['person'][7]['eyes2']
            line = []
            for j in range(4):
                eye2_b_8 = eye2_a_8.split(',')[j]
                eye2_c_8 = float(eye2_b_8)
                eye2_d_8 = eye2_c_8
                eye2_e_8 = round(eye2_d_8)
                line.append(eye2_e_8)
            eye2_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['eyes2']) != 0:
            eye2_a_7 = json_data[0]['data'][i]['person'][6]['eyes2']
            line = []
            for j in range(4):
                eye2_b_7 = eye2_a_7.split(',')[j]
                eye2_c_7 = float(eye2_b_7)
                eye2_d_7 = eye2_c_7
                eye2_e_7 = round(eye2_d_7)
                line.append(eye2_e_7)
            eye2_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes2']) != 0:
            eye2_a_6 = json_data[0]['data'][i]['person'][5]['eyes2']
            line = []
            for j in range(4):
                eye2_b_6 = eye2_a_6.split(',')[j]
                eye2_c_6 = float(eye2_b_6)
                eye2_d_6 = eye2_c_6
                eye2_e_6 = round(eye2_d_6)
                line.append(eye2_e_6)
            eye2_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes2']) != 0:
            eye2_a_5 = json_data[0]['data'][i]['person'][4]['eyes2']
            line = []
            for j in range(4):
                eye2_b_5 = eye2_a_5.split(',')[j]
                eye2_c_5 = float(eye2_b_5)
                eye2_d_5 = eye2_c_5
                eye2_e_5 = round(eye2_d_5)
                line.append(eye2_e_5)
            eye2_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes2']) != 0:
            eye2_a_4 = json_data[0]['data'][i]['person'][3]['eyes2']
            line = []
            for j in range(4):
                eye2_b_4 = eye2_a_4.split(',')[j]
                eye2_c_4 = float(eye2_b_4)
                eye2_d_4 = eye2_c_4
                eye2_e_4 = round(eye2_d_4)
                line.append(eye2_e_4)
            eye2_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes2']) != 0:
            eye2_a_3 = json_data[0]['data'][i]['person'][2]['eyes2']
            line = []
            for j in range(4):
                eye2_b_3 = eye2_a_3.split(',')[j]
                eye2_c_3 = float(eye2_b_3)
                eye2_d_3 = eye2_c_3
                eye2_e_3 = round(eye2_d_3)
                line.append(eye2_e_3)
            eye2_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes2']) != 0:
            eye2_a_2 = json_data[0]['data'][i]['person'][1]['eyes2']
            line = []
            for j in range(4):
                eye2_b_2 = eye2_a_2.split(',')[j]
                eye2_c_2 = float(eye2_b_2)
                eye2_d_2 = eye2_c_2
                eye2_e_2 = round(eye2_d_2)
                line.append(eye2_e_2)
            eye2_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 10:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][9]['eyes2']) != 0:
            eye2_a_10 = json_data[0]['data'][i]['person'][9]['eyes2']
            line = []
            for j in range(4):
                eye2_b_10 = eye2_a_10.split(',')[j]
                eye2_c_10 = float(eye2_b_10)
                eye2_d_10 = eye2_c_10
                eye2_e_10 = round(eye2_d_10)
                line.append(eye2_e_10)
            eye2_list_10.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_10.append(line)

        if len(json_data[0]['data'][i]['person'][8]['eyes2']) != 0:
            eye2_a_9 = json_data[0]['data'][i]['person'][8]['eyes2']
            line = []
            for j in range(4):
                eye2_b_9 = eye2_a_9.split(',')[j]
                eye2_c_9 = float(eye2_b_9)
                eye2_d_9 = eye2_c_9
                eye2_e_9 = round(eye2_d_9)
                line.append(eye2_e_9)
            eye2_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['eyes2']) != 0:
            eye2_a_8 = json_data[0]['data'][i]['person'][7]['eyes2']
            line = []
            for j in range(4):
                eye2_b_8 = eye2_a_8.split(',')[j]
                eye2_c_8 = float(eye2_b_8)
                eye2_d_8 = eye2_c_8
                eye2_e_8 = round(eye2_d_8)
                line.append(eye2_e_8)
            eye2_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['eyes2']) != 0:
            eye2_a_7 = json_data[0]['data'][i]['person'][6]['eyes2']
            line = []
            for j in range(4):
                eye2_b_7 = eye2_a_7.split(',')[j]
                eye2_c_7 = float(eye2_b_7)
                eye2_d_7 = eye2_c_7
                eye2_e_7 = round(eye2_d_7)
                line.append(eye2_e_7)
            eye2_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes2']) != 0:
            eye2_a_6 = json_data[0]['data'][i]['person'][5]['eyes2']
            line = []
            for j in range(4):
                eye2_b_6 = eye2_a_6.split(',')[j]
                eye2_c_6 = float(eye2_b_6)
                eye2_d_6 = eye2_c_6
                eye2_e_6 = round(eye2_d_6)
                line.append(eye2_e_6)
            eye2_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes2']) != 0:
            eye2_a_5 = json_data[0]['data'][i]['person'][4]['eyes2']
            line = []
            for j in range(4):
                eye2_b_5 = eye2_a_5.split(',')[j]
                eye2_c_5 = float(eye2_b_5)
                eye2_d_5 = eye2_c_5
                eye2_e_5 = round(eye2_d_5)
                line.append(eye2_e_5)
            eye2_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes2']) != 0:
            eye2_a_4 = json_data[0]['data'][i]['person'][3]['eyes2']
            line = []
            for j in range(4):
                eye2_b_4 = eye2_a_4.split(',')[j]
                eye2_c_4 = float(eye2_b_4)
                eye2_d_4 = eye2_c_4
                eye2_e_4 = round(eye2_d_4)
                line.append(eye2_e_4)
            eye2_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes2']) != 0:
            eye2_a_3 = json_data[0]['data'][i]['person'][2]['eyes2']
            line = []
            for j in range(4):
                eye2_b_3 = eye2_a_3.split(',')[j]
                eye2_c_3 = float(eye2_b_3)
                eye2_d_3 = eye2_c_3
                eye2_e_3 = round(eye2_d_3)
                line.append(eye2_e_3)
            eye2_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes2']) != 0:
            eye2_a_2 = json_data[0]['data'][i]['person'][1]['eyes2']
            line = []
            for j in range(4):
                eye2_b_2 = eye2_a_2.split(',')[j]
                eye2_c_2 = float(eye2_b_2)
                eye2_d_2 = eye2_c_2
                eye2_e_2 = round(eye2_d_2)
                line.append(eye2_e_2)
            eye2_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 9:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list_10.append(line)
        eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][8]['eyes2']) != 0:
            eye2_a_9 = json_data[0]['data'][i]['person'][8]['eyes2']
            line = []
            for j in range(4):
                eye2_b_9 = eye2_a_9.split(',')[j]
                eye2_c_9 = float(eye2_b_9)
                eye2_d_9 = eye2_c_9
                eye2_e_9 = round(eye2_d_9)
                line.append(eye2_e_9)
            eye2_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['eyes2']) != 0:
            eye2_a_8 = json_data[0]['data'][i]['person'][7]['eyes2']
            line = []
            for j in range(4):
                eye2_b_8 = eye2_a_8.split(',')[j]
                eye2_c_8 = float(eye2_b_8)
                eye2_d_8 = eye2_c_8
                eye2_e_8 = round(eye2_d_8)
                line.append(eye2_e_8)
            eye2_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['eyes2']) != 0:
            eye2_a_7 = json_data[0]['data'][i]['person'][6]['eyes2']
            line = []
            for j in range(4):
                eye2_b_7 = eye2_a_7.split(',')[j]
                eye2_c_7 = float(eye2_b_7)
                eye2_d_7 = eye2_c_7
                eye2_e_7 = round(eye2_d_7)
                line.append(eye2_e_7)
            eye2_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes2']) != 0:
            eye2_a_6 = json_data[0]['data'][i]['person'][5]['eyes2']
            line = []
            for j in range(4):
                eye2_b_6 = eye2_a_6.split(',')[j]
                eye2_c_6 = float(eye2_b_6)
                eye2_d_6 = eye2_c_6
                eye2_e_6 = round(eye2_d_6)
                line.append(eye2_e_6)
            eye2_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes2']) != 0:
            eye2_a_5 = json_data[0]['data'][i]['person'][4]['eyes2']
            line = []
            for j in range(4):
                eye2_b_5 = eye2_a_5.split(',')[j]
                eye2_c_5 = float(eye2_b_5)
                eye2_d_5 = eye2_c_5
                eye2_e_5 = round(eye2_d_5)
                line.append(eye2_e_5)
            eye2_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes2']) != 0:
            eye2_a_4 = json_data[0]['data'][i]['person'][3]['eyes2']
            line = []
            for j in range(4):
                eye2_b_4 = eye2_a_4.split(',')[j]
                eye2_c_4 = float(eye2_b_4)
                eye2_d_4 = eye2_c_4
                eye2_e_4 = round(eye2_d_4)
                line.append(eye2_e_4)
            eye2_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes2']) != 0:
            eye2_a_3 = json_data[0]['data'][i]['person'][2]['eyes2']
            line = []
            for j in range(4):
                eye2_b_3 = eye2_a_3.split(',')[j]
                eye2_c_3 = float(eye2_b_3)
                eye2_d_3 = eye2_c_3
                eye2_e_3 = round(eye2_d_3)
                line.append(eye2_e_3)
            eye2_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes2']) != 0:
            eye2_a_2 = json_data[0]['data'][i]['person'][1]['eyes2']
            line = []
            for j in range(4):
                eye2_b_2 = eye2_a_2.split(',')[j]
                eye2_c_2 = float(eye2_b_2)
                eye2_d_2 = eye2_c_2
                eye2_e_2 = round(eye2_d_2)
                line.append(eye2_e_2)
            eye2_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 8:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list_9.append(line)
        eye2_list_10.append(line)
        eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][7]['eyes2']) != 0:
            eye2_a_8 = json_data[0]['data'][i]['person'][7]['eyes2']
            line = []
            for j in range(4):
                eye2_b_8 = eye2_a_8.split(',')[j]
                eye2_c_8 = float(eye2_b_8)
                eye2_d_8 = eye2_c_8
                eye2_e_8 = round(eye2_d_8)
                line.append(eye2_e_8)
            eye2_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['eyes2']) != 0:
            eye2_a_7 = json_data[0]['data'][i]['person'][6]['eyes2']
            line = []
            for j in range(4):
                eye2_b_7 = eye2_a_7.split(',')[j]
                eye2_c_7 = float(eye2_b_7)
                eye2_d_7 = eye2_c_7
                eye2_e_7 = round(eye2_d_7)
                line.append(eye2_e_7)
            eye2_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes2']) != 0:
            eye2_a_6 = json_data[0]['data'][i]['person'][5]['eyes2']
            line = []
            for j in range(4):
                eye2_b_6 = eye2_a_6.split(',')[j]
                eye2_c_6 = float(eye2_b_6)
                eye2_d_6 = eye2_c_6
                eye2_e_6 = round(eye2_d_6)
                line.append(eye2_e_6)
            eye2_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes2']) != 0:
            eye2_a_5 = json_data[0]['data'][i]['person'][4]['eyes2']
            line = []
            for j in range(4):
                eye2_b_5 = eye2_a_5.split(',')[j]
                eye2_c_5 = float(eye2_b_5)
                eye2_d_5 = eye2_c_5
                eye2_e_5 = round(eye2_d_5)
                line.append(eye2_e_5)
            eye2_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes2']) != 0:
            eye2_a_4 = json_data[0]['data'][i]['person'][3]['eyes2']
            line = []
            for j in range(4):
                eye2_b_4 = eye2_a_4.split(',')[j]
                eye2_c_4 = float(eye2_b_4)
                eye2_d_4 = eye2_c_4
                eye2_e_4 = round(eye2_d_4)
                line.append(eye2_e_4)
            eye2_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes2']) != 0:
            eye2_a_3 = json_data[0]['data'][i]['person'][2]['eyes2']
            line = []
            for j in range(4):
                eye2_b_3 = eye2_a_3.split(',')[j]
                eye2_c_3 = float(eye2_b_3)
                eye2_d_3 = eye2_c_3
                eye2_e_3 = round(eye2_d_3)
                line.append(eye2_e_3)
            eye2_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes2']) != 0:
            eye2_a_2 = json_data[0]['data'][i]['person'][1]['eyes2']
            line = []
            for j in range(4):
                eye2_b_2 = eye2_a_2.split(',')[j]
                eye2_c_2 = float(eye2_b_2)
                eye2_d_2 = eye2_c_2
                eye2_e_2 = round(eye2_d_2)
                line.append(eye2_e_2)
            eye2_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 7:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list_8.append(line)
        eye2_list_9.append(line)
        eye2_list_10.append(line)
        eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][6]['eyes2']) != 0:
            eye2_a_7 = json_data[0]['data'][i]['person'][6]['eyes2']
            line = []
            for j in range(4):
                eye2_b_7 = eye2_a_7.split(',')[j]
                eye2_c_7 = float(eye2_b_7)
                eye2_d_7 = eye2_c_7
                eye2_e_7 = round(eye2_d_7)
                line.append(eye2_e_7)
            eye2_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes2']) != 0:
            eye2_a_6 = json_data[0]['data'][i]['person'][5]['eyes2']
            line = []
            for j in range(4):
                eye2_b_6 = eye2_a_6.split(',')[j]
                eye2_c_6 = float(eye2_b_6)
                eye2_d_6 = eye2_c_6
                eye2_e_6 = round(eye2_d_6)
                line.append(eye2_e_6)
            eye2_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes2']) != 0:
            eye2_a_5 = json_data[0]['data'][i]['person'][4]['eyes2']
            line = []
            for j in range(4):
                eye2_b_5 = eye2_a_5.split(',')[j]
                eye2_c_5 = float(eye2_b_5)
                eye2_d_5 = eye2_c_5
                eye2_e_5 = round(eye2_d_5)
                line.append(eye2_e_5)
            eye2_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes2']) != 0:
            eye2_a_4 = json_data[0]['data'][i]['person'][3]['eyes2']
            line = []
            for j in range(4):
                eye2_b_4 = eye2_a_4.split(',')[j]
                eye2_c_4 = float(eye2_b_4)
                eye2_d_4 = eye2_c_4
                eye2_e_4 = round(eye2_d_4)
                line.append(eye2_e_4)
            eye2_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes2']) != 0:
            eye2_a_3 = json_data[0]['data'][i]['person'][2]['eyes2']
            line = []
            for j in range(4):
                eye2_b_3 = eye2_a_3.split(',')[j]
                eye2_c_3 = float(eye2_b_3)
                eye2_d_3 = eye2_c_3
                eye2_e_3 = round(eye2_d_3)
                line.append(eye2_e_3)
            eye2_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes2']) != 0:
            eye2_a_2 = json_data[0]['data'][i]['person'][1]['eyes2']
            line = []
            for j in range(4):
                eye2_b_2 = eye2_a_2.split(',')[j]
                eye2_c_2 = float(eye2_b_2)
                eye2_d_2 = eye2_c_2
                eye2_e_2 = round(eye2_d_2)
                line.append(eye2_e_2)
            eye2_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 6:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list_7.append(line)
        eye2_list_8.append(line)
        eye2_list_9.append(line)
        eye2_list_10.append(line)
        eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][5]['eyes2']) != 0:
            eye2_a_6 = json_data[0]['data'][i]['person'][5]['eyes2']
            line = []
            for j in range(4):
                eye2_b_6 = eye2_a_6.split(',')[j]
                eye2_c_6 = float(eye2_b_6)
                eye2_d_6 = eye2_c_6
                eye2_e_6 = round(eye2_d_6)
                line.append(eye2_e_6)
            eye2_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes2']) != 0:
            eye2_a_5 = json_data[0]['data'][i]['person'][4]['eyes2']
            line = []
            for j in range(4):
                eye2_b_5 = eye2_a_5.split(',')[j]
                eye2_c_5 = float(eye2_b_5)
                eye2_d_5 = eye2_c_5
                eye2_e_5 = round(eye2_d_5)
                line.append(eye2_e_5)
            eye2_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes2']) != 0:
            eye2_a_4 = json_data[0]['data'][i]['person'][3]['eyes2']
            line = []
            for j in range(4):
                eye2_b_4 = eye2_a_4.split(',')[j]
                eye2_c_4 = float(eye2_b_4)
                eye2_d_4 = eye2_c_4
                eye2_e_4 = round(eye2_d_4)
                line.append(eye2_e_4)
            eye2_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes2']) != 0:
            eye2_a_3 = json_data[0]['data'][i]['person'][2]['eyes2']
            line = []
            for j in range(4):
                eye2_b_3 = eye2_a_3.split(',')[j]
                eye2_c_3 = float(eye2_b_3)
                eye2_d_3 = eye2_c_3
                eye2_e_3 = round(eye2_d_3)
                line.append(eye2_e_3)
            eye2_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes2']) != 0:
            eye2_a_2 = json_data[0]['data'][i]['person'][1]['eyes2']
            line = []
            for j in range(4):
                eye2_b_2 = eye2_a_2.split(',')[j]
                eye2_c_2 = float(eye2_b_2)
                eye2_d_2 = eye2_c_2
                eye2_e_2 = round(eye2_d_2)
                line.append(eye2_e_2)
            eye2_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 5:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list_6.append(line)
        eye2_list_7.append(line)
        eye2_list_8.append(line)
        eye2_list_9.append(line)
        eye2_list_10.append(line)
        eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][4]['eyes2']) != 0:
            eye2_a_5 = json_data[0]['data'][i]['person'][4]['eyes2']
            line = []
            for j in range(4):
                eye2_b_5 = eye2_a_5.split(',')[j]
                eye2_c_5 = float(eye2_b_5)
                eye2_d_5 = eye2_c_5
                eye2_e_5 = round(eye2_d_5)
                line.append(eye2_e_5)
            eye2_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes2']) != 0:
            eye2_a_4 = json_data[0]['data'][i]['person'][3]['eyes2']
            line = []
            for j in range(4):
                eye2_b_4 = eye2_a_4.split(',')[j]
                eye2_c_4 = float(eye2_b_4)
                eye2_d_4 = eye2_c_4
                eye2_e_4 = round(eye2_d_4)
                line.append(eye2_e_4)
            eye2_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes2']) != 0:
            eye2_a_3 = json_data[0]['data'][i]['person'][2]['eyes2']
            line = []
            for j in range(4):
                eye2_b_3 = eye2_a_3.split(',')[j]
                eye2_c_3 = float(eye2_b_3)
                eye2_d_3 = eye2_c_3
                eye2_e_3 = round(eye2_d_3)
                line.append(eye2_e_3)
            eye2_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes2']) != 0:
            eye2_a_2 = json_data[0]['data'][i]['person'][1]['eyes2']
            line = []
            for j in range(4):
                eye2_b_2 = eye2_a_2.split(',')[j]
                eye2_c_2 = float(eye2_b_2)
                eye2_d_2 = eye2_c_2
                eye2_e_2 = round(eye2_d_2)
                line.append(eye2_e_2)
            eye2_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 4:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list_5.append(line)
        eye2_list_6.append(line)
        eye2_list_7.append(line)
        eye2_list_8.append(line)
        eye2_list_9.append(line)
        eye2_list_10.append(line)
        eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][3]['eyes2']) != 0:
            eye2_a_4 = json_data[0]['data'][i]['person'][3]['eyes2']
            line = []
            for j in range(4):
                eye2_b_4 = eye2_a_4.split(',')[j]
                eye2_c_4 = float(eye2_b_4)
                eye2_d_4 = eye2_c_4
                eye2_e_4 = round(eye2_d_4)
                line.append(eye2_e_4)
            eye2_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes2']) != 0:
            eye2_a_3 = json_data[0]['data'][i]['person'][2]['eyes2']
            line = []
            for j in range(4):
                eye2_b_3 = eye2_a_3.split(',')[j]
                eye2_c_3 = float(eye2_b_3)
                eye2_d_3 = eye2_c_3
                eye2_e_3 = round(eye2_d_3)
                line.append(eye2_e_3)
            eye2_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes2']) != 0:
            eye2_a_2 = json_data[0]['data'][i]['person'][1]['eyes2']
            line = []
            for j in range(4):
                eye2_b_2 = eye2_a_2.split(',')[j]
                eye2_c_2 = float(eye2_b_2)
                eye2_d_2 = eye2_c_2
                eye2_e_2 = round(eye2_d_2)
                line.append(eye2_e_2)
            eye2_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 3:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list_4.append(line)
        eye2_list_5.append(line)
        eye2_list_6.append(line)
        eye2_list_7.append(line)
        eye2_list_8.append(line)
        eye2_list_9.append(line)
        eye2_list_10.append(line)
        eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][2]['eyes2']) != 0:
            eye2_a_3 = json_data[0]['data'][i]['person'][2]['eyes2']
            line = []
            for j in range(4):
                eye2_b_3 = eye2_a_3.split(',')[j]
                eye2_c_3 = float(eye2_b_3)
                eye2_d_3 = eye2_c_3
                eye2_e_3 = round(eye2_d_3)
                line.append(eye2_e_3)
            eye2_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes2']) != 0:
            eye2_a_2 = json_data[0]['data'][i]['person'][1]['eyes2']
            line = []
            for j in range(4):
                eye2_b_2 = eye2_a_2.split(',')[j]
                eye2_c_2 = float(eye2_b_2)
                eye2_d_2 = eye2_c_2
                eye2_e_2 = round(eye2_d_2)
                line.append(eye2_e_2)
            eye2_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 2:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list_3.append(line)
        eye2_list_4.append(line)
        eye2_list_5.append(line)
        eye2_list_6.append(line)
        eye2_list_7.append(line)
        eye2_list_8.append(line)
        eye2_list_9.append(line)
        eye2_list_10.append(line)
        eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][1]['eyes2']) != 0:
            eye2_a_2 = json_data[0]['data'][i]['person'][1]['eyes2']
            line = []
            for j in range(4):
                eye2_b_2 = eye2_a_2.split(',')[j]
                eye2_c_2 = float(eye2_b_2)
                eye2_d_2 = eye2_c_2
                eye2_e_2 = round(eye2_d_2)
                line.append(eye2_e_2)
            eye2_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 1:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list_2.append(line)
        eye2_list_3.append(line)
        eye2_list_4.append(line)
        eye2_list_5.append(line)
        eye2_list_6.append(line)
        eye2_list_7.append(line)
        eye2_list_8.append(line)
        eye2_list_9.append(line)
        eye2_list_10.append(line)
        eye2_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][0]['eyes2']) != 0:
            eye2_a = json_data[0]['data'][i]['person'][0]['eyes2']
            line = []
            for j in range(4):
                eye2_b = eye2_a.split(',')[j]
                eye2_c = float(eye2_b)
                eye2_d = eye2_c
                eye2_e = round(eye2_d)
                line.append(eye2_e)
            eye2_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            eye2_list.append(line)

    else:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        eye2_list.append(line)
        eye2_list_2.append(line)
        eye2_list_3.append(line)
        eye2_list_4.append(line)
        eye2_list_5.append(line)
        eye2_list_6.append(line)
        eye2_list_7.append(line)
        eye2_list_8.append(line)
        eye2_list_9.append(line)
        eye2_list_10.append(line)
        eye2_list_11.append(line)

print(eye2_list)
print(eye2_list_2)

# bounding box face 좌표 리스트로 빼기

face_list = []
face_list_2 = []
face_list_3 = []
face_list_4 = []
face_list_5 = []
face_list_6 = []
face_list_7 = []
face_list_8 = []
face_list_9 = []
face_list_10 = []
face_list_11 = []

faces = range(0, len(json_data[0]['data']))

for i in faces:
    if len(json_data[0]['data'][i]['person']) == 11:
        if len(json_data[0]['data'][i]['person'][10]['face']) != 0:
            face_a_11 = json_data[0]['data'][i]['person'][10]['face']
            line = []
            for j in range(4):
                face_b_11 = face_a_11.split(',')[j]
                face_c_11 = float(face_b_11)
                face_d_11 = face_c_11
                face_e_11 = round(face_d_11)
                line.append(face_e_11)
            face_list_11.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][9]['face']) != 0:
            face_a_10 = json_data[0]['data'][i]['person'][9]['face']
            line = []
            for j in range(4):
                face_b_10 = face_a_10.split(',')[j]
                face_c_10 = float(face_b_10)
                face_d_10 = face_c_10
                face_e_10 = round(face_d_10)
                line.append(face_e_10)
            face_list_10.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_10.append(line)

        if len(json_data[0]['data'][i]['person'][8]['face']) != 0:
            face_a_9 = json_data[0]['data'][i]['person'][8]['face']
            line = []
            for j in range(4):
                face_b_9 = face_a_9.split(',')[j]
                face_c_9 = float(face_b_9)
                face_d_9 = face_c_9
                face_e_9 = round(face_d_9)
                line.append(face_e_9)
            face_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['face']) != 0:
            face_a_8 = json_data[0]['data'][i]['person'][7]['face']
            line = []
            for j in range(4):
                face_b_8 = face_a_8.split(',')[j]
                face_c_8 = float(face_b_8)
                face_d_8 = face_c_8
                face_e_8 = round(face_d_8)
                line.append(face_e_8)
            face_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['face']) != 0:
            face_a_7 = json_data[0]['data'][i]['person'][6]['face']
            line = []
            for j in range(4):
                face_b_7 = face_a_7.split(',')[j]
                face_c_7 = float(face_b_7)
                face_d_7 = face_c_7
                face_e_7 = round(face_d_7)
                line.append(face_e_7)
            face_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['face']) != 0:
            face_a_6 = json_data[0]['data'][i]['person'][5]['face']
            line = []
            for j in range(4):
                face_b_6 = face_a_6.split(',')[j]
                face_c_6 = float(face_b_6)
                face_d_6 = face_c_6
                face_e_6 = round(face_d_6)
                line.append(face_e_6)
            face_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['face']) != 0:
            face_a_5 = json_data[0]['data'][i]['person'][4]['face']
            line = []
            for j in range(4):
                face_b_5 = face_a_5.split(',')[j]
                face_c_5 = float(face_b_5)
                face_d_5 = face_c_5
                face_e_5 = round(face_d_5)
                line.append(face_e_5)
            face_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['face']) != 0:
            face_a_4 = json_data[0]['data'][i]['person'][3]['face']
            line = []
            for j in range(4):
                face_b_4 = face_a_4.split(',')[j]
                face_c_4 = float(face_b_4)
                face_d_4 = face_c_4
                face_e_4 = round(face_d_4)
                line.append(face_e_4)
            face_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['face']) != 0:
            face_a_3 = json_data[0]['data'][i]['person'][2]['face']
            line = []
            for j in range(4):
                face_b_3 = face_a_3.split(',')[j]
                face_c_3 = float(face_b_3)
                face_d_3 = face_c_3
                face_e_3 = round(face_d_3)
                line.append(face_e_3)
            face_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['face']) != 0:
            face_a_2 = json_data[0]['data'][i]['person'][1]['face']
            line = []
            for j in range(4):
                face_b_2 = face_a_2.split(',')[j]
                face_c_2 = float(face_b_2)
                face_d_2 = face_c_2
                face_e_2 = round(face_d_2)
                line.append(face_e_2)
            face_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 10:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][9]['face']) != 0:
            face_a_10 = json_data[0]['data'][i]['person'][9]['face']
            line = []
            for j in range(4):
                face_b_10 = face_a_10.split(',')[j]
                face_c_10 = float(face_b_10)
                face_d_10 = face_c_10
                face_e_10 = round(face_d_10)
                line.append(face_e_10)
            face_list_10.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_10.append(line)

        if len(json_data[0]['data'][i]['person'][8]['face']) != 0:
            face_a_9 = json_data[0]['data'][i]['person'][8]['face']
            line = []
            for j in range(4):
                face_b_9 = face_a_9.split(',')[j]
                face_c_9 = float(face_b_9)
                face_d_9 = face_c_9
                face_e_9 = round(face_d_9)
                line.append(face_e_9)
            face_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['face']) != 0:
            face_a_8 = json_data[0]['data'][i]['person'][7]['face']
            line = []
            for j in range(4):
                face_b_8 = face_a_8.split(',')[j]
                face_c_8 = float(face_b_8)
                face_d_8 = face_c_8
                face_e_8 = round(face_d_8)
                line.append(face_e_8)
            face_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['face']) != 0:
            face_a_7 = json_data[0]['data'][i]['person'][6]['face']
            line = []
            for j in range(4):
                face_b_7 = face_a_7.split(',')[j]
                face_c_7 = float(face_b_7)
                face_d_7 = face_c_7
                face_e_7 = round(face_d_7)
                line.append(face_e_7)
            face_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['face']) != 0:
            face_a_6 = json_data[0]['data'][i]['person'][5]['face']
            line = []
            for j in range(4):
                face_b_6 = face_a_6.split(',')[j]
                face_c_6 = float(face_b_6)
                face_d_6 = face_c_6
                face_e_6 = round(face_d_6)
                line.append(face_e_6)
            face_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['face']) != 0:
            face_a_5 = json_data[0]['data'][i]['person'][4]['face']
            line = []
            for j in range(4):
                face_b_5 = face_a_5.split(',')[j]
                face_c_5 = float(face_b_5)
                face_d_5 = face_c_5
                face_e_5 = round(face_d_5)
                line.append(face_e_5)
            face_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['face']) != 0:
            face_a_4 = json_data[0]['data'][i]['person'][3]['face']
            line = []
            for j in range(4):
                face_b_4 = face_a_4.split(',')[j]
                face_c_4 = float(face_b_4)
                face_d_4 = face_c_4
                face_e_4 = round(face_d_4)
                line.append(face_e_4)
            face_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['face']) != 0:
            face_a_3 = json_data[0]['data'][i]['person'][2]['face']
            line = []
            for j in range(4):
                face_b_3 = face_a_3.split(',')[j]
                face_c_3 = float(face_b_3)
                face_d_3 = face_c_3
                face_e_3 = round(face_d_3)
                line.append(face_e_3)
            face_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['face']) != 0:
            face_a_2 = json_data[0]['data'][i]['person'][1]['face']
            line = []
            for j in range(4):
                face_b_2 = face_a_2.split(',')[j]
                face_c_2 = float(face_b_2)
                face_d_2 = face_c_2
                face_e_2 = round(face_d_2)
                line.append(face_e_2)
            face_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 9:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list_10.append(line)
        face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][8]['face']) != 0:
            face_a_9 = json_data[0]['data'][i]['person'][8]['face']
            line = []
            for j in range(4):
                face_b_9 = face_a_9.split(',')[j]
                face_c_9 = float(face_b_9)
                face_d_9 = face_c_9
                face_e_9 = round(face_d_9)
                line.append(face_e_9)
            face_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['face']) != 0:
            face_a_8 = json_data[0]['data'][i]['person'][7]['face']
            line = []
            for j in range(4):
                face_b_8 = face_a_8.split(',')[j]
                face_c_8 = float(face_b_8)
                face_d_8 = face_c_8
                face_e_8 = round(face_d_8)
                line.append(face_e_8)
            face_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['face']) != 0:
            face_a_7 = json_data[0]['data'][i]['person'][6]['face']
            line = []
            for j in range(4):
                face_b_7 = face_a_7.split(',')[j]
                face_c_7 = float(face_b_7)
                face_d_7 = face_c_7
                face_e_7 = round(face_d_7)
                line.append(face_e_7)
            face_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['face']) != 0:
            face_a_6 = json_data[0]['data'][i]['person'][5]['face']
            line = []
            for j in range(4):
                face_b_6 = face_a_6.split(',')[j]
                face_c_6 = float(face_b_6)
                face_d_6 = face_c_6
                face_e_6 = round(face_d_6)
                line.append(face_e_6)
            face_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['face']) != 0:
            face_a_5 = json_data[0]['data'][i]['person'][4]['face']
            line = []
            for j in range(4):
                face_b_5 = face_a_5.split(',')[j]
                face_c_5 = float(face_b_5)
                face_d_5 = face_c_5
                face_e_5 = round(face_d_5)
                line.append(face_e_5)
            face_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['face']) != 0:
            face_a_4 = json_data[0]['data'][i]['person'][3]['face']
            line = []
            for j in range(4):
                face_b_4 = face_a_4.split(',')[j]
                face_c_4 = float(face_b_4)
                face_d_4 = face_c_4
                face_e_4 = round(face_d_4)
                line.append(face_e_4)
            face_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['face']) != 0:
            face_a_3 = json_data[0]['data'][i]['person'][2]['face']
            line = []
            for j in range(4):
                face_b_3 = face_a_3.split(',')[j]
                face_c_3 = float(face_b_3)
                face_d_3 = face_c_3
                face_e_3 = round(face_d_3)
                line.append(face_e_3)
            face_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['face']) != 0:
            face_a_2 = json_data[0]['data'][i]['person'][1]['face']
            line = []
            for j in range(4):
                face_b_2 = face_a_2.split(',')[j]
                face_c_2 = float(face_b_2)
                face_d_2 = face_c_2
                face_e_2 = round(face_d_2)
                line.append(face_e_2)
            face_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 8:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list_9.append(line)
        face_list_10.append(line)
        face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][7]['face']) != 0:
            face_a_8 = json_data[0]['data'][i]['person'][7]['face']
            line = []
            for j in range(4):
                face_b_8 = face_a_8.split(',')[j]
                face_c_8 = float(face_b_8)
                face_d_8 = face_c_8
                face_e_8 = round(face_d_8)
                line.append(face_e_8)
            face_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['face']) != 0:
            face_a_7 = json_data[0]['data'][i]['person'][6]['face']
            line = []
            for j in range(4):
                face_b_7 = face_a_7.split(',')[j]
                face_c_7 = float(face_b_7)
                face_d_7 = face_c_7
                face_e_7 = round(face_d_7)
                line.append(face_e_7)
            face_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['face']) != 0:
            face_a_6 = json_data[0]['data'][i]['person'][5]['face']
            line = []
            for j in range(4):
                face_b_6 = face_a_6.split(',')[j]
                face_c_6 = float(face_b_6)
                face_d_6 = face_c_6
                face_e_6 = round(face_d_6)
                line.append(face_e_6)
            face_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['face']) != 0:
            face_a_5 = json_data[0]['data'][i]['person'][4]['face']
            line = []
            for j in range(4):
                face_b_5 = face_a_5.split(',')[j]
                face_c_5 = float(face_b_5)
                face_d_5 = face_c_5
                face_e_5 = round(face_d_5)
                line.append(face_e_5)
            face_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['face']) != 0:
            face_a_4 = json_data[0]['data'][i]['person'][3]['face']
            line = []
            for j in range(4):
                face_b_4 = face_a_4.split(',')[j]
                face_c_4 = float(face_b_4)
                face_d_4 = face_c_4
                face_e_4 = round(face_d_4)
                line.append(face_e_4)
            face_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['face']) != 0:
            face_a_3 = json_data[0]['data'][i]['person'][2]['face']
            line = []
            for j in range(4):
                face_b_3 = face_a_3.split(',')[j]
                face_c_3 = float(face_b_3)
                face_d_3 = face_c_3
                face_e_3 = round(face_d_3)
                line.append(face_e_3)
            face_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['face']) != 0:
            face_a_2 = json_data[0]['data'][i]['person'][1]['face']
            line = []
            for j in range(4):
                face_b_2 = face_a_2.split(',')[j]
                face_c_2 = float(face_b_2)
                face_d_2 = face_c_2
                face_e_2 = round(face_d_2)
                line.append(face_e_2)
            face_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 7:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list_8.append(line)
        face_list_9.append(line)
        face_list_10.append(line)
        face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][6]['face']) != 0:
            face_a_7 = json_data[0]['data'][i]['person'][6]['face']
            line = []
            for j in range(4):
                face_b_7 = face_a_7.split(',')[j]
                face_c_7 = float(face_b_7)
                face_d_7 = face_c_7
                face_e_7 = round(face_d_7)
                line.append(face_e_7)
            face_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['face']) != 0:
            face_a_6 = json_data[0]['data'][i]['person'][5]['face']
            line = []
            for j in range(4):
                face_b_6 = face_a_6.split(',')[j]
                face_c_6 = float(face_b_6)
                face_d_6 = face_c_6
                face_e_6 = round(face_d_6)
                line.append(face_e_6)
            face_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['face']) != 0:
            face_a_5 = json_data[0]['data'][i]['person'][4]['face']
            line = []
            for j in range(4):
                face_b_5 = face_a_5.split(',')[j]
                face_c_5 = float(face_b_5)
                face_d_5 = face_c_5
                face_e_5 = round(face_d_5)
                line.append(face_e_5)
            face_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['face']) != 0:
            face_a_4 = json_data[0]['data'][i]['person'][3]['face']
            line = []
            for j in range(4):
                face_b_4 = face_a_4.split(',')[j]
                face_c_4 = float(face_b_4)
                face_d_4 = face_c_4
                face_e_4 = round(face_d_4)
                line.append(face_e_4)
            face_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['face']) != 0:
            face_a_3 = json_data[0]['data'][i]['person'][2]['face']
            line = []
            for j in range(4):
                face_b_3 = face_a_3.split(',')[j]
                face_c_3 = float(face_b_3)
                face_d_3 = face_c_3
                face_e_3 = round(face_d_3)
                line.append(face_e_3)
            face_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['face']) != 0:
            face_a_2 = json_data[0]['data'][i]['person'][1]['face']
            line = []
            for j in range(4):
                face_b_2 = face_a_2.split(',')[j]
                face_c_2 = float(face_b_2)
                face_d_2 = face_c_2
                face_e_2 = round(face_d_2)
                line.append(face_e_2)
            face_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 6:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list_7.append(line)
        face_list_8.append(line)
        face_list_9.append(line)
        face_list_10.append(line)
        face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][5]['face']) != 0:
            face_a_6 = json_data[0]['data'][i]['person'][5]['face']
            line = []
            for j in range(4):
                face_b_6 = face_a_6.split(',')[j]
                face_c_6 = float(face_b_6)
                face_d_6 = face_c_6
                face_e_6 = round(face_d_6)
                line.append(face_e_6)
            face_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['face']) != 0:
            face_a_5 = json_data[0]['data'][i]['person'][4]['face']
            line = []
            for j in range(4):
                face_b_5 = face_a_5.split(',')[j]
                face_c_5 = float(face_b_5)
                face_d_5 = face_c_5
                face_e_5 = round(face_d_5)
                line.append(face_e_5)
            face_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['face']) != 0:
            face_a_4 = json_data[0]['data'][i]['person'][3]['face']
            line = []
            for j in range(4):
                face_b_4 = face_a_4.split(',')[j]
                face_c_4 = float(face_b_4)
                face_d_4 = face_c_4
                face_e_4 = round(face_d_4)
                line.append(face_e_4)
            face_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['face']) != 0:
            face_a_3 = json_data[0]['data'][i]['person'][2]['face']
            line = []
            for j in range(4):
                face_b_3 = face_a_3.split(',')[j]
                face_c_3 = float(face_b_3)
                face_d_3 = face_c_3
                face_e_3 = round(face_d_3)
                line.append(face_e_3)
            face_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['face']) != 0:
            face_a_2 = json_data[0]['data'][i]['person'][1]['face']
            line = []
            for j in range(4):
                face_b_2 = face_a_2.split(',')[j]
                face_c_2 = float(face_b_2)
                face_d_2 = face_c_2
                face_e_2 = round(face_d_2)
                line.append(face_e_2)
            face_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 5:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list_6.append(line)
        face_list_7.append(line)
        face_list_8.append(line)
        face_list_9.append(line)
        face_list_10.append(line)
        face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][4]['face']) != 0:
            face_a_5 = json_data[0]['data'][i]['person'][4]['face']
            line = []
            for j in range(4):
                face_b_5 = face_a_5.split(',')[j]
                face_c_5 = float(face_b_5)
                face_d_5 = face_c_5
                face_e_5 = round(face_d_5)
                line.append(face_e_5)
            face_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['face']) != 0:
            face_a_4 = json_data[0]['data'][i]['person'][3]['face']
            line = []
            for j in range(4):
                face_b_4 = face_a_4.split(',')[j]
                face_c_4 = float(face_b_4)
                face_d_4 = face_c_4
                face_e_4 = round(face_d_4)
                line.append(face_e_4)
            face_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['face']) != 0:
            face_a_3 = json_data[0]['data'][i]['person'][2]['face']
            line = []
            for j in range(4):
                face_b_3 = face_a_3.split(',')[j]
                face_c_3 = float(face_b_3)
                face_d_3 = face_c_3
                face_e_3 = round(face_d_3)
                line.append(face_e_3)
            face_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['face']) != 0:
            face_a_2 = json_data[0]['data'][i]['person'][1]['face']
            line = []
            for j in range(4):
                face_b_2 = face_a_2.split(',')[j]
                face_c_2 = float(face_b_2)
                face_d_2 = face_c_2
                face_e_2 = round(face_d_2)
                line.append(face_e_2)
            face_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 4:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list_5.append(line)
        face_list_6.append(line)
        face_list_7.append(line)
        face_list_8.append(line)
        face_list_9.append(line)
        face_list_10.append(line)
        face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][3]['face']) != 0:
            face_a_4 = json_data[0]['data'][i]['person'][3]['face']
            line = []
            for j in range(4):
                face_b_4 = face_a_4.split(',')[j]
                face_c_4 = float(face_b_4)
                face_d_4 = face_c_4
                face_e_4 = round(face_d_4)
                line.append(face_e_4)
            face_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['face']) != 0:
            face_a_3 = json_data[0]['data'][i]['person'][2]['face']
            line = []
            for j in range(4):
                face_b_3 = face_a_3.split(',')[j]
                face_c_3 = float(face_b_3)
                face_d_3 = face_c_3
                face_e_3 = round(face_d_3)
                line.append(face_e_3)
            face_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['face']) != 0:
            face_a_2 = json_data[0]['data'][i]['person'][1]['face']
            line = []
            for j in range(4):
                face_b_2 = face_a_2.split(',')[j]
                face_c_2 = float(face_b_2)
                face_d_2 = face_c_2
                face_e_2 = round(face_d_2)
                line.append(face_e_2)
            face_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 3:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list_4.append(line)
        face_list_5.append(line)
        face_list_6.append(line)
        face_list_7.append(line)
        face_list_8.append(line)
        face_list_9.append(line)
        face_list_10.append(line)
        face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][2]['face']) != 0:
            face_a_3 = json_data[0]['data'][i]['person'][2]['face']
            line = []
            for j in range(4):
                face_b_3 = face_a_3.split(',')[j]
                face_c_3 = float(face_b_3)
                face_d_3 = face_c_3
                face_e_3 = round(face_d_3)
                line.append(face_e_3)
            face_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['face']) != 0:
            face_a_2 = json_data[0]['data'][i]['person'][1]['face']
            line = []
            for j in range(4):
                face_b_2 = face_a_2.split(',')[j]
                face_c_2 = float(face_b_2)
                face_d_2 = face_c_2
                face_e_2 = round(face_d_2)
                line.append(face_e_2)
            face_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 2:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list_3.append(line)
        face_list_4.append(line)
        face_list_5.append(line)
        face_list_6.append(line)
        face_list_7.append(line)
        face_list_8.append(line)
        face_list_9.append(line)
        face_list_10.append(line)
        face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][1]['face']) != 0:
            face_a_2 = json_data[0]['data'][i]['person'][1]['face']
            line = []
            for j in range(4):
                face_b_2 = face_a_2.split(',')[j]
                face_c_2 = float(face_b_2)
                face_d_2 = face_c_2
                face_e_2 = round(face_d_2)
                line.append(face_e_2)
            face_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 1:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list_2.append(line)
        face_list_3.append(line)
        face_list_4.append(line)
        face_list_5.append(line)
        face_list_6.append(line)
        face_list_7.append(line)
        face_list_8.append(line)
        face_list_9.append(line)
        face_list_10.append(line)
        face_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][0]['face']) != 0:
            face_a = json_data[0]['data'][i]['person'][0]['face']
            line = []
            for j in range(4):
                face_b = face_a.split(',')[j]
                face_c = float(face_b)
                face_d = face_c
                face_e = round(face_d)
                line.append(face_e)
            face_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            face_list.append(line)

    else:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        face_list.append(line)
        face_list_2.append(line)
        face_list_3.append(line)
        face_list_4.append(line)
        face_list_5.append(line)
        face_list_6.append(line)
        face_list_7.append(line)
        face_list_8.append(line)
        face_list_9.append(line)
        face_list_10.append(line)
        face_list_11.append(line)

print(face_list)
print(face_list_2)



# bounding box mouth 좌표 리스트로 빼기

mouth_list = []
mouth_list_2 = []
mouth_list_3 = []
mouth_list_4 = []
mouth_list_5 = []
mouth_list_6 = []
mouth_list_7 = []
mouth_list_8 = []
mouth_list_9 = []
mouth_list_10 = []
mouth_list_11 = []

mouths = range(0, len(json_data[0]['data']))

for i in mouths:
    if len(json_data[0]['data'][i]['person']) == 11:
        if len(json_data[0]['data'][i]['person'][10]['mouth']) != 0:
            mouth_a_11 = json_data[0]['data'][i]['person'][10]['mouth']
            line = []
            for j in range(4):
                mouth_b_11 = mouth_a_11.split(',')[j]
                mouth_c_11 = float(mouth_b_11)
                mouth_d_11 = mouth_c_11
                mouth_e_11 = round(mouth_d_11)
                line.append(mouth_e_11)
            mouth_list_11.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][9]['mouth']) != 0:
            mouth_a_10 = json_data[0]['data'][i]['person'][9]['mouth']
            line = []
            for j in range(4):
                mouth_b_10 = mouth_a_10.split(',')[j]
                mouth_c_10 = float(mouth_b_10)
                mouth_d_10 = mouth_c_10
                mouth_e_10 = round(mouth_d_10)
                line.append(mouth_e_10)
            mouth_list_10.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_10.append(line)

        if len(json_data[0]['data'][i]['person'][8]['mouth']) != 0:
            mouth_a_9 = json_data[0]['data'][i]['person'][8]['mouth']
            line = []
            for j in range(4):
                mouth_b_9 = mouth_a_9.split(',')[j]
                mouth_c_9 = float(mouth_b_9)
                mouth_d_9 = mouth_c_9
                mouth_e_9 = round(mouth_d_9)
                line.append(mouth_e_9)
            mouth_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['mouth']) != 0:
            mouth_a_8 = json_data[0]['data'][i]['person'][7]['mouth']
            line = []
            for j in range(4):
                mouth_b_8 = mouth_a_8.split(',')[j]
                mouth_c_8 = float(mouth_b_8)
                mouth_d_8 = mouth_c_8
                mouth_e_8 = round(mouth_d_8)
                line.append(mouth_e_8)
            mouth_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['mouth']) != 0:
            mouth_a_7 = json_data[0]['data'][i]['person'][6]['mouth']
            line = []
            for j in range(4):
                mouth_b_7 = mouth_a_7.split(',')[j]
                mouth_c_7 = float(mouth_b_7)
                mouth_d_7 = mouth_c_7
                mouth_e_7 = round(mouth_d_7)
                line.append(mouth_e_7)
            mouth_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['mouth']) != 0:
            mouth_a_6 = json_data[0]['data'][i]['person'][5]['mouth']
            line = []
            for j in range(4):
                mouth_b_6 = mouth_a_6.split(',')[j]
                mouth_c_6 = float(mouth_b_6)
                mouth_d_6 = mouth_c_6
                mouth_e_6 = round(mouth_d_6)
                line.append(mouth_e_6)
            mouth_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['mouth']) != 0:
            mouth_a_5 = json_data[0]['data'][i]['person'][4]['mouth']
            line = []
            for j in range(4):
                mouth_b_5 = mouth_a_5.split(',')[j]
                mouth_c_5 = float(mouth_b_5)
                mouth_d_5 = mouth_c_5
                mouth_e_5 = round(mouth_d_5)
                line.append(mouth_e_5)
            mouth_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['mouth']) != 0:
            mouth_a_4 = json_data[0]['data'][i]['person'][3]['mouth']
            line = []
            for j in range(4):
                mouth_b_4 = mouth_a_4.split(',')[j]
                mouth_c_4 = float(mouth_b_4)
                mouth_d_4 = mouth_c_4
                mouth_e_4 = round(mouth_d_4)
                line.append(mouth_e_4)
            mouth_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['mouth']) != 0:
            mouth_a_3 = json_data[0]['data'][i]['person'][2]['mouth']
            line = []
            for j in range(4):
                mouth_b_3 = mouth_a_3.split(',')[j]
                mouth_c_3 = float(mouth_b_3)
                mouth_d_3 = mouth_c_3
                mouth_e_3 = round(mouth_d_3)
                line.append(mouth_e_3)
            mouth_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['mouth']) != 0:
            mouth_a_2 = json_data[0]['data'][i]['person'][1]['mouth']
            line = []
            for j in range(4):
                mouth_b_2 = mouth_a_2.split(',')[j]
                mouth_c_2 = float(mouth_b_2)
                mouth_d_2 = mouth_c_2
                mouth_e_2 = round(mouth_d_2)
                line.append(mouth_e_2)
            mouth_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 10:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][9]['mouth']) != 0:
            mouth_a_10 = json_data[0]['data'][i]['person'][9]['mouth']
            line = []
            for j in range(4):
                mouth_b_10 = mouth_a_10.split(',')[j]
                mouth_c_10 = float(mouth_b_10)
                mouth_d_10 = mouth_c_10
                mouth_e_10 = round(mouth_d_10)
                line.append(mouth_e_10)
            mouth_list_10.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_10.append(line)

        if len(json_data[0]['data'][i]['person'][8]['mouth']) != 0:
            mouth_a_9 = json_data[0]['data'][i]['person'][8]['mouth']
            line = []
            for j in range(4):
                mouth_b_9 = mouth_a_9.split(',')[j]
                mouth_c_9 = float(mouth_b_9)
                mouth_d_9 = mouth_c_9
                mouth_e_9 = round(mouth_d_9)
                line.append(mouth_e_9)
            mouth_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['mouth']) != 0:
            mouth_a_8 = json_data[0]['data'][i]['person'][7]['mouth']
            line = []
            for j in range(4):
                mouth_b_8 = mouth_a_8.split(',')[j]
                mouth_c_8 = float(mouth_b_8)
                mouth_d_8 = mouth_c_8
                mouth_e_8 = round(mouth_d_8)
                line.append(mouth_e_8)
            mouth_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['mouth']) != 0:
            mouth_a_7 = json_data[0]['data'][i]['person'][6]['mouth']
            line = []
            for j in range(4):
                mouth_b_7 = mouth_a_7.split(',')[j]
                mouth_c_7 = float(mouth_b_7)
                mouth_d_7 = mouth_c_7
                mouth_e_7 = round(mouth_d_7)
                line.append(mouth_e_7)
            mouth_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['mouth']) != 0:
            mouth_a_6 = json_data[0]['data'][i]['person'][5]['mouth']
            line = []
            for j in range(4):
                mouth_b_6 = mouth_a_6.split(',')[j]
                mouth_c_6 = float(mouth_b_6)
                mouth_d_6 = mouth_c_6
                mouth_e_6 = round(mouth_d_6)
                line.append(mouth_e_6)
            mouth_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['mouth']) != 0:
            mouth_a_5 = json_data[0]['data'][i]['person'][4]['mouth']
            line = []
            for j in range(4):
                mouth_b_5 = mouth_a_5.split(',')[j]
                mouth_c_5 = float(mouth_b_5)
                mouth_d_5 = mouth_c_5
                mouth_e_5 = round(mouth_d_5)
                line.append(mouth_e_5)
            mouth_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['mouth']) != 0:
            mouth_a_4 = json_data[0]['data'][i]['person'][3]['mouth']
            line = []
            for j in range(4):
                mouth_b_4 = mouth_a_4.split(',')[j]
                mouth_c_4 = float(mouth_b_4)
                mouth_d_4 = mouth_c_4
                mouth_e_4 = round(mouth_d_4)
                line.append(mouth_e_4)
            mouth_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['mouth']) != 0:
            mouth_a_3 = json_data[0]['data'][i]['person'][2]['mouth']
            line = []
            for j in range(4):
                mouth_b_3 = mouth_a_3.split(',')[j]
                mouth_c_3 = float(mouth_b_3)
                mouth_d_3 = mouth_c_3
                mouth_e_3 = round(mouth_d_3)
                line.append(mouth_e_3)
            mouth_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['mouth']) != 0:
            mouth_a_2 = json_data[0]['data'][i]['person'][1]['mouth']
            line = []
            for j in range(4):
                mouth_b_2 = mouth_a_2.split(',')[j]
                mouth_c_2 = float(mouth_b_2)
                mouth_d_2 = mouth_c_2
                mouth_e_2 = round(mouth_d_2)
                line.append(mouth_e_2)
            mouth_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 9:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list_10.append(line)
        mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][8]['mouth']) != 0:
            mouth_a_9 = json_data[0]['data'][i]['person'][8]['mouth']
            line = []
            for j in range(4):
                mouth_b_9 = mouth_a_9.split(',')[j]
                mouth_c_9 = float(mouth_b_9)
                mouth_d_9 = mouth_c_9
                mouth_e_9 = round(mouth_d_9)
                line.append(mouth_e_9)
            mouth_list_9.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_9.append(line)

        if len(json_data[0]['data'][i]['person'][7]['mouth']) != 0:
            mouth_a_8 = json_data[0]['data'][i]['person'][7]['mouth']
            line = []
            for j in range(4):
                mouth_b_8 = mouth_a_8.split(',')[j]
                mouth_c_8 = float(mouth_b_8)
                mouth_d_8 = mouth_c_8
                mouth_e_8 = round(mouth_d_8)
                line.append(mouth_e_8)
            mouth_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['mouth']) != 0:
            mouth_a_7 = json_data[0]['data'][i]['person'][6]['mouth']
            line = []
            for j in range(4):
                mouth_b_7 = mouth_a_7.split(',')[j]
                mouth_c_7 = float(mouth_b_7)
                mouth_d_7 = mouth_c_7
                mouth_e_7 = round(mouth_d_7)
                line.append(mouth_e_7)
            mouth_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['mouth']) != 0:
            mouth_a_6 = json_data[0]['data'][i]['person'][5]['mouth']
            line = []
            for j in range(4):
                mouth_b_6 = mouth_a_6.split(',')[j]
                mouth_c_6 = float(mouth_b_6)
                mouth_d_6 = mouth_c_6
                mouth_e_6 = round(mouth_d_6)
                line.append(mouth_e_6)
            mouth_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['mouth']) != 0:
            mouth_a_5 = json_data[0]['data'][i]['person'][4]['mouth']
            line = []
            for j in range(4):
                mouth_b_5 = mouth_a_5.split(',')[j]
                mouth_c_5 = float(mouth_b_5)
                mouth_d_5 = mouth_c_5
                mouth_e_5 = round(mouth_d_5)
                line.append(mouth_e_5)
            mouth_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['mouth']) != 0:
            mouth_a_4 = json_data[0]['data'][i]['person'][3]['mouth']
            line = []
            for j in range(4):
                mouth_b_4 = mouth_a_4.split(',')[j]
                mouth_c_4 = float(mouth_b_4)
                mouth_d_4 = mouth_c_4
                mouth_e_4 = round(mouth_d_4)
                line.append(mouth_e_4)
            mouth_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['mouth']) != 0:
            mouth_a_3 = json_data[0]['data'][i]['person'][2]['mouth']
            line = []
            for j in range(4):
                mouth_b_3 = mouth_a_3.split(',')[j]
                mouth_c_3 = float(mouth_b_3)
                mouth_d_3 = mouth_c_3
                mouth_e_3 = round(mouth_d_3)
                line.append(mouth_e_3)
            mouth_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['mouth']) != 0:
            mouth_a_2 = json_data[0]['data'][i]['person'][1]['mouth']
            line = []
            for j in range(4):
                mouth_b_2 = mouth_a_2.split(',')[j]
                mouth_c_2 = float(mouth_b_2)
                mouth_d_2 = mouth_c_2
                mouth_e_2 = round(mouth_d_2)
                line.append(mouth_e_2)
            mouth_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)

    elif len(json_data[0]['data'][i]['person']) == 8:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list_9.append(line)
        mouth_list_10.append(line)
        mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][7]['mouth']) != 0:
            mouth_a_8 = json_data[0]['data'][i]['person'][7]['mouth']
            line = []
            for j in range(4):
                mouth_b_8 = mouth_a_8.split(',')[j]
                mouth_c_8 = float(mouth_b_8)
                mouth_d_8 = mouth_c_8
                mouth_e_8 = round(mouth_d_8)
                line.append(mouth_e_8)
            mouth_list_8.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_8.append(line)

        if len(json_data[0]['data'][i]['person'][6]['mouth']) != 0:
            mouth_a_7 = json_data[0]['data'][i]['person'][6]['mouth']
            line = []
            for j in range(4):
                mouth_b_7 = mouth_a_7.split(',')[j]
                mouth_c_7 = float(mouth_b_7)
                mouth_d_7 = mouth_c_7
                mouth_e_7 = round(mouth_d_7)
                line.append(mouth_e_7)
            mouth_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['mouth']) != 0:
            mouth_a_6 = json_data[0]['data'][i]['person'][5]['mouth']
            line = []
            for j in range(4):
                mouth_b_6 = mouth_a_6.split(',')[j]
                mouth_c_6 = float(mouth_b_6)
                mouth_d_6 = mouth_c_6
                mouth_e_6 = round(mouth_d_6)
                line.append(mouth_e_6)
            mouth_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['mouth']) != 0:
            mouth_a_5 = json_data[0]['data'][i]['person'][4]['mouth']
            line = []
            for j in range(4):
                mouth_b_5 = mouth_a_5.split(',')[j]
                mouth_c_5 = float(mouth_b_5)
                mouth_d_5 = mouth_c_5
                mouth_e_5 = round(mouth_d_5)
                line.append(mouth_e_5)
            mouth_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['mouth']) != 0:
            mouth_a_4 = json_data[0]['data'][i]['person'][3]['mouth']
            line = []
            for j in range(4):
                mouth_b_4 = mouth_a_4.split(',')[j]
                mouth_c_4 = float(mouth_b_4)
                mouth_d_4 = mouth_c_4
                mouth_e_4 = round(mouth_d_4)
                line.append(mouth_e_4)
            mouth_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['mouth']) != 0:
            mouth_a_3 = json_data[0]['data'][i]['person'][2]['mouth']
            line = []
            for j in range(4):
                mouth_b_3 = mouth_a_3.split(',')[j]
                mouth_c_3 = float(mouth_b_3)
                mouth_d_3 = mouth_c_3
                mouth_e_3 = round(mouth_d_3)
                line.append(mouth_e_3)
            mouth_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['mouth']) != 0:
            mouth_a_2 = json_data[0]['data'][i]['person'][1]['mouth']
            line = []
            for j in range(4):
                mouth_b_2 = mouth_a_2.split(',')[j]
                mouth_c_2 = float(mouth_b_2)
                mouth_d_2 = mouth_c_2
                mouth_e_2 = round(mouth_d_2)
                line.append(mouth_e_2)
            mouth_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 7:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list_8.append(line)
        mouth_list_9.append(line)
        mouth_list_10.append(line)
        mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][6]['mouth']) != 0:
            mouth_a_7 = json_data[0]['data'][i]['person'][6]['mouth']
            line = []
            for j in range(4):
                mouth_b_7 = mouth_a_7.split(',')[j]
                mouth_c_7 = float(mouth_b_7)
                mouth_d_7 = mouth_c_7
                mouth_e_7 = round(mouth_d_7)
                line.append(mouth_e_7)
            mouth_list_7.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_7.append(line)

        if len(json_data[0]['data'][i]['person'][5]['mouth']) != 0:
            mouth_a_6 = json_data[0]['data'][i]['person'][5]['mouth']
            line = []
            for j in range(4):
                mouth_b_6 = mouth_a_6.split(',')[j]
                mouth_c_6 = float(mouth_b_6)
                mouth_d_6 = mouth_c_6
                mouth_e_6 = round(mouth_d_6)
                line.append(mouth_e_6)
            mouth_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['mouth']) != 0:
            mouth_a_5 = json_data[0]['data'][i]['person'][4]['mouth']
            line = []
            for j in range(4):
                mouth_b_5 = mouth_a_5.split(',')[j]
                mouth_c_5 = float(mouth_b_5)
                mouth_d_5 = mouth_c_5
                mouth_e_5 = round(mouth_d_5)
                line.append(mouth_e_5)
            mouth_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['mouth']) != 0:
            mouth_a_4 = json_data[0]['data'][i]['person'][3]['mouth']
            line = []
            for j in range(4):
                mouth_b_4 = mouth_a_4.split(',')[j]
                mouth_c_4 = float(mouth_b_4)
                mouth_d_4 = mouth_c_4
                mouth_e_4 = round(mouth_d_4)
                line.append(mouth_e_4)
            mouth_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['mouth']) != 0:
            mouth_a_3 = json_data[0]['data'][i]['person'][2]['mouth']
            line = []
            for j in range(4):
                mouth_b_3 = mouth_a_3.split(',')[j]
                mouth_c_3 = float(mouth_b_3)
                mouth_d_3 = mouth_c_3
                mouth_e_3 = round(mouth_d_3)
                line.append(mouth_e_3)
            mouth_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['mouth']) != 0:
            mouth_a_2 = json_data[0]['data'][i]['person'][1]['mouth']
            line = []
            for j in range(4):
                mouth_b_2 = mouth_a_2.split(',')[j]
                mouth_c_2 = float(mouth_b_2)
                mouth_d_2 = mouth_c_2
                mouth_e_2 = round(mouth_d_2)
                line.append(mouth_e_2)
            mouth_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 6:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list_7.append(line)
        mouth_list_8.append(line)
        mouth_list_9.append(line)
        mouth_list_10.append(line)
        mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][5]['mouth']) != 0:
            mouth_a_6 = json_data[0]['data'][i]['person'][5]['mouth']
            line = []
            for j in range(4):
                mouth_b_6 = mouth_a_6.split(',')[j]
                mouth_c_6 = float(mouth_b_6)
                mouth_d_6 = mouth_c_6
                mouth_e_6 = round(mouth_d_6)
                line.append(mouth_e_6)
            mouth_list_6.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_6.append(line)

        if len(json_data[0]['data'][i]['person'][4]['mouth']) != 0:
            mouth_a_5 = json_data[0]['data'][i]['person'][4]['mouth']
            line = []
            for j in range(4):
                mouth_b_5 = mouth_a_5.split(',')[j]
                mouth_c_5 = float(mouth_b_5)
                mouth_d_5 = mouth_c_5
                mouth_e_5 = round(mouth_d_5)
                line.append(mouth_e_5)
            mouth_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['mouth']) != 0:
            mouth_a_4 = json_data[0]['data'][i]['person'][3]['mouth']
            line = []
            for j in range(4):
                mouth_b_4 = mouth_a_4.split(',')[j]
                mouth_c_4 = float(mouth_b_4)
                mouth_d_4 = mouth_c_4
                mouth_e_4 = round(mouth_d_4)
                line.append(mouth_e_4)
            mouth_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['mouth']) != 0:
            mouth_a_3 = json_data[0]['data'][i]['person'][2]['mouth']
            line = []
            for j in range(4):
                mouth_b_3 = mouth_a_3.split(',')[j]
                mouth_c_3 = float(mouth_b_3)
                mouth_d_3 = mouth_c_3
                mouth_e_3 = round(mouth_d_3)
                line.append(mouth_e_3)
            mouth_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['mouth']) != 0:
            mouth_a_2 = json_data[0]['data'][i]['person'][1]['mouth']
            line = []
            for j in range(4):
                mouth_b_2 = mouth_a_2.split(',')[j]
                mouth_c_2 = float(mouth_b_2)
                mouth_d_2 = mouth_c_2
                mouth_e_2 = round(mouth_d_2)
                line.append(mouth_e_2)
            mouth_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 5:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list_6.append(line)
        mouth_list_7.append(line)
        mouth_list_8.append(line)
        mouth_list_9.append(line)
        mouth_list_10.append(line)
        mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][4]['mouth']) != 0:
            mouth_a_5 = json_data[0]['data'][i]['person'][4]['mouth']
            line = []
            for j in range(4):
                mouth_b_5 = mouth_a_5.split(',')[j]
                mouth_c_5 = float(mouth_b_5)
                mouth_d_5 = mouth_c_5
                mouth_e_5 = round(mouth_d_5)
                line.append(mouth_e_5)
            mouth_list_5.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_5.append(line)

        if len(json_data[0]['data'][i]['person'][3]['mouth']) != 0:
            mouth_a_4 = json_data[0]['data'][i]['person'][3]['mouth']
            line = []
            for j in range(4):
                mouth_b_4 = mouth_a_4.split(',')[j]
                mouth_c_4 = float(mouth_b_4)
                mouth_d_4 = mouth_c_4
                mouth_e_4 = round(mouth_d_4)
                line.append(mouth_e_4)
            mouth_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['mouth']) != 0:
            mouth_a_3 = json_data[0]['data'][i]['person'][2]['mouth']
            line = []
            for j in range(4):
                mouth_b_3 = mouth_a_3.split(',')[j]
                mouth_c_3 = float(mouth_b_3)
                mouth_d_3 = mouth_c_3
                mouth_e_3 = round(mouth_d_3)
                line.append(mouth_e_3)
            mouth_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['mouth']) != 0:
            mouth_a_2 = json_data[0]['data'][i]['person'][1]['mouth']
            line = []
            for j in range(4):
                mouth_b_2 = mouth_a_2.split(',')[j]
                mouth_c_2 = float(mouth_b_2)
                mouth_d_2 = mouth_c_2
                mouth_e_2 = round(mouth_d_2)
                line.append(mouth_e_2)
            mouth_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 4:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list_5.append(line)
        mouth_list_6.append(line)
        mouth_list_7.append(line)
        mouth_list_8.append(line)
        mouth_list_9.append(line)
        mouth_list_10.append(line)
        mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][3]['mouth']) != 0:
            mouth_a_4 = json_data[0]['data'][i]['person'][3]['mouth']
            line = []
            for j in range(4):
                mouth_b_4 = mouth_a_4.split(',')[j]
                mouth_c_4 = float(mouth_b_4)
                mouth_d_4 = mouth_c_4
                mouth_e_4 = round(mouth_d_4)
                line.append(mouth_e_4)
            mouth_list_4.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_4.append(line)

        if len(json_data[0]['data'][i]['person'][2]['mouth']) != 0:
            mouth_a_3 = json_data[0]['data'][i]['person'][2]['mouth']
            line = []
            for j in range(4):
                mouth_b_3 = mouth_a_3.split(',')[j]
                mouth_c_3 = float(mouth_b_3)
                mouth_d_3 = mouth_c_3
                mouth_e_3 = round(mouth_d_3)
                line.append(mouth_e_3)
            mouth_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['mouth']) != 0:
            mouth_a_2 = json_data[0]['data'][i]['person'][1]['mouth']
            line = []
            for j in range(4):
                mouth_b_2 = mouth_a_2.split(',')[j]
                mouth_c_2 = float(mouth_b_2)
                mouth_d_2 = mouth_c_2
                mouth_e_2 = round(mouth_d_2)
                line.append(mouth_e_2)
            mouth_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 3:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list_4.append(line)
        mouth_list_5.append(line)
        mouth_list_6.append(line)
        mouth_list_7.append(line)
        mouth_list_8.append(line)
        mouth_list_9.append(line)
        mouth_list_10.append(line)
        mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][2]['mouth']) != 0:
            mouth_a_3 = json_data[0]['data'][i]['person'][2]['mouth']
            line = []
            for j in range(4):
                mouth_b_3 = mouth_a_3.split(',')[j]
                mouth_c_3 = float(mouth_b_3)
                mouth_d_3 = mouth_c_3
                mouth_e_3 = round(mouth_d_3)
                line.append(mouth_e_3)
            mouth_list_3.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_3.append(line)

        if len(json_data[0]['data'][i]['person'][1]['mouth']) != 0:
            mouth_a_2 = json_data[0]['data'][i]['person'][1]['mouth']
            line = []
            for j in range(4):
                mouth_b_2 = mouth_a_2.split(',')[j]
                mouth_c_2 = float(mouth_b_2)
                mouth_d_2 = mouth_c_2
                mouth_e_2 = round(mouth_d_2)
                line.append(mouth_e_2)
            mouth_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 2:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list_3.append(line)
        mouth_list_4.append(line)
        mouth_list_5.append(line)
        mouth_list_6.append(line)
        mouth_list_7.append(line)
        mouth_list_8.append(line)
        mouth_list_9.append(line)
        mouth_list_10.append(line)
        mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][1]['mouth']) != 0:
            mouth_a_2 = json_data[0]['data'][i]['person'][1]['mouth']
            line = []
            for j in range(4):
                mouth_b_2 = mouth_a_2.split(',')[j]
                mouth_c_2 = float(mouth_b_2)
                mouth_d_2 = mouth_c_2
                mouth_e_2 = round(mouth_d_2)
                line.append(mouth_e_2)
            mouth_list_2.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list_2.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)


    elif len(json_data[0]['data'][i]['person']) == 1:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list_2.append(line)
        mouth_list_3.append(line)
        mouth_list_4.append(line)
        mouth_list_5.append(line)
        mouth_list_6.append(line)
        mouth_list_7.append(line)
        mouth_list_8.append(line)
        mouth_list_9.append(line)
        mouth_list_10.append(line)
        mouth_list_11.append(line)

        if len(json_data[0]['data'][i]['person'][0]['mouth']) != 0:
            mouth_a = json_data[0]['data'][i]['person'][0]['mouth']
            line = []
            for j in range(4):
                mouth_b = mouth_a.split(',')[j]
                mouth_c = float(mouth_b)
                mouth_d = mouth_c
                mouth_e = round(mouth_d)
                line.append(mouth_e)
            mouth_list.append(line)

        else:
            line = []
            line.append(1)
            line.append(1)
            line.append(1)
            line.append(1)
            mouth_list.append(line)

    else:
        line = []
        line.append(1)
        line.append(1)
        line.append(1)
        line.append(1)
        mouth_list.append(line)
        mouth_list_2.append(line)
        mouth_list_3.append(line)
        mouth_list_4.append(line)
        mouth_list_5.append(line)
        mouth_list_6.append(line)
        mouth_list_7.append(line)
        mouth_list_8.append(line)
        mouth_list_9.append(line)
        mouth_list_10.append(line)
        mouth_list_11.append(line)

print(mouth_list)
print(mouth_list_2)


# frame 리스트로 빼기

frame_list = []
frame1 = range(0, len(json_data[0]['data']))
for i in frame1:
    frame_a = json_data[0]['data'][i]['frame']
    line = []
    frame_b = int(frame_a)
    line.append(frame_b)
    frame_list.append(line)

print(frame_list)
print(len(frame_list))

# 메인 실행
# import cv2


capture = cv2.VideoCapture("C:\data\GOODDAY_Mple+210706+2+CAM2.mp4")

while cv2.waitKey(33) < 0:
    for i in range(len(frame_list)):
        if capture.set(cv2.CAP_PROP_POS_FRAMES, frame_list[i][0]) == capture.set(cv2.CAP_PROP_FRAME_COUNT,
                                                                                 frame_list[i][0]):
            capture.set(cv2.CAP_PROP_POS_FRAMES, frame_list[i][0])
            break
        # capture.set(cv2.CAP_PROP_POS_FRAMES, frame_list[i][0])
        # print(frame_list[i][0])
        ret, frame = capture.read()

        if len(json_data[0]['data'][i]['person']) == 11:
            frame = cv2.rectangle(frame, (eye1_list_11[i][0], eye1_list_11[i][1]),
                                  (eye1_list_11[i][0] + eye1_list_11[i][2], eye1_list_11[i][1] + eye1_list_11[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_11[i][0], eye2_list_11[i][1]),
                                  (eye2_list_11[i][0] + eye2_list_11[i][2], eye2_list_11[i][1] + eye2_list_11[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_11[i][0], face_list_11[i][1]),
                                  (face_list_11[i][0] + face_list_11[i][2], face_list_11[i][1] + face_list_11[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_11[i][0], mouth_list_11[i][1]),
                                  (mouth_list_11[i][0] + mouth_list_11[i][2], mouth_list_11[i][1] + mouth_list_11[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_10[i][0], eye1_list_10[i][1]),
                                  (eye1_list_10[i][0] + eye1_list_10[i][2], eye1_list_10[i][1] + eye1_list_10[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_10[i][0], eye2_list_10[i][1]),
                                  (eye2_list_10[i][0] + eye2_list_10[i][2], eye2_list_10[i][1] + eye2_list_10[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_10[i][0], face_list_10[i][1]),
                                  (face_list_10[i][0] + face_list_10[i][2], face_list_10[i][1] + face_list_10[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_10[i][0], mouth_list_10[i][1]),
                                  (mouth_list_10[i][0] + mouth_list_10[i][2], mouth_list_10[i][1] + mouth_list_10[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_9[i][0], eye1_list_9[i][1]),
                                  (eye1_list_9[i][0] + eye1_list_9[i][2], eye1_list_9[i][1] + eye1_list_9[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_9[i][0], eye2_list_9[i][1]),
                                  (eye2_list_9[i][0] + eye2_list_9[i][2], eye2_list_9[i][1] + eye2_list_9[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_9[i][0], face_list_9[i][1]),
                                  (face_list_9[i][0] + face_list_9[i][2], face_list_9[i][1] + face_list_9[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_9[i][0], mouth_list_9[i][1]),
                                  (mouth_list_9[i][0] + mouth_list_9[i][2], mouth_list_9[i][1] + mouth_list_9[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_8[i][0], eye1_list_8[i][1]),
                                  (eye1_list_8[i][0] + eye1_list_8[i][2], eye1_list_8[i][1] + eye1_list_8[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_8[i][0], eye2_list_8[i][1]),
                                  (eye2_list_8[i][0] + eye2_list_8[i][2], eye2_list_8[i][1] + eye2_list_8[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_8[i][0], face_list_8[i][1]),
                                  (face_list_8[i][0] + face_list_8[i][2], face_list_8[i][1] + face_list_8[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_8[i][0], mouth_list_8[i][1]),
                                  (mouth_list_8[i][0] + mouth_list_8[i][2], mouth_list_8[i][1] + mouth_list_8[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_7[i][0], eye1_list_7[i][1]),
                                  (eye1_list_7[i][0] + eye1_list_7[i][2], eye1_list_7[i][1] + eye1_list_7[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_7[i][0], eye2_list_7[i][1]),
                                  (eye2_list_7[i][0] + eye2_list_7[i][2], eye2_list_7[i][1] + eye2_list_7[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_7[i][0], face_list_7[i][1]),
                                  (face_list_7[i][0] + face_list_7[i][2], face_list_7[i][1] + face_list_7[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_7[i][0], mouth_list_7[i][1]),
                                  (mouth_list_7[i][0] + mouth_list_7[i][2], mouth_list_7[i][1] + mouth_list_7[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_6[i][0], eye1_list_6[i][1]),
                                  (eye1_list_6[i][0] + eye1_list_6[i][2], eye1_list_6[i][1] + eye1_list_6[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_6[i][0], eye2_list_6[i][1]),
                                  (eye2_list_6[i][0] + eye2_list_6[i][2], eye2_list_6[i][1] + eye2_list_6[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_6[i][0], face_list_6[i][1]),
                                  (face_list_6[i][0] + face_list_6[i][2], face_list_6[i][1] + face_list_6[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_6[i][0], mouth_list_6[i][1]),
                                  (mouth_list_6[i][0] + mouth_list_6[i][2], mouth_list_6[i][1] + mouth_list_6[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_5[i][0], eye1_list_5[i][1]),
                                  (eye1_list_5[i][0] + eye1_list_5[i][2], eye1_list_5[i][1] + eye1_list_5[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_5[i][0], eye2_list_5[i][1]),
                                  (eye2_list_5[i][0] + eye2_list_5[i][2], eye2_list_5[i][1] + eye2_list_5[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_5[i][0], face_list_5[i][1]),
                                  (face_list_5[i][0] + face_list_5[i][2], face_list_5[i][1] + face_list_5[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_5[i][0], mouth_list_5[i][1]),
                                  (mouth_list_5[i][0] + mouth_list_5[i][2], mouth_list_5[i][1] + mouth_list_5[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_4[i][0], eye1_list_4[i][1]),
                                  (eye1_list_4[i][0] + eye1_list_4[i][2], eye1_list_4[i][1] + eye1_list_4[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_4[i][0], eye2_list_4[i][1]),
                                  (eye2_list_4[i][0] + eye2_list_4[i][2], eye2_list_4[i][1] + eye2_list_4[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_4[i][0], face_list_4[i][1]),
                                  (face_list_4[i][0] + face_list_4[i][2], face_list_4[i][1] + face_list_4[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_4[i][0], mouth_list_4[i][1]),
                                  (mouth_list_4[i][0] + mouth_list_4[i][2], mouth_list_4[i][1] + mouth_list_4[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_3[i][0], eye1_list_3[i][1]),
                                  (eye1_list_3[i][0] + eye1_list_3[i][2], eye1_list_3[i][1] + eye1_list_3[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_3[i][0], eye2_list_3[i][1]),
                                  (eye2_list_3[i][0] + eye2_list_3[i][2], eye2_list_3[i][1] + eye2_list_3[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_3[i][0], face_list_3[i][1]),
                                  (face_list_3[i][0] + face_list_3[i][2], face_list_3[i][1] + face_list_3[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_3[i][0], mouth_list_3[i][1]),
                                  (mouth_list_3[i][0] + mouth_list_3[i][2], mouth_list_3[i][1] + mouth_list_3[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_2[i][0], eye1_list_2[i][1]),
                                  (eye1_list_2[i][0] + eye1_list_2[i][2], eye1_list_2[i][1] + eye1_list_2[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_2[i][0], eye2_list_2[i][1]),
                                  (eye2_list_2[i][0] + eye2_list_2[i][2], eye2_list_2[i][1] + eye2_list_2[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_2[i][0], face_list_2[i][1]),
                                  (face_list_2[i][0] + face_list_2[i][2], face_list_2[i][1] + face_list_2[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_2[i][0], mouth_list_2[i][1]),
                                  (mouth_list_2[i][0] + mouth_list_2[i][2], mouth_list_2[i][1] + mouth_list_2[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)

        elif len(json_data[0]['data'][i]['person']) == 10:
            frame = cv2.rectangle(frame, (eye1_list_10[i][0], eye1_list_10[i][1]),
                                  (eye1_list_10[i][0] + eye1_list_10[i][2], eye1_list_10[i][1] + eye1_list_10[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_10[i][0], eye2_list_10[i][1]),
                                  (eye2_list_10[i][0] + eye2_list_10[i][2], eye2_list_10[i][1] + eye2_list_10[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_10[i][0], face_list_10[i][1]),
                                  (face_list_10[i][0] + face_list_10[i][2], face_list_10[i][1] + face_list_10[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_10[i][0], mouth_list_10[i][1]),
                                  (mouth_list_10[i][0] + mouth_list_10[i][2], mouth_list_10[i][1] + mouth_list_10[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_9[i][0], eye1_list_9[i][1]),
                                  (eye1_list_9[i][0] + eye1_list_9[i][2], eye1_list_9[i][1] + eye1_list_9[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_9[i][0], eye2_list_9[i][1]),
                                  (eye2_list_9[i][0] + eye2_list_9[i][2], eye2_list_9[i][1] + eye2_list_9[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_9[i][0], face_list_9[i][1]),
                                  (face_list_9[i][0] + face_list_9[i][2], face_list_9[i][1] + face_list_9[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_9[i][0], mouth_list_9[i][1]),
                                  (mouth_list_9[i][0] + mouth_list_9[i][2], mouth_list_9[i][1] + mouth_list_9[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_8[i][0], eye1_list_8[i][1]),
                                  (eye1_list_8[i][0] + eye1_list_8[i][2], eye1_list_8[i][1] + eye1_list_8[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_8[i][0], eye2_list_8[i][1]),
                                  (eye2_list_8[i][0] + eye2_list_8[i][2], eye2_list_8[i][1] + eye2_list_8[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_8[i][0], face_list_8[i][1]),
                                  (face_list_8[i][0] + face_list_8[i][2], face_list_8[i][1] + face_list_8[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_8[i][0], mouth_list_8[i][1]),
                                  (mouth_list_8[i][0] + mouth_list_8[i][2], mouth_list_8[i][1] + mouth_list_8[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_7[i][0], eye1_list_7[i][1]),
                                  (eye1_list_7[i][0] + eye1_list_7[i][2], eye1_list_7[i][1] + eye1_list_7[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_7[i][0], eye2_list_7[i][1]),
                                  (eye2_list_7[i][0] + eye2_list_7[i][2], eye2_list_7[i][1] + eye2_list_7[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_7[i][0], face_list_7[i][1]),
                                  (face_list_7[i][0] + face_list_7[i][2], face_list_7[i][1] + face_list_7[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_7[i][0], mouth_list_7[i][1]),
                                  (mouth_list_7[i][0] + mouth_list_7[i][2], mouth_list_7[i][1] + mouth_list_7[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_6[i][0], eye1_list_6[i][1]),
                                  (eye1_list_6[i][0] + eye1_list_6[i][2], eye1_list_6[i][1] + eye1_list_6[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_6[i][0], eye2_list_6[i][1]),
                                  (eye2_list_6[i][0] + eye2_list_6[i][2], eye2_list_6[i][1] + eye2_list_6[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_6[i][0], face_list_6[i][1]),
                                  (face_list_6[i][0] + face_list_6[i][2], face_list_6[i][1] + face_list_6[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_6[i][0], mouth_list_6[i][1]),
                                  (mouth_list_6[i][0] + mouth_list_6[i][2], mouth_list_6[i][1] + mouth_list_6[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_5[i][0], eye1_list_5[i][1]),
                                  (eye1_list_5[i][0] + eye1_list_5[i][2], eye1_list_5[i][1] + eye1_list_5[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_5[i][0], eye2_list_5[i][1]),
                                  (eye2_list_5[i][0] + eye2_list_5[i][2], eye2_list_5[i][1] + eye2_list_5[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_5[i][0], face_list_5[i][1]),
                                  (face_list_5[i][0] + face_list_5[i][2], face_list_5[i][1] + face_list_5[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_5[i][0], mouth_list_5[i][1]),
                                  (mouth_list_5[i][0] + mouth_list_5[i][2], mouth_list_5[i][1] + mouth_list_5[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_4[i][0], eye1_list_4[i][1]),
                                  (eye1_list_4[i][0] + eye1_list_4[i][2], eye1_list_4[i][1] + eye1_list_4[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_4[i][0], eye2_list_4[i][1]),
                                  (eye2_list_4[i][0] + eye2_list_4[i][2], eye2_list_4[i][1] + eye2_list_4[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_4[i][0], face_list_4[i][1]),
                                  (face_list_4[i][0] + face_list_4[i][2], face_list_4[i][1] + face_list_4[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_4[i][0], mouth_list_4[i][1]),
                                  (mouth_list_4[i][0] + mouth_list_4[i][2], mouth_list_4[i][1] + mouth_list_4[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_3[i][0], eye1_list_3[i][1]),
                                  (eye1_list_3[i][0] + eye1_list_3[i][2], eye1_list_3[i][1] + eye1_list_3[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_3[i][0], eye2_list_3[i][1]),
                                  (eye2_list_3[i][0] + eye2_list_3[i][2], eye2_list_3[i][1] + eye2_list_3[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_3[i][0], face_list_3[i][1]),
                                  (face_list_3[i][0] + face_list_3[i][2], face_list_3[i][1] + face_list_3[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_3[i][0], mouth_list_3[i][1]),
                                  (mouth_list_3[i][0] + mouth_list_3[i][2], mouth_list_3[i][1] + mouth_list_3[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_2[i][0], eye1_list_2[i][1]),
                                  (eye1_list_2[i][0] + eye1_list_2[i][2], eye1_list_2[i][1] + eye1_list_2[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_2[i][0], eye2_list_2[i][1]),
                                  (eye2_list_2[i][0] + eye2_list_2[i][2], eye2_list_2[i][1] + eye2_list_2[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_2[i][0], face_list_2[i][1]),
                                  (face_list_2[i][0] + face_list_2[i][2], face_list_2[i][1] + face_list_2[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_2[i][0], mouth_list_2[i][1]),
                                  (mouth_list_2[i][0] + mouth_list_2[i][2], mouth_list_2[i][1] + mouth_list_2[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)

        elif len(json_data[0]['data'][i]['person']) == 9:
            frame = cv2.rectangle(frame, (eye1_list_9[i][0], eye1_list_9[i][1]),
                                  (eye1_list_9[i][0] + eye1_list_9[i][2], eye1_list_9[i][1] + eye1_list_9[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_9[i][0], eye2_list_9[i][1]),
                                  (eye2_list_9[i][0] + eye2_list_9[i][2], eye2_list_9[i][1] + eye2_list_9[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_9[i][0], face_list_9[i][1]),
                                  (face_list_9[i][0] + face_list_9[i][2], face_list_9[i][1] + face_list_9[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_9[i][0], mouth_list_9[i][1]),
                                  (mouth_list_9[i][0] + mouth_list_9[i][2], mouth_list_9[i][1] + mouth_list_9[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_8[i][0], eye1_list_8[i][1]),
                                  (eye1_list_8[i][0] + eye1_list_8[i][2], eye1_list_8[i][1] + eye1_list_8[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_8[i][0], eye2_list_8[i][1]),
                                  (eye2_list_8[i][0] + eye2_list_8[i][2], eye2_list_8[i][1] + eye2_list_8[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_8[i][0], face_list_8[i][1]),
                                  (face_list_8[i][0] + face_list_8[i][2], face_list_8[i][1] + face_list_8[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_8[i][0], mouth_list_8[i][1]),
                                  (mouth_list_8[i][0] + mouth_list_8[i][2], mouth_list_8[i][1] + mouth_list_8[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_7[i][0], eye1_list_7[i][1]),
                                  (eye1_list_7[i][0] + eye1_list_7[i][2], eye1_list_7[i][1] + eye1_list_7[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_7[i][0], eye2_list_7[i][1]),
                                  (eye2_list_7[i][0] + eye2_list_7[i][2], eye2_list_7[i][1] + eye2_list_7[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_7[i][0], face_list_7[i][1]),
                                  (face_list_7[i][0] + face_list_7[i][2], face_list_7[i][1] + face_list_7[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_7[i][0], mouth_list_7[i][1]),
                                  (mouth_list_7[i][0] + mouth_list_7[i][2], mouth_list_7[i][1] + mouth_list_7[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_6[i][0], eye1_list_6[i][1]),
                                  (eye1_list_6[i][0] + eye1_list_6[i][2], eye1_list_6[i][1] + eye1_list_6[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_6[i][0], eye2_list_6[i][1]),
                                  (eye2_list_6[i][0] + eye2_list_6[i][2], eye2_list_6[i][1] + eye2_list_6[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_6[i][0], face_list_6[i][1]),
                                  (face_list_6[i][0] + face_list_6[i][2], face_list_6[i][1] + face_list_6[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_6[i][0], mouth_list_6[i][1]),
                                  (mouth_list_6[i][0] + mouth_list_6[i][2], mouth_list_6[i][1] + mouth_list_6[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_5[i][0], eye1_list_5[i][1]),
                                  (eye1_list_5[i][0] + eye1_list_5[i][2], eye1_list_5[i][1] + eye1_list_5[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_5[i][0], eye2_list_5[i][1]),
                                  (eye2_list_5[i][0] + eye2_list_5[i][2], eye2_list_5[i][1] + eye2_list_5[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_5[i][0], face_list_5[i][1]),
                                  (face_list_5[i][0] + face_list_5[i][2], face_list_5[i][1] + face_list_5[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_5[i][0], mouth_list_5[i][1]),
                                  (mouth_list_5[i][0] + mouth_list_5[i][2], mouth_list_5[i][1] + mouth_list_5[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_4[i][0], eye1_list_4[i][1]),
                                  (eye1_list_4[i][0] + eye1_list_4[i][2], eye1_list_4[i][1] + eye1_list_4[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_4[i][0], eye2_list_4[i][1]),
                                  (eye2_list_4[i][0] + eye2_list_4[i][2], eye2_list_4[i][1] + eye2_list_4[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_4[i][0], face_list_4[i][1]),
                                  (face_list_4[i][0] + face_list_4[i][2], face_list_4[i][1] + face_list_4[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_4[i][0], mouth_list_4[i][1]),
                                  (mouth_list_4[i][0] + mouth_list_4[i][2], mouth_list_4[i][1] + mouth_list_4[i][3]),
                                  (255, 0, 0), 2)



            frame = cv2.rectangle(frame, (eye1_list_3[i][0], eye1_list_3[i][1]),
                                  (eye1_list_3[i][0] + eye1_list_3[i][2], eye1_list_3[i][1] + eye1_list_3[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_3[i][0], eye2_list_3[i][1]),
                                  (eye2_list_3[i][0] + eye2_list_3[i][2], eye2_list_3[i][1] + eye2_list_3[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_3[i][0], face_list_3[i][1]),
                                  (face_list_3[i][0] + face_list_3[i][2], face_list_3[i][1] + face_list_3[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_3[i][0], mouth_list_3[i][1]),
                                  (mouth_list_3[i][0] + mouth_list_3[i][2], mouth_list_3[i][1] + mouth_list_3[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_2[i][0], eye1_list_2[i][1]),
                                  (eye1_list_2[i][0] + eye1_list_2[i][2], eye1_list_2[i][1] + eye1_list_2[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_2[i][0], eye2_list_2[i][1]),
                                  (eye2_list_2[i][0] + eye2_list_2[i][2], eye2_list_2[i][1] + eye2_list_2[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_2[i][0], face_list_2[i][1]),
                                  (face_list_2[i][0] + face_list_2[i][2], face_list_2[i][1] + face_list_2[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_2[i][0], mouth_list_2[i][1]),
                                  (mouth_list_2[i][0] + mouth_list_2[i][2], mouth_list_2[i][1] + mouth_list_2[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)

        elif len(json_data[0]['data'][i]['person']) == 8:
            frame = cv2.rectangle(frame, (eye1_list_8[i][0], eye1_list_8[i][1]),
                                  (eye1_list_8[i][0] + eye1_list_8[i][2], eye1_list_8[i][1] + eye1_list_8[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_8[i][0], eye2_list_8[i][1]),
                                  (eye2_list_8[i][0] + eye2_list_8[i][2], eye2_list_8[i][1] + eye2_list_8[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_8[i][0], face_list_8[i][1]),
                                  (face_list_8[i][0] + face_list_8[i][2], face_list_8[i][1] + face_list_8[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_8[i][0], mouth_list_8[i][1]),
                                  (mouth_list_8[i][0] + mouth_list_8[i][2], mouth_list_8[i][1] + mouth_list_8[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_7[i][0], eye1_list_7[i][1]),
                                  (eye1_list_7[i][0] + eye1_list_7[i][2], eye1_list_7[i][1] + eye1_list_7[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_7[i][0], eye2_list_7[i][1]),
                                  (eye2_list_7[i][0] + eye2_list_7[i][2], eye2_list_7[i][1] + eye2_list_7[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_7[i][0], face_list_7[i][1]),
                                  (face_list_7[i][0] + face_list_7[i][2], face_list_7[i][1] + face_list_7[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_7[i][0], mouth_list_7[i][1]),
                                  (mouth_list_7[i][0] + mouth_list_7[i][2], mouth_list_7[i][1] + mouth_list_7[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_6[i][0], eye1_list_6[i][1]),
                                  (eye1_list_6[i][0] + eye1_list_6[i][2], eye1_list_6[i][1] + eye1_list_6[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_6[i][0], eye2_list_6[i][1]),
                                  (eye2_list_6[i][0] + eye2_list_6[i][2], eye2_list_6[i][1] + eye2_list_6[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_6[i][0], face_list_6[i][1]),
                                  (face_list_6[i][0] + face_list_6[i][2], face_list_6[i][1] + face_list_6[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_6[i][0], mouth_list_6[i][1]),
                                  (mouth_list_6[i][0] + mouth_list_6[i][2], mouth_list_6[i][1] + mouth_list_6[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_5[i][0], eye1_list_5[i][1]),
                                  (eye1_list_5[i][0] + eye1_list_5[i][2], eye1_list_5[i][1] + eye1_list_5[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_5[i][0], eye2_list_5[i][1]),
                                  (eye2_list_5[i][0] + eye2_list_5[i][2], eye2_list_5[i][1] + eye2_list_5[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_5[i][0], face_list_5[i][1]),
                                  (face_list_5[i][0] + face_list_5[i][2], face_list_5[i][1] + face_list_5[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_5[i][0], mouth_list_5[i][1]),
                                  (mouth_list_5[i][0] + mouth_list_5[i][2], mouth_list_5[i][1] + mouth_list_5[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_4[i][0], eye1_list_4[i][1]),
                                  (eye1_list_4[i][0] + eye1_list_4[i][2], eye1_list_4[i][1] + eye1_list_4[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_4[i][0], eye2_list_4[i][1]),
                                  (eye2_list_4[i][0] + eye2_list_4[i][2], eye2_list_4[i][1] + eye2_list_4[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_4[i][0], face_list_4[i][1]),
                                  (face_list_4[i][0] + face_list_4[i][2], face_list_4[i][1] + face_list_4[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_4[i][0], mouth_list_4[i][1]),
                                  (mouth_list_4[i][0] + mouth_list_4[i][2], mouth_list_4[i][1] + mouth_list_4[i][3]),
                                  (255, 0, 0), 2)



            frame = cv2.rectangle(frame, (eye1_list_3[i][0], eye1_list_3[i][1]),
                                  (eye1_list_3[i][0] + eye1_list_3[i][2], eye1_list_3[i][1] + eye1_list_3[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_3[i][0], eye2_list_3[i][1]),
                                  (eye2_list_3[i][0] + eye2_list_3[i][2], eye2_list_3[i][1] + eye2_list_3[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_3[i][0], face_list_3[i][1]),
                                  (face_list_3[i][0] + face_list_3[i][2], face_list_3[i][1] + face_list_3[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_3[i][0], mouth_list_3[i][1]),
                                  (mouth_list_3[i][0] + mouth_list_3[i][2], mouth_list_3[i][1] + mouth_list_3[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_2[i][0], eye1_list_2[i][1]),
                                  (eye1_list_2[i][0] + eye1_list_2[i][2], eye1_list_2[i][1] + eye1_list_2[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_2[i][0], eye2_list_2[i][1]),
                                  (eye2_list_2[i][0] + eye2_list_2[i][2], eye2_list_2[i][1] + eye2_list_2[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_2[i][0], face_list_2[i][1]),
                                  (face_list_2[i][0] + face_list_2[i][2], face_list_2[i][1] + face_list_2[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_2[i][0], mouth_list_2[i][1]),
                                  (mouth_list_2[i][0] + mouth_list_2[i][2], mouth_list_2[i][1] + mouth_list_2[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)


        elif len(json_data[0]['data'][i]['person']) == 7:
            frame = cv2.rectangle(frame, (eye1_list_7[i][0], eye1_list_7[i][1]),
                                  (eye1_list_7[i][0] + eye1_list_7[i][2], eye1_list_7[i][1] + eye1_list_7[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_7[i][0], eye2_list_7[i][1]),
                                  (eye2_list_7[i][0] + eye2_list_7[i][2], eye2_list_7[i][1] + eye2_list_7[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_7[i][0], face_list_7[i][1]),
                                  (face_list_7[i][0] + face_list_7[i][2], face_list_7[i][1] + face_list_7[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_7[i][0], mouth_list_7[i][1]),
                                  (mouth_list_7[i][0] + mouth_list_7[i][2], mouth_list_7[i][1] + mouth_list_7[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_6[i][0], eye1_list_6[i][1]),
                                  (eye1_list_6[i][0] + eye1_list_6[i][2], eye1_list_6[i][1] + eye1_list_6[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_6[i][0], eye2_list_6[i][1]),
                                  (eye2_list_6[i][0] + eye2_list_6[i][2], eye2_list_6[i][1] + eye2_list_6[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_6[i][0], face_list_6[i][1]),
                                  (face_list_6[i][0] + face_list_6[i][2], face_list_6[i][1] + face_list_6[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_6[i][0], mouth_list_6[i][1]),
                                  (mouth_list_6[i][0] + mouth_list_6[i][2], mouth_list_6[i][1] + mouth_list_6[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_5[i][0], eye1_list_5[i][1]),
                                  (eye1_list_5[i][0] + eye1_list_5[i][2], eye1_list_5[i][1] + eye1_list_5[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_5[i][0], eye2_list_5[i][1]),
                                  (eye2_list_5[i][0] + eye2_list_5[i][2], eye2_list_5[i][1] + eye2_list_5[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_5[i][0], face_list_5[i][1]),
                                  (face_list_5[i][0] + face_list_5[i][2], face_list_5[i][1] + face_list_5[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_5[i][0], mouth_list_5[i][1]),
                                  (mouth_list_5[i][0] + mouth_list_5[i][2], mouth_list_5[i][1] + mouth_list_5[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_4[i][0], eye1_list_4[i][1]),
                                  (eye1_list_4[i][0] + eye1_list_4[i][2], eye1_list_4[i][1] + eye1_list_4[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_4[i][0], eye2_list_4[i][1]),
                                  (eye2_list_4[i][0] + eye2_list_4[i][2], eye2_list_4[i][1] + eye2_list_4[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_4[i][0], face_list_4[i][1]),
                                  (face_list_4[i][0] + face_list_4[i][2], face_list_4[i][1] + face_list_4[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_4[i][0], mouth_list_4[i][1]),
                                  (mouth_list_4[i][0] + mouth_list_4[i][2], mouth_list_4[i][1] + mouth_list_4[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_3[i][0], eye1_list_3[i][1]),
                                  (eye1_list_3[i][0] + eye1_list_3[i][2], eye1_list_3[i][1] + eye1_list_3[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_3[i][0], eye2_list_3[i][1]),
                                  (eye2_list_3[i][0] + eye2_list_3[i][2], eye2_list_3[i][1] + eye2_list_3[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_3[i][0], face_list_3[i][1]),
                                  (face_list_3[i][0] + face_list_3[i][2], face_list_3[i][1] + face_list_3[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_3[i][0], mouth_list_3[i][1]),
                                  (mouth_list_3[i][0] + mouth_list_3[i][2], mouth_list_3[i][1] + mouth_list_3[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_2[i][0], eye1_list_2[i][1]),
                                  (eye1_list_2[i][0] + eye1_list_2[i][2], eye1_list_2[i][1] + eye1_list_2[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_2[i][0], eye2_list_2[i][1]),
                                  (eye2_list_2[i][0] + eye2_list_2[i][2], eye2_list_2[i][1] + eye2_list_2[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_2[i][0], face_list_2[i][1]),
                                  (face_list_2[i][0] + face_list_2[i][2], face_list_2[i][1] + face_list_2[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_2[i][0], mouth_list_2[i][1]),
                                  (mouth_list_2[i][0] + mouth_list_2[i][2], mouth_list_2[i][1] + mouth_list_2[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)


        elif len(json_data[0]['data'][i]['person']) == 6:
            frame = cv2.rectangle(frame, (eye1_list_6[i][0], eye1_list_6[i][1]),
                                  (eye1_list_6[i][0] + eye1_list_6[i][2], eye1_list_6[i][1] + eye1_list_6[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_6[i][0], eye2_list_6[i][1]),
                                  (eye2_list_6[i][0] + eye2_list_6[i][2], eye2_list_6[i][1] + eye2_list_6[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_6[i][0], face_list_6[i][1]),
                                  (face_list_6[i][0] + face_list_6[i][2], face_list_6[i][1] + face_list_6[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_6[i][0], mouth_list_6[i][1]),
                                  (mouth_list_6[i][0] + mouth_list_6[i][2], mouth_list_6[i][1] + mouth_list_6[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_5[i][0], eye1_list_5[i][1]),
                                  (eye1_list_5[i][0] + eye1_list_5[i][2], eye1_list_5[i][1] + eye1_list_5[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_5[i][0], eye2_list_5[i][1]),
                                  (eye2_list_5[i][0] + eye2_list_5[i][2], eye2_list_5[i][1] + eye2_list_5[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_5[i][0], face_list_5[i][1]),
                                  (face_list_5[i][0] + face_list_5[i][2], face_list_5[i][1] + face_list_5[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_5[i][0], mouth_list_5[i][1]),
                                  (mouth_list_5[i][0] + mouth_list_5[i][2], mouth_list_5[i][1] + mouth_list_5[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_4[i][0], eye1_list_4[i][1]),
                                  (eye1_list_4[i][0] + eye1_list_4[i][2], eye1_list_4[i][1] + eye1_list_4[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_4[i][0], eye2_list_4[i][1]),
                                  (eye2_list_4[i][0] + eye2_list_4[i][2], eye2_list_4[i][1] + eye2_list_4[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_4[i][0], face_list_4[i][1]),
                                  (face_list_4[i][0] + face_list_4[i][2], face_list_4[i][1] + face_list_4[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_4[i][0], mouth_list_4[i][1]),
                                  (mouth_list_4[i][0] + mouth_list_4[i][2], mouth_list_4[i][1] + mouth_list_4[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_3[i][0], eye1_list_3[i][1]),
                                  (eye1_list_3[i][0] + eye1_list_3[i][2], eye1_list_3[i][1] + eye1_list_3[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_3[i][0], eye2_list_3[i][1]),
                                  (eye2_list_3[i][0] + eye2_list_3[i][2], eye2_list_3[i][1] + eye2_list_3[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_3[i][0], face_list_3[i][1]),
                                  (face_list_3[i][0] + face_list_3[i][2], face_list_3[i][1] + face_list_3[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_3[i][0], mouth_list_3[i][1]),
                                  (mouth_list_3[i][0] + mouth_list_3[i][2], mouth_list_3[i][1] + mouth_list_3[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_2[i][0], eye1_list_2[i][1]),
                                  (eye1_list_2[i][0] + eye1_list_2[i][2], eye1_list_2[i][1] + eye1_list_2[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_2[i][0], eye2_list_2[i][1]),
                                  (eye2_list_2[i][0] + eye2_list_2[i][2], eye2_list_2[i][1] + eye2_list_2[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_2[i][0], face_list_2[i][1]),
                                  (face_list_2[i][0] + face_list_2[i][2], face_list_2[i][1] + face_list_2[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_2[i][0], mouth_list_2[i][1]),
                                  (mouth_list_2[i][0] + mouth_list_2[i][2], mouth_list_2[i][1] + mouth_list_2[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)


        elif len(json_data[0]['data'][i]['person']) == 5:
            frame = cv2.rectangle(frame, (eye1_list_5[i][0], eye1_list_5[i][1]),
                                  (eye1_list_5[i][0] + eye1_list_5[i][2], eye1_list_5[i][1] + eye1_list_5[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_5[i][0], eye2_list_5[i][1]),
                                  (eye2_list_5[i][0] + eye2_list_5[i][2], eye2_list_5[i][1] + eye2_list_5[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_5[i][0], face_list_5[i][1]),
                                  (face_list_5[i][0] + face_list_5[i][2], face_list_5[i][1] + face_list_5[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_5[i][0], mouth_list_5[i][1]),
                                  (mouth_list_5[i][0] + mouth_list_5[i][2], mouth_list_5[i][1] + mouth_list_5[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_4[i][0], eye1_list_4[i][1]),
                                  (eye1_list_4[i][0] + eye1_list_4[i][2], eye1_list_4[i][1] + eye1_list_4[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_4[i][0], eye2_list_4[i][1]),
                                  (eye2_list_4[i][0] + eye2_list_4[i][2], eye2_list_4[i][1] + eye2_list_4[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_4[i][0], face_list_4[i][1]),
                                  (face_list_4[i][0] + face_list_4[i][2], face_list_4[i][1] + face_list_4[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_4[i][0], mouth_list_4[i][1]),
                                  (mouth_list_4[i][0] + mouth_list_4[i][2], mouth_list_4[i][1] + mouth_list_4[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_3[i][0], eye1_list_3[i][1]),
                                  (eye1_list_3[i][0] + eye1_list_3[i][2], eye1_list_3[i][1] + eye1_list_3[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_3[i][0], eye2_list_3[i][1]),
                                  (eye2_list_3[i][0] + eye2_list_3[i][2], eye2_list_3[i][1] + eye2_list_3[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_3[i][0], face_list_3[i][1]),
                                  (face_list_3[i][0] + face_list_3[i][2], face_list_3[i][1] + face_list_3[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_3[i][0], mouth_list_3[i][1]),
                                  (mouth_list_3[i][0] + mouth_list_3[i][2], mouth_list_3[i][1] + mouth_list_3[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_2[i][0], eye1_list_2[i][1]),
                                  (eye1_list_2[i][0] + eye1_list_2[i][2], eye1_list_2[i][1] + eye1_list_2[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_2[i][0], eye2_list_2[i][1]),
                                  (eye2_list_2[i][0] + eye2_list_2[i][2], eye2_list_2[i][1] + eye2_list_2[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_2[i][0], face_list_2[i][1]),
                                  (face_list_2[i][0] + face_list_2[i][2], face_list_2[i][1] + face_list_2[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_2[i][0], mouth_list_2[i][1]),
                                  (mouth_list_2[i][0] + mouth_list_2[i][2], mouth_list_2[i][1] + mouth_list_2[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)


        elif len(json_data[0]['data'][i]['person']) == 4:
            frame = cv2.rectangle(frame, (eye1_list_4[i][0], eye1_list_4[i][1]),
                                  (eye1_list_4[i][0] + eye1_list_4[i][2], eye1_list_4[i][1] + eye1_list_4[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_4[i][0], eye2_list_4[i][1]),
                                  (eye2_list_4[i][0] + eye2_list_4[i][2], eye2_list_4[i][1] + eye2_list_4[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_4[i][0], face_list_4[i][1]),
                                  (face_list_4[i][0] + face_list_4[i][2], face_list_4[i][1] + face_list_4[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_4[i][0], mouth_list_4[i][1]),
                                  (mouth_list_4[i][0] + mouth_list_4[i][2], mouth_list_4[i][1] + mouth_list_4[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_3[i][0], eye1_list_3[i][1]),
                                  (eye1_list_3[i][0] + eye1_list_3[i][2], eye1_list_3[i][1] + eye1_list_3[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_3[i][0], eye2_list_3[i][1]),
                                  (eye2_list_3[i][0] + eye2_list_3[i][2], eye2_list_3[i][1] + eye2_list_3[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_3[i][0], face_list_3[i][1]),
                                  (face_list_3[i][0] + face_list_3[i][2], face_list_3[i][1] + face_list_3[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_3[i][0], mouth_list_3[i][1]),
                                  (mouth_list_3[i][0] + mouth_list_3[i][2], mouth_list_3[i][1] + mouth_list_3[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list_2[i][0], eye1_list_2[i][1]),
                                  (eye1_list_2[i][0] + eye1_list_2[i][2], eye1_list_2[i][1] + eye1_list_2[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_2[i][0], eye2_list_2[i][1]),
                                  (eye2_list_2[i][0] + eye2_list_2[i][2], eye2_list_2[i][1] + eye2_list_2[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_2[i][0], face_list_2[i][1]),
                                  (face_list_2[i][0] + face_list_2[i][2], face_list_2[i][1] + face_list_2[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_2[i][0], mouth_list_2[i][1]),
                                  (mouth_list_2[i][0] + mouth_list_2[i][2], mouth_list_2[i][1] + mouth_list_2[i][3]),
                                  (255, 0, 0), 2)

            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)



        elif len(json_data[0]['data'][i]['person']) == 3:
            frame = cv2.rectangle(frame, (eye1_list_3[i][0], eye1_list_3[i][1]),
                                  (eye1_list_3[i][0] + eye1_list_3[i][2], eye1_list_3[i][1] + eye1_list_3[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_3[i][0], eye2_list_3[i][1]),
                                  (eye2_list_3[i][0] + eye2_list_3[i][2], eye2_list_3[i][1] + eye2_list_3[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_3[i][0], face_list_3[i][1]),
                                  (face_list_3[i][0] + face_list_3[i][2], face_list_3[i][1] + face_list_3[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_3[i][0], mouth_list_3[i][1]),
                                  (mouth_list_3[i][0] + mouth_list_3[i][2], mouth_list_3[i][1] + mouth_list_3[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list_2[i][0], eye1_list_2[i][1]),
                                  (eye1_list_2[i][0] + eye1_list_2[i][2], eye1_list_2[i][1] + eye1_list_2[i][3]),
                                  (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_2[i][0], eye2_list_2[i][1]),
                                  (eye2_list_2[i][0] + eye2_list_2[i][2], eye2_list_2[i][1] + eye2_list_2[i][3]),
                                  (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_2[i][0], face_list_2[i][1]),
                                  (face_list_2[i][0] + face_list_2[i][2], face_list_2[i][1] + face_list_2[i][3]),
                                  (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_2[i][0], mouth_list_2[i][1]),
                                  (mouth_list_2[i][0] + mouth_list_2[i][2], mouth_list_2[i][1] + mouth_list_2[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)


        elif len(json_data[0]['data'][i]['person']) == 2:
            frame = cv2.rectangle(frame, (eye1_list_2[i][0], eye1_list_2[i][1]),
                                  (eye1_list_2[i][0] + eye1_list_2[i][2], eye1_list_2[i][1] + eye1_list_2[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list_2[i][0], eye2_list_2[i][1]),
                                  (eye2_list_2[i][0] + eye2_list_2[i][2], eye2_list_2[i][1] + eye2_list_2[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list_2[i][0], face_list_2[i][1]),
                                  (face_list_2[i][0] + face_list_2[i][2], face_list_2[i][1] + face_list_2[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list_2[i][0], mouth_list_2[i][1]),
                                  (mouth_list_2[i][0] + mouth_list_2[i][2], mouth_list_2[i][1] + mouth_list_2[i][3]),
                                  (255, 0, 0), 2)


            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)


        else:
            frame = cv2.rectangle(frame, (eye1_list[i][0], eye1_list[i][1]),
                                  (eye1_list[i][0] + eye1_list[i][2], eye1_list[i][1] + eye1_list[i][3]), (0, 0, 255),
                                  2)

            frame = cv2.rectangle(frame, (eye2_list[i][0], eye2_list[i][1]),
                                  (eye2_list[i][0] + eye2_list[i][2], eye2_list[i][1] + eye2_list[i][3]), (0, 0, 255),
                                  2)  # eye2

            frame = cv2.rectangle(frame, (face_list[i][0], face_list[i][1]),
                                  (face_list[i][0] + face_list[i][2], face_list[i][1] + face_list[i][3]), (0, 255, 0),
                                  2)  # face

            frame = cv2.rectangle(frame, (mouth_list[i][0], mouth_list[i][1]),
                                  (mouth_list[i][0] + mouth_list[i][2], mouth_list[i][1] + mouth_list[i][3]),
                                  (255, 0, 0), 2)

        frame_num = "{:d}".format(frame_list[i][0])
        frame_name = "C:/check/" + frame_num + ".jpg"
        cv2.imwrite(frame_name, frame)
        # cv2.imshow(frame_name, frame)

    break

capture.release()
cv2.destroyAllWindows()
