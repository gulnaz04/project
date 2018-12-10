#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <math.h>
#include <string>
#include <fstream> 
#include <iomanip> 
#include <cstring>
#include <vector>           
#include <sstream>          
#include <algorithm>    
#include "storage_1.h"
#include <list>
#include <iterator>

int main()
{   
    Storage<std::string> stor_1;
    stor_1.readDataBase();
    //stor_1.readBook();
    stor_1.InsertBook();
    //stor_1.DeleteBook();
    return 0;
} 
    
 


