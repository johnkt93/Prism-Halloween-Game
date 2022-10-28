image black = "/images/Yura_Dungeon/black.png"
image white = "/images/Yura_Dungeon/white.png"
image red = "/images/Yura_Dungeon/red.png"

screen mini_map:
    #add Solid("#000")
    frame:
        align (.95, .05)
        grid 19 20:
            allow_underfull True
            if position == 't1':
                add "red"
            elif position != 't1':
                add "black"
            if position == 't2':
                add "red"
            elif position != 't2':
                add "black"
            if position == 't3':
                add "red"
            elif position != 't3':
                add "black"
            if position == 't4':
                add "red"
            elif position != 't4':
                add "white"
            if position == 't5':
                add "red"
            elif position != 't5':
                add "white"
            if position == 't6':
                add "red"
            elif position != 't6':
                add "white"
            if position == 't7':
                add "red"
            elif position != 't7':
                add "white"
            if position == 't8':
                add "red"
            elif position != 't8':
                add "white"
            if position == 't9':
                add "red"
            elif position != 't9':
                add "black"
            if position == 't10':
                add "red"
            elif position != 't10':
                add "black"
            if position == 't11':
                add "red"
            elif position != 't11':
                add "black"
            if position == 't12':
                add "red"
            elif position != 't12':
                add "black"
            if position == 't13':
                add "red"
            elif position != 't13':
                add "black"
            if position == 't14':
                add "red"
            elif position != 't14':
                add "black"
            if position == 't15':
                add "red"
            elif position != 't15':
                add "black"
            if position == 't16':
                add "red"
            elif position != 't16':
                add "black"
            if position == 't17':
                add "red"
            elif position != 't17':
                add "black"
            if position == 't18':
                add "red"
            elif position != 't18':
                add "black"
            if position == 't19':
                add "red"
            elif position != 't19':
                add "black"

            if position == 's1':
                add "red"
            elif position != 's1':
                add "black"
            if position == 's2':
                add "red"
            elif position != 's2':
                add "black"
            if position == 's3':
                add "red"
            elif position != 's3':
                add "black"
            if position == 's4':
                add "red"
            elif position != 's4':
                add "white"
            if position == 's5':
                add "red"
            elif position != 's5':
                add "black"
            if position == 's6':
                add "red"
            elif position != 's6':
                add "black"
            if position == 's7':
                add "red"
            elif position != 's7':
                add "black"
            if position == 's8':
                add "red"
            elif position != 's8':
                add "white"
            if position == 's9':
                add "red"
            elif position != 's9':
                add "black"
            if position == 's10':
                add "red"
            elif position != 's10':
                add "black"
            if position == 's11':
                add "red"
            elif position != 's11':
                add "black"
            if position == 's12':
                add "red"
            elif position != 's12':
                add "white"
            if position == 's13':
                add "red"
            elif position != 's13':
                add "white"
            if position == 's14':
                add "red"
            elif position != 's14':
                add "white"
            if position == 's15':
                add "red"
            elif position != 's15':
                add "white"
            if position == 's16':
                add "red"
            elif position != 's16':
                add "white"
            if position == 's17':
                add "red"
            elif position != 's17':
                add "white"
            if position == 's18':
                add "red"
            elif position != 's18':
                add "white"
            if position == 's19':
                add "red"
            elif position != 's19':
                add "black"

            if position == 'r1':
                add "red"
            elif position != 'r1':
                add "black"
            if position == 'r2':
                add "red"
            elif position != 'r2':
                add "black"
            if position == 'r3':
                add "red"
            elif position != 'r3':
                add "black"
            if position == 'r4':
                add "red"
            elif position != 'r4':
                add "black"
            if position == 'r5':
                add "red"
            elif position != 'r5':
                add "black"
            if position == 'r6':
                add "red"
            elif position != 'r6':
                add "black"
            if position == 'r7':
                add "red"
            elif position != 'r7':
                add "black"
            if position == 'r8':
                add "red"
            elif position != 'r8':
                add "white"
            if position == 'r9':
                add "red"
            elif position != 'r9':
                add "black"
            if position == 'r10':
                add "red"
            elif position != 'r10':
                add "black"
            if position == 'r11':
                add "red"
            elif position != 'r11':
                add "black"
            if position == 'r12':
                add "red"
            elif position != 'r12':
                add "white"
            if position == 'r13':
                add "red"
            elif position != 'r13':
                add "white"
            if position == 'r14':
                add "red"
            elif position != 'r14':
                add "white"
            if position == 'r15':
                add "red"
            elif position != 'r15':
                add "white"
            if position == 'r16':
                add "red"
            elif position != 'r16':
                add "white"
            if position == 'r17':
                add "red"
            elif position != 'r17':
                add "white"
            if position == 'r18':
                add "red"
            elif position != 'r18':
                add "white"
            if position == 'r19':
                add "red"
            elif position != 'r19':
                add "black"

            if position == 'q1':
                add "red"
            elif position != 'q1':
                add "black"
            if position == 'q2':
                add "red"
            elif position != 'q2':
                add "black"
            if position == 'q3':
                add "red"
            elif position != 'q3':
                add "black"
            if position == 'q4':
                add "red"
            elif position != 'q4':
                add "white"
            if position == 'q5':
                add "red"
            elif position != 'q5':
                add "black"
            if position == 'q6':
                add "red"
            elif position != 'q6':
                add "black"
            if position == 'q7':
                add "red"
            elif position != 'q7':
                add "black"
            if position == 'q8':
                add "red"
            elif position != 'q8':
                add "white"
            if position == 'q9':
                add "red"
            elif position != 'q9':
                add "black"
            if position == 'q10':
                add "red"
            elif position != 'q10':
                add "black"
            if position == 'q11':
                add "red"
            elif position != 'q11':
                add "black"
            if position == 'q12':
                add "red"
            elif position != 'q12':
                add "white"
            if position == 'q13':
                add "red"
            elif position != 'q13':
                add "white"
            if position == 'q14':
                add "red"
            elif position != 'q14':
                add "white"
            if position == 'q15':
                add "red"
            elif position != 'q15':
                add "white"
            if position == 'q16':
                add "red"
            elif position != 'q16':
                add "white"
            if position == 'q17':
                add "red"
            elif position != 'q17':
                add "white"
            if position == 'q18':
                add "red"
            elif position != 'q18':
                add "white"
            if position == 'q19':
                add "red"
            elif position != 'q19':
                add "black"

            if position == 'p1':
                add "red"
            elif position != 'p1':
                add "white"
            if position == 'p2':
                add "red"
            elif position != 'p2':
                add "white"
            if position == 'p3':
                add "red"
            elif position != 'p3':
                add "white"
            if position == 'p4':
                add "red"
            elif position != 'p4':
                add "white"
            if position == 'p5':
                add "red"
            elif position != 'p5':
                add "white"
            if position == 'p6':
                add "red"
            elif position != 'p6':
                add "black"
            if position == 'p7':
                add "red"
            elif position != 'p7':
                add "white"
            if position == 'p8':
                add "red"
            elif position != 'p8':
                add "white"
            if position == 'p9':
                add "red"
            elif position != 'p9':
                add "white"
            if position == 'p10':
                add "red"
            elif position != 'p10':
                add "white"
            if position == 'p11':
                add "red"
            elif position != 'p11':
                add "white"
            if position == 'p12':
                add "red"
            elif position != 'p12':
                add "white"
            if position == 'p13':
                add "red"
            elif position != 'p13':
                add "white"
            if position == 'p14':
                add "red"
            elif position != 'p14':
                add "white"
            if position == 'p15':
                add "red"
            elif position != 'p15':
                add "white"
            if position == 'p16':
                add "red"
            elif position != 'p16':
                add "white"
            if position == 'p17':
                add "red"
            elif position != 'p17':
                add "white"
            if position == 'p18':
                add "red"
            elif position != 'p18':
                add "white"
            if position == 'p19':
                add "red"
            elif position != 'p19':
                add "black"

            if position == 'o1':
                add "red"
            elif position != 'o1':
                add "black"
            if position == 'o2':
                add "red"
            elif position != 'o2':
                add "black"
            if position == 'o3':
                add "red"
            elif position != 'o3':
                add "black"
            if position == 'o4':
                add "red"
            elif position != 'o4':
                add "black"
            if position == 'o5':
                add "red"
            elif position != 'o5':
                add "black"
            if position == 'o6':
                add "red"
            elif position != 'o6':
                add "black"
            if position == 'o7':
                add "red"
            elif position != 'o7':
                add "black"
            if position == 'o8':
                add "red"
            elif position != 'o8':
                add "black"
            if position == 'o9':
                add "red"
            elif position != 'o9':
                add "black"
            if position == 'o10':
                add "red"
            elif position != 'o10':
                add "black"
            if position == 'o11':
                add "red"
            elif position != 'o11':
                add "black"
            if position == 'o12':
                add "red"
            elif position != 'o12':
                add "black"
            if position == 'o13':
                add "red"
            elif position != 'o13':
                add "black"
            if position == 'o14':
                add "red"
            elif position != 'o14':
                add "black"
            if position == 'o15':
                add "red"
            elif position != 'o15':
                add "black"
            if position == 'o16':
                add "red"
            elif position != 'o16':
                add "black"
            if position == 'o17':
                add "red"
            elif position != 'o17':
                add "black"
            if position == 'o18':
                add "red"
            elif position != 'o18':
                add "black"
            if position == 'o19':
                add "red"
            elif position != 'o19':
                add "black"
            if position == 'n1':
                add "red"
            elif position != 'n1':
                add "black"
            if position == 'n2':
                add "red"
            elif position != 'n2':
                add "white"
            if position == 'n3':
                add "red"
            elif position != 'n3':
                add "white"
            if position == 'n4':
                add "red"
            elif position != 'n4':
                add "white"
            if position == 'n5':
                add "red"
            elif position != 'n5':
                add "white"
            if position == 'n6':
                add "red"
            elif position != 'n6':
                add "black"
            if position == 'n7':
                add "red"
            elif position != 'n7':
                add "white"
            if position == 'n8':
                add "red"
            elif position != 'n8':
                add "white"
            if position == 'n9':
                add "red"
            elif position != 'n9':
                add "white"
            if position == 'n10':
                add "red"
            elif position != 'n10':
                add "white"
            if position == 'n11':
                add "red"
            elif position != 'n11':
                add "white"
            if position == 'n12':
                add "red"
            elif position != 'n12':
                add "white"
            if position == 'n13':
                add "red"
            elif position != 'n13':
                add "white"
            if position == 'n14':
                add "red"
            elif position != 'n14':
                add "white"
            if position == 'n15':
                add "red"
            elif position != 'n15':
                add "white"
            if position == 'n16':
                add "red"
            elif position != 'n16':
                add "white"
            if position == 'n17':
                add "red"
            elif position != 'n17':
                add "white"
            if position == 'n18':
                add "red"
            elif position != 'n18':
                add "white"
            if position == 'n19':
                add "red"
            elif position != 'n19':
                add "black"

            if position == 'm1':
                add "red"
            elif position != 'm1':
                add "black"
            if position == 'm2':
                add "red"
            elif position != 'm2':
                add "white"
            if position == 'm3':
                add "red"
            elif position != 'm3':
                add "black"
            if position == 'm4':
                add "red"
            elif position != 'm4':
                add "black"
            if position == 'm5':
                add "red"
            elif position != 'm5':
                add "black"
            if position == 'm6':
                add "red"
            elif position != 'm6':
                add "black"
            if position == 'm7':
                add "red"
            elif position != 'm7':
                add "black"
            if position == 'm8':
                add "red"
            elif position != 'm8':
                add "black"
            if position == 'm9':
                add "red"
            elif position != 'm9':
                add "black"
            if position == 'm10':
                add "red"
            elif position != 'm10':
                add "black"
            if position == 'm11':
                add "red"
            elif position != 'm11':
                add "black"
            if position == 'm12':
                add "red"
            elif position != 'm12':
                add "black"
            if position == 'm13':
                add "red"
            elif position != 'm13':
                add "black"
            if position == 'm14':
                add "red"
            elif position != 'm14':
                add "black"
            if position == 'm15':
                add "red"
            elif position != 'm15':
                add "black"
            if position == 'm16':
                add "red"
            elif position != 'm16':
                add "black"
            if position == 'm17':
                add "red"
            elif position != 'm17':
                add "black"
            if position == 'm18':
                add "red"
            elif position != 'm18':
                add "white"
            if position == 'm19':
                add "red"
            elif position != 'm19':
                add "black"

            if position == 'l1':
                add "red"
            elif position != 'l1':
                add "black"
            if position == 'l2':
                add "red"
            elif position != 'l2':
                add "white"
            if position == 'l3':
                add "red"
            elif position != 'l3':
                add "black"
            if position == 'l4':
                add "red"
            elif position != 'l4':
                add "black"
            if position == 'l5':
                add "red"
            elif position != 'l5':
                add "black"
            if position == 'l6':
                add "red"
            elif position != 'l6':
                add "black"
            if position == 'l7':
                add "red"
            elif position != 'l7':
                add "black"
            if position == 'l8':
                add "red"
            elif position != 'l8':
                add "black"
            if position == 'l9':
                add "red"
            elif position != 'l9':
                add "black"
            if position == 'l10':
                add "red"
            elif position != 'l10':
                add "white"
            if position == 'l11':
                add "red"
            elif position != 'l11':
                add "white"
            if position == 'l12':
                add "red"
            elif position != 'l12':
                add "white"
            if position == 'l13':
                add "red"
            elif position != 'l13':
                add "white"
            if position == 'l14':
                add "red"
            elif position != 'l14':
                add "white"
            if position == 'l15':
                add "red"
            elif position != 'l15':
                add "white"
            if position == 'l16':
                add "red"
            elif position != 'l16':
                add "white"
            if position == 'l17':
                add "red"
            elif position != 'l17':
                add "black"
            if position == 'l18':
                add "red"
            elif position != 'l18':
                add "white"
            if position == 'l19':
                add "red"
            elif position != 'l19':
                add "black"

            if position == 'k1':
                add "red"
            elif position != 'k1':
                add "black"
            if position == 'k2':
                add "red"
            elif position != 'k2':
                add "white"
            if position == 'k3':
                add "red"
            elif position != 'k3':
                add "black"
            if position == 'k4':
                add "red"
            elif position != 'k4':
                add "black"
            if position == 'k5':
                add "red"
            elif position != 'k5':
                add "black"
            if position == 'k6':
                add "red"
            elif position != 'k6':
                add "black"
            if position == 'k7':
                add "red"
            elif position != 'k7':
                add "black"
            if position == 'k8':
                add "red"
            elif position != 'k8':
                add "black"
            if position == 'k9':
                add "red"
            elif position != 'k9':
                add "black"
            if position == 'k10':
                add "red"
            elif position != 'k10':
                add "white"
            if position == 'k11':
                add "red"
            elif position != 'k11':
                add "white"
            if position == 'k12':
                add "red"
            elif position != 'k12':
                add "white"
            if position == 'k13':
                add "red"
            elif position != 'k13':
                add "black"
            if position == 'k14':
                add "red"
            elif position != 'k14':
                add "white"
            if position == 'k15':
                add "red"
            elif position != 'k15':
                add "white"
            if position == 'k16':
                add "red"
            elif position != 'k16':
                add "white"
            if position == 'k17':
                add "red"
            elif position != 'k17':
                add "black"
            if position == 'k18':
                add "red"
            elif position != 'k18':
                add "white"
            if position == 'k19':
                add "red"
            elif position != 'k19':
                add "black"

            if position == 'j1':
                add "red"
            elif position != 'j1':
                add "black"
            if position == 'j2':
                add "red"
            elif position != 'j2':
                add "white"
            if position == 'j3':
                add "red"
            elif position != 'j3':
                add "black"
            if position == 'j4':
                add "red"
            elif position != 'j4':
                add "black"
            if position == 'j5':
                add "red"
            elif position != 'j5':
                add "black"
            if position == 'j6':
                add "red"
            elif position != 'j6':
                add "black"
            if position == 'j7':
                add "red"
            elif position != 'j7':
                add "black"
            if position == 'j8':
                add "red"
            elif position != 'j8':
                add "black"
            if position == 'j9':
                add "red"
            elif position != 'j9':
                add "black"
            if position == 'j10':
                add "red"
            elif position != 'j10':
                add "white"
            if position == 'j11':
                add "red"
            elif position != 'j11':
                add "white"
            if position == 'j12':
                add "red"
            elif position != 'j12':
                add "white"
            if position == 'j13':
                add "red"
            elif position != 'j13':
                add "black"
            if position == 'j14':
                add "red"
            elif position != 'j14':
                add "white"
            if position == 'j15':
                add "red"
            elif position != 'j15':
                add "white"
            if position == 'j16':
                add "red"
            elif position != 'j16':
                add "white"
            if position == 'j17':
                add "red"
            elif position != 'j17':
                add "black"
            if position == 'j18':
                add "red"
            elif position != 'j18':
                add "white"
            if position == 'j19':
                add "red"
            elif position != 'j19':
                add "black"
            if position == 'i1':
                add "red"
            elif position != 'i1':
                add "white"
            if position == 'i2':
                add "red"
            elif position != 'i2':
                add "white"
            if position == 'i3':
                add "red"
            elif position != 'i3':
                add "white"
            if position == 'i4':
                add "red"
            elif position != 'i4':
                add "white"
            if position == 'i5':
                add "red"
            elif position != 'i5':
                add "white"
            if position == 'i6':
                add "red"
            elif position != 'i6':
                add "black"
            if position == 'i7':
                add "red"
            elif position != 'i7':
                add "white"
            if position == 'i8':
                add "red"
            elif position != 'i8':
                add "white"
            if position == 'i9':
                add "red"
            elif position != 'i9':
                add "white"
            if position == 'i10':
                add "red"
            elif position != 'i10':
                add "white"
            if position == 'i11':
                add "red"
            elif position != 'i11':
                add "white"
            if position == 'i12':
                add "red"
            elif position != 'i12':
                add "black"
            if position == 'i13':
                add "red"
            elif position != 'i13':
                add "black"
            if position == 'i14':
                add "red"
            elif position != 'i14':
                add "black"
            if position == 'i15':
                add "red"
            elif position != 'i15':
                add "black"
            if position == 'i16':
                add "red"
            elif position != 'i16':
                add "white"
            if position == 'i17':
                add "red"
            elif position != 'i17':
                add "black"
            if position == 'i18':
                add "red"
            elif position != 'i18':
                add "white"
            if position == 'i19':
                add "red"
            elif position != 'i19':
                add "black"

            if position == 'h1':
                add "red"
            elif position != 'h1':
                add "black"
            if position == 'h2':
                add "red"
            elif position != 'h2':
                add "black"
            if position == 'h3':
                add "red"
            elif position != 'h3':
                add "black"
            if position == 'h4':
                add "red"
            elif position != 'h4':
                add "white"
            if position == 'h5':
                add "red"
            elif position != 'h5':
                add "white"
            if position == 'h6':
                add "red"
            elif position != 'h6':
                add "black"
            if position == 'h7':
                add "red"
            elif position != 'h7':
                add "white"
            if position == 'h8':
                add "red"
            elif position != 'h8':
                add "white"
            if position == 'h9':
                add "red"
            elif position != 'h9':
                add "black"
            if position == 'h10':
                add "red"
            elif position != 'h10':
                add "black"
            if position == 'h11':
                add "red"
            elif position != 'h11':
                add "black"
            if position == 'h12':
                add "red"
            elif position != 'h12':
                add "black"
            if position == 'h13':
                add "red"
            elif position != 'h13':
                add "white"
            if position == 'h14':
                add "red"
            elif position != 'h14':
                add "white"
            if position == 'h15':
                add "red"
            elif position != 'h15':
                add "black"
            if position == 'h16':
                add "red"
            elif position != 'h16':
                add "white"
            if position == 'h17':
                add "red"
            elif position != 'h17':
                add "black"
            if position == 'h18':
                add "red"
            elif position != 'h18':
                add "white"
            if position == 'h19':
                add "red"
            elif position != 'h19':
                add "black"

            if position == 'g1':
                add "red"
            elif position != 'g1':
                add "black"
            if position == 'g2':
                add "red"
            elif position != 'g2':
                add "black"
            if position == 'g3':
                add "red"
            elif position != 'g3':
                add "black"
            if position == 'g4':
                add "red"
            elif position != 'g4':
                add "white"
            if position == 'g5':
                add "red"
            elif position != 'g5':
                add "white"
            if position == 'g6':
                add "red"
            elif position != 'g6':
                add "black"
            if position == 'g7':
                add "red"
            elif position != 'g7':
                add "white"
            if position == 'g8':
                add "red"
            elif position != 'g8':
                add "white"
            if position == 'g9':
                add "red"
            elif position != 'g9':
                add "black"
            if position == 'g10':
                add "red"
            elif position != 'g10':
                add "black"
            if position == 'g11':
                add "red"
            elif position != 'g11':
                add "black"
            if position == 'g12':
                add "red"
            elif position != 'g12':
                add "black"
            if position == 'g13':
                add "red"
            elif position != 'g13':
                add "white"
            if position == 'g14':
                add "red"
            elif position != 'g14':
                add "white"
            if position == 'g15':
                add "red"
            elif position != 'g15':
                add "black"
            if position == 'g16':
                add "red"
            elif position != 'g16':
                add "white"
            if position == 'g17':
                add "red"
            elif position != 'g17':
                add "black"
            if position == 'g18':
                add "red"
            elif position != 'g18':
                add "white"
            if position == 'g19':
                add "red"
            elif position != 'g19':
                add "black"

            if position == 'f1':
                add "red"
            elif position != 'f1':
                add "black"
            if position == 'f2':
                add "red"
            elif position != 'f2':
                add "black"
            if position == 'f3':
                add "red"
            elif position != 'f3':
                add "black"
            if position == 'f4':
                add "red"
            elif position != 'f4':
                add "white"
            if position == 'f5':
                add "red"
            elif position != 'f5':
                add "black"
            if position == 'f6':
                add "red"
            elif position != 'f6':
                add "black"
            if position == 'f7':
                add "red"
            elif position != 'f7':
                add "black"
            if position == 'f8':
                add "red"
            elif position != 'f8':
                add "white"
            if position == 'f9':
                add "red"
            elif position != 'f9':
                add "black"
            if position == 'f10':
                add "red"
            elif position != 'f10':
                add "black"
            if position == 'f11':
                add "red"
            elif position != 'f11':
                add "black"
            if position == 'f12':
                add "red"
            elif position != 'f12':
                add "black"
            if position == 'f13':
                add "red"
            elif position != 'f13':
                add "white"
            if position == 'f14':
                add "red"
            elif position != 'f14':
                add "white"
            if position == 'f15':
                add "red"
            elif position != 'f15':
                add "black"
            if position == 'f16':
                add "red"
            elif position != 'f16':
                add "black"
            if position == 'f17':
                add "red"
            elif position != 'f17':
                add "black"
            if position == 'f18':
                add "red"
            elif position != 'f18':
                add "black"
            if position == 'f19':
                add "red"
            elif position != 'f19':
                add "black"

            if position == 'e1':
                add "red"
            elif position != 'e1':
                add "white"
            if position == 'e2':
                add "red"
            elif position != 'e2':
                add "black"
            if position == 'e3':
                add "red"
            elif position != 'e3':
                add "white"
            if position == 'e4':
                add "red"
            elif position != 'e4':
                add "white"
            if position == 'e5':
                add "red"
            elif position != 'e5':
                add "black"
            if position == 'e6':
                add "red"
            elif position != 'e6':
                add "black"
            if position == 'e7':
                add "red"
            elif position != 'e7':
                add "black"
            if position == 'e8':
                add "red"
            elif position != 'e8':
                add "white"
            if position == 'e9':
                add "red"
            elif position != 'e9':
                add "black"
            if position == 'e10':
                add "red"
            elif position != 'e10':
                add "black"
            if position == 'e11':
                add "red"
            elif position != 'e11':
                add "black"
            if position == 'e12':
                add "red"
            elif position != 'e12':
                add "black"
            if position == 'e13':
                add "red"
            elif position != 'e13':
                add "white"
            if position == 'e14':
                add "red"
            elif position != 'e14':
                add "white"
            if position == 'e15':
                add "red"
            elif position != 'e15':
                add "black"
            if position == 'e16':
                add "red"
            elif position != 'e16':
                add "white"
            if position == 'e17':
                add "red"
            elif position != 'e17':
                add "black"
            if position == 'e18':
                add "red"
            elif position != 'e18':
                add "white"
            if position == 'e19':
                add "red"
            elif position != 'e19':
                add "black"

            if position == 'd1':
                add "red"
            elif position != 'd1':
                add "white"
            if position == 'd2':
                add "red"
            elif position != 'd2':
                add "black"
            if position == 'd3':
                add "red"
            elif position != 'd3':
                add "black"
            if position == 'd4':
                add "red"
            elif position != 'd4':
                add "white"
            if position == 'd5':
                add "red"
            elif position != 'd5':
                add "white"
            if position == 'd6':
                add "red"
            elif position != 'd6':
                add "black"
            if position == 'd7':
                add "red"
            elif position != 'd7':
                add "white"
            if position == 'd8':
                add "red"
            elif position != 'd8':
                add "white"
            if position == 'd9':
                add "red"
            elif position != 'd9':
                add "black"
            if position == 'd10':
                add "red"
            elif position != 'd10':
                add "black"
            if position == 'd11':
                add "red"
            elif position != 'd11':
                add "black"
            if position == 'd12':
                add "red"
            elif position != 'd12':
                add "black"
            if position == 'd13':
                add "red"
            elif position != 'd13':
                add "white"
            if position == 'd14':
                add "red"
            elif position != 'd14':
                add "white"
            if position == 'd15':
                add "red"
            elif position != 'd15':
                add "black"
            if position == 'd16':
                add "red"
            elif position != 'd16':
                add "white"
            if position == 'd17':
                add "red"
            elif position != 'd17':
                add "black"
            if position == 'd18':
                add "red"
            elif position != 'd18':
                add "white"
            if position == 'd19':
                add "red"
            elif position != 'd19':
                add "black"

            if position == 'c1':
                add "red"
            elif position != 'c1':
                add "white"
            if position == 'c2':
                add "red"
            elif position != 'c2':
                add "white"
            if position == 'c3':
                add "red"
            elif position != 'c3':
                add "black"
            if position == 'c4':
                add "red"
            elif position != 'c4':
                add "white"
            if position == 'c5':
                add "red"
            elif position != 'c5':
                add "white"
            if position == 'c6':
                add "red"
            elif position != 'c6':
                add "black"
            if position == 'c7':
                add "red"
            elif position != 'c7':
                add "white"
            if position == 'c8':
                add "red"
            elif position != 'c8':
                add "white"
            if position == 'c9':
                add "red"
            elif position != 'c9':
                add "black"
            if position == 'c10':
                add "red"
            elif position != 'c10':
                add "black"
            if position == 'c11':
                add "red"
            elif position != 'c11':
                add "black"
            if position == 'c12':
                add "red"
            elif position != 'c12':
                add "black"
            if position == 'c13':
                add "red"
            elif position != 'c13':
                add "white"
            if position == 'c14':
                add "red"
            elif position != 'c14':
                add "black"
            if position == 'c15':
                add "red"
            elif position != 'c15':
                add "black"
            if position == 'c16':
                add "red"
            elif position != 'c16':
                add "white"
            if position == 'c17':
                add "red"
            elif position != 'c17':
                add "black"
            if position == 'c18':
                add "red"
            elif position != 'c18':
                add "white"
            if position == 'c19':
                add "red"
            elif position != 'c19':
                add "black"

            if position == 'b1':
                add "red"
            elif position != 'b1':
                add "black"
            if position == 'b2':
                add "red"
            elif position != 'b2':
                add "white"
            if position == 'b3':
                add "red"
            elif position != 'b3':
                add "black"
            if position == 'b4':
                add "red"
            elif position != 'b4':
                add "white"
            if position == 'b5':
                add "red"
            elif position != 'b5':
                add "white"
            if position == 'b6':
                add "red"
            elif position != 'b6':
                add "white"
            if position == 'b6':
                add "red"
            if position == 'b7':
                add "red"
            elif position != 'b7':
                add "white"
            if position == 'b8':
                add "red"
            elif position != 'b8':
                add "white"
            if position == 'b9':
                add "red"
            elif position != 'b9':
                add "white"
            if position == 'b10':
                add "red"
            elif position != 'b10':
                add "white"
            if position == 'b11':
                add "red"
            elif position != 'b11':
                add "white"
            if position == 'b12':
                add "red"
            elif position != 'b12':
                add "white"
            if position == 'b13':
                add "red"
            elif position != 'b13':
                add "white"
            if position == 'b14':
                add "red"
            elif position != 'b14':
                add "black"
            if position == 'b15':
                add "red"
            elif position != 'b15':
                add "white"
            if position == 'b16':
                add "red"
            elif position != 'b16':
                add "white"
            if position == 'b17':
                add "red"
            elif position != 'b17':
                add "black"
            if position == 'b18':
                add "red"
            elif position != 'b18':
                add "white"
            if position == 'b19':
                add "red"
            elif position != 'b19':
                add "black"

            if position == 'a1':
                add "red"
            elif position != 'a1':
                add "black"
            if position == 'a2':
                add "red"
            elif position != 'a2':
                add "black"
            if position == 'a3':
                add "red"
            elif position != 'a3':
                add "black"
            if position == 'a4':
                add "red"
            elif position != 'a4':
                add "black"
            if position == 'a5':
                add "red"
            elif position != 'a5':
                add "black"
            if position == 'a6':
                add "red"
            elif position != 'a6':
                add "black"
            if position == 'a7':
                add "red"
            elif position != 'a7':
                add "black"
            if position == 'a8':
                add "red"
            elif position != 'a8':
                add "black"
            if position == 'a9':
                add "red"
            elif position != 'a9':
                add "black"
            if position == 'a10':
                add "red"
            elif position != 'a10':
                add "black"
            if position == 'a11':
                add "red"
            elif position != 'a11':
                add "black"
            if position == 'a12':
                add "red"
            elif position != 'a12':
                add "black"
            if position == 'a13':
                add "red"
            elif position != 'a13':
                add "black"
            if position == 'a14':
                add "red"
            elif position != 'a14':
                add "black"
            if position == 'a15':
                add "red"
            elif position != 'a15':
                add "white"
            if position == 'a16':
                add "red"
            elif position != 'a16':
                add "black"
            if position == 'a17':
                add "red"
            elif position != 'a17':
                add "black"
            if position == 'a18':
                add "red"
            elif position != 'a18':
                add "white"
            if position == 'a19':
                add "red"
            elif position != 'a19':
                add "black"

