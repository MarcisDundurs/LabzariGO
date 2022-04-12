
sar1 = []

nam1 = str(input('Ievadiet jūsu spēles segvārdu: -  '))
Rwin = str(input('Ievadiet cik raundus jūsu komanda uzvarēja? -  '))
Rloss = str(input('Ievadiet cik raundus pretinieku komanda uzvarēja? -  '))

if Rwin < Rloss:
    result = 'uzvarēja'

elif Rwin > Rloss:
    result = 'zaudēja'

elif Rwin == Rloss:
    result = 'vienādoja rezultātu ar pretiniekiem'

kls1 = float(input('Cik pretinieku nāves tu dabūji? -  '))
dts1 = float(input('Cik reizes tu nomiri ? -  '))
dmg1 = float(input('Cik ievainojuma punktus tu izdarīji pa visu spēli? -  '))
kdr1 = round(kls1/dts1, 2)
adg1 = round(dmg1/float(Rwin)+float(Rloss), 0)

sar1.append(nam1)

sar1.append(kls1)

sar1.append(dts1)

sar1.append(kdr1)

sar1.append(adg1)

print('Spēles rezultāts ir ' + Rwin + ':' + Rloss + ' un jūsu komanda ' + str(result) + '.')

print('Šajā spēlē tu dabuji ' + str(sar1[1]) + ' pretinieku nāves, bet nomiri ' + str(sar1[2]) + ' reizes.')

print('Tavs KDR (Kills to Death Ratio) ir ' + str(sar1[3]) + '.')

print('Tavs ADG (Vidējais ievainojumu punktu skaits visā spēlē) ir ' + str(sar1[4]) + '.')

trpn = str(input('Vai jūs vēlaties turpināt un ievadīt savas komandas '
                 'citu spēlētāju statistikas (Lūdzu atbildiet ar "Jā/Nē")? -  '))

if trpn == "Nē":
    print('Statistikas piefiksēšana ir principā pabeigta.')

