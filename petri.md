# Задание. Сеть Петри
Задана сеть Петри N = <P, T, I, O>.
Для своего варианта:    
1. Построить входную и выходную расширенные функции.
2. Построить граф.
3. Построить матрицу инцидентности  
```
Вариант 20
P={P1, P2, P3, P4, P5}
T={t1, t2, t3}
I(t1)={P1, P4}                     O(t1)={P1, P5 }
I(t2)={P2, P3, P5}                 O(t2)={P5}
I(t3)={P4, P5}                     O(t3)={P3, P4} 
```
```
 1. Входные и выходные расширенные функции: 
   I(P1)={t1}                      O(P1)={t1}
   I(P2)={ }                       O(P2)={t2}
   I(P3)={t3}                      O(P3)={t2}
   I(P4)={t3}                      O(P4)={t1, t3}
   I(P5)={t1, t2}                  O(P5)={t2, t3}        
```  
2.     
  ![title](/images/petri.png?raw=true "Optional Title")
  
3. 
 Матрица входных и выходных инциденций:  
![title](/images/in.png?raw=true "Optional Title")  
![title](/Image/out.png?raw=true "Optional Title")  
 Матрица инцидентности:  
 ![title](/images/incind.png?raw=true "Optional Title")    