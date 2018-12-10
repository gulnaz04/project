#pragma once
#ifndef STORAGE_H_
#define STORAGE_H_
#include <string>
#include <cstdlib>
#include <list>
#include "hashFunc.h"
#include "iostream"
#include "fstream"
template<typename T>
struct Storage
{
    
    std::list<T>* storage = new std::list<T> [2756];
    void readDataBase();
    void readBook();
    void InsertBook();
    void DeleteBook();
    ~Storage();
};


template <typename T>
void Storage<T>::readDataBase()
{
    
    
    std::string filename = "lib.txt";

    std::ifstream DATABASE(filename);
    T tmp_str;
    int tmp_hash;
    int hash;
    int sum = 0;
    
    while(DATABASE)
    {
        
        T str;
        std::getline(DATABASE, str);
        
        if (str != "") 
        {
    
            int index = abs((int)(comp_hash(tmp_str) %2756));
            storage[index].push_back(tmp_str);
            tmp_str = "";
        }
        
    }
}
template<typename T>
void Storage<T>::readBook()
{   T book_name;
    std::cin >> book_name;
    int index = abs((int)(comp_hash(book_name) % 2756));
    auto iter_1 = std::find(storage[index].begin(), storage[index].end(), book_name);
    if (iter_1 != storage[index].end())
    {
        std::cout << "Yes" << std::endl;
    }
}

template<typename T>
void Storage<T>::DeleteBook()
{
    T book_name;
    std::cin >> book_name;
    int index = abs((int)(comp_hash(book_name) % 2756));
    auto iter_1 = std::find(storage[index].begin(), storage[index].end(), book_name);
    if (iter_1 != storage[index].end())
    {
        storage[index].erase(iter_1);
    }
    
}

template<typename T>
void Storage<T>::InsertBook()
{
    
    T book_name;
    std::cin>>book_name;
    int index = abs((int)(comp_hash(book_name) % 2756));
    
    storage[index].push_back(book_name);
    
    std::ofstream fout; 
    
    fout.open("lib.txt", std::ofstream::app); 
    
    if (fout.is_open()) 
    { 
        fout<< book_name <<  std::endl; 
        fout.close(); 
    } 
    else 
    { 
        std::cout << "File not found" << std::endl; 
    } 
}
template <typename T>
Storage<T>::~Storage()
{
    for (int i = 0; i < 2756; i++)
    {
    storage[i].clear();
    }
    delete[]storage;

 }



#endif
