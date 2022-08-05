import string
import random
from typing import ParamSpecArgs
from unittest import result

def evaluate_password(password,show_info=True):
    result = False
    password_state=0b00000
    for char in password:
        if char.isupper():
            password_state |= 0b10000
        elif char.islower():
            password_state |= 0b01000
        elif char in string.digits:
            password_state |= 0b00100
        else:
            password_state |= 0b00010

    if len(password) >= 8:
        password_state |= 0b00001

   
    #TODO：输出
    if password_state==0b11111:
        if show_info:
            print("密码符合要求！")
        result = True
    else:
        if show_info:
            prompt='密码不符合要求,'
            if password_state & 0b00001 == 0b00000:
                prompt = prompt+'长度不足8位，'
            if password_state & 0b10000 == 0b00000:
                prompt = prompt+'无大写字母，'
            if password_state & 0b01000 == 0b00000:
                prompt = prompt+'无小写字母，'
            if password_state & 0b00100 == 0b00000:
                prompt = prompt+'无阿拉伯数字，'
            if password_state & 0b00010 == 0b00000:
                prompt = prompt+'无特殊符号，'
            prompt = prompt[:-1]
            print(prompt)
    return result

def gen_password():
    all_char_set = string.printable[:-6]
    all_char_set *= 9
    result = ''.join(random.sample(all_char_set,k=9))
    return result

def create_password(pass_length,confuse=True):
    result = ''
    #TODO:生成指定长度前4位
    result += random.choice(string.ascii_uppercase)
    result += random.choice(string.ascii_lowercase)
    result += random.choice(string.digits)
    result += random.choice(string.punctuation)
    if confuse:
        result += 'Il'
        result += ''.join(random.sample(string.printable[:-6]*pass_length,pass_length-6))
    else:
        result += ''.join(random.sample(string.printable[:-6]*pass_length,pass_length-4))
    result = ''.join(random.sample(result,len(result)))
    return result

def main_userinput():
    while 1:
        user_password = input('请输入密码：')
        if evaluate_password(user_password):
            break
def main_gen_password():
    while 1:
        user_password = gen_password()
        if evaluate_password(user_password,show_info = False):
            print(f'您的密码是:{user_password}')
            break
def main():
    for i in range(1):
            print(f'您的密码是:{create_password(9)}')
main()