elif trpn == "Jā":

    sar2 = []

    nam2 = str(input('Ievadiet jūsu otrā komandas biedra segvārdu: -  '))
    kls2 = float(input('Cik pretinieku nāves ' + nam2 + ' dabūja? -  '))
    dts2 = float(input('Cik reizes ' + nam2 + ' nomira? -  '))
    dmg2 = float(input('Cik ievainojuma punktus ' + nam2 + ' izdarīja pa visu spēli? -  '))
    kdr2 = round(kls2 / dts2, 2)
    adg2 = round(dmg2 / float(Rwin) + float(Rloss), 0)

    sar2.append(nam2)
    sar2.append(kls2)
    sar2.append(dts2)
    sar2.append(kdr2)
    sar2.append(adg2)

    print('Šajā spēlē ' + sar2[0] + ' dabuja ' + str(sar2[1]) + ' pretinieku nāves, bet nomira ' + str(sar2[2]) +
          ' reizes.')

    print(sar2[0] + ' KDR (Kills to Death Ratio) ir ' + str(sar2[3]) + '.')

    print(sar2[0] + ' ADG (Vidējais ievainojumu punktu skaits visā spēlē) ir ' + str(sar2[4]) + '.')

    sar3 = []

    nam3 = str(input('Ievadiet jūsu trešā komandas biedra segvārdu: -  '))
    kls3 = float(input('Cik pretinieku nāves ' + nam3 + ' dabūja? -  '))
    dts3 = float(input('Cik reizes ' + nam3 + ' nomira? -  '))
    dmg3 = float(input('Cik ievainojuma punktus ' + nam3 + ' izdarīja pa visu spēli? -  '))
    kdr3 = round(kls3 / dts3, 2)
    adg3 = round(dmg3 / float(Rwin) + float(Rloss), 0)

    sar3.append(nam3)
    sar3.append(kls3)
    sar3.append(dts3)
    sar3.append(kdr3)
    sar3.append(adg3)

    print('Šajā spēlē ' + sar3[0] + ' dabuja ' + str(sar3[1]) + ' pretinieku nāves, bet nomira ' + str(sar3[2]) +
          ' reizes.')

    print(sar3[0] + ' KDR (Kills to Death Ratio) ir ' + str(sar3[3]) + '.')

    print(sar3[0] + ' ADG (Vidējais ievainojumu punktu skaits visā spēlē) ir ' + str(sar3[4]) + '.')

    sar4 = []

    nam4 = str(input('Ievadiet jūsu ceturtā komandas biedra segvārdu: -  '))
    kls4 = float(input('Cik pretinieku nāves ' + nam4 + ' dabūja? -  '))
    dts4 = float(input('Cik reizes ' + nam4 + ' nomira? -  '))
    dmg4 = float(input('Cik ievainojuma punktus ' + nam4 + ' izdarīja pa visu spēli? -  '))
    kdr4 = round(kls4 / dts4, 2)
    adg4 = round(dmg4 / float(Rwin) + float(Rloss), 0)

    sar4.append(nam4)
    sar4.append(kls4)
    sar4.append(dts4)
    sar4.append(kdr4)
    sar4.append(adg4)

    print('Šajā spēlē ' + sar4[0] + ' dabuja ' + str(sar4[1]) + ' pretinieku nāves, bet nomira ' + str(sar4[2]) +
          ' reizes.')

    print(sar4[0] + ' KDR (Kills to Death Ratio) ir ' + str(sar4[3]) + '.')

    print(sar4[0] + ' ADG (Vidējais ievainojumu punktu skaits visā spēlē) ir ' + str(sar4[4]) + '.')

    sar5 = []

    nam5 = str(input('Ievadiet jūsu piektā komandas biedra segvārdu: -  '))
    kls5 = float(input('Cik pretinieku nāves ' + nam5 + ' dabūja? -  '))
    dts5 = float(input('Cik reizes ' + nam5 + ' nomira? -  '))
    dmg5 = float(input('Cik ievainojuma punktus ' + nam5 + ' izdarīja pa visu spēli? -  '))
    kdr5 = round(kls5 / dts5, 2)
    adg5 = round(dmg5 / float(Rwin) + float(Rloss), 0)

    sar5.append(nam5)
    sar5.append(kls5)
    sar5.append(dts5)
    sar5.append(kdr5)
    sar5.append(adg5)

    print('Šajā spēlē ' + sar5[0] + ' dabuja ' + str(sar5[1]) + ' pretinieku nāves, bet nomira ' + str(sar5[2]) +
          ' reizes.')

    print(sar5[0] + ' KDR (Kills to Death Ratio) ir ' + str(sar5[3]) + '.')

    print(sar5[0] + ' ADG (Vidējais ievainojumu punktu skaits visā spēlē) ir ' + str(sar5[4]) + '.')

    if float(kls1) > float(kls2) > float(kls3) > float(kls4) > float(kls5):
        print('Visvairāk pretinieku nāves dabūja ' + str(nam1) + '.' + str(kls1))
    elif float(kls2) > float(kls1) > float(kls3) > float(kls4) > float(kls5):
        print('Visvairāk pretinieku nāves dabūja ' + str(nam2) + '.' + str(kls2))
    elif float(kls3) > float(kls1) > float(kls2) > float(kls4) > float(kls5):
        print('Visvairāk pretinieku nāves dabūja ' + str(nam3) + '.' + str(kls3))
    elif float(kls4) > float(kls1) > float(kls2) > float(kls3) > float(kls5):
        print('Visvairāk pretinieku nāves dabūja ' + str(nam4) + '.' + str(kls4))
    elif float(kls5) > float(kls1) > float(kls2) > float(kls3) > float(kls4):
        print('Visvairāk pretinieku nāves dabūja ' + str(nam5) + '.' + str(kls5))

    if float(dts1) > float(dts2) > float(dts3) > float(dts4) > float(dts5):
        print('Visvairāk nomira ' + str(nam1) + '.')
    elif float(dts2) > float(dts1) > float(dts3) > float(dts4) > float(dts5):
        print('Visvairāk nomira ' + str(nam2) + '.')
    elif float(dts3) > float(dts1) > float(dts2) > float(dts4) > float(dts5):
        print('Visvairāk nomira ' + str(nam3) + '.')
    elif float(dts4) > float(dts1) > float(dts2) > float(dts3) > float(dts5):
        print('Visvairāk nomira ' + str(nam4) + '.')
    elif float(dts5) > float(dts1) > float(dts2) > float(dts3) > float(dts4):
        print('Visvairāk nomira ' + str(nam5) + '.')

    if float(kdr1) > float(kdr2) > float(kdr3) > float(kdr4) > float(kdr5):
        print('Vislabākais KDR bija ' + str(nam1) + '.')
    elif float(kdr2) > float(kdr1) > float(kdr3) > float(kdr4) > float(kdr5):
        print('Vislabākais KDR bija ' + str(nam2) + '.')
    elif float(kls3) > float(kdr1) > float(kdr2) > float(kdr4) > float(kdr5):
        print('Vislabākais KDR bija ' + str(nam3) + '.')
    elif float(kdr4) > float(kdr1) > float(kdr2) > float(kdr3) > float(kdr5):
        print('Vislabākais KDR bija ' + str(nam4) + '.')
    elif float(kdr5) > float(kdr1) > float(kdr2) > float(kdr3) > float(kdr4):
        print('Vislabākais KDR bija ' + str(nam5) + '.')

    print("Tava komanda sastāvēja no " + sar1[0] + " ; " + sar2[0] + " ; " + sar3[0] + " ; " + sar4[0] + " ; "
          + sar5[0] + " ; ")
