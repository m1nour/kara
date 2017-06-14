def main():
  f_ip = open("inputfile.txt","r")
  f_op = open("outputfile.html","w")
  f_mobi = open("mobifile.mobi","w")
  
  book_header = "<html DIR=\"RTL\">\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\">\r\n<title> Thank you </title>\r\n</head>\r\n<body>\r\n<p DIR=\"RTL\">\r\n"
  ip_data = f_ip.read()
  book_footer = "\r\n</p>\r\n</body>\r\n</html>"
  f_op.write(book_header+ip_data+book_footer)
  
  f_ip.close()
  f_op.close()
  f_mobi.close()

if __name__ == "__main__":
  main()