label yura_dungeon_start:
    #$ minimap_data =["101"]
    default wisp_count = 0
    default crane_count = 0
    default inventory_purple_crane = False
    default inventory_blue_crane = False
    default inventory_yellow_crane = False
    default inventory_red_crane = False
    default sliders_are_fun = True
    default position = 'c6'
    image bbb = "images/Yura_Dungeon/bbb.png"
    image lbb = "images/Yura_Dungeon/lbb.png"
    image bcb = "images/Yura_Dungeon/bcb.png"
    image lcb = "images/Yura_Dungeon/lcb.png"
    image bbr = "images/Yura_Dungeon/bbr.png"
    image lbr = "images/Yura_Dungeon/lbr.png"
    image bcr = "images/Yura_Dungeon/bcr.png"
    image lcr = "images/Yura_Dungeon/lcr.png"

    "I turned the knob to open the door but it did not open."
    s "What the heck."
    "I pushed against the door again. It felt like something was jamming the door. Each time I pushed against the door I felt it open a little bit more."
    "Not wanting to waste any time, I braced myself and threw myself against the door."
    scene image "images/Yura_Dungeon/black.png":
        size(1280,720)
    "The door flung wide open as I fell to the ground unceremoniously."
    s "Ouch."
    s "I shouldn't have slammed the door so hard."
    "I looked up and noticed the room was pitch black, the only illumination coming from the doorway."
    s "Should be a light switch around here somewhere."
    "Before I could get up, the door shut behind me, leaving me in the darkness."
    "I could hear the sound of someone approaching."
    "I wanted to call out to it, but my body just froze in place."
    "The sound slowly came closer and closer {w} until eventually it faded away."
    "After the sound faded from my hearing, I felt my body relax."
    "Now to do something about the lighting situation."
    "As soon as I thought that, a small blue orb of light appeared in front of me."
    "Yuragumi" "Save... us...light..."
    "The ball of light shined dimly, barely revealing my immediate surrounding."
    "It was still difficult to see too far ahead of me, but at least I wouldn't be tripping over my own feet."
    show screen mini_map
    "I noticed a piece of paper by my feet. I picked it up and read it."

    hide screen mini_map
    show screen renfield_text_1
    $ renpy.pause()
    stop voice
    hide screen renfield_text_1
    s "I don't like the sound of that."
    show screen mini_map
    jump c6

