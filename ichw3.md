 ## 结构  
高速缓冲存储器是存在于主存与CPU之间的一级存储器， 由静态存储芯片(SRAM)组成，容量比较小但速度比主存高得多， 接近于CPU的速度。  
缓存主要由三大部分组成：
1 Cache存储体：存放由主存调入的指令与数据块。  
2 地址转换部件：建立目录表以实现主存地址到缓存地址的转换。   
3 替换部件：在缓存已满时按一定策略进行数据块替换，并修改地址转换部件。
## 工作原理  
高速缓冲存储器通常由高速存储器、联想存储器、替换逻辑电路和相应的控制线路组成。在有高速缓冲存储器的计算机系统中，中央处理器存取主存储器的地址划分为行号、列号和组内地址三个字段。于是，主存储器就在逻辑上划分为若干行；每行划分为若干的存储单元组；每组包含几个或几十个字。高速存储器也相应地划分为行和列的存储单元组。二者的列数相同，组的大小也相同，但高速存储器的行数却比主存储器的行数少得多。   
联想存储器用于地址联想，有与高速存储器相同行数和列数的存储单元。当主存储器某一列某一行存储单元组调入高速存储器同一列某一空着的存储单元组时，与联想存储器对应位置的存储单元就记录调入的存储单元组在主存储器中的行号。    
当中央处理器存取主存储器时，硬件首先自动对存取地址的列号字段进行译码，以便将联想存储器该列的全部行号与存取主存储器地址的行号字段进行比较：若有相同的，表明要存取的主存储器单元已在高速存储器中，称为命中，硬件就将存取主存储器的地址映射为高速存储器的地址并执行存取操作；若都不相同，表明该单元不在高速存储器中，称为脱靶，硬件将执行存取主存储器操作并自动将该单元所在的那一主存储器单元组调入高速存储器相同列中空着的存储单元组中，同时将该组在主存储器中的行号存入联想存储器对应位置的单元内。    
当出现脱靶而高速存储器对应列中没有空的位置时，便淘汰该列中的某一组以腾出位置存放新调入的组，这称为替换。确定替换的规则叫替换算法，常用的替换算法有:最近最少使用算法（LRU）、先进先出法（FIFO）和随机法（RAND）等。替换逻辑电路就是执行这个功能的。另外，当执行写主存储器操作时，为保持主存储器和高速存储器内容的一致性，对命中和脱靶须分别处理。