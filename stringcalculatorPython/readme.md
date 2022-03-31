
1. Run main.py for individual input string

2. Run test.py for all testcases

3. Run onefunction.py for individual input string 
    (onefunction.py grouped all defs in one def)

#----------------------------------------------------------------------
How to process an input string: 
I. Without "//" at the beginning of the input string
    Test case 1 with string: 1,2,5 ---> 1+2+5 = 8
    Result : 8
    Test case 2 with string: 1,3,5,7,9 ---> 1+3+5+7+9 = 25 
    Result : 25
    Test case 3 with string: 0,2,1001,3 ---> 0+2+3=5  (only add number in range 0 .. 1000)
    Result : 5
    Test case 4 with string: 1\n,2,3 ---> 1+2+3=6 (bypass \n right after a number)
    Result : 6
    Test case 5 with string: 1,\n2,4 ---> 1+2+4=7 (bypass \n right before a number)
    Result : 7

II. With "//" at the beginning of the input string
    Test case 6 with string: //;\n1;3;4   --> //;\n  replace ; --> ,  so 1;3;4 --> 1,3,4 --> 1+3+4 = 8    
    Result : 8
    Test case 7 with string: //$\n1$2$3   --> //$\n  replace $ --> ,  so 1$2$3 --> 1,2,3 --> 1+2+3 = 6
    Result : 6
    Test case 8 with string: //@\n2@3@8   --> //@\n  replace @ --> ,  so 2@3$8 --> 2,3,8 --> 2+3+8 = 13
    Result : 13
    Test case 9 with string: //***\n1***2***3 --> //***\n  replace *** --> , so 1***2***3 --> 1,2,3 --> 1+2+3 = 6
    Result : 6
    Test case 10 with string: //$,@,*,^\n1$2@3*4^5 --> //$,@,*,^\n  replace $ @ * ^ --> ,  so 1$2@3*4^5 --> 1,2,3,4,5 --> 1+2+3+4+5 = 15
    Result : 15
    Test case 11 with string: //***,$$,@@\n1***2$$\n3@@4  --> //***,$$,@@\n  replace *** $$ @@ --> ,  so 1***2$$\n3@@4 --> 1,2,\n3,4 --> bypass \n --> 1,2,3,4 --> 1+2+3+4 = 10
    Result : 10

III. Negatives not allowed and list all negative numbers   
    Test case 12 with string: 1,-2,3,-4,6,-5 --> exceptString: -2,-4,-5
    Negatives not allowed:-2,-4,-5