label slider_puzzle_1:
    "Once I cleared my path, the mote shone it's light to another note"
    voice "audio/Miscellaneous/Renfield/Narration_2_Renfield.mp3"
    centered "As we made our way down the stairs, we found a wide space with a door that wasn’t locked but was heavily barricaded\nA bunch of us managed to clear the blockade after some time\nbut as a precaution, we left a tall and heavy shelf beside the door just in case we need to block it off due to what’s inside\nThe door produced a loud click and an eerie creak as it opened"

    "I got an eerie feeling as I made my way further in."
    jump g6

label qtini_crane:
    image qtini = "images/Yura_Dungeon/Qarrot.png"
    image qtini_wisp = "images/Yura_Dungeon/Qarrot.png"
    show yura:
        zoom 0.48
        xalign 0.2
    hide screen mini_map
    show qtini:
        xalign 0.8
    voice "audio/Yuragumi/Qtini/Qtini1.wav"
    "Qtini" "Do you think I could make the other papercraft Gen 3 members?"
    y "What, why do you need other girls Qti?"
    voice "audio/Yuragumi/Qtini/Qtini2.wav"
    "Qtini" "They're not for me, they're for Smol Yura."
    voice "audio/Yuragumi/Qtini/Qtini3.wav"
    "Qtini" "Don't you want Smol Yura to be with her wifey?"
    y "Smol Yura is fine by herself, hmmph."
    y "Where are you going Qtini?"
    voice "audio/Yuragumi/Qtini/Qtini4.wav"
    "Qtini" "I'm just going to get some milk. By myself. Totally not going with anyone else."
    hide qtini
    hide yura

    #Qtini the Wisp
    "I held the crane in my hand."
    "What was that scene I just saw?"
    show qtini_wisp:
        xalign 0.8
    s "Is this yours? Are you Qtini?"
    "I directed my question at the mote."
    "It offered no response, but it now seemed to be shining brighter than before."
    hide qtini_wisp
    $ renpy.notify("A Purple Crane has been added to your inventory.")
    $ inventory_purple_crane = True
    $ wisp_count+=1
    show screen mini_map
    return

