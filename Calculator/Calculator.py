import re
import math
import sys
import json

def mul(a, b):
    return a*b


def div(a, b):
    try:
        a/b
    except ZeroDivisionError:
        print 'Division by zero!'
        sys.exit()
    else:
        return a/b


def add(a, b):
    return a+b


def degree(a,b):
    return a**b


def wholepart(a,b):
    return a//b


def fraction(a,b):
    return a%b


data = [{'expression':'result'}]
#math.sqrt(),abs(),math.log(),math.log10(),math.sin(),math.cos(),math.tan(),math.asin(),math.acos(),math.atan(),math.atan2(),math.hypot()

# Read file and write infomation in list
with open('expressions.txt','r') as expr:
    list_expr=list(expr);

print  list_expr;
# Replace some mistakes(features)
for a in range(len(list_expr)):
    expression = '('+list_expr[a]+')'

    expression = expression.replace('+-', '-')
    expression = expression.replace('+(-', '(-')
    expression = expression.replace('--', '+')
    expression = expression.replace('-+', '-')
    expression = expression.replace('\n', '')

    zero_dot = re.findall('\D[.][0-9]',expression)
    for z in range (len(zero_dot)):
        expression = expression.replace(zero_dot[z],zero_dot[z][0]+'0'+zero_dot[z][1:])
    mult_dot = re.findall('\d[(]|[)]\d|\d[A-Za-z]',expression)
    for m in range (len(mult_dot)):
        expression = expression.replace(mult_dot[m],mult_dot[m][0]+'*'+mult_dot[m][1:])

    print expression

    count_mul_div = 0
    count_brackets = 0
# Count brackets in the whole expression
    for i in range(len(expression)):
        if expression[i] == '(':
            count_brackets = count_brackets + 1

    print count_brackets

# Divide expression on small brackets
    for i in range(count_brackets):
        res_brackets = re.search('[+-]?[(][^()]*[)]', expression)
        exp_brackets = res_brackets.group()
        print "RES: %s" % exp_brackets


# Count */ in small brackets
        for j in range(len(exp_brackets)-1):
            if exp_brackets[j] == '*' or exp_brackets[j] == '/' or (exp_brackets[j] == '/' and exp_brackets[j+1] == '/')\
                    or exp_brackets[j] == '%' or exp_brackets[j] == '^':
                count_mul_div = count_mul_div + 1
        print count_mul_div

