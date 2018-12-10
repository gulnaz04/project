#pragma once
#ifndef HASHFUNC_H_
#define HASHFUNC_H_
#include <string>
#include <cmath>
#include <sstream>


template<typename T>
int comp_hash(T book_name)
{
    int hash = 0;
    float elem_1 = 0;
    for (int i =0; i < book_name.length(); i++)
    {
        hash += pow((int)(book_name[i])+ pow(i,4), 1.90);
        hash -= ((int)(book_name[i]) - 65) * (i + 1000)*i;
    }
   
    return (int)hash;

} 

#endif 
