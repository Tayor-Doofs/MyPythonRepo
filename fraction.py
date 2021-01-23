ff_num = int(input("Enter First Fraction Numerator"))
ff_denom = int(input("Enter First Fraction Denominator"))

sf_num = int(input("Enter Second Fraction Numerator"))
sf_denom = int(input("Enter Second Fraction Denominator"))

if ff_denom == sf_denom:
    mul_denom = ff_denom
    frac_num = ff_num + sf_num
    print(frac_num,"/",mul_denom)
else:
    mul_denom = ff_denom * sf_denom
    frac_num = (ff_num * sf_denom + sf_num * ff_denom)
    print(frac_num,"/",mul_denom)