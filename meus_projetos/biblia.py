from tkinter import *
from tkinter import filedialog
import tkinter as tk 

janela = Tk()
janela.title('Biblia Sagrada')
janela.geometry('500x600')
def janela1 ():
    janela1 = Tk()
    janela1.title('Biblia Sagrada')
    janela1.geometry('600x500')
    Canvas = tk.Canvas(janela1,)
    Scrollbar = tk.Scrollbar(janela1, orient='vertical', command=Canvas.yview)
    Scrollbar.pack(side='right', fill='y')
    Label(janela1, text='qual capitulo?', font=('arial', 30), bg='lightblue', anchor='center').pack(fill='x')
    def  ge ():
            janela2 = Tk()
            janela2.title('Biblia sagrada')
            janela2.geometry('535x600')
            def ger1 ():
                janela3 = Tk()
                janela3.title('Biblia Sagrada')
                janela3.geometry('1300x876')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                vers1 = Label(janela3, text='¹ No princípio criou Deus os céus e a terra.', font=('arial', 30), bg='lightblue', anchor='center')
                vers1.grid(row=20, column=20)
                vers1.pack(fill='x') 
                proximo = Button(janela3, text='proximo', command=ger2)
                proximo.pack(side=BOTTOM)
                janela3.mainloop()
            ger1 = Button(janela2, text='VERSICULO: 1', command=ger1)
            ger1.grid(row=0, column=0)
            def ger2 ():
                janela4 = Tk()
                janela4.title('Biblia Sagrada') 
                janela4.geometry('1300x876')
                vers3 = Label(janela4, text='² E a terra era sem forma e vazia; e havia trevas sobre a face do abismo;\n e o Espírito de Deus se movia sobre a face das águas.', font=('arial', 30), bg='lightblue', anchor='center')
                vers3.pack(fill='x')
                janela4.mainloop()
            ger2 = Button(janela2, text='VERSICULO: 2', command=ger2)
            ger2.grid(row=0, column=1)

            def ger3 ():
                janela5 = Tk()
                janela5.title('Biblia Sagrada')
                janela5.geometry('1300x876')
                vers4 = Label(janela5, text='³ E disse Deus: Haja luz; e houve luz.', font=('arial', 30), bg='lightblue', anchor='center')
                vers4.pack(fill='x')
                janela5.mainloop()
            ger3 = Button(janela2, text='VERSICULO: 3', command=ger3)
            ger3.grid(row=0, column=2)
    
            def ger4 ():
                janela6 = Tk()
                janela6.title('Biblia Sagrada')
                janela6.geometry('1300x876')
                vers5 = Label(janela6, text='⁴ E viu Deus que era boa a luz;\n e fez Deus separação entre a luz e as trevas.', font=('arial', 30), bg='lightblue', anchor='center')
                vers5.pack(fill='x')
                janela6.mainloop()
            ger4 = Button(janela2, text='VERSICULO: 4', command=ger4)
            ger4.grid(row=0, column=3)

            def ger5 ():
                janela7 = Tk()
                janela7.title('Biblia Sagrada')
                janela7.geometry('1300x876')
                vers6 = Label(janela7, text='⁵ E Deus chamou à luz Dia; e às trevas chamou Noite.\n E foi a tarde e a manhã, o dia primeiro.', font=('arial', 30), bg='lightblue', anchor='center')
                vers6.pack(fill='x')
                janela7.mainloop()
            ger5 = Button(janela2, text='VERSICULO: 5', command=ger5)
            ger5.grid(row=0, column=4)

            def ger6 ():
                janela8 = Tk()
                janela8.title('Biblia Sagrada')
                janela8.geometry('1300x876')
                vers7 = Label(janela8, text='⁶ E disse Deus: Haja uma expansão no meio das águas,\n e haja separação entre águas e águas.', font=('arial', 30), bg='lightblue', anchor='center')
                vers7.pack(fill='x')
                janela8.mainloop()
            ger6 = Button(janela2, text='VERSICULO: 6', command=ger6)
            ger6.grid(row=0, column=5)

            def ger7 ():
                janela9 = Tk()
                janela9.title('Biblia Sagrada')
                janela9.geometry('1300x876')
                vers8 = Label(janela9, text='⁷ E fez Deus a expansão, e fez separação\n entre as águas que estavam debaixo \nda expansão e as águas que estavam sobre a expansão; e assim foi.', font=('arial', 30), bg='lightblue', anchor='center')
                vers8.pack(fill='x')
                janela9.mainloop()
            ger7 = Button(janela2, text='VERSICULO: 7', command=ger7)
            ger7.grid(row=1, column=0)

            def ger8 ():
                janela10 = Tk()
                janela10.title('Biblia Sagrada')
                janela10.geometry('1300x876')
                vers9 = Label(janela10, text='⁸ E chamou Deus à expansão Céus.\n E foi a tarde e a manhã, o dia segundo.', font=('arial', 30), bg='lightblue', anchor='center')
                vers9.pack(fill='x')
                janela10.mainloop()
            ger8 = Button(janela2, text='VERSICULO: 8', command=ger8)
            ger8.grid(row=1, column=1)
            
            def ger9 ():
                janela11 = Tk()
                janela11.title('Biblia Sagrada')
                janela11.geometry('1300x876')
                vers10 = Label(janela11, text='⁹ E disse Deus: Ajuntem-se as águas debaixo dos céus num lugar;\n e apareça a porção seca. E assim foi.', font=('arial', 30), bg='lightblue', anchor='center')
                vers10.pack(fill='x')
                janela11.mainloop()
            ger9 = Button(janela2, text='VERSICULO: 9', command=ger9)
            ger9.grid(row=1, column=2)
            
            def ger10 ():
                janela12 = Tk()
                janela12.title('Biblia Sagrada')
                janela12.geometry('1300x876')
                vers11 = Label(janela12, text='¹⁰ E chamou Deus à porção seca Terra;\n e ao ajuntamento das águas chamou Mares.\n E viu Deus que era bom.', font=('arial', 30), bg='lightblue', anchor='center')
                vers11.pack(fill='x')
                janela12.mainloop()
            ger10 = Button(janela2, text='VERSICULO: 10', command=ger10)
            ger10.grid(row=1, column=3)
            
            def ger11 ():
                janela13 = Tk()
                janela13.title('Biblia Sagrada')
                janela13.geometry('1300x876')
                vers12 = Label(janela13, text='¹¹ E disse Deus: Produza a terra relva, ervas que dêem semente,\n árvores frutíferas que dêem fruto segundo a sua espécie, cuja semente esteja nela,\n sobre a terra. E assim foi.', font=('arial', 30), bg='lightblue', anchor='center')
                vers12.pack(fill='x')
                janela13.mainloop()
            ger11 = Button(janela2, text='VERSICULO: 11', command=ger11)
            ger11.grid(row=1, column=4)

            def ger12 ():
                janela14 = Tk()
                janela14.title('Biblia Sagrada')
                janela14.geometry('1300x876')
                vers13 = Label(janela14, text='¹² E a terra produziu relva, ervas que davam semente segundo a sua espécie,\n e árvores que davam fruto, cuja\n semente estava nela, segundo a sua espécie.\n E viu Deus que era bom.', font=('arial', 30), bg='lightblue', anchor='center')
                vers13.pack(fill='x')
                janela14.mainloop()
            ger12 = Button(janela2, text='VERSICULO: 12', command=ger12)
            ger12.grid(row=1, column=5)

            def ger13 ():
                janela15 = Tk()
                janela15.title('Biblia Sagrada')
                janela15.geometry('1300x876')
                vers14 = Label(janela15, text='¹³ E foi a tarde e a manhã, o dia terceiro.', font=('arial', 30), bg='lightblue', anchor='center')
                vers14.pack(fill='x')
                janela15.mainloop()
            ger13 = Button(janela2, text='VERSICULO: 13', command=ger13)
            ger13.grid(row=2, column=0)

            def ger14 ():
                janela16 = Tk()
                janela16.title('Biblia Sagrada')
                janela16.geometry('1300x876')
                vers15 = Label(janela16, text='¹⁴ E disse Deus: Haja luminares na expansão dos céus para separar o dia da noite;\n e sejam eles para sinais, e para estações, e para dias e anos;\n ¹⁵ e sejam para luminares na expansão dos céus para iluminar a terra. E assim foi.', font=('arial', 30), bg='lightblue', anchor='center')
                vers15.pack(fill='x')
                janela16.mainloop()
            ger14 = Button(janela2, text='VERSICULO: 14', command=ger14)
            ger14.grid(row=2, column=1)

            def ger15 ():
                janela17 = Tk()
                janela17.title('Biblia Sagrada')
                janela17.geometry('1300x876')
                vers16 = Label(janela17, text='¹⁵ E sejam para luminares na expansão dos céus, para iluminar a terra; e assim foi.', font=('arial', 30), bg='lightblue', anchor='center')
                vers16.pack(fill='x')
                janela17.mainloop()
            ger15 = Button(janela2, text='VERSICULO: 15', command=ger15)
            ger15.grid(row=2, column=2)

            
            def ger50 ():
                janela17 = Tk()
                janela17.title('Biblia Sagrada')
                janela17.geometry('1300x876')
                vers16 = Label(janela17, text='¹⁶ E fez Deus os dois grandes luminares: o luminar maior para governar o dia, e o luminar menor para governar a noite;\n e fez as estrelas.', font=('arial', 30), bg='lightblue', anchor='center')
                vers16.pack(fill='x')
                janela17.mainloop()
            ger15 = Button(janela2, text='VERSICULO: 16', command=ger50)
            ger15.grid(row=2, column=3)

            def ger16 ():
                janela18 = Tk()
                janela18.title('Biblia Sagrada')
                janela18.geometry('1300x876')
                vers17 = Label(janela18, text='¹⁷ E os colocou na expansão dos céus para iluminar a terra,\n ¹⁸ e para governar o dia e a noite, e para separar a luz das trevas;\n e viu Deus que era bom.', font=('arial', 30), bg='lightblue', anchor='center')
                vers17.pack(fill='x')
                janela18.mainloop()
            ger16 = Button(janela2, text='VERSICULO: 17', command=ger16)
            ger16.grid(row=2, column=4)

            def ger17 ():
                janela19 = Tk()
                janela19.title('Biblia Sagrada')
                janela19.geometry('1300x876')
                vers18 = Label(janela19, text='¹⁸ E os colocou na expansão dos céus para iluminar a terra,\n ¹⁸ e para governar o dia e a noite, e para separar a luz das trevas;\n e viu Deus que era bom.', font=('arial', 30), bg='lightblue', anchor='center')
                vers18.pack(fill='x')
                janela19.mainloop()
            ger17 = Button(janela2, text='VERSICULO: 18', command=ger17)
            ger17.grid(row=2, column=5)

            def ger18 ():
                janela20 = Tk()
                janela20.title('Biblia Sagrada')
                janela20.geometry('1300x876')
                vers19 = Label(janela20, text='¹⁹ E foi a tarde e a manhã, o dia quarto.', font=('arial', 30), bg='lightblue', anchor='center')
                vers19.pack(fill='x')
                janela20.mainloop()
            ger18 = Button(janela2, text='VERSICULO: 19', command=ger18)
            ger18.grid(row=3, column=0)

            def ger19 ():
                janela21 = Tk()
                janela21.title('Biblia Sagrada')
                janela21.geometry('1300x876')
                vers20 = Label(janela21, text='²⁰ E disse Deus: Produzam as águas abundantemente répteis de alma vivente;\n e voem as aves sobre a face da expansão dos céus.', font=('arial', 30), bg='lightblue', anchor='center')
                vers20.pack(fill='x')
                janela21.mainloop()
            ger19 = Button(janela2, text='VERSICULO: 20', command=ger19)    
            ger19.grid(row=3, column=1)

            def ger20 ():
                janela22 = Tk()
                janela22.title('Biblia Sagrada')
                janela22.geometry('1300x876')
                vers21 = Label(janela22, text='²¹ E criou Deus os grandes répteis marinhos, e todo o ser vivente que se move,\n os quais as águas abundantemente produziram segundo as suas espécies;\n e toda a ave segundo a sua espécie. E viu Deus que era bom.', font=('arial', 30), bg='lightblue', anchor='center')
                vers21.pack(fill='x')
                janela22.mainloop()
            ger20 = Button(janela2, text='VERSICULO: 21', command=ger20)
            ger20.grid(row=3, column=2)

            def ger21 ():
                janela23 = Tk()
                janela23.title('Biblia Sagrada')
                janela23.geometry('1300x876')
                vers22 = Label(janela23, text='²² E Deus os abençoou, dizendo: Frutificai e multiplicai-vos, e enchei as águas nos mares;\n e as aves se multipliquem na terra.', font=('arial', 30), bg='lightblue', anchor='center')
                vers22.pack(fill='x')
                janela23.mainloop()
            ger21 = Button(janela2, text='VERSICULO: 22', command=ger21)
            ger21.grid(row=3, column=3)

            def ger22 ():
                janela24 = Tk()
                janela24.title('Biblia Sagrada')
                janela24.geometry('1300x876')
                vers23 = Label(janela24, text='²³ E foi a tarde e a manhã, o dia quinto.', font=('arial', 30), bg='lightblue', anchor='center')
                vers23.pack(fill='x')
                janela24.mainloop()
            ger22 = Button(janela2, text='VERSICULO: 23', command=ger22)
            ger22.grid(row=3, column=4)

            def ger23 ():
                janela25 = Tk()
                janela25.title('Biblia Sagrada')
                janela25.geometry('1300x876')
                vers24 = Label(janela25, text='²⁴ E disse Deus: Produza a terra seres viventes segundo as suas espécies: gado, répteis e animais selvagens da terra segundo as suas espécies. E assim foi.', font=('arial', 30), bg='lightblue', anchor='center')
                vers24.pack(fill='x')
                janela25.mainloop()
            ger23 = Button(janela2, text='VERSICULO: 24', command=ger23, )
            ger23.grid(row=3, column=5)

            def ger24 ():
                janela26 = Tk()
                janela26.title('Biblia Sagrada')
                janela26.geometry('1300x876')
                vers25 = Label(janela26, text='²⁵ E fez Deus os animais selvagens da terra segundo as suas espécies, e o gado segundo as suas espécies, e tudo o que se move sobre a terra segundo as suas espécies. E viu Deus que era bom.', font=('arial', 30), bg='lightblue', anchor='center')
                vers25.pack(fill='x')
                janela26.mainloop()
            ger24 = Button(janela2, text='VERSICULO: 25', command=ger24)
            ger24.grid(row=4, column=0)

            def ger25 ():
                janela27 = Tk()
                janela27.title('Biblia Sagrada')
                janela27.geometry('1300x876')
                vers26 = Label(janela27, text='²⁶ E disse Deus: Façamos o homem à nossa imagem, conforme a nossa semelhança;\n e domine sobre os peixes do mar, e sobre as aves dos céus, e sobre o gado, e sobre toda a terra,\n e sobre todo réptil que se move sobre a terra.', font=('arial', 30), bg='lightblue', anchor='center')
                vers26.pack(fill='x')
                janela27.mainloop()
            ger25 = Button(janela2, text='VERSICULO: 26', command=ger25)
            ger25.grid(row=4, column=1)

            def ger26 ():
                janela28 = Tk()
                janela28.title('Biblia Sagrada')
                janela28.geometry('1300x876')
                vers27 = Label(janela28, text='²⁷ E criou Deus o homem à sua imagem;\n à imagem de Deus o criou; homem e mulher os criou.', font=('arial', 30), bg='lightblue', anchor='center')
                vers27.pack(fill='x')
                janela28.mainloop()
            ger26 = Button(janela2, text='VERSICULO: 27', command=ger26)
            ger26.grid(row=4, column=2)
            
            def ger27 ():
                janela29 = Tk()
                janela29.title('Biblia Sagrada')
                janela29.geometry('1300x876')
                vers28 = Label(janela29, text='²⁸ E Deus os abençoou, e Deus lhes disse: Frutificai e multiplicai-vos, e enchei a terra, e sujeitai-a;\n e dominai sobre os peixes do mar, e sobre as aves dos céus, e sobre todo animal que se move sobre a terra.', font=('arial', 30), bg='lightblue', anchor='center')
                vers28.pack(fill='x')
                janela29.mainloop()
            ger27 = Button(janela2, text='VERSICULO: 28', command=ger27)
            ger27.grid(row=4, column=3)

            def ger28 ():
                janela30 = Tk()
                janela30.title('Biblia Sagrada')
                janela30.geometry('1300x876')
                vers29 = Label(janela30, text='²⁹ E disse Deus: Eis que vos tenho dado toda erva que dá semente,\n que está sobre a face de toda a terra; e toda árvore em que\n há fruto que dá semente ser-vos-á para mantimento;', font=('arial', 30), bg='lightblue', anchor='center')
                vers29.pack(fill='x')
                janela30.mainloop()
            ger28 = Button(janela2, text='VERSICULO: 29', command=ger28)
            ger28.grid(row=4, column=4)

            def ger29 ():
                janela31 = Tk()
                janela31.title('Biblia Sagrada')
                janela31.geometry('1300x876')
                vers30 = Label(janela31, text='³⁰ e a todo animal da terra, e a toda ave dos céus,\n e a todo réptil da terra, em que há alma vivente,\n toda erva verde lhes será para mantimento. E assim foi.', font=('arial', 30), bg='lightblue', anchor='center')
                vers30.pack(fill='x')
                janela31.mainloop()
            ger29 = Button(janela2, text='VERSICULO: 30', command=ger29)
            ger29.grid(row=4, column=5)

            def ger30 ():
                janela32 = Tk()
                janela32.title('Biblia Sagrada')
                janela32.geometry('1300x876')
                vers31 = Label(janela32, text='³¹ E viu Deus tudo quanto tinha feito, e eis que era muito bom.\n E foi a tarde e a manhã, o dia sexto.', font=('arial', 30), bg='lightblue', anchor='center')
                vers31.pack(fill='x')
                janela32.mainloop()
            ger30 = Button(janela2, text='VERSICULO: 31', command=ger30)
            ger30.grid(row=5, column=0)

    
    janela = Button(janela1, text='capitulo: 1', command=ge)
    janela.pack(side=TOP)
    capitulo2 = Button(janela1, text='capitulo: 2', command=cap2)
    capitulo2.pack(side=TOP)
    #capitulo3 = Button(janela1, text='capitulo: 3', command=cap3)
    #capitulo3.pack(side=TOP)
    janela1.mainloop()