# FOR loop for functions in small bracket
        res_functions = re.findall('(sqrt|abs|log|log10|sin|cos|tan|asin|acos|atan)([-+]?\d+[.]?\d*)', exp_brackets)

        for i in range(len(res_functions)):
            if res_functions[i][0] == 'sqrt':
                exp_brackets = exp_brackets.replace(str(res_functions[i][0]) + str(res_functions[i][1]),
                                                str(math.sqrt(float(res_functions[i][1]))))
            elif res_functions[i][0] == 'abs':
                exp_brackets = exp_brackets.replace(str(res_functions[i][0]) + str(res_functions[i][1]),
                                                str(abs(float(res_functions[i][1]))))
            elif res_functions[i][0] == 'log':
                exp_brackets = exp_brackets.replace(str(res_functions[i][0]) + str(res_functions[i][1]),
                                                str(math.log(float(res_functions[i][1]))))
            elif res_functions[i][0] == 'log10':
                exp_brackets = exp_brackets.replace(str(res_functions[i][0]) + str(res_functions[i][1]),
                                                str(math.log10(float(res_functions[i][1]))))
            elif res_functions[i][0] == 'sin':
                exp_brackets = exp_brackets.replace(str(res_functions[i][0]) + str(res_functions[i][1]),
                                                str(math.sin(float(res_functions[i][1]))))
            elif res_functions[i][0] == 'cos':
                exp_brackets = exp_brackets.replace(str(res_functions[i][0]) + str(res_functions[i][1]),
                                                str(math.cos(float(res_functions[i][1]))))
            elif res_functions[i][0] == 'tan':
                exp_brackets = exp_brackets.replace(str(res_functions[i][0]) + str(res_functions[i][1]),
                                                str(math.tan(float(res_functions[i][1]))))
            elif res_functions[i][0] == 'asin':
                exp_brackets = exp_brackets.replace(str(res_functions[i][0]) + str(res_functions[i][1]),
                                                str(math.asin(float(res_functions[i][1]))))
            elif res_functions[i][0] == 'acos':
                exp_brackets = exp_brackets.replace(str(res_functions[i][0]) + str(res_functions[i][1]),
                                                str(math.acos(float(res_functions[i][1]))))
            elif res_functions[i][0] == 'atan':
                exp_brackets = exp_brackets.replace(str(res_functions[i][0]) + str(res_functions[i][1]),
                                                str(math.atan(float(res_functions[i][1]))))

            # FOR loop for */ in small bracket
        for k in range(count_mul_div):
            res = re.search(r'[-+]?\d+[.]?\d*[*/%^][/]?[-+]?\d+[.]?\d*', exp_brackets)
            print "RES1: %s" % res.group()
            symbols = re.split(r'[*/^%\s][/]?', res.group())
            digits = re.findall(r'[*/^%\s][/]?', res.group())
            print symbols
            print digits
            if '*' in digits:
                factor1 = float(symbols[digits.index("*")])
                factor2 = float(symbols[digits.index("*") + 1])
                product = mul(factor1, factor2)
                print product
                exp_product = "%s*%s" % (symbols[digits.index("*")], symbols[digits.index("*") + 1])
                print 'exp: '+ exp_product
                if ((factor1<0)&(factor2<0)):
                    exp_brackets= exp_brackets.replace(exp_product, '+'+str(product))
                else:
                    exp_brackets = exp_brackets.replace(exp_product, str(product))
      #          print expression
            elif '/' in digits:
                dividend = float(symbols[digits.index("/")])
                divisor = float(symbols[digits.index("/") + 1])
                quotient = div(dividend, divisor)
                print quotient
                exp_quotient = "%s/%s" % (symbols[digits.index("/")], symbols[digits.index("/") + 1])
                if ((dividend<0)&(divisor<0)):
                    exp_brackets= exp_brackets.replace(exp_quotient, '+'+str(quotient))
                else:
                    exp_brackets = exp_brackets.replace(exp_quotient, str(quotient))

            elif '//' in digits:
                dividendw = float(symbols[digits.index("//")])
                divisorw = float(symbols[digits.index("//") + 1])
                quotientw = wholepart(dividendw, divisorw)
                print quotientw
                exp_quotientw = "%s//%s" % (symbols[digits.index("//")], symbols[digits.index("//") + 1])
                if ((dividendw < 0) & (divisorw < 0)):
                    exp_brackets = exp_brackets.replace(exp_quotientw, '+' + str(quotientw))
                else:
                    exp_brackets = exp_brackets.replace(exp_quotientw, str(quotientw))
            elif '%' in digits:
                dividendp = float(symbols[digits.index("%")])
                divisorp = float(symbols[digits.index("%") + 1])
                quotientp = fraction(dividendp, divisorp)
                print quotientp
                exp_quotientp = "{0}%{1}".format(symbols[digits.index("%")], symbols[digits.index("%") + 1])
                if ((dividendp < 0) & (divisorp < 0)):
                    exp_brackets = exp_brackets.replace(exp_quotientp, '+' + str(quotientp))
                else:
                    exp_brackets = exp_brackets.replace(exp_quotientp, str(quotientp))
            elif '^' in digits:
                factor1d = float(symbols[digits.index("^")])
                factor2d = float(symbols[digits.index("^") + 1])
                productd = degree(factor1d, factor2d)
                print productd
                exp_productd = "%s^%s" % (symbols[digits.index("^")], symbols[digits.index("^") + 1])
                if ((factor1d < 0) & (factor2d < 0)):
                    exp_brackets = exp_brackets.replace(exp_productd, '+' + str(productd))
                else:
                    exp_brackets = exp_brackets.replace(exp_productd, str(productd))


                print expression
        print exp_brackets

        count_mul_div=0
# SUM for small bracket
        outcome_ins = re.findall(r'[-+]?\d+[.]?\d*',exp_brackets )
        print outcome_ins
        result = outcome_ins[0]
        for i in range(len(outcome_ins) - 1):
            print outcome_ins
            result = add(float(result), float(outcome_ins[i + 1]))
        print result
        print exp_brackets
        exp_brackets = exp_brackets.replace(exp_brackets,str(result))
        exp_brackets = exp_brackets.replace('+-', '-')
        exp_brackets = exp_brackets.replace('--', '+')
        if res_brackets.group()[0]=='-' or res_brackets.group()[0]=='+':
            expression = expression.replace(res_brackets.group(), res_brackets.group()[0]+str(exp_brackets))
        else :
            expression = expression.replace(res_brackets.group(), str(exp_brackets))

    print expression

    file_result = open('result.txt','ab')

    file_result.writelines(str.strip(list_expr[a])+'='+str(expression)+'\n')

    file_result.close()

    data[0][list_expr[a]]=expression
    print data
    jsonData = json.dumps(data)

with open ('JSONData.json' , 'w') as f:
    json.dump(jsonData,f)