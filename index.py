def is_prime(num):
    if num<2:return False
    i=2
    while True:
        if i>(num//2)+1:break
        if i!=2 and i%2==0:pass
        if num!=2 and num%i==0:return False
        if num%i==0:break
        i+=1
    return True

def prime_range(range_):
    if range_<2:raise ArithmeticError
    p_nums=[]
    for i in range(2,range_+1):p_nums.append(i)
    for num in range(2,range_+1):
        if not is_prime(num):p_nums.remove(num)
    return p_nums

def prime_factors(num):
    def compact(l):
        last_itm,end=[],[]
        for i in range(len(l)):
            if l[i] in last_itm:last_itm.append(l[i])
            else:
                try:
                    if len(last_itm)>1:end.append('%s^%s'%(last_itm[0],len(last_itm)))
                    else:end.append('%s'%(last_itm[0]))
                except:
                    pass
                last_itm=[l[i]]
        if len(last_itm)>1:end.append('%s^%s'%(last_itm[0],len(last_itm)))
        else:end.append('%s'%(last_itm[0]))
        return end
            
    div,divs,calc=prime_range((num//2)+1),[],[]
    while True:
        if is_prime(num):
            divs.append(num)
            calc.append('%s/%s=1'%(num,num))
            return [divs,compact(divs),calc]
        x=0
        while True:
            if num%div[x]==0:
                calc.append('%s/%s=%s'%(num,div[x],num//div[x]))
                divs.append(div[x])
                num=num//div[x]
                break
            x+=1

def calc_(x_,divs):
    out=[]
    sp=len(str(x_))+1
    x=x_*1
    for div in divs:
        out.append('%s%s|%s'%(' '*(sp-len(str(x))),x,div))
        x=x//div
    out.append('%s1|\n%s|\n%s/|\ \n%s/-+-\%s'%(' '*(sp-1),' '*sp,' '*(sp-1),'-'*(sp-2),'-'*(sp-2)))
    return out

def f_(inp):
    nums,inp_num,f_nums=prime_factors(int(inp)),int(inp),[]
    for line in calc_(inp_num,nums[0]):print(line)
    for itm in nums[0]:f_nums.append(str(itm))
    print(inp_num,'=','*'.join(nums[1]),'=','*'.join(f_nums))

def BCD(n,m):
    print('===%s==='%(n))
    f_(n)
    print('\n')
    print('===%s==='%(m))
    f_(m)
    r,q=(n%m),(n//m)
    if r==0:return m
    while True:
        n,m=m,r
        r,q=(n%m),(n//m)
        if r==0:return m
        
if __name__=='__main__':
    while True:
        inp=input('>>>')
        if 'isP' in inp:
            if is_prime(int(inp[4:])):print('%s is prime'%(inp[4:]))
            else:print('%s is not prime'%(inp[4:]))
        elif 'range' in inp:
            for num in prime_range(int(inp[6:])):print(num)
        elif 'factors' in inp:f_(inp[8:])
        elif 'BCD' in inp:
            try:print('BCD of %s and %s is %s'%(inp[4:].split(',')[0],inp[4:].split(',')[1],BCD(int(inp[4:].split(',')[0]),int(inp[4:].split(',')[1]))))
            except:print('Values must be separated by a commer (\',\').')
        else:
            try:print(str(eval(inp)))
            except:print('string \'%s\' cannot be reconized.\nMake sure that input starts with one of \'isP\'/\'range\'/\'factors\'/\'BCD\' followed by a number.'%(inp))