label slider_puzzle_2:
    "As I made my way down the corridor I found more furniture, arranged haphazardly to block my path."
    s "Not this again."
    $ sliders_are_fun = False
    return

label slider_puzzle_end:
    default count = 0
    $ count +=1
    if count < 1:
        s "Jeez, who's stacking furniture like a weirdo. And let me guess..."
        "I had to shuffle a few of the smaller objects around, but I eventually found a note taped to one of the sides."
        voice "audio/Miscellaneous/Renfield/Narration_3_Renfield.mp3"
        centered """
        Unlike the rest of the abandoned asylum, the basement looked nothing like a psychiatric ward.\nMore like, it had the appearance of some lab used for shady research or experimentation with all the gurney tables and surgical equipment strewn about.\nWhatever this place was used for, it was definitely the reason why the entire facility was shut down.
    	"""
        return
    else:
        return

label froze_crane:
    #Froze the Wisp
    image froze = "Yura_Dungeon/Froze_Wisp.png"
    show froze
    voice "audio/Yuragumi/Froze/Froze1.wav"
    "Froze" "You good, Yura?"
    y "Yeah, I'm good"
    y "Oh Froze, I see that you're from Indonesia. Let me practice my bahasa on you."
    y "Uhhhhm... {rb}awa sudah makan{/rb}{rt}I already ate{/rt}. ah... {rb}saya belum makan{/rb}{rt}I haven't eaten{/rt}. {rb}saya tak lapar{/rb}{rt}I'm not hungry yet{/rt}?"
    voice "audio/Yuragumi/Froze/Froze2.wav"
    "Froze" "Then eat now"
    y "No, not yet. Almost done. Which means like in a few hours."
    voice "audio/Yuragumi/Alicerez/Alicerez4.wav"
    "Alicerez" "Froze says he loves you"
    y "Love you too!"
    voice "audio/Yuragumi/Froze/Froze3.wav"
    "Froze" "Can Yura give me some motivation? Been lazy too long."
    y """Why are you being lazy Froze? Huh?

    Is that why I don't see you during my workout streams?

    Yesterday you said tomorrow.

    Don't let your dreams just be dreams.

    JUST DO IT!
    """

    "Another vision."
    show froze
    "I suppose that means that this wisp is Froze?"
    "The wisp hovered silently over my shoulder."
    "I heard a whisper in my head"
    "?" "Save Yura, bring us together. We will bring back her light."
    $ froze_wisp_crane = True
    $ wisp_count +=1
    if wisp_count == 3:
        jump yura_dungeon_end
    else:
        jump t2

label alicerez_crane:
    show yura:
        zoom 0.6
        xalign 0.1
    show image "Yura_Dungeon/Alicerez.png":
        xalign 0.9
    #Alicerez the Wisp
    y "Oh, hello Alicerez"
    y "Aren't you an RKAngel? How would you like to become a Yuragumi?"
    voice "audio/Yuragumi/Alicerez/Alicerez1.wav"
    "Alicerez" "Sorry Yura, I'm mostly an RKAngel."
    y "That's okay, Yuragumi clan is allowing all types."
    voice "audio/Yuragumi/Alicerez/Alicerez2.wav"
    "Alicerez" "I'll pop in from time to time."
    y "The door is always open Alice!"
    voice "audio/Yuragumi/Alicerez/Alicerez3.wav"
    "Alicerez" "Thanks for the invite, I really appreciate it."
    hide yura
    hide image "Yura_Dungeon/Alicerez.png"

    show image "Yura_Dungeon/Alicerez_Wisp.png"
    s "Alicerez"
    "The mote fluttered around me before settling in front of my face."
    s "You're a lively one aren't you?"
    hide image "Yura_Dungeon/Alicerez_Wisp.png"
    $ alicrez_wisp_crane = True
    $ wisp_count +=1
    if wisp_count == 3:
        jump yura_dungeon_end
    else:
        jump k13
screen renfield_text_1:
    #window hide
    on "show" action Play("voice","audio/Miscellaneous/Renfield/Narration_1_Renfield.mp3")
    frame:
        xalign 0.5
        yalign 0.2
        xsize 640
        has  vbox
        text "My friends and I once had this smart idea to visit an abandoned asylum\nWe did manage to explore the place and capture footage in the process\nHowever, there was one terrifying thing we learned from our experience:\nJust because a place has been abandoned doesn’t mean it would remain 'uninhabited'"

screen renfield_text_3:
    on "show" action Play("voice","audio/Miscellaneous/Renfield/Narration_4_Renfield.mp3")
    frame:
        xalign 0.5
        yalign 0.2
        xsize 640
        ysize 420
        has vbox

        text "As it frantically began clawing at the air in desperation, we realized that we would have to step away from the door to place a barricade which could give the creature a window of opportunity to escape. The two of us then opted to ram the door shut regardless of the creature that was trying to force its way out. Fortunately, it had some sense of pain, so it eventually withdrew and we managed to shut the door while the others toppled the shelf that was previously set up to be used as a barricade. The creature then howled in frustration and pounded at the door. Everybody hurriedly rushed to replace the rest of the blockade that had been put aside. We then quickly left the ungodly building while the creature’s wailing and hammering on the door echoed throughout the place."

label renfield_3:
    if body_found == False:
        hide screen mini_map
        window hide
        "I came across a body on the ground. It looked like it had been there for a while, considering the amount of dust layering on its jacket."
        "A small patch on its arm read 'Renfield', the same name as the one I found on the journal entries."
        "In his outstretched hand was a journal, a few of its pages had been torn."
        "I gently pried it from his hands and began reading."
        $ body_found = True
        show screen renfield_text_3
        $ renpy.pause()
        hide screen renfield_text_3
        window show
        show screen mini_map
        jump o19
    else:
        pass

label yura_dungeon_end:
    hide screen mini_map
    "There's three of them now. The dancing lights flickered, as if they were speaking to one another."
    "I could hear a voice clear in my head."
    "Yuragumi" "Thank you."
    s "Oh. You're welcome."
    "The lights flickered once more and then disappeared into darkness"
    scene black:
        size(1280,720)
    s "Wait!"
    "My protests came too late."
    "I was once again left alone in the darkness."
    s "Come back! I can't see a thing."
    "I got on my hands and knees and began to feel around for my surroundings."
    "I slowly inched my way around in the darkness, until I heard something crunch beneath my knee."
    s "Oww!"
    "Whatever it was felt very hard and bony."
    "I felt around my leg and removed the obtrusion."
    "Correction. {w} It wasn't just bony."
    "It WAS a bone."
    s "AHHHH!"
    "I threw the bone away from me, which made a loud clattering sound that echoed from through the corridor."
    "The darkness answered back with a deranged shriek. The same shriek that the monster had made earlier."
    "I could my body tense up once again."
    "The most I could muster was to cover my mouth and the sound of thumping flesh grew closer."
    "After what seemed like an eternity I could hear it shuffling around nearby."
    show image "Yura_Dungeon/Yura_Monster.png":
        xalign 0.5
        yalign 0.5
        zoom 0.4
    "When the light shone on its face I could clearly see it's sunken gray eyes staring at me."
    "Wait, how was I able to see the monster in the darkness?"
    y "OHAYURA!"
    "A sickening thud could be heard as flesh impacted flesh."
    "The creature recoiled in pain as Yura had punched it"
    hide image "Yura_Dungeon/Yura_Monster.png"
    y "You thought it was over because you got the drop on me? Tsk tsk tsk."
    "In front of me stood a figure I knew all too well."
    s "Yura!"
    y "Hi Shiki!"
    "It was no figure of speech when I say that Yura is my knight in shining armor, as she was the only source of light in here."
    y "Come on, let's get out of here before that things decides to come back."
    "She single handedly pulled me off the ground and back towards the entrance."
    s "Where have you been? I searched all over this place."
    y "Come on Shiki, you know how dullahans are summoned."
    s "Uhhhh"
    "I pondered at the statement for a moment."
    s "I...I don't think I do."
    "Yura stopped in her tracks"
    y "WHAT?!"
    "She quickly turned and faced me."
    y "Did you not watch my debut video Shiki?!"
    s "What?! I did! I promise!"
    y "Mhmmm. A likely story. Quick! What happens to the food I eat! If you watched my debut, you should know!"
    s "UHHHHH...."
    "I panicked"
    y "Shiki..."
    "Yabe."
    jump escape_hub

default g1_blocked = True
default g2_blocked = True
default g3_blocked = True
default h1_blocked = True
default h3_blocked = True

default f5_blocked = False
default f6_blocked = True
default f7_blocked = False

default m8_blocked = False
default m9_blocked = True

default c9_blocked = True
default c10_blocked = True
default c11_blocked = False
default d9_blocked = False
default d10_blocked = False
default d11_blocked = True
default d12_blocked = False
default e9_blocked = False
default e10_blocked = True
default e11_blocked = False
default e12_blocked = False
default f9_blocked = False
default f10_blocked = True
default f11_blocked = True
default f12_blocked = True
default g9_blocked = False
default g10_blocked = False
default g11_blocked = True
default g12_blocked = False
default h9_blocked = False
default h10_blocked = False
default h11_blocked = True
default h12_blocked = True

default q9_blocked = False
default q11_blocked = False
default r9_blocked = False
default r10_blocked = True
default r11_blocked = False
default s9_blocked = False
default s10_blocked = True
default s11_blocked = True
default t9_blocked = False
default t10_blocked = True

label a1:
    $ position = 'a1'
    scene bcr
    menu:
        "Go North":
            jump b1
        "Go East":
            jump a2

label a2:
    $ position = 'a2'
    scene lbr
    menu:
        "Go West":
            jump a1
        "Go East":
            jump a3

label a3:
    $ position = 'a3'
    scene lcr
    menu:
        "Go North":
            jump b3
        "Go West":
            jump a2
        "Go East":
            jump a4

label a4:
    $ position = 'a4'
    scene lbr
    menu:
        "Go West":
            jump a3
        "Go East":
            jump a5
label a5:
    $ position = 'a5'
    scene lbr
    menu:
        "Go West":
            jump a4
        "Go East":
            jump a6

label a6:
    $ position = 'a6'
    scene lbr
    menu:
        "Go West":
            jump a5
        "Go East":
            jump a7

label a7:
    $ position = 'a7'
    scene lbr
    menu:
        "Go West":
            jump a6
        "Go East":
            jump a8

label a8:
    $ position = 'a8'
    scene lbr
    menu:
        "Go West":
            jump a7
        "Go East":
            jump a9

label a9:
    $ position = 'a9'
    scene lbr
    menu:
        "Go West":
            jump a8
        "Go East":
            jump a10

label a10:
    $ position = 'a10'
    scene lbr
    menu:
        "Go West":
            jump a9
        "Go East":
            jump a11

label a11:
    $ position = 'a11'
    scene lbr
    menu:
        "Go West":
            jump a10
        "Go East":
            jump a12

