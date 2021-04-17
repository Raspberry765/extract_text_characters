import pathlib
import glob
import re
import pprint
#import matplotlib.pyplot as plt
import pandas as pd

#p_temp = pathlib.Path('C:/Users/')  #ectraction filename in directory(/) below
list_file_name=["C:/Users/produ/Desktop/excel_data/test.txt"]  # test file


df1 = pd.DataFrame([], index=['delay (s)','count (times)' ])  #create initiation 
for w in list_file_name:
     # print(w)
     with open(w) as f:
          s = f.read()
          delay_list =re.findall('start="(.*)"\sw', s)  #() extraction characters in ().
          delay_num_list=num_list = list(map(float, delay_list))
          count_list =re.findall('count="(.*)"\s/>', s)
          #count_num_list=num_list = list(map(float, count_list))
          #signal_result= pd.Series( [delay_list,count_list, index=['delay (s)','count (times)'] )
          # place_index=re.findall('result_(.*)_', str(w))
          # wifi_info =re.findall('_.*_(.)', str(w))   #result_7F_a
          #place_index=re.findall('\re.+\lt', w)
          # num_list = list(map(float, signal_list))
          #print(s)
          dict = {'delay (s)': delay_list, 'count (times)': count_list} 
          df = pd.DataFrame(dict) 
          df.to_csv('C:/Users/produ/Desktop/excel_data/delay_result.csv')
          #print(count_list)
          #print("\n")
          
     #df1=df1.append(signal_result, ignore_index=True)
     f.close()



    

   