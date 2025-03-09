# Hunt - IP to ISP Tracing Tool
         
         Hunt is a Python-based command-line tool that resolves the Internet Service Provider (ISP) associated with a given IP address.
## Requirements:
           - Python 3.x
           - ipwhois library (Install it via pip)
## Installation
          git clone https://github.com/Breached-07/hunt.git

           <!-- downloading ip whois -->
          pip install pipwhois
            
## Post-Download Setup:
           After downloading the script, follow these steps to set it up as a command-line tool:

## Rename the file:
   
         ```bash
         mv hunt.py hunt
         ```
## Make it executable:
          ```bash
          chmod +x hunt
          ```
## Move it to a directory in your system (to run it globally):
          ```bash
          sudo mv hunt /usr/local/bin
          ```
## Running the script: 
          ```bash
          hunt <IP_ADDRESS>  
          ```
          <!-- look into the hunt --help page-->
## NOTE : 
     if there is a issue is related to the line-ending characters 
     RUN the following command 
     dos2unix hunt.py
     
then run the script           
          
          
                   
          
 
          
          
           