label a12:
    $ position = 'a12'
    scene lbr
    menu:
        "Go West":
            jump a11
        "Go East":
            jump a13

label a13:
    $ position = 'a13'
    scene lbr
    menu:
        "Go West":
            jump a12
        "Go East":
            jump a14

label a14:
    $ position = 'a14'
    scene lcb
    menu:
        "Go North":
            jump b14
        "Go West":
            jump a13
label a16:
    $ position = 'a16'
    scene bbr
    menu:
        "Go East":
            jump a17

label a17:
    $ position = 'a17'
    scene lcb
    menu:
        "Go North":
            jump b17
        "Go West":
            jump a16

label a19:
    $ position = 'a19'
    scene bcb
    menu:
        "Go North":
            jump b19

label b1:
    $ position = 'b1'
    scene bbb
    menu:
        "Go South":
            jump a1

label b3:
    $ position = 'b3'
    scene bcb
    menu:
        "Go North":
            jump c3
        "Go South":
            jump a3

label b14:
    $ position = 'b14'
    scene bcb
    menu:
        "Go North":
            jump c14
        "Go South":
            jump a14

label b17:
    $ position = 'b17'
    scene bcb
    menu:
        "Go North":
            jump c17
        "Go South":
            jump a17

label b19:
    $ position = 'b19'
    scene bcb
    menu:
        "Go North":
            jump c19
        "Go South":
            jump a19

label c3:
    $ position = 'c3'
    scene bcb
    menu:
        "Go North":
            jump d3
        "Go South":
            jump b3

label c6:
    $ position = 'c6'
    scene bcb
    menu:
        "Go North":
            jump d6

label c9:
    $ position = 'c9'
    "There is a shelf blocking my way. It doesn't look like there is a way to move it."
    jump d9

label c10:
    $ position = 'c10'
    "There is a shelf blocking my way. It doesn't look like there is a way to move it."
    return

label c11:
    $ position = 'c11'
    menu:
        "Go North":
            jump d11
        "Go West":
            jump c10
        "Go East":
            jump c12

label c12:
    $ position = 'c12'
    scene lcb
    default c12_found = False
    if crane_count == 0 and c12_found == False:
        """As I aimlessly moved through the endless corridors, I came across an origami crane.

        It was beautifully made, clearly folded with care by whomever made it.

        The mote encircled the crane, as if it wanted to draw attention to it.

        I went to pick up the crane.
        """
        $ crane_count +=1
        $ c12_found = True
        call qtini_crane from _call_qtini_crane
        jump c12
    elif crane_count == 1 and c12_found == False:
        "Another intricate origami crane laid at my feet."
        $ crane_count +=1
        $ inventory_blue_crane == True
        $ renpy.notify ("You have found a blue crane.")
        $ c12_found = True
        jump c12
    elif crane_count == 2 and c12_found == False:
        "There was another crane at my feet. I wonder who's leaving them behind."
        $ crane_count +=1
        $ inventory_yellow_crane == True
        $ renpy.notify ("You have found a yellow crane.")
        $ c12_found = True
        jump c12
    elif crane_count == 3 and c12_found == False:
        "Yet another crane laid on the ground."
        $ crane_count +=1
        $ inventory_red_crane == True
        $ renpy.notify ("You have found a red crane.")
        $ c12_found = True
        jump c12
    menu:
        "Go North" if d12_blocked == True:
            if e12_blocked == True:
                "There is an obstacle in my way. It won't budge."
                jump c12
            if e12_blocked == False:
                "I pushed the obstacle out of my way."
                $ d12_blocked = False
                $ e12_blocked = True
                jump d12
        "Go North" if d12_blocked == False:
            jump d12
        "Go West" if c11_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump c12
        "Go West" if c11_blocked == False:
            jump c11

label c14:
    $ position = 'c14'
    scene bbr
    menu:
        "Go East":
            jump c15
        "Go South":
            jump b14
label c15:
    $ position = 'c15'
    scene lcb
    menu:
        "Go North":
            jump d15
        "Go West":
            jump c14
label c17:
    $ position = 'c17'
    scene bcb
    menu:
        "Go North":
            jump d17
        "Go South":
            jump b17

label c19:
    $ position = 'c19'
    scene bcb
    menu:
        "Go North":
            jump d19
        "Go South":
            jump b19

label d2:
    $ position = 'd2'
    scene bcr
    menu:
        "Go North":
            jump e2
        "Go East":
            jump d3
label d3:
    $ position = 'd3'
    scene lbb
    menu:
        "Go West":
            jump d2
        "Go South":
            jump c3
label d6:
    $ position = 'd6'
    scene bcb
    menu:
        "Go North":
            jump e6
        "Go South":
            jump c6
label d9:
    $ position = 'd9'
    scene bcr
    menu:
        "Go North":
            jump e9
        "Go East":
            jump d10
        "Go South":
            "There is an obstacle in my way. It won't budge."
            jump d9
label d10:
    $ position = 'd10'
    scene lcr
    menu:
        "Go North" if e10_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump d10
        "Go North" if e10_blocked == False:
            jump e10
        "Go West":
            jump d9
        "Go East" if d11_blocked == True:
            "I pushed the obstacle out of my way."
            $ d11_blocked = False
            $ d12_blocked = True
            jump d11
        "Go East" if d11_blocked == False:
            jump d11
        "Go South":
            "There is an obstacle in my way. It won't budge."
            jump d10
label d11:
    $ position = 'd11'
    scene lcr
    menu:
        "Go North" if e11_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump d11
        "Go North" if e11_blocked == False:
            jump e11
        "Go West":
            jump d10
        "Go East" if d12_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump d11
        "Go East" if d12_blocked == False:
            jump d12
        "Go South" if c11_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump d11
        "Go South" if c11_blocked == False:
            jump c11
label d12:
    $ position = 'd12'
    scene lcb
    menu:
        "Go North" if e12_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump d12
        "Go North" if e12_blocked == False:
            jump e12
        "Go West":
            jump d11
        "Go South":
            jump c12
label d15:
    $ position = 'd15'
    scene bcb
    menu:
        "Go North":
            jump e15
        "Go South":
            jump c15
label d17:
    $ position = 'd17'
    scene bcb
    menu:
        "Go North":
            jump e17
        "Go South":
            jump c17
label d19:
    $ position = 'd19'
    scene bcb
    menu:
        "Go North":
            jump e19
        "Go South":
            jump c19

label e2:
    $ position = 'e2'
    scene bcb
    menu:
        "Go North":
            jump f2
        "Go South":
            jump d2
label e5:
    $ position = 'e5'
    scene bcr
    menu:
        "Go North" if f5_blocked == True:
            "There is an obstruction in my path. I can't move it from here."
            jump e5
        "Go North" if f5_blocked == False:
            jump f5
        "Go East":
            jump e6
label e6:
    $ position = 'e6'
    scene lcr
    default slider_start = False
    if slider_start == False:
        "I eventually came across some old furniture that blocked my way forward."
        $ slider_start = True
    menu:
        "Go North" if f6_blocked == True:
            "There is an obstruction in my path. I can't move it from here."
            jump e6
        "Go North" if f6_blocked == False:
            jump f6
        "Go West":
            jump e5
        "Go East":
            jump e7
        "Go South":
            jump d6
label e7:
    $ position = 'e7'
    scene lcb
    menu:
        "Go North" if f7_blocked == True:
            "There is an obstruction in my path. I can't move it from here."
            jump e7
        "Go North" if f7_blocked == False:
            jump f7
        "Go West":
            jump e6
label e9:
    $ position = 'e9'
    scene bcr
    menu:
        "Go North":
            jump f9
        "Go East" if e10_blocked == True:
            "I pushed the obstacle out of my way."
            $ e10_blocked = False
            $ e11_blocked = True
        "Go East" if e10_blocked == False:
            jump e10
        "Go South":
            jump d9
label e10:
    $ position = 'e10'
    scene lcr
    menu:
        "Go North" if f10_blocked == True:
            "There is an obstacle in my path. I tried to push it out of the way but it won't budge."
            "What?"
            "I pushed on it again."
            s "What the heck?"
            s "There's nothing behind it. Why won't it move."
            s "Who made this puzzle?"
            jump e10
        "Go West":
            jump e9
        "Go East" if e11_blocked == True:
            "I pushed the obstacle out of my way."
            $ e11_blocked = False
            $ e12_blocked = True
            jump e11
        "Go East" if e11_blocked == False:
            jump e11
        "Go South":
            jump d10
label e11:
    $ position = 'e11'
    scene lcr
    menu:
        "Go North":
            "There is an obstacle in my way. It won't budge."
            jump e11
        "Go West" if e10_blocked == True:
            "There is an obstacle in my way. Something is preventing it from moving."
            jump e11
        "Go West" if e10_blocked == False:
            jump e10
        "Go East" if e12_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump e11
        "Go East" if e12_blocked == False:
            jump e12
        "Go South" if d11_blocked == True:
            "I pushed the obstacle out of my way."
            $ d11_blocked = False
            $ c11_blocked = True
            jump d11
        "Go South" if d11_blocked == False:
            jump d11
label e12:
    $ position = 'e12'
    scene lcb
    menu:
        "Go North":
            jump f12
        "Go West":
            jump e11
        "Go South":
            jump d12
label e15:
    $ position = 'e15'
    scene bcb
    menu:
        "Go North":
            jump f15
        "Go South":
            jump d15
label e17:
    $ position = 'e17'
    scene bcb
    menu:
        "Go North":
            jump f17
        "Go South":
            jump d17
label e19:
    $ position = 'e19'
    scene bcb
    menu:
        "Go North":
            jump f19
        "Go South":
            jump d19

label f1:
    $ position = 'f1'
    scene bcr
    menu:
        "Go North" if g1_blocked == True:
            "I push the obstacle out of my way."
            $ g1_blocked = False
            $ h1_blocked = True
            jump g1
        "Go North" if g1_blocked == False:
            jump g1
        "Go East":
            jump f2
label f2:
    $ position = 'f2'
    scene lcr
    if sliders_are_fun == True:
        call slider_puzzle_2 from _call_slider_puzzle_2
    menu:
        "Go North" if g2_blocked == True:
            "There is an obstruction in my way."
            jump f2
        "Go North" if g2_blocked == False:
            jump g2
        "Go West":
            jump f1
        "Go East":
            jump f3
        "Go South":
            jump e2
label f3:
    $ position = 'f3'
    scene lcb
    menu:
        "Go North" if g3_blocked == True:
            "I push the obstacle out of my way."
            $ g3_blocked = False
            $ h3_blocked = True
            jump g3
        "Go North" if g3_blocked == False:
            jump g3
        "Go West":
            jump f2
label f5:
    $ position = 'f5'
    scene bbr
    menu:
        "Go East" if f6_blocked == True:
            "I push the obstacle out of my way."
            $ f6_blocked = False
            $ f7_blocked = True
            jump f6
        "Go East" if f6_blocked == False:
            jump f6
        "Go South":
            jump e5
label f6:
    $ position = 'f6'
    scene lcr
    menu:
        "Go North":
            jump g6
        "Go West" if f5_blocked == True:
            "There is an obstruction in my path. I can't move it from here."
            jump f6
        "Go West" if f5_blocked == False:
            jump f5
        "Go East" if f7_blocked == True:
            "There is an obstruction in my path. I can't move it from here."
            jump f6
        "Go East" if f7_blocked == False:
            jump f7
        "Go South":
            jump e6
