while 1:
    #TODO：让用户输入密码
    user_password = input('请输入新密码')
    #TODO：判断密码是否合格
    UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWER = 'abcdefghijklmnopqrstuvwxyz'
    DIGIT = '0123456789'
  
    have_upper = False
    have_lower = False
    have_digit = False
    have_punctuation =False
    for char in user_password:
        if char in UPPER:
            have_upper = True
        elif char in LOWER:
            have_lower = True
        elif char in DIGIT:
            have_digit = True
        else:
            have_punctuation = True
    have_enough_len = len(user_password)>=8
    is_secure = have_enough_len and have_upper and \
        have_lower and \
            have_digit and \
                have_punctuation
    #TODO：输出
    if is_secure:
        print("密码符合要求！")
        break
    else:
        prompt='密码不符合要求,'
        if not have_enough_len:
            prompt = prompt+'长度不足8，'
        if not have_upper:
            prompt = prompt+'无大写字母，'
        if not have_lower:
            prompt = prompt+'无小写字母，'
        if not have_digit:
            prompt = prompt+'无阿拉伯数字，'
        if not have_punctuation:
            prompt = prompt+'无特殊符号，'
        prompt=prompt[:-1]
        print(prompt)