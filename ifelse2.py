# age=int (input("enter your age:"))


if (age >= 18):
    license=(input("do you have license:"))
    if(license=='Yes'):
       print("eligble for drive license")  #prints if age is greather than #18 and has a license

    else:
       print('Go and get license')
else:
    print("not eligible for drive license")
