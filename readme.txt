1001570332_Talati_Anshul


1)computer used to run the code MacBook Pro, Code Runs from terminal as well as Browser.

2) Download the code and store in the a folder on computer.











RUNNING FROM BROWSER 

1) Open Terminal, go to the directory where the code is saved with the help on the cd command.

2)Once, you are in the directory run aserver.py using the command “python aserver.py 9001” to initiate the server. It will give message in the terminal that the “waiting for incoming connection”.

*Instead of 9001 any port can be used but both the ports should be same viz at client and server end.

3) a)Open any browser, in the url field type - “http://localhost:9001” it will show the “Server is Running”

   b)“http://localhost:9001/anshul1.txt” it will give the response http://1.1 200 in the server terminal and download the file in the browser.

   c)“http://localhost:9001/anshul2.txt” it will give the response http://1.1 200 in the server terminal and download the file in the browser. 

   d)“http://localhost:9001/anshul3.txt” it will give the response http:// in the server terminal and “File Not Found” the file in the browser.

   e)In each of the request it will show/give the parameters including the RTT in the terminal window.












RUNNING FROM Terminal.

1) Open 2 Terminal windows(one for client and one for server), go to the directory where the code is saved with the help on the cd command.

2) Once, you are in the directory run aserver.py using the command “python aserver.py localhost 9001” to initiate the server. It will give message in the terminal that the “waiting for the connection”.

*Instead of 9001 any port can be used but both the ports should be same viz at client and server end.

3) a)Now, in the other terminal run aclient.py using the command “python aclient.py localhost 9001” - it will display the connection parameters in the terminal window 

   b)“python aclient.py localhost 9001 anshul1.txt” it will the connection parameters the terminal window and download the file named “received_file” where source files are stored.

   c)“python aclient.py localhost 9001 anshul2.txt” it will the connection parameters the terminal window and download the file named “received_file” where source files are stored.

   d)“python aclient.py localhost 9001 anshul3.txt” it will the connection parameters the terminal window and give the message “File not found”.