label f7:
    $ position = 'f7'
    scene lbb
    menu:
        "Go West" if f6_blocked == True:
            "I push the obstacle out of my way."
            $ f6_blocked = False
            $ f5_blocked = True
            jump f6
        "Go South":
            jump e7
label f9:
    $ position = 'f9'
    scene bcr
    menu:
        "Go North":
            jump g9
        "Go East":
            "There is an obstacle blocking my path. It won't budge."
            jump f9
        "Go South":
            jump e9
label f10:
    $ position = 'f10'
    scene lcr
    menu:
        "Go North":
            jump g10
        "Go West":
            jump f9
        "Go East":
            jump f11
        "Go South":
            jump e10
label f11:
    $ position = 'f11'
    scene lcr
    menu:
        "Go North":
            jump g11
        "Go West":
            jump f10
        "Go East":
            jump f12
        "Go South":
            jump e11
label f12:
    $ position = 'f12'
    scene lcb
    menu:
        "Go North":
            jump g12
        "Go West":
            jump f11
        "Go South":
            jump e12
label f15:
    $ position = 'f15'
    scene bcr
    menu:
        "Go North":
            jump g15
        "Go East":
            jump f16
        "Go South":
            jump e15
label f16:
    $ position = 'f16'
    scene lbr
    menu:
        "Go West":
            jump f15
        "Go East":
            jump f17
label f17:
    $ position = 'f17'
    scene lcr
    menu:
        "Go North":
            jump g17
        "Go West":
            jump f16
        "Go East":
            jump f18
        "Go South":
            jump e17
label f18:
    $ position = 'f18'
    scene lbr
    menu:
        "Go West":
            jump f17
        "Go East":
            jump f19
label f19:
    $ position = 'f19'
    scene lcb
    menu:
        "Go North":
            jump g19
        "Go West":
            jump f18
        "Go South":
            jump e19

label g1:
    $ position = 'g1'
    scene bcr
    menu:
        "Go North" if h1_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump g1
        "Go North" if h1_blocked == False:
            jump h1
        "Go East" if g2_blocked == True:
            if g3_blocked == True:
                "There is an obstacle in my way. It won't budge."
                jump g1
            if g3_blocked == False:
                "I pushed the block out of my way."
                $ g2_blocked = False
                $ g3_blocked = True
                jump g2
        "Go East" if g2_blocked == False:
            jump g2
        "Go South":
            jump f1
label g2:
    $ position = 'g2'
    scene lcr
    menu:
        "Go North":
            jump h2
        "Go West" if g1_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump g2
        "Go West" if g1_blocked == False:
            jump g1
        "Go East" if g3_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump g2
        "Go East" if g3_blocked == False:
            jump g3
        "Go South":
            jump f2
label g3:
    $ position = 'g3'
    scene lcb
    menu:
        "Go North" if h3_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump g3
        "Go North" if h3_blocked == False:
            jump h3
        "Go West" if g2_blocked == True:
            "I pushed the obstacle out of my way."
            $ g2_blocked = False
            $ g1_blocked = True
            jump g2
        "Go West" if g2_blocked == False:
            jump g2
        "Go South":
            jump f3
label g6:
    $ position = 'g6'
    scene bcb
    menu:
        "Go North":
            jump h6
        "Go South":
            jump f6
label g9:
    $ position = 'g9'
    scene bcr
    menu:
        "Go North":
            "There is an obstacle blocking my path. It won't budge."
            jump g9
        "Go East":
            jump g10
        "Go South":
            jump f9
label g10:
    $ position = 'g10'
    scene lcr
    menu:
        "Go North":
            jump h10
        "Go West":
            jump g9
        "Go East":
            "There is an obstacle blocking my path. It won't budge."
            jump g10
        "Go South":
            "There is an obstacle blocking my path. It won't budge."
            jump g10
label g11:
    $ position = 'g11'
    scene lcr
    menu:
        "Go North":
            jump h11
        "Go West":
            jump g10
        "Go East":
            jump g12
        "Go South":
            jump f11
label g12:
    $ position = 'g12'
    scene lcb
    menu:
        "Go North":
            jump h12
        "Go West":
            jump g11
        "Go South":
            jump f12
label g15:
    $ position = 'g15'
    scene bcb
    menu:
        "Go North":
            jump h15
        "Go South":
            jump f15
label g17:
    $ position = 'g17'
    scene bcb
    menu:
        "Go North":
            jump h17
        "Go South":
            jump f17
label g19:
    $ position = 'g19'
    scene bcb
    menu:
        "Go North":
            jump h19
        "Go South":
            jump f19

label h1:
    $ position = 'h1'
    scene bbr
    menu:
        "Go East":
            jump h2
        "Go South":
            jump g1
label h2:
    $ position = 'h2'
    scene lbr
    default h2_found = False
    if crane_count == 0 and h2_found == False:
        "As I aimlessly moved through the endless corridors, I came across an origami crane."
        "It was beautifully made, clearly folded with care by whomever made it."
        "The mote encircled the crane, as if it wanted to draw attention to it."
        "I went to pick up the crane."
        $ crane_count +=1
        $ h2_found = True
        call qtini_crane from _call_qtini_crane_3
        jump h2
    elif crane_count == 1 and h2_found == False:
        "Another intricate origami crane laid at my feet."
        $ crane_count +=1
        $ inventory_blue_crane = True
        $ renpy.notify ("You have found a blue crane.")
        $ h2_found = True
        jump h2
    elif crane_count == 2 and h2_found == False:
        "There was another crane at my feet. I wonder who's leaving them behind."
        $ crane_count +=1
        $ inventory_yellow_crane = True
        $ renpy.notify ("You have found a yellow crane.")
        $ h2_found = True
        jump h2
    elif crane_count == 3 and h2_found == False:
        "Yet another crane laid on the ground."
        $ crane_count +=1
        $ inventory_red_crane = True
        $ renpy.notify ("You have found a red crane.")
        $ h2_found = True
        jump h2
    menu:
        "Go West":
            "The way is blocked."
            jump h2
        "Go East":
            "The way is blocked."
            jump h2
        "Go South":
            jump g2
label h3:
    $ position = 'h3'
    scene lbb
    menu:
        "Go West":
            jump h2
        "Go South":
            jump g3
label h6:
    $ position = 'h6'
    scene bcb
    menu:
        "Go North":
            jump i6
        "Go South":
            jump g6
label h9:
    $ position = 'h9'
    scene bbr
    menu:
        "Go East":
            jump h10
        "Go South":
            jump g9
label h10:
    $ position = 'h10'
    scene lbr
    menu:
        "Go West":
            "There is an obstacle blocking my path. It won't budge."
            jump h10
        "Go East":
            jump h11
        "Go South":
            jump g10
label h11:
    $ position = 'h11'
    scene lbr
    menu:
        "Go West" if h10_blocked == True:
            "I pushed the obstacle out of my way"
            $ h10_blocked = False
            $ h9_blocked = True
            jump h10
        "Go West" if h10_blocked == False:
            jump h10
        "Go East":
            jump h12
        "Go South":
            "There is an obstacle blocking my path. It won't budge."
            jump h11
label h12:
    $ position = 'h12'
    scene lcb
    menu:
        "Go North":
            jump i12
        "Go West" if h11_blocked == True:
            "I pushed the obstacle out of my way"
            $ h11_blocked = False
            $ h10_blocked = True
            jump h11
        "Go West" if h11_blocked == False:
            jump h11
        "Go South" if g12_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump h12
        "Go South" if g12_blocked == False:
            jump g12
label h15:
    $ position = 'h15'
    scene bcb
    menu:
        "Go North":
            jump i15
        "Go South":
            jump g15
label h17:
    $ position = 'h17'
    scene bcb
    menu:
        "Go North":
            jump i17
        "Go South":
            jump g17
label h19:
    $ position = 'h19'
    scene bcb
    menu:
        "Go North":
            jump i19
        "Go South":
            jump g19
label i6:
    $ position = 'i6'
    scene bcb
    menu:
        "Go North":
            jump j6
        "Go South":
            jump h6
label i12:
    $ position = 'i12'
    scene bbr
    if sliders_are_fun == True:
        call slider_puzzle_2 from _call_slider_puzzle_2_1
    elif sliders_are_fun == False:
        call slider_puzzle_end from _call_slider_puzzle_end
    menu:
        "Go East":
            jump i13
        "Go South" if h12_blocked == True:
            "I pushed the obstacle out of my way."
            $ h12_blocked = False
            $ g12_blocked = True
            jump h12
        "Go South" if h12_blocked == False:
            jump h12
label i13:
    $ position = 'i13'
    scene lcr
    menu:
        "Go North":
            jump j13
        "Go West":
            jump i12
        "Go East":
            jump i14
label i14:
    $ position = 'i14'
    scene lbr
    menu:
        "Go West":
            jump i13
        "Go East":
            jump i15
label i15:
    $ position = 'i15'
    scene lbb
    menu:
        "Go West":
            jump i14
        "Go South":
            jump h15
label i17:
    $ position = 'i17'
    scene bcb
    menu:
        "Go North":
            jump j17
        "Go South":
            jump h17
label i19:
    $ position = 'i19'
    scene bcb
    menu:
        "Go North":
            jump j19
        "Go South":
            jump h19

label j1:
    $ position = 'j1'
    scene bcb
    default j1_found = False
    if crane_count == 0 and j1_found == False:
        """As I aimlessly moved through the endless corridors, I came across an origami crane.

        It was beautifully made, clearly folded with care by whomever made it.

        The mote encircled the crane, as if it wanted to draw attention to it.

        I went to pick up the crane.
        """
        $ crane_count +=1
        $ j1_found = True
        call qtini_crane from _call_qtini_crane_2
        jump j1
    elif crane_count == 1 and j1_found == False:
        "Another intricate origami crane laid at my feet."
        $ crane_count +=1
        $ inventory_blue_crane == True
        $ renpy.notify ("You have found a blue crane.")
        $ j1_found = True
        jump j1
    elif crane_count == 2 and j1_found == False:
        "There was another crane at my feet. I wonder who's leaving them behind."
        $ crane_count +=1
        $ inventory_yellow_crane == True
        $ renpy.notify ("You have found a yellow crane.")
        $ j1_found = True
        jump j1
    elif crane_count == 3 and j1_found == False:
        "Yet another crane laid on the ground."
        $ crane_count +=1
        $ inventory_red_crane == True
        $ renpy.notify ("You have found a red crane.")
        $ j1_found = True
        jump j1
    menu:
        "Go North":
            jump k1
label j3:
    $ position = 'j3'
    scene bcr
    menu:
        "Go North":
            jump k3
        "Go East":
            jump j4
label j4:
    $ position = 'j4'
    scene lcr
    menu:
        "Go North":
            jump k4
        "Go West":
            jump j3
        "Go East":
            jump j5
label j5:
    $ position = 'j5'
    scene lcr
    menu:
        "Go North":
            jump k5
        "Go West":
            jump j4
        "Go East":
            jump j6
label j6:
    $ position = 'j6'
    scene lcr
    menu:
        "Go North":
            jump k6
        "Go West":
            jump j5
        "Go East":
            jump j7
        "Go South":
            jump i6
label j7:
    $ position = 'j7'
    scene lcr
    menu:
        "Go North":
            jump k7
        "Go West":
            jump j6
        "Go East":
            jump j8
label j8:
    $ position = 'j8'
    scene lcr
    menu:
        "Go North":
            jump k8
        "Go West":
            jump j7
        "Go East":
            jump j9
label j9:
    $ position = 'j9'
    scene lcb
    menu:
        "Go North":
            jump k9
        "Go West":
            jump j8
