1. Install docker and start the service 
2. Clone the Buyondips_kite dir 
3. Now add the username, password, secret to Buyondips_kite/config.py
3. Add the stock you watch and buy when its 1% down on buy_on_dips.py file line number 16 
stocks list 
Eg: stocks = ['NSE:NAHARPOLY','NSE:LIKHITHA'] 
4. Build the container image. 
sudo docker build -t imagename .
eg:  sudo docker build -t buyondips .

5. Now run the container 
eg: sudo docker run buyondips

6. Check if the container started 
sudo docker ps -a 
7. Add container name into buydips.sh 

8. We can start the container using crontab 
eg : 
crontab -e 

25 9 * * 1-5 /home/opc/buydips.sh
