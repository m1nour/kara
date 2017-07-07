import time
from __builtin__ import int
import locale
from re import LOCALE
from struct import *
from _ast import Num

book_title = "Thank you"
f_ip = open("inputfile.txt","r")
f_html = open("outputfile.html", "w")
html_header = "<html DIR=\"RTL\"><head>\r\r\n<meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\"/>\r\r\n<title>" + book_title +"</title>\r\r\n</head><body aid=\"0\"></body></html>\r\r\n<p DIR=\"RTL\" aid=\"1\">\r\r\n"
html_header_mod = "<html><head><guide></guide></head><body><p dir=\"RTL\"> "
html_footer = "\r\r\n</p>\r\r\n"
html_footer_mod = " </p>  </body></html>"
ip_data = f_ip.read()
html_data = html_header+ip_data+html_footer
f_html.write(html_data)
f_html.close()
f_ip.close()


class TAGX:
    _01id = 'TAGX'
    _02hdr_len = 0
    _03control_byte_count = 0


class INDX:
    _01id = 'INDX'
    _02hdr_len = 0
    _03idx_type = 0
    _03zunknown = 0
    _03zzunknown = 0
    _04idxt_start = 0
    _05idx_count = 0
    _06idx_encoding = 0
    _07idx_lang = 0
    _08total_idx_count = 0
    _09ordt_start = 0
    _10ligt_start = 0
    _10zunknown = 0
    _10zzunknown = 0


class CMET:
    _01id = 'CMET'
    _02fixed_val_1 = pack('>i', 0xC)
    _03text_len = pack('>i', 10)
#     _04text = pack('>i', 1)
#     _05unknown_data = 'ts '
    
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
    records_list = [0x00E8, #PalmDOC + MOBI + EXTH
                    0x22C0, #html
                    0x2323, #00
                    0x2324, #FLIS
                    0x2348, #FCIS
                    0x2374, #CMET
                    0x28F0-0x564, #BOUNDARY 
                    0x28F8-0x564, #PalmDOC + MOBI + EXTH
                    0x4AD0-0x564, #html
                    0x4BAA-0x564, #0000
                    0x4BAC-0x564, #INDX
                    0x4CA4-0x564, #INDX
                    0x4D80-0x564, #P-//*[@aid='0']
                    0x4D90-0x564, #INDX
                    0x4E84-0x564, #INDX
                    0x4F64-0x564, #FLIS
                    0x4F88-0x564, #FCIS
                    0x4FB4-0x564, #DATP
                    0x4FCC-0x564] #EOF
    
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
        if record_unique_id == 12:
            record_unique_id = 14
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
    mobi_hdr._18full_name_offset = pack('>i', 0x1D8)
    mobi_hdr._19full_name_len = pack('>i', 9)
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
    exth_hdr.hdr_len = 0xC0
    f_mobi.write(str('%08x'%exth_hdr.hdr_len).decode("hex"))
    exth_hdr.rec_count = 0xA
    f_mobi.write(str('%08x'%exth_hdr.rec_count).decode("hex"))

#     exth_rec_1 = ExthRecord
#     exth_rec_1.rec_type = 0x216
#     f_mobi.write(str('%08x'%exth_rec_1.rec_type).decode("hex"))
#     exth_rec_1.rec_len = 0xB
#     f_mobi.write(str('%08x'%exth_rec_1.rec_len).decode("hex"))
#     exth_rec_1.rec_data = "kpr"
#     f_mobi.write(str(exth_rec_1.rec_data))

    exth_rec_2 = ExthRecord
    exth_rec_2.rec_type = 0x21E
    f_mobi.write(str('%08x'%exth_rec_2.rec_type).decode("hex"))
    exth_rec_2.rec_len = 0xC
    f_mobi.write(str('%08x'%exth_rec_2.rec_len).decode("hex"))
    exth_rec_2.rec_data = "W3bm"
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
    exth_rec_11.rec_data = 0x7
    f_mobi.write(str('%08x'%exth_rec_11.rec_data).decode("hex"))

    f_mobi.write(book_title)
    
    exth_hdr.padding = pdb_hdr.records_list[1] - pdb_hdr.records_list[0] - 0x1E1
    for i in range(exth_hdr.padding):
        f_mobi.write("\x00")
    