label j13:
    $ position = 'j13'
    scene bcb
    menu:
        "Go North":
            jump k13
        "Go South":
            jump i13
label j17:
    $ position = 'j17'
    scene bcb
    menu:
        "Go North":
            jump k17
        "Go South":
            jump i17
label j19:
    $ position = 'j19'
    scene bcb
    menu:
        "Go North":
            jump k19
        "Go South":
            jump i19

label k1:
    $ position = 'k1'
    scene bcb
    menu:
        "Go North":
            jump l1
        "Go South":
            jump j1
label k3:
    $ position = 'k3'
    scene bcr
    menu:
        "Go North":
            jump l4
        "Go East":
            jump k5
        "Go South":
            jump j4
label k4:
    $ position = 'k4'
    scene lcr
    menu:
        "Go North":
            jump l4
        "Go West":
            jump k3
        "Go East":
            jump k5
        "Go South":
            jump j4
label k5:
    $ position = 'k5'
    scene lcr
    menu:
        "Go North":
            jump l5
        "Go West":
            jump l4
        "Go East":
            jump l6
        "Go South":
            jump j5
label k6:
    $ position = 'k6'
    scene lcr
    menu:
        "Go North":
            jump l6
        "Go West":
            jump k5
        "Go East":
            jump k7
        "Go South":
            jump j6
label k7:
    $ position = 'k7'
    scene lcr
    menu:
        "Go North":
            jump l7
        "Go West":
            jump k6
        "Go East":
            jump k8
        "Go South":
            jump j7
label k8:
    $ position = 'k8'
    scene lcr
    menu:
        "Go North":
            jump l8
        "Go West":
            jump k7
        "Go East":
            jump k9
        "Go South":
            jump j8
label k9:
    $ position = 'k9'
    scene lcb
    menu:
        "Go North":
            jump l9
        "Go West":
            jump k8
        "Go South":
            jump j9
label k13:
    $ position = 'k13'
    scene bbb
    default alicerez_wisp_found = False
    default alicerez_wisp_crane = False
    if alicerez_wisp_found == False and alicerez_wisp_crane == False:
        "Another wisp idling around. Maybe another crane is needed?"

    menu:
        "Offer a crane" if alicerez_wisp_crane == False:
            "I held out a crane to the mote."
            if inventory_yellow_crane == True:
                jump alicerez_crane
            else:
                "It doesn't respond."
                jump k13
        "Go South":
            jump j13
label k17:
    $ position = 'k17'
    scene bcb
    menu:
        "Go North":
            jump l17
        "Go South":
            jump j17
label k19:
    $ position = 'k19'
    scene bcb
    menu:
        "Go North":
            jump l19
        "Go South":
            jump j19

label l1:
    $ position = 'l1'
    scene bcb
    menu:
        "Go North":
            jump m1
        "Go South":
            jump k1
label l3:
    $ position = 'l3'
    scene bcr
    menu:
        "Go North":
            jump m3
        "Go East":
            jump l4
        "Go South":
            jump k3
label l4:
    $ position = 'l4'
    scene lcr
    menu:
        "Go North":
            jump m4
        "Go West":
            jump l3
        "Go East":
            jump l5
        "Go South":
            jump k4
label l5:
    $ position = 'l5'
    scene lcr
    menu:
        "Go North":
            jump m5
        "Go West":
            jump l4
        "Go East":
            jump l6
        "Go South":
            jump k5
label l6:
    $ position = 'l6'
    scene lcr
    menu:
        "Go North":
            jump m6
        "Go West":
            jump l5
        "Go East":
            jump l7
        "Go South":
            jump k6
label l7:
    $ position = 'l7'
    scene lcr
    menu:
        "Go North":
            jump m7
        "Go West":
            jump l6
        "Go East":
            jump l8
        "Go South":
            jump k7
label l8:
    $ position = 'l8'
    scene lcr
    menu:
        "Go North":
            jump m8
        "Go West":
            jump l7
        "Go East":
            jump l9
        "Go South":
            jump k8
label l9:
    $ position = 'l9'
    scene lcb
    menu:
        "Go North":
            jump m9
        "Go West":
            jump l8
        "Go South":
            jump k9
label l17:
    $ position = 'l17'
    scene bcb
    menu:
        "Go North":
            jump m17
        "Go South":
            jump k17
label l19:
    $ position = 'l19'
    scene bcb
    menu:
        "Go North":
            jump m19
        "Go South":
            jump k19

label m1:
    $ position = 'm1'
    scene bcb
    menu:
        "Go North":
            jump n1
        "Go South":
            jump l1
label m3:
    $ position = 'm3'
    scene bbr
    menu:
        "Go East":
            jump m4
        "Go South":
            jump l4
label m4:
    $ position = 'm4'
    scene lbr
    menu:
        "Go West":
            jump m3
        "Go East":
            jump m5
        "Go South":
            jump l4
label m5:
    $ position = 'm5'
    scene lbr
    menu:
        "Go West":
            jump m4
        "Go East":
            jump m6
        "Go South":
            jump l5
label m6:
    $ position = 'm6'
    scene lcr
    menu:
        "Go North":
            jump n6
        "Go West":
            jump m5
        "Go East":
            jump m7
        "Go South":
            jump l6
label m7:
    $ position = 'm7'
    scene lbr
    menu:
        "Go West":
            jump m6
        "Go East" if m8_blocked == False:
            "There is an obstacle blocking my path. It doesn't seem to move, no matter how much I push it."
        "Go East" if m8_blocked == False:
            jump m8
        "Go South":
            jump l7
label m8:
    $ position = 'm8'
    scene lbr
    menu:
        "Go West":
            jump m7
        "Go East" if m9_blocked == True:
            "There is an obstacle blocking my path. There doesn't seem to be a way to move it from here."
            jump m8
        "Go South":
            jump l4
label m9:
    $ position = 'm9'
    scene lbr
    menu:
        "Go West" if m8_blocked == True:
            "There is an obstacle blocking my path. It doesn't seem to move, no matter how much I push it."
            jump m9
        "Go East":
            jump m10
        "Go South":
            jump l9
label m10:
    $ position = 'm10'
    scene lbr
    menu:
        "Go West" if m9_blocked == True:
            "I push the obstacle out of the way."
            $ m9_blocked = False
            $ m8_blocked = True
            jump m9
        "Go East":
            jump m11
label m11:
    $ position = 'm11'
    scene lbr
    menu:
        "Go West":
            jump m10
        "Go East":
            jump m12
label m12:
    $ position = 'm12'
    scene lbr
    menu:
        "Go West":
            jump m11
        "Go East":
            jump m13
label m13:
    $ position = 'm13'
    scene lbr
    menu:
        "Go West":
            jump m12
        "Go East":
            jump m14
label m14:
    $ position = 'm14'
    scene lbr
    menu:
        "Go West":
            jump m13
        "Go East":
            jump m15
label m15:
    $ position = 'm15'
    scene lbr
    menu:
        "Go West":
            jump m14
        "Go East":
            jump m16
label m16:
    $ position = 'm16'
    scene lbr
    menu:
        "Go West":
            jump m15
        "Go East":
            jump m17
label m17:
    $ position = 'm17'
    scene lbb
    menu:
        "Go West":
            jump m16
        "Go South":
            jump l17
label m19:
    $ position = 'm19'
    scene bcb
    menu:
        "Go North":
            jump n19
        "Go South":
            jump l19

label n1:
    $ position = 'n1'
    scene bcb
    menu:
        "Go North":
            jump o1
        "Go South":
            jump m1
label n6:
    $ position = 'n6'
    scene bcb
    menu:
        "Go North":
            jump o6
        "Go South":
            jump m6

label n19:
    $ position = 'n19'
    scene bcb
    menu:
        "Go North":
            jump o19
        "Go South":
            jump m19

label o1:
    $ position = 'o1'
    scene bcr
    menu:
        "Go East":
            jump o2
        "Go South":
            jump n1
label o2:
    $ position = 'o2'
    scene lbr
    menu:
        "Go West":
            jump o1
        "Go East":
            jump o3
label o3:
    $ position = 'o3'
    scene lbr
    menu:
        "Go West":
            jump o2
        "Go East":
            jump o4
label o4:
    $ position = 'o4'
    scene lbr
    menu:
        "Go West":
            jump o3
        "Go East":
            jump o5
label o5:
    $ position = 'o5'
    scene lbr
    menu:
        "Go West":
            jump o4
        "Go East":
            jump o6
label o6:
    $ position = 'o6'
    scene lcr
    menu:
        "Go North":
            jump p6
        "Go West":
            jump o5
        "Go East":
            jump o7
        "Go South":
            jump n6
label o7:
    $ position = 'o7'
    scene lbr
    menu:
        "Go West":
            jump o6
        "Go East":
            jump o8
label o8:
    $ position = 'o8'
    scene lbr
    menu:
        "Go West":
            jump o7
        "Go East":
            jump o9
label o9:
    $ position = 'o9'
    scene lbr
    menu:
        "Go West":
            jump o8
        "Go East":
            jump o10
label o10:
    $ position = 'o10'
    scene lbr
    menu:
        "Go West":
            jump o9
        "Go East":
            jump o11
label o11:
    $ position = 'o11'
    scene lbr
    menu:
        "Go West":
            jump o10
        "Go East":
            jump o12
label o12:
    $ position = 'o12'
    scene lbr
    menu:
        "Go West":
            jump o11
        "Go East":
            jump o13
label o13:
    $ position = 'o13'
    scene lbr
    menu:
        "Go West":
            jump o12
        "Go East":
            jump o14
label o14:
    $ position = 'o14'
    scene lbr
    menu:
        "Go West":
            jump o13
        "Go East":
            jump o15
label o15:
    $ position = 'o15'
    scene lbr
    menu:
        "Go West":
            jump o14
        "Go East":
            jump o16
label o16:
    $ position = 'o16'
    scene lbr
    menu:
        "Go West":
            jump o15
        "Go East":
            jump o17
label o17:
    $ position = 'o17'
    scene lbr
    menu:
        "Go West":
            jump o16
        "Go East":
            jump o18
label o18:
    $ position = 'o18'
    scene lbr
    menu:
        "Go West":
            jump o17
        "Go East":
            jump o19
label o19:
    $ position = 'o19'
    scene lcb
    default body_found = False
    if body_found == False:
        jump renfield_3
    menu:
        "Go North":
            jump p19
        "Go West":
            jump o18
        "Go South":
            jump n19

label p6:
    $ position = 'p6'
    scene bcb
    menu:
        "Go North":
            jump q6
        "Go South":
            jump o6
label p19:
    $ position = 'p19'
    scene bcb
    menu:
        "Go North":
            jump q19
        "Go South":
            jump o19

label q1:
    $ position = 'q1'
    scene bcr
    menu:
        "Go North":
            jump r1
        "Go East":
            jump q2
label q2:
    $ position = 'q2'
    scene lcr
    menu:
        "Go North":
            jump r2
        "Go West":
            jump q1
        "Go East":
            jump q3
label q3:
    $ position = 'q3'
    scene lcb
    menu:
        "Go North":
            jump r3
        "Go West":
            jump q2
label q5:
    $ position = 'q5'
    scene bcr
    menu:
        "Go North":
            jump r5
        "Go East":
            jump q6
label q6:
    $ position = 'q6'
    scene lcr
    menu:
        "Go North":
            jump r6
        "Go West":
            jump q5
        "Go East":
            jump q7
        "Go South":
            jump p6
label q7:
    $ position = 'q7'
    scene lcb
    menu:
        "Go North":
            jump r7
        "Go West":
            jump q6
label q9:
    $ position = 'q9'
    scene bcr
    menu:
        "Go North":
            jump r9
        "Go East":
            jump q10
label q10:
    $ position = 'q10'
    scene lcr
    default q10_found = False
    if crane_count == 0 and q10_found == False:
        "As I aimlessly moved through the endless corridors, I came across an origami crane."
        "It was beautifully made, clearly folded with care by whomever made it."
        "The mote encircled the crane, as if it wanted to draw attention to it."
        "I went to pick up the crane."
        $ crane_count +=1
        $ q10_found = True
        call qtini_crane from _call_qtini_crane_1
        jump q10
    elif crane_count == 1 and q10_found == False:
        "Another intricate origami crane laid at my feet."
        $ crane_count +=1
        $ inventory_blue_crane = True
        $ renpy.notify ("You have found a blue crane.")
        $ q10_found = True
        jump q10
    elif crane_count == 2 and q10_found == False:
        "There was another crane at my feet. I wonder who's leaving them behind."
        $ crane_count +=1
        $ inventory_yellow_crane = True
        $ renpy.notify ("You have found a yellow crane.")
        $ q10_found = True
        jump q10
    elif crane_count == 3 and q10_found == False:
        "Yet another crane laid on the ground."
        $ crane_count +=1
        $ inventory_red_crane = True
        $ renpy.notify ("You have found a red crane.")
        $ q10_found = True
        jump q10
    menu:
        "Go North":
            jump r10
        "Go West" if q9_blocked == True:
            "There is an obstacle in my way. It won't budge."
        "Go West" if q9_blocked == False:
            jump q9
        "Go East" if q11_blocked == True:
            "There is an obstacle in my way. It won't budge."
            jump q10
        "Go East" if q11_blocked == False:
            jump q11
label q11:
    $ position = 'q11'
    scene lcb
    menu:
        "Go North":
            jump r11
        "Go West":
            jump q10
label q19:
    $ position = 'q19'
    scene bcb
    menu:
        "Go North":
            jump r19
        "Go South":
            jump p19

label r1:
    $ position = 'r1'
    scene bcr
    menu:
        "Go North":
            jump s1
        "Go East":
            jump r2
        "Go South":
            jump q1
label r2:
    $ position = 'r2'
    scene lcr
    menu:
        "Go North":
            jump s2
        "Go West":
            jump r1
        "Go East":
            jump r3
        "Go South":
            jump q2
label r3:
    $ position = 'r3'
    scene lcr
    menu:
        "Go North":
            jump s3
        "Go West":
            jump r2
        "Go East":
            jump r4
        "Go South":
            jump q3
label r4:
    $ position = 'r4'
    scene lbr
    menu:
        "Go West":
            jump r3
        "Go East":
            jump r5
label r5:
    $ position = 'r5'
    scene lcr
    menu:
        "Go North":
            jump s5
        "Go West":
            jump r4
        "Go East":
            jump r6
        "Go South":
            jump q5
label r6:
    $ position = 'r6'
    scene lcr
    menu:
        "Go North":
            jump s6
        "Go West":
            jump r5
        "Go East":
            jump r7
        "Go South":
            jump q6
label r7:
    $ position = 'r7'
    menu:
        "Go North":
            jump s7
        "Go West":
            jump r6
        "Go South":
            jump q7
label r9:
    $ position = 'r9'
    scene bcr
    menu:
        "Go North" if s9_blocked == True:
            if t9_blocked == True:
                "There is an obstacle blocking the way. It won't budge."
                jump r9
            if t9_blocked == False:
                "I pushed the obstacle out of the way."
                $ s9_blocked = False
                $ t9_blocked = True
                jump s9
        "Go North" if s9_blocked == False:
                jump s9
        "Go East" if r11_blocked == True:
            jump r10
        "Go South":
            jump q9
label r10:
    $ position = 'r10'
    scene lcr
    menu:
        "Go North" if s10_blocked == True:
            if t10_blocked == True:
                "There is an obstacle blocking the way. It won't budge."
                jump r10
            if t10_blocked == False:
                "I pushed the obstacle out of the way."
                $ s10_blocked = False
                $ t10_blocked = True
                jump s10
        "Go North" if s10_blocked == False:
            jump s10
        "Go West" if r9_blocked == True:
            "There is an obstacle blocking the way. It won't budge."
            jump r10
        "Go West" if r9_blocked == False:
            jump r9
        "Go East":
            jump r11
        "Go South":
            jump q10
label r11:
    $ position = 'r11'
    scene lcb
    menu:
        "Go North":
            jump s11
        "Go West" if r10_blocked == True:
            "I pushed the obstacle out of my way."
            $ r10_blocked = False
            $ r9_blocked = True
            jump r10
        "Go West" if r10_blocked == False:
            jump r10
        "Go South" if q11_blocked == True:
            "There is an obstacle blocking the way. It won't budge."
            jump r11
        "Go South" if q11_blocked == False:
            jump q11
label r19:
    $ position = 'r19'
    scene bcb
    menu:
        "Go North":
            jump s19
        "Go South":
            jump q19

label s1:
    $ position = 's1'
    scene bcr
    menu:
        "Go North":
            jump t1
        "Go East":
            jump s2
        "Go South":
            jump r1
label s2:
    $ position = 's2'
    scene lcr
    menu:
        "Go North":
            jump t2
        "Go West":
            jump s1
        "Go East":
            jump s3
        "Go South":
            jump r2
label s3:
    $ position = 's3'
    scene lcb
    menu:
        "Go North":
            jump t3
        "Go West":
            jump s2
        "Go South":
            jump r3
label s5:
    $ position = 's5'
    scene bbr
    menu:
        "Go East":
            jump s6
        "Go South":
            jump r6
label s6:
    $ position = 's6'
    scene lbr
    menu:
        "Go West":
            jump s5
        "Go East":
            jump s7
        "Go South":
            jump r6
label s7:
    $ position = 's7'
    scene lbb
    menu:
        "Go West":
            jump s6
        "Go South":
            jump r7
label s9:
    $ position = 's9'
    scene bcr
    menu:
        "Go North" if t9_blocked == True:
            "There is an obstacle blocking the path. It won't budge."
            jump s9
        "Go North" if t9_blocked == False:
            jump t9
        "Go East" if s10_blocked == True:
            if s11_blocked == True:
                "There is an obstacle blocking the path. It won't budge."
                jump s9
            if s11_blocked == False:
                "I pushed the obstacle out of the way."
                $ s10_blocked = False
                $ s11_blocked = True
                jump s10
        "Go East" if s10_blocked == False:
            jump s10
        "Go South":
            jump r9
label s10:
    $ position = 's10'
    scene lcr
    menu:
        "Go North" if t10_blocked == True:
            "There is an obstacle blocking the path. It won't budge."
            jump s10
        "Go North" if t10_blocked == False:
            jump t10
        "Go West" if s9_blocked == True:
            "There is an obstacle blocking the path. It won't budge."
            jump s10
        "Go West" if s9_blocked == False:
            jump s9
        "Go East" if s11_blocked == True:
            "There is an obstacle blocking the path. It won't budge."
            jump s10
        "Go East" if s11_blocked == False:
            jump s11
        "Go South" if r10_blocked == True:
            "There is an obstacle blocking the path. It won't budge."
            jump s10
        "Go South" if r10_blocked == False:
            jump r10
label s11:
    $ position = 's11'
    scene lcb
    menu:
        "Go North":
            jump t11
        "Go West" if s10_blocked == True:
            "I pushed the obstacle out of the way."
            $ s10_blocked = False
            $ s9_blocked = True
            jump s10
        "Go West" if s10_blocked == False:
            jump s10
        "Go South" if r11_blocked == True:
            "I pushed the obstacle out of the way."
            $ r11_blocked = False
            $ q11_blocked = True
            jump r11
        "Go South" if r11_blocked == False:
            jump r11
label s19:
    $ position = 's19'
    scene bcb
    menu:
        "Go North":
            jump t19
        "Go South":
            jump r19

label t1:
    $ position = 't1'
    scene bbr
    menu:
        "Go East":
            jump t2
        "Go South":
            jump s1
label t2:
    $ position = 't2'
    scene lbr
    default froze_wisp_found = False
    default froze_wisp_crane = False
    if froze_wisp_found == False:
        "As I explored the place more I came across another mote. It was wandering in the same area aimlessly"

        s "Oh, another one of you guys?"
        s "Is this your friend Qtini?"
        "The mote that had been lighting my path offered no response"
        "Although I tried to get the new mote to come with me, it still continued to wander."
        "Maybe if I show it the right item? The other mote responded to this paper crane"
        $ froze_wisp_found = True
        jump t2
    if froze_wisp_found == True and froze_wisp_crane == False:
        "The mote of light wandered aimlessly."

    menu:
        "Offer a crane" if froze_wisp_crane == False:
            "I held out a crane to the mote."
            if inventory_blue_crane == True:
                jump froze_crane
            else:
                "It isn't responding"
                jump t2
        "Go West":
            jump t1
        "Go East":
            jump t3
        "Go South":
            jump s2
label t3:
    $ position = 't3'
    scene lbb
    menu:
        "Go West":
            jump t2
        "Go South":
            jump s3
label t9:
    $ position = 't9'
    scene bbr
    menu:
        "Go East":
            jump t10
        "Go South":
            jump s9
label t10:
    $ position = 't10'
    scene lbr
    menu:
        "Go West" if t9_blocked == True:
            "There is an obstacle in the way. It doesn't budge."
            jump t10
        "Go West" if t9_blocked == False:
            jump t9
        "Go East":
            jump t11
        "Go South" if s10_blocked == True:
            if r10_blocked == True:
                "There is an obstacle in the way. It doesn't budge."
                jump t10
            if r10_blocked == False:
                "I pushed the obstacle out of my way."
                $ s10_blocked == False
                $ r10_blocked == True
                jump s10
        "Go South" if s10_blocked == False:
            jump s10

label t11:
    $ position = 't11'
    scene lbr
    if sliders_are_fun == True:
        call slider_puzzle_2 from _call_slider_puzzle_2_2
    elif sliders_are_fun == False:
        call slider_puzzle_end from _call_slider_puzzle_end_1
    menu:
        "Go West" if t10_blocked == True:
            "I pushed the obstacle out of my way."
            $ t10_blocked = False
            $ t9_blocked = True
            jump t10
        "Go West" if t10_blocked == False:
            jump t10
        "Go East":
            jump t12
        "Go South" if s11_blocked == True:
            "I pushed the obstacle out of my way."
            $ s11_blocked = False
            $ r11_blocked = True
            jump s11
label t12:
    $ position = 't12'
    scene lbr
    menu:
        "Go West":
            jump t11
        "Go East":
            jump t13
label t13:
    $ position = 't13'
    scene lbr
    menu:
        "Go West":
            jump t12
        "Go East":
            jump t14
label t14:
    $ position = 't14'
    scene lbr
    menu:
        "Go West":
            jump t13
        "Go East":
            jump t15
label t15:
    $ position = 't15'
    scene lbr
    menu:
        "Go West":
            jump t14
        "Go East":
            jump t16
label t16:
    $ position = 't16'
    scene lbr
    menu:
        "Go West":
            jump t15
        "Go East":
            jump t17
label t17:
    $ position = 't17'
    scene lbr
    menu:
        "Go West":
            jump t16
        "Go East":
            jump t18
label t18:
    $ position = 't18'
    scene lbr
    menu:
        "Go West":
            jump t17
        "Go East":
            jump t19
label t19:
    $ position = 't19'
    scene lbb
    menu:
        "Go West":
            jump t18
        "Go South":
            jump s19