def cap2 ():
    janela2 = Tk()
    janela2.title('Biblia sagrada')
    janela2.geometry('535x600')
    
    def versiculo1 ():
        janela3 = Tk()
        janela3.title('Biblia Sagrada')
        janela3.geometry('1300x876')
        vars1 = Label(janela3, text='¹ Assim os céus, a terra e todo o seu exército foram acabados.', font=('arial', 30), bg='lightblue', anchor='center')
        vars1.pack(fill='x')
    versiculo1 = Button(janela2, text='VERSICULO: 1', command=versiculo1)
    versiculo1.grid(row=0, column=0)
    
    def versiculo2 ():
        janela4 = Tk()
        janela4.title('Biblia Sagrada') 
        janela4.geometry('1300x876')
        vars2 = Label(janela4, text='² E no sétimo dia Deus já tinha acabado a obra que tinha feito;\n e descansou no sétimo dia de toda a obra que tinha feito.', font=('arial', 30), bg='lightblue', anchor='center')
        vars2.pack(fill='x')
    versiculo2 = Button(janela2, text='VERSICULO: 2', command=versiculo2)
    versiculo2.grid(row=0, column=1)
    
    def versiculo3 ():
        janela5 = Tk()
        janela5.title('Biblia Sagrada')
        janela5.geometry('1300x876')
        vars3 = Label(janela5, text='³ E Deus abençoou o sétimo dia e o santificou,\n porque nele descansou de toda a obra que tinha criado e feito.', font=('arial', 30), bg='lightblue', anchor='center')
        vars3.pack(fill='x')
    versiculo3 = Button(janela2, text='VERSICULO: 3', command=versiculo3)
    versiculo3.grid(row=0, column=2)
    def versiculo4 ():
        janela6 = Tk()
        janela6.title('Biblia Sagrada')
        janela6.geometry('1300x876')
        vars4 = Label(janela6, text='⁴ Estas são as origens dos céus e da terra, quando foram criados,\n no dia em que o Senhor Deus fez a terra e os céus,', font=('arial', 30), bg='lightblue', anchor='center')
        vars4.pack(fill='x')
    versiculo4 = Button(janela2, text='VERSICULO: 4', command=versiculo4)
    versiculo4.grid(row=0, column=3)

    def versiculo5 ():
        janela7 = Tk()
        janela7.title('Biblia Sagrada')
        janela7.geometry('1300x876')
        vars5 = Label(janela7, text='⁵ e toda planta do campo antes de crescer na terra,\n e toda erva do campo antes de brotar, porque o Senhor Deus ainda\n não tinha feito chover sobre a terra,\n e não havia homem para cultivar a terra.', font=('arial', 30), bg='lightblue', anchor='center')
        vars5.pack(fill='x')
    versiculo5 = Button(janela2, text='VERSICULO: 5', command=versiculo5)
    versiculo5.grid(row=0, column=4)

    def versiculo6 ():
        janela8 = Tk()
        janela8.title('Biblia Sagrada')
        janela8.geometry('1300x876')
        vars6 = Label(janela8, text='⁶ Mas subia da terra um vapor, o qual regava toda a face da terra.', font=('arial', 30), bg='lightblue', anchor='center')
        vars6.pack(fill='x')
    versiculo6 = Button(janela2, text='VERSICULO: 6', command=versiculo6)
    versiculo6.grid(row=0, column=5)

    def versiculo7 ():
        janela9 = Tk()
        janela9.title('Biblia Sagrada')
        janela9.geometry('1300x876')
        vars7 = Label(janela9, text='⁷ E formou o Senhor Deus o homem do pó da terra,\n e soprou em suas narinas o fôlego de vida;\n e o homem tornou-se alma vivente.', font=('arial', 30), bg='lightblue', anchor='center')
        vars7.pack(fill='x')
    versiculo7 = Button(janela2, text='VERSICULO: 7', command=versiculo7)
    versiculo7.grid(row=1, column=0)



ge = Button(janela, text='Genisis', command=janela1)
ge.pack(side=TOP)


janela.mainloop()

