HAI 1.2
    HOW IZ I palindrome YR number       BTW define is_palindrome function
        I HAS A original ITZ number
        I HAS A reversed ITZ 0
        I HAS A remainder ITZ 0
        IM IN YR loop
            BOTH SAEM number AN 0, O RLY?	 BTW Break loop when number == 0
                YA RLY, GTFO, OIC
            remainder R MOD OF number AN 10     BTW remainder = number % 10
            reversed R SUM OF PRODUKT OF reversed AN 10 AN remainder    BTW reversed = 10 * reversed + remainder
            number R QUOSHUNT OF number AN 10   BTW number = number / 10
        IM OUTTA YR loop
        FOUND YR BOTH SAEM reversed AN original
    IF U SAY SO

    HOW IZ I three_digit_palindrome
        I HAS A largest ITZ 0   BTW set largest palindrome found
        I HAS A start_1 ITZ 999 BTW start at highest 3 digit number
        IM IN YR loop_1
            BOTH SAEM start_1 AN 99, O RLY?	 BTW Break loop when first number is no longer 3 digits
                YA RLY, GTFO, OIC
            OBTW 
                Either the first or the second number is a multiple of 11, 
                assume it's the second and check the first afterwards
            TLDR
            I HAS A start_2 ITZ 990
            I HAS A decrement_2 ITZ 11
            BOTH SAEM MOD OF start_1 AN 11 AN 0, O RLY?
                YA RLY
                    start_2 R 999
                    decrement_2 R 1
            OIC
            IM IN YR loop_2
                BOTH SAEM start_1 AN BIGGR OF start_1 AN start_2, O RLY?	 BTW Break loop when first number is bigger than the second
                    YA RLY, GTFO, OIC
                
                I HAS A product ITZ PRODUKT OF start_1 AN start_2
                BOTH SAEM product AN BIGGR OF product AN largest, O RLY?    BTW Only due palindrome logic if product is bigger than current largest
                    YA RLY
                        I IZ palindrome YR product MKAY, O RLY?
                            YA RLY
                                largest R product
                        OIC
                OIC
                start_2 R DIFF OF start_2 AN decrement_2 
            IM OUTTA YR loop_2
            start_1 R DIFF OF start_1 AN 1
        IM OUTTA YR loop_1
        FOUND YR largest
    IF U SAY SO
    VISIBLE I IZ three_digit_palindrome MKAY
KTHXBYE
