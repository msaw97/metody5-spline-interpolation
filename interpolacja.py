import numpy as np
import matplotlib.pyplot as plt

#przyklady do wykorzystania
#t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#y = np.array([2, 3, 4, 2, 1, 0, -1, -3, -6, -4, -1])
#t= np.array([1,2,3])   #funkcja liniowa
#y= np.array([2,3,4])
t= np.array([0,1,2,3])
y= np.array([1,1,0,10])

n = len(t) - 1

def wartosc_S(x, i, t):
    """Liczy wartosc S w punkcie"""
    return S[i][0]* np.power((t[i+1] - x), 3) + S[i][1]* np.power((x - t[i]), 3) + S[i][2]*(x-t[i]) + S[i][3]*(t[i+1]-x)

def interpolacja_funkcji_skladanej(t,y):

    h1 = np.zeros(n)
    u = np.ones(n+1)    #srodkowa przekatna
    h2 = np.zeros(n)
    z = np.zeros(n+1)

    #Tworzy macierz trojprzekatniowa [h1 u h2]
    h1[0:n-1] = t[0:n-1] - t[1:n]
    u[1:n] = 2.0*(t[0:n-1] - t[2:n+1])
    h2[1:n] = t[1:n] - t[2:n+1]
    #tworzy macierz wynikowa z
    z[1:n] =6.0*(y[0:n-1] - y[1:n]) \
                 /(t[0:n-1] - t[1:n]) \
             -6.0*(y[1:n] - y[2:n+1])   \
                 /(t[1:n] - t[2:n+1])

    def LUrozklad(h1,u,h2):
        """Rozklad LU macierzy trojprzekatniowej gdzie h1, u, h2 sa diagonalnymi macierzy"""
        n = len(u)
        for z in range(1,n):
            z0 = h1[z-1]/u[z-1]
            u[z] = u[z] - z0*h2[z-1]
            h1[z-1] = z0
        return h1,u,h2

    def LUrozwiaz(h1,u,h2,b):
        """Rozwiazanie rozkladu LU [a]{x} = {b}, gdzie a jest rokladem LU macierzy [h1 u h2]"""
        n = len(u)
        for z in range(1,n):
            b[z] = b[z] - h1[z-1]*b[z-1]
        b[n-1] = b[n-1]/u[n-1]
        for z in range(n-2,-1,-1):
            b[z] = (b[z] - h2[z]*b[z+1])/u[z]
        return b

    LUrozklad(h1,u,h2)  #macierz [h1 u h2] rozkladana jest na LU
    LUrozwiaz(h1,u,h2,z)    #za b brana jest z, zwracana jest macierz z

    S = np.zeros((n, 4))
    h= np.zeros(n+1)

    for i in range(n):
       h[i] = t[i+1] - t[i]

    #wyliczanie wspolczynnikow wielomianu S
    for i in range(n):
        S[i][0] = z[i]/(6*h[i])
        S[i][1] = z[i+1]/(6*h[i])
        S[i][2] = (y[i+1]/h[i] - z[i+1]*h[i]/6)
        S[i][3] = (y[i]/h[i] - z[i]*h[i]/6)

    return z, S

def wykres(z, S):
    """Rysowanie wykresu"""
    X,Y =[],[]

    for i in range(n):
        x_range = np.arange(t[i], t[i+1]+0.01, 0.05)
        y_range = [wartosc_S(x, i, t) for x in x_range]
        X.extend(x_range)
        Y.extend(y_range)

    plt.plot(X, Y)
    plt.plot(t, y)
    plt.grid(linestyle='--', linewidth=0.3)
    plt.show()

if __name__== '__main__':
    print("t:", t)
    print("y:", y)
    z, S = interpolacja_funkcji_skladanej(t,y)
    for i in range(n):
        print(f"S{i}(x) = {S[i][0]}({t[i+1]} - x)^3 + {S[i][1]}(x - {t[i]})^3 + {S[i][2]}(x - {t[i]}) + {S[i][3]}({t[i+1]} - x)")
    wykres(z, S)
