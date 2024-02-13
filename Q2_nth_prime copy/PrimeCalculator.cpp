//Nom, Matricule
//Nom, Matricule

#include "PrimeCalculator.h"
// #include <vector>
#include <math.h>

// ce fichier contient les definitions des methodes de la classe PrimeCalculator
// this file contains the definitions of the methods of the PrimeCalculator class

PrimeCalculator::PrimeCalculator()
{
}

int PrimeCalculator::CalculateNthPrime(int N)
{   
    int resultat = 0;
        // Répéter N fois, trouver le premier suivant
        for(int i = 0; i <= N-1; i++){
            resultat = CalculateNextPrime(resultat);
        }
        return resultat;
}

// trouve le plus petit nombre premier plus grand que N 
int PrimeCalculator::CalculateNextPrime(int N)
{   
    bool isPrime = false;
        int i = N;
        while(!isPrime){
            i++;
            isPrime = IsPrime(i); // if isPrime becomes true, it'll become false
        }
    return i;
}

bool PrimeCalculator::IsPrime(int N)
{   
   bool isPrime = true;

   if (N == 2 || N == 3 || N == 5) {
        return true;
    }
   
   if (N < 2 || N % 2 == 0) {
        return false;
    }

    // Skip numbers divisible by 3 or 5
    if (N % 3 == 0 || N % 5 == 0) {
        return false;
    }

   for (int i = 5; i <= sqrt(N); i += 6) { // bonds de 6 car on a déjà vérifié 2 & 3
        if (N % i == 0 || N % (i + 2) == 0) {
            return false;
        }
    }
   return true;
}
