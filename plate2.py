#08/07/23
#MMM MKHABELE
def main():
    plate=input("Plate: ")
    def plate_checker(n):
        if 2<=len(n)<=6:#min and max num of charecter
            alpha=''
            num=''
            for charecter in n:
                if charecter.isalpha():
                    alpha=alpha+charecter
                if charecter.isnumeric():
                    num=num+charecter
            if alpha==n:#atleast 2 and most 6 latter charecter is valid
                return "Valid"
            elif alpha+num==n and num[0]!='0':#no number between latters and number part not start with 0
                if n[0:2].isalpha():
                    return "Valid"

            else:
                return "Invalid"
        else: 
            return "Invalid"
    print(plate_checker(plate))
main()