################## Book Data ##################

    f_mobi.write(html_header_mod+ip_data+html_footer_mod)  
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


################## CMET ##################
    cmet_hdr = CMET
    for i, v in sorted(cmet_hdr.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
#     for i in range(30):
    f_mobi.write("MadeByKara")
    f_mobi.write("\x00\x00")
    


################## BOUNDARY ##################
    f_mobi.write("BOUNDARY")
  


################## PalmDOC Header ##################
    palmdoc_hdr2 = PalmDOC_Header
    palmdoc_hdr2._3text_len = pack('>i', 194 + len(ip_data))
    for i, v in sorted(palmdoc_hdr2.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)

################## MOBI Header ##################
    mobi_hdr2 = Mobi
    mobi_hdr2._02hdr_len = pack('>i', 0x108)
    mobi_hdr2._06file_ver = pack('>i', 0x8)
    mobi_hdr2._07ortographic_idx = pack('>i', 0x3)
    mobi_hdr2._17first_non_book_idx = pack('>i', 0x3)
    mobi_hdr2._18full_name_offset = pack('>i', 0x1CC)
    mobi_hdr2._19full_name_len = pack('>i', 9)
    mobi_hdr2._23min_ver = pack('>i', 8)
    mobi_hdr2._24first_img_idx = pack('>i', 8)
    mobi_hdr2._29exth_flags = pack('>i', 0x50) 
    mobi_hdr2._35last_content_rec_num = pack('>h', 7)
    mobi_hdr2._36fcis_rec_num = pack('>i', 9)
    mobi_hdr2._38flis_rec_num = pack('>i', 8)
    mobi_hdr2._39zzzunused = pack('>I', 0xFFFFFFFF)
    mobi_hdr2._40first_comp_data_sec_count = pack('>i', 0)
    mobi_hdr2._43zunused = pack('>i', 3)
    mobi_hdr2._43zzunused = pack('>i', 6)
    mobi_hdr2._43zzzunused = pack('>i', 0xA)
    for i, v in sorted(mobi_hdr2.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
        
################## EXTH Header ##################
    exth_hdr2 = Exth
    # Identifier #
    f_mobi.write(exth_hdr2.id)
    # Header length #
    exth_hdr2.hdr_len = 0xB4
    f_mobi.write(str('%08x'%exth_hdr.hdr_len).decode("hex"))
    exth_hdr.rec_count = 0x9
    f_mobi.write(str('%08x'%exth_hdr.rec_count).decode("hex"))

#     exth_rec_1 = ExthRecord
#     exth_rec_1.rec_type = 0x216
#     f_mobi.write(str('%08x'%exth_rec_1.rec_type).decode("hex"))
#     exth_rec_1.rec_len = 0xB
#     f_mobi.write(str('%08x'%exth_rec_1.rec_len).decode("hex"))
#     exth_rec_1.rec_data = "kpr"
#     f_mobi.write(str(exth_rec_1.rec_data))

    exth_rec_2 = ExthRecord
    exth_rec_2.rec_type = 0x21E
    f_mobi.write(str('%08x'%exth_rec_2.rec_type).decode("hex"))
    exth_rec_2.rec_len = 0xC
    f_mobi.write(str('%08x'%exth_rec_2.rec_len).decode("hex"))
    exth_rec_2.rec_data = "W3bm"
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
    exth_rec_3.rec_data = 0xBCAFF0BE
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

    f_mobi.write(book_title)
    
    exth_hdr2.padding = pdb_hdr.records_list[8] - pdb_hdr.records_list[7] - 0x1D5
    for i in range(exth_hdr2.padding):
        f_mobi.write("\x00")


################## Book Data ##################

    f_mobi.write(html_header+ip_data+html_footer)  
    f_mobi.write("\x00\x00\x00")


################## INDX Header ##################
    indx_hdr = INDX
    indx_hdr._02hdr_len = pack('>I', 0xC0)
    indx_hdr._03idx_type = pack('>I', 0)
    indx_hdr._03zunknown = pack('>I', 0)
    indx_hdr._03zzunknown = pack('>I', 2)
    indx_hdr._04idxt_start = pack('>I', 0xF0)
    indx_hdr._05idx_count = pack('>I', 1)
    indx_hdr._06idx_encoding = pack('>I', 65001)
    indx_hdr._07idx_lang = pack('>I', 0xFFFFFFFF)
    indx_hdr._08total_idx_count = pack('>I', 1)
    indx_hdr._09ordt_start = pack('>I', 0)
    indx_hdr._10ligt_start = pack('>I', 0)
    indx_hdr._10zunknown = pack('>I', 0)
    indx_hdr._10zzunknown = pack('>I', 1)
    for i, v in sorted(indx_hdr.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
    for i in range(0x7C):
        f_mobi.write("\x00")
    f_mobi.write("\x00\x00\x00\xC0")
    f_mobi.write("\x00\x00\x00\x00")
    f_mobi.write("\x00\x00\x00\x00")
    tagx_hdr = TAGX
    tagx_hdr._02hdr_len = pack('>I', 0x20)
    tagx_hdr._03control_byte_count = pack('>I', 1)
    for i, v in sorted(tagx_hdr.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
    f_mobi.write("\x02\x01\x01\x00")
    f_mobi.write("\x03\x01\x02\x00")
    f_mobi.write("\x04\x01\x04\x00")
    f_mobi.write("\x06\x02\x08\x00")
    f_mobi.write("\x00\x00\x00\x01")
    f_mobi.write("\n0000000143\0")
    f_mobi.write("\x01\x00\x00\x00")
    f_mobi.write('IDXT')
    f_mobi.write("\x00\xE0\x00\x00")

################## INDX Header ##################
    indx_hdr2 = INDX
    indx_hdr2._02hdr_len = pack('>I', 0xC0)
    indx_hdr2._03idx_type = pack('>I', 0)
    indx_hdr2._03zunknown = pack('>I', 1)
    indx_hdr2._03zzunknown = pack('>I', 0)
    indx_hdr2._04idxt_start = pack('>I', 0xD4)
    indx_hdr2._05idx_count = pack('>I', 1)
    indx_hdr2._06idx_encoding = pack('>I', 0xFFFFFFFF)
    indx_hdr2._07idx_lang = pack('>I', 0xFFFFFFFF)
    indx_hdr2._08total_idx_count = pack('>I', 0)
    indx_hdr2._09ordt_start = pack('>I', 0)
    indx_hdr2._10ligt_start = pack('>I', 0)
    indx_hdr2._10zunknown = pack('>I', 0)
    indx_hdr2._10zzunknown = pack('>I', 0)
    for i, v in sorted(indx_hdr2.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
    for i in range(0x88):
        f_mobi.write("\x00")
    f_mobi.write("\n0000000143\x0F")
    f_mobi.write("\x80\x80\x80\x80")
    f_mobi.write("\xBC\x00\x00\x00")
    f_mobi.write('IDXT')
    f_mobi.write("\x00\xC0\x00\x00")

################## Unknown ##################
    f_mobi.write("\x8F")
    f_mobi.write("P-//*[@aid=\'0\']")


################## INDX Header ##################
    indx_hdr3 = INDX
    indx_hdr3._02hdr_len = pack('>I', 0xC0)
    indx_hdr3._03idx_type = pack('>I', 0)
    indx_hdr3._03zunknown = pack('>I', 0)
    indx_hdr3._03zzunknown = pack('>I', 2)
    indx_hdr3._04idxt_start = pack('>I', 0xEC)
    indx_hdr3._05idx_count = pack('>I', 1)
    indx_hdr3._06idx_encoding = pack('>I', 65001)
    indx_hdr3._07idx_lang = pack('>I', 0xFFFFFFFF)
    indx_hdr3._08total_idx_count = pack('>I', 1)
    indx_hdr3._09ordt_start = pack('>I', 0)
    indx_hdr3._10ligt_start = pack('>I', 0)
    indx_hdr3._10zunknown = pack('>I', 0)
    indx_hdr3._10zzunknown = pack('>I', 0)
    for i, v in sorted(indx_hdr3.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
    for i in range(0x7C):
        f_mobi.write("\x00")
    f_mobi.write("\x00\x00\x00\xC0")
    f_mobi.write("\x00\x00\x00\x00")
    f_mobi.write("\x00\x00\x00\x00")
    tagx_hdr = TAGX
    tagx_hdr._02hdr_len = pack('>I', 0x18)
    tagx_hdr._03control_byte_count = pack('>I', 1)
    for i, v in sorted(tagx_hdr.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
    f_mobi.write("\x01\x01\x03\x00")
    f_mobi.write("\x06\x02\x0C\x00")
    f_mobi.write("\x00\x00\x00\x01")
    f_mobi.write("\x0ESKEL0000000000\0")
    f_mobi.write("\x01\x00\x00\x00")
    f_mobi.write('IDXT')
    f_mobi.write("\x00\xD8\x00\x00")

################## INDX Header ##################
    indx_hdr4 = INDX
    indx_hdr4._02hdr_len = pack('>I', 0xC0)
    indx_hdr4._03idx_type = pack('>I', 0)
    indx_hdr4._03zunknown = pack('>I', 1)
    indx_hdr4._03zzunknown = pack('>I', 0)
    indx_hdr4._04idxt_start = pack('>I', 0xD8)
    indx_hdr4._05idx_count = pack('>I', 1)
    indx_hdr4._06idx_encoding = pack('>I', 0xFFFFFFFF)
    indx_hdr4._07idx_lang = pack('>I', 0xFFFFFFFF)
    indx_hdr4._08total_idx_count = pack('>I', 0)
    indx_hdr4._09ordt_start = pack('>I', 0)
    indx_hdr4._10ligt_start = pack('>I', 0)
    indx_hdr4._10zunknown = pack('>I', 0)
    indx_hdr4._10zzunknown = pack('>I', 0)
    for i, v in sorted(indx_hdr4.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
    for i in range(0x88):
        f_mobi.write("\x00")
    f_mobi.write("\x0ESKEL0000000000\n")
    f_mobi.write("\x81\x81\x80\x01")
    f_mobi.write("\x9D\x80\x01\x9D")
    f_mobi.write('IDXT')
    f_mobi.write("\x00\xC0\x00\x00")


################## FLIS ##################
    flis_hdr2 = FLIS
    for i, v in sorted(flis_hdr2.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)
  
################## FCIS ##################
    fcis_hdr2 = FCIS
    fcis_hdr2._06text_len = palmdoc_hdr._3text_len
    for i, v in sorted(fcis_hdr2.__dict__.iteritems()):
        if not i.startswith("__"):
            if i.startswith("_"):
                f_mobi.write(v)

################## DATP ##################
    f_mobi.write('DATP')
    f_mobi.write("\x00\x00\x00\x0D")
    f_mobi.write("\x01\x04\x00\x01")
    f_mobi.write("\x02\x00\x00\x00")
    f_mobi.write("\x00\x00\x00\x00")
    f_mobi.write("\x00\x00\x00\x00")

################## EOF ##################
    f_mobi.write("\xE9\x8E\x0D\x0A")
  
    
    f_mobi.close()

if __name__ == "__main__":
  main()
