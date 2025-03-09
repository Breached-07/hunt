#!/usr/bin/env python3
import os 
import ipaddress
import json
from ipwhois import IPWhois 
import argparse
import logging
from datetime import datetime
import threading

# defining a path to json file (file will be stored in home directory)
LOG = os.path.expanduser("~/log_file.json")

# setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# handles invalid ip values by returning false
def private_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False
    
def load():
# if the json file doesnt exists create one
    if not os.path.exists(LOG):
        with open(LOG,"w") as file:
            json.dump({},file) 
            
    if os.path.exists(LOG):
        try:
         with open(LOG,"r") as file:
              try:
                  return json.load(file)
              except json.JSONDecodeError:
                  return {}
        except IOError:
            logging.error("error occured while loading the log file")
    return {}

def save(new_data):
    # saves new IP_ISP file and updates existing data with new entries and ensures json formatting
    log_data = load()
    log_data.update(new_data)
    
    try:
        with open(LOG,"w") as file:
            json.dump(log_data,file,indent=4) 
        logging.info("log file succesfully updated")    
    except Exception as e:
        logging.error(f"error resolving the given ip: {e}")
                       
                                              
def resolving(ip):
    # resolves the given IP to its ISP name  
    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap()
        name = result["network"].get("name","Unknown isp")    
        return name 
    except Exception as e:
        logging.error(f"resolving error of the given {ip} : {e}") 

# # traces the ISP of the given IP address
def tracing(ip,recheck = False):
   
    if private_ip(ip):
        logging.info(f"{ip} is a private ip and cannot be resolved to its isp")
        return
    log_data = load()
    
    if ip in log_data:
        if not  recheck:
            logging.info(f"{ip} is already logged with the isp: {log_data[ip]}")
            return
        
         
    logging.info(f"tracing the given ip: {ip}")
    name = resolving(ip)
    
    
    if name:
        log_data[ip] = name
        save(log_data)
        logging.info(f"{ip} ip is tied to the isp: {name}")
    else:
        logging.info(f"unable to resolve the isp of {ip}")

def tracing_ip_thread(ip ,recheck):
    tracing(ip,recheck)
    
            
        
def main():
    parser =  argparse.ArgumentParser(description="trace the isp of the ip")
    parser.add_argument("ip",nargs="?",help="target ip address or a list of ip's using -l")
    parser.add_argument("-v","--verbose",action="store_true",help="enabling verbose output")
    parser.add_argument("-r","--recheck",action = "store_true",help = "forcing a check on ip")
    parser.add_argument("-l","--list",nargs="+", help= "list the ips but separpate it with spaces")
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        
        
    if args.list:
        threads = []   
        for ip in args.list:   
           thread = threading.Thread(target=tracing_ip_thread,args=(ip, args.recheck))
           threads.append(thread)
           thread.start()
           
        for thread in threads:
            threads.join()    
    else:
            tracing(args.ip,args.recheck)
    
if __name__ == "__main__":
    main()    
    
    
            
            
                       