#! python
##
## This is just to supply a fake dadabase of price to test my code
import numpy as np
import pandas as pd
import sqlite3
from datetime import datetime 
import time 

def main():
    
    db = '../Dados/fakePrices.db'
    
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        
        create_table_normal = 'CREATE TABLE IF NOT EXISTS {}("date", "ultimo", "hora")'.format('ABCB4')
        c.execute(create_table_normal)
    
        create_table_chi = 'CREATE TABLE IF NOT EXISTS {}("date", "ultimo", "hora")'.format('ABEV3')
        c.execute(create_table_chi)
        
        conn.commit()
        
        
        today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        hora= datetime.today().strftime('%H:%M:%S')
        today = '2019-08-27 {}'.format(hora)

        normal = 18 + np.random.randn(1)[0]
        chi = 18 + np.random.chisquare(1)

        insert_table_n = 'INSERT INTO {}("date", "ultimo", "hora") VALUES("{}", \
        {:.2f}, "{}")'.format('ABCB4', today, normal, hora)
        print(insert_table_n)
        c.execute(insert_table_n)

        insert_table_chi = 'INSERT INTO {}("date", "ultimo", "hora") VALUES("{}", \
        {:.2f}, "{}")'.format('ABEV3', today, chi, hora)
        c.execute(insert_table_chi)
        print(insert_table_chi)
        conn.commit()

        
    
if __name__ == '__main__':
    while True:
        main()
        time.sleep(60)