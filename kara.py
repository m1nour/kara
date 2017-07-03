import time
from __builtin__ import int
import locale
from re import LOCALE
from zipfile import ZipInfo, ZIP_DEFLATED
import zipfile
from struct import *
from _ast import Num

book_title = "Thank you"
f_ip = open("inputfile.txt","r")
f_html = open("outputfile.html", "w")
html_header = "<html DIR=\"RTL\">\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\">\r\n<title>" + book_title +"</title>\r\n</head>\r\n<body>\r\n<p DIR=\"RTL\">\r\n"
html_footer = "\r\n</p>\r\n</body>\r\n</html>"
ip_data = f_ip.read()
html_data = html_header+ip_data+html_footer
f_html.write(html_data)
f_html.close()
f_ip.close()
myzip = zipfile.ZipFile('outputfile.zip', mode='w')
myzip.write("outputfile.html", compress_type=zipfile.ZIP_DEFLATED)
myzip.close()
    
class FLIS:
    _01id = 'FLIS'
    _02fixed_val_1 = pack('>i', 8)
    _03fixed_val_2 = pack('>h', 65)
    _04fixed_val_3 = pack('>h', 0)
    _05fixed_val_4 = pack('>i', 0)
    _06fixed_val_5 = pack('>I', 0xFFFFFFFF)
    _07fixed_val_6 = pack('>h', 1)
    _08fixed_val_7 = pack('>h', 3)
    _09fixed_val_8 = pack('>i', 3)
    _10fixed_val_9 = pack('>i', 1)
    _11fixed_val_10 = pack('>I', 0xFFFFFFFF)

class FCIS:
    _01id = 'FCIS'
    _02fixed_val_1 = pack('>i', 20)
    _03fixed_val_2 = pack('>i', 16)
    _04fixed_val_3 = pack('>i', 1)
    _05fixed_val_4 = pack('>i', 0)
    _06text_len = 0
    _07fixed_val_5 = pack('>i', 0)
    _08fixed_val_6 = pack('>i', 32)
    _09fixed_val_7 = pack('>i', 8)
    _10fixed_val_8 = pack('>h', 1)
    _11fixed_val_9 = pack('>h', 1)
    _12fixed_val_10 = pack('>i', 0)

class CMET:
    _01id = 'CMET'
    _02fixed_val_1 = pack('>i', 0xC)
    _03text_len = 0
    _04fixed_val_3 = 1
    _05fixed_val_4 = 0


class ExthRecord:
    rec_type = 0
    rec_len = 0
    rec_data = 0
    
class Exth:
    id = 'EXTH'
    hdr_len = 0
    rec_count = 0
    padding = 0
    
class Mobi:
    _01id = 'MOBI'
    _02hdr_len = 0
    _03mobi_type = pack('>i', 2)
    _04text_encoding = pack('>i', 65001)
    _05unique_id = pack('>I',0x92602E61)
    _06file_ver = pack('>i', 5)
    _07ortographic_idx = pack('>I',0xFFFFFFFF)
    _08inflection_idx = pack('>I',0xFFFFFFFF)
    _09index_names = pack('>I',0xFFFFFFFF)
    _10index_keys = pack('>I',0xFFFFFFFF)
    _11extra_idx_0 = pack('>I',0xFFFFFFFF)
    _12extra_idx_1 = pack('>I',0xFFFFFFFF)
    _13extra_idx_2 = pack('>I',0xFFFFFFFF)
    _14extra_idx_3 = pack('>I',0xFFFFFFFF)
    _15extra_idx_4 = pack('>I',0xFFFFFFFF)
    _16extra_idx_5 = pack('>I',0xFFFFFFFF)
    _17first_non_book_idx = pack('>I',0xFFFFFFFF)
    _18full_name_offset = 0
    _19full_name_len = 0
    _20locale = pack('>i', 0)
    _21input_language = pack('>i', 0)
    _22output_language = pack('>i', 0)
    _23min_ver = pack('>i', 5)
    _24first_img_idx = pack('>i', 0)
    _25huffman_rec_offset = pack('>i', 0)
    _26huffman_record_count = pack('>i', 0)
    _27huffman_table_offset = pack('>i', 0)
    _28huffman_table_len = pack('>i', 0)
    _29exth_flags = pack('>i', 0)
    _29zunused = pack('>i', 0)
    _29zzunused = pack('>i', 0)
    _29zzzunused = pack('>i', 0)
    _29zzzzunused = pack('>i', 0)
    _29zzzzzunused = pack('>i', 0)
    _29zzzzzzunused = pack('>i', 0)
    _29zzzzzzzunused = pack('>i', 0)
    _29zzzzzzzzunused = pack('>i', 0)
    _29zzzzzzzzzunused = pack('>I',0xFFFFFFFF)
    _30drm_offset = pack('>I',0xFFFFFFFF)
    _31drm_count = pack('>i', 0)
    _32drm_size = pack('>i', 0)
    _33drm_flags = pack('>i', 0)
    _33zunused = pack('>i', 0)
    _33zzunused = pack('>i', 0)
    _34first_content_rec_num = pack('>h', 1)
    _35last_content_rec_num = pack('>h', 2)
    _35zunused = pack('>i', 1)
    _36fcis_rec_num = pack('>i', 4)
    _37fcis_rec_count = pack('>i', 1)
    _38flis_rec_num = pack('>i', 3)
    _39flis_rec_count = pack('>i', 1)
    _39zunused = pack('>i', 0)
    _39zzunused = pack('>i', 0)
    _39zzzunused = pack('>i', 5)
    _40first_comp_data_sec_count = pack('>i', 2)
    _41num_of_comp_data_sec = pack('>I',0xFFFFFFFF)
    _41zunused = pack('>I',0xFFFFFFFF)
    _42extra_rec_data_flags = pack('>i', 1)
    _43indx_rec_offset = pack('>I',0xFFFFFFFF)
    _43zunused = pack('>I',0xFFFFFFFF)
    _43zzunused = pack('>I',0xFFFFFFFF)
    _43zzzunused = pack('>I',0xFFFFFFFF)
    _43zzzzunused = pack('>I',0xFFFFFFFF)
    _43zzzzzunused = pack('>I',0xFFFFFFFF)
    _43zzzzzzunused = pack('>I',0)
    _43zzzzzzzunused = pack('>I',0xFFFFFFFF)
    _43zzzzzzzzunused = pack('>I',0)


class PalmDOC_Header:
    _1compression = pack('>h', 1)
    _2unused = pack('>h', 0)
    _3text_len = 0
    _4record_count = pack('>h', 1)
    _5record_size = pack('>h', 4096)
    _6curr_pos = pack('>i', 0)
    
class PDB_Header:
    name  = pack('>32s', book_title.replace(" ", "_")) 
    name_padding= 32 - len(name)
    _03file_attr = pack('>h', 0)
    _04version = pack('>h', 0)
    _05creation_time = 0
    _06mod_time = 0
    _07bkup_time = pack('>i', 0)
    _08mod_num = pack('>i', 0)
    _09app_info = pack('>i', 0)
    _10sort_info = pack('>i', 0)
    _11type = 'BOOK'
    _12creator = 'MOBI'
    _13unique_id_seed = pack('>i', 0x27)
    _14next_record_list = pack('>i', 0)
    _15num_records = pack('>h', 19)
    records_list = [0x00E8, 
                    0x22D0, 
                    0x2322+0x67, 
                    0x2324+0x67, 
                    0x2348+0x67,
                    0x2374+0x67,
                    0x24B9+0x67,
                    0x3045+0x67,
                    0x304D+0x67, 
                    0x5235+0x67,
                    0x52E1+0x67, 
                    0x53D9+0x67,
                    0x54B5+0x67, 
                    0x54C5+0x67, 
                    0x55B9+0x67,
                    0x5699+0x67, 
                    0x56BD+0x67, 
                    0x56E9+0x67, 
                    0x5701+0x67]
    
def main():
    f_mobi = open("outputfile.mobi","wb")
    zero_padding = 0
    zero_unused = 0

