import os

jamo_start = 44032
jamo_end = 55203
cho_start = 4352
jung_start = 4449
jong_start = 4520

cho_list = [
    "ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"
]
jung_list = [
    "ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"
]
jong_list = [
    "","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ","ㅆ",
    "ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"
]

def combine(cho,jung,jong):
    return chr((cho*21+jung)*28+jong+44032)

def reorganize_hangul(line):
    result = ""
    finish = False
    jong_index = 0 #종성은 없는 경우가 있기 때문에 먼저 정의해준다.
    for index,letter in enumerate(line):
        letter  = ord(letter)
        if letter>=cho_start and letter<jung_start:       #초성일경우
         #첫번째가 아니고 초성이 돌아왔을 경우는 한글이 완성 되었기 때문에 결과값을 가져온다.
            if index != 0 and finish:                            
                result += combine(cho_index,jung_index,jong_index)
                cho_index = 0
                jung_index = 0
                jong_index = 0
            cho_index = letter-cho_start
            finish = True
        elif letter>=jung_start and letter<jong_start:    #중성일경우
            jung_index = letter-jung_start
        elif letter>=jong_start and letter<4549:          #종성일경우
            jong_index = letter-jong_start+1
        else:
            # 한글이 완성된후 한글이 아닌 것이 왔을 경우 결과값을 가져온다.
            if finish:                          
                result += combine(cho_index,jung_index,jong_index)
                cho_index = 0
                jung_index = 0
                jong_index = 0
                finish = False
            letter = chr(letter)
            result += letter
    return result


for dir_name, subdir_list, file_list in os.walk("."):
    dir_dot_flag = False
    for d in os.path.split(dir_name):
        if len(d) > 1 and d.startswith("."):
            dir_dot_flag = True
    if not dir_dot_flag:
        print("directory:", dir_name)
        for fname in file_list:
            fname2 = reorganize_hangul(fname)
            if fname2 != fname:
                print("{} => {}".format(os.path.join(dir_name, fname), os.path.join(dir_name, fname2)))
                os.rename(os.path.join(dir_name, fname), os.path.join(dir_name, fname2))
