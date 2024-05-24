# if문 연습
'''
today = input('요일을 입력하세요:')

if today == '일요일':
    print('게임 세판 하시고')
print('공부 시작')
'''

# 2. if~else문
'''
today = input('요일을 입력하세요:')

if today =='일요일':
    print('게임 세판 합시다')
else:
    print('게임한판 합시다')
print('공부 시작')
'''
# 3. if~elif~else문
'''
today = input('요일을 입력합시다')

if today == '일요일':
    print('게임 열판')
elif today == '토요일':
    print('게임 세판')
else:
    print('물 한잔 먹고 공부시작')
    '''
'''
total = int(input('입장 인원을 입력하세요:'))

if total <= 4:
    print('추가비용X')
elif total == 5:
    print(f'추가비용은 {total - 4}만원입니다')
elif total == 6:
    print(f'추가비용은 {total - 4}만원입니다')
elif total == 7:
    print(f'추가비용은 {total - 4}만원입니다')
elif total == 8:
    print(f'추가비용은 {total - 4}만원입니다')        
else:
    print('입장인원은 최대 8명 입니다')
'''



total = int(input('입장 인원을 입력하세요:'))
if total <=4:
    print('추가비용이 없습니다')
elif total > 4 and total <=8:
    print(f'추가 비용은 {total - 4}만원 입니다')
else:
    print('최대 입장인원은 8명 입니다')



















