################## PDB Header ##################
    pdb_hdr = PDB_Header
    print pdb_hdr.name
    f_mobi.write(pdb_hdr.name)
    for i in range(0, pdb_hdr.name_padding):
        f_mobi.write('\x00')
    pdb_hdr._05creation_time = hex(int((time.time())))
    pdb_hdr._05creation_time = pdb_hdr._05creation_time.replace("0x", '').decode("hex")
    pdb_hdr._06mod_time = pdb_hdr._05creation_time
    for i, v in sorted(pdb_hdr.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
    record_unique_id = 0
    for i in pdb_hdr.records_list:
        record_unique_id_hex = str('%02x'%record_unique_id).decode("hex") 
        f_mobi.write("\x00\x00" + str('%04x'%i).decode("hex") + "\x00\x00\x00" + record_unique_id_hex)
        record_unique_id = record_unique_id + 2
        if record_unique_id == 14:
            record_unique_id = 16
    f_mobi.write(str('%04x'%zero_padding).decode("hex"))
            
            
################## PalmDOC Header ##################
    palmdoc_hdr = PalmDOC_Header
    palmdoc_hdr._3text_len = pack('>i', 75 + len(ip_data))
    for i, v in sorted(palmdoc_hdr.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)

################## MOBI Header ##################
    mobi_hdr = Mobi
    mobi_hdr._02hdr_len = pack('>i', 0x108)
    mobi_hdr._18full_name_offset = pack('>i', 0x1E4)
    mobi_hdr._19full_name_len = pack('>i', 11)
    mobi_hdr._24first_img_idx = pack('>i', 3)
    mobi_hdr._29exth_flags = pack('>i', 0x850) 
    for i, v in sorted(mobi_hdr.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
        
################## EXTH Header ##################
    exth_hdr = Exth
    # Identifier #
    f_mobi.write(exth_hdr.id)
    # Header length #
    exth_hdr.hdr_len = 0xCC
    f_mobi.write(str('%08x'%exth_hdr.hdr_len).decode("hex"))
    exth_hdr.rec_count = 0xB
    f_mobi.write(str('%08x'%exth_hdr.rec_count).decode("hex"))

    exth_rec_1 = ExthRecord
    exth_rec_1.rec_type = 0x216
    f_mobi.write(str('%08x'%exth_rec_1.rec_type).decode("hex"))
    exth_rec_1.rec_len = 0xB
    f_mobi.write(str('%08x'%exth_rec_1.rec_len).decode("hex"))
    exth_rec_1.rec_data = "kpr"
    f_mobi.write(str(exth_rec_1.rec_data))

    exth_rec_2 = ExthRecord
    exth_rec_2.rec_type = 0x21E
    f_mobi.write(str('%08x'%exth_rec_2.rec_type).decode("hex"))
    exth_rec_2.rec_len = 0xc
    f_mobi.write(str('%08x'%exth_rec_2.rec_len).decode("hex"))
    exth_rec_2.rec_data = "HgIU"
    f_mobi.write(str(exth_rec_2.rec_data))

    exth_rec_3 = ExthRecord
    exth_rec_3.rec_type = 0x12C
    f_mobi.write(str('%08x'%exth_rec_3.rec_type).decode("hex"))
    exth_rec_3.rec_len = 0x34
    f_mobi.write(str('%08x'%exth_rec_3.rec_len).decode("hex"))
    exth_rec_3.rec_data = 0x01200000
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))
    exth_rec_3.rec_data = 0x00000000
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))
    exth_rec_3.rec_data = 0x00000000
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))
    exth_rec_3.rec_data = 0x00000080
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))
    exth_rec_3.rec_data = 0x00000000
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))
    exth_rec_3.rec_data = 0x00000000
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))
    exth_rec_3.rec_data = 0x00000000
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))
    exth_rec_3.rec_data = 0x00000000
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))
    exth_rec_3.rec_data = 0xECBEF4ED
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))
    exth_rec_3.rec_data = 0x0CB90CCA
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))
    exth_rec_3.rec_data = 0x0CC30CC5
    f_mobi.write(str('%08x'%exth_rec_3.rec_data).decode("hex"))

    exth_rec_4 = ExthRecord
    exth_rec_4.rec_type = 0xCC
    f_mobi.write(str('%08x'%exth_rec_4.rec_type).decode("hex"))
    exth_rec_4.rec_len = 0xC
    f_mobi.write(str('%08x'%exth_rec_4.rec_len).decode("hex"))
    exth_rec_4.rec_data = 0xC8
    f_mobi.write(str('%08x'%exth_rec_4.rec_data).decode("hex"))

    exth_rec_5 = ExthRecord
    exth_rec_5.rec_type = 0xCD
    f_mobi.write(str('%08x'%exth_rec_5.rec_type).decode("hex"))
    exth_rec_5.rec_len = 0xC
    f_mobi.write(str('%08x'%exth_rec_5.rec_len).decode("hex"))
    exth_rec_5.rec_data = 0x2
    f_mobi.write(str('%08x'%exth_rec_5.rec_data).decode("hex"))

    exth_rec_6 = ExthRecord
    exth_rec_6.rec_type = 0xCE
    f_mobi.write(str('%08x'%exth_rec_6.rec_type).decode("hex"))
    exth_rec_6.rec_len = 0xC
    f_mobi.write(str('%08x'%exth_rec_6.rec_len).decode("hex"))
    exth_rec_6.rec_data = 0x9
    f_mobi.write(str('%08x'%exth_rec_6.rec_data).decode("hex"))

    exth_rec_7 = ExthRecord
    exth_rec_7.rec_type = 0x217
    f_mobi.write(str('%08x'%exth_rec_7.rec_type).decode("hex"))
    exth_rec_7.rec_len = 0x14
    f_mobi.write(str('%08x'%exth_rec_7.rec_len).decode("hex"))
    exth_rec_7.rec_data = "1029-0897292"
    f_mobi.write(exth_rec_7.rec_data)

    exth_rec_8 = ExthRecord
    exth_rec_8.rec_type = 0xCF
    f_mobi.write(str('%08x'%exth_rec_8.rec_type).decode("hex"))
    exth_rec_8.rec_len = 0xC
    f_mobi.write(str('%08x'%exth_rec_8.rec_len).decode("hex"))
    exth_rec_8.rec_data = 0x0
    f_mobi.write(str('%08x'%exth_rec_8.rec_data).decode("hex"))

    exth_rec_9 = ExthRecord
    exth_rec_9.rec_type = 0x223
    f_mobi.write(str('%08x'%exth_rec_9.rec_type).decode("hex"))
    exth_rec_9.rec_len = 0x18
    f_mobi.write(str('%08x'%exth_rec_9.rec_len).decode("hex"))
    exth_rec_9.rec_data = "I\0n\0M\0e\0m\0o\0r\0y\0"
    f_mobi.write(exth_rec_9.rec_data)

    exth_rec_10 = ExthRecord
    exth_rec_10.rec_type = 0x7D
    f_mobi.write(str('%08x'%exth_rec_10.rec_type).decode("hex"))
    exth_rec_10.rec_len = 0xC
    f_mobi.write(str('%08x'%exth_rec_10.rec_len).decode("hex"))
    exth_rec_10.rec_data = 0x0
    f_mobi.write(str('%08x'%exth_rec_10.rec_data).decode("hex"))

    exth_rec_11 = ExthRecord
    exth_rec_11.rec_type = 0x79
    f_mobi.write(str('%08x'%exth_rec_11.rec_type).decode("hex"))
    exth_rec_11.rec_len = 0xC
    f_mobi.write(str('%08x'%exth_rec_11.rec_len).decode("hex"))
    exth_rec_11.rec_data = 0x8
    f_mobi.write(str('%08x'%exth_rec_11.rec_data).decode("hex"))

    f_mobi.write("\0 "+book_title+" \0")
    
    exth_hdr.padding = pdb_hdr.records_list[1] - 0x2D8
    for i in range(exth_hdr.padding):
        f_mobi.write("\x00")
    
################## Book Data ##################

    html_header = "<html DIR=\"RTL\"><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\"><title> Thank you </title></head><body><p DIR=\"RTL\"> "
    html_footer = "</p> </body></html> \0"
    f_mobi.write(html_header+ip_data+html_footer)
  
    f_mobi.write("\x00\x00")
  
################## FLIS ##################
    flis_hdr = FLIS
    for i, v in sorted(flis_hdr.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
  
################## FCIS ##################
    fcis_hdr = FCIS
    fcis_hdr._06text_len = palmdoc_hdr._3text_len
    for i, v in sorted(fcis_hdr.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
  
################## EOF ##################
    f_mobi.write("\xE9\x8E\x0D\x0A")
  
    
    f_mobi.close()

if __name__ == "__main__":
  main()
