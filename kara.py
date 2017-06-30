import time
from __builtin__ import int
import locale
from re import LOCALE
from pip._vendor.distlib.compat import ZipFile
from zipfile import ZipInfo, ZIP_DEFLATED
import zipfile

book_title = " Thank you "
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
    id = 'FLIS'
    fixed_val_1 = 8
    fixed_val_2 = 65
    fixed_val_3 = 0
    fixed_val_4 = 0
    fixed_val_5 = 0xFFFFFFFF
    fixed_val_6 = 1
    fixed_val_7 = 3
    fixed_val_8 = 3
    fixed_val_9 = 1
    fixed_val_10 = 0xFFFFFFFF

class FCIS:
    id = 'FCIS'
    fixed_val_1 = 20
    fixed_val_2 = 16
    fixed_val_3 = 1
    fixed_val_4 = 0
    text_len = 0
    fixed_val_5 = 0
    fixed_val_6 = 32
    fixed_val_7 = 8
    fixed_val_8 = 1
    fixed_val_9 = 1
    fixed_val_10 = 0

class CMET:
    id = 'CMET'
    fixed_val_1 = 0xC
    text_len = 0
    fixed_val_3 = 1
    fixed_val_4 = 0


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
    id = 'MOBI'
    hdr_len = 0
    mobi_type = 2
    text_encoding = 65001
    unique_id = 0x92602E61
    file_ver = 5
    ortographic_idx = 0xFFFFFFFF
    inflection_idx = 0xFFFFFFFF
    index_names = 0xFFFFFFFF
    index_keys = 0xFFFFFFFF
    extra_idx_0 = 0xFFFFFFFF
    extra_idx_1 = 0xFFFFFFFF
    extra_idx_2 = 0xFFFFFFFF
    extra_idx_3 = 0xFFFFFFFF
    extra_idx_4 = 0xFFFFFFFF
    extra_idx_5 = 0xFFFFFFFF
    first_non_book_idx = 0xFFFFFFFF
    full_name_offset = 0
    full_name_len = 0
    locale = 0
    input_language = 0
    output_language = 0
    min_ver = 5
    first_img_idx = 0
    huffman_rec_offset = 0
    huffman_record_count = 0
    huffman_table_offset = 0
    huffman_table_len = 0
    exth_flags = 0
    drm_offset = 0xFFFFFFFF
    drm_count = 0
    drm_size = 0
    drm_flags = 0
    first_content_rec_num = 1
    last_content_rec_num = 2
    fcis_rec_num = 4
    fcis_rec_count = 1
    flis_rec_num = 3
    flis_rec_count = 1
    first_comp_data_sec_count = 2
    num_of_comp_data_sec = 0xFFFFFFFF
    extra_rec_data_flags = 1
    indx_rec_offset = 0xFFFFFFFF
    
class PDB_Header:
    name = book_title.replace(" ", "_")
    name_padding= 32 - len(name)
    file_attr = 0
    version = 0
    creation_time = 0
    mod_time = 0
    bkup_time = 0
    mod_num = 0
    app_info = 0
    sort_info = 0
    type = 'BOOK'
    creator = 'MOBI'
    unique_id_seed = 0x27
    next_record_list = 0
    num_records = 6
    records_list = [0x00E8, 
                    0x22D0, 
                    0x2322, 
                    0x2324, 
                    0x2348,
                    0x2374,
                    0x24B9,
                    0x3045,
                    0x304D, 
                    0x5235,
                    0x52E1, 
                    0x53D9, 
                    0x54B5, 
                    0x54C5, 
                    0x55B9,
                    0x5699, 
                    0x56BD, 
                    0x56E9, 
                    0x5701]
    
def main():
    f_mobi = open("outputfile.mobi","wb")
    zero_padding = 0
    zero_unused = 0

################## PDB Header ##################
    pdb_hdr = PDB_Header
    f_mobi.write(pdb_hdr.name)
    for i in range(0, pdb_hdr.name_padding):
        f_mobi.write('\x00')
    f_mobi.write(str('%04x'%pdb_hdr.file_attr).decode("hex"))
    f_mobi.write(str('%04x'%pdb_hdr.version).decode("hex"))
    pdb_hdr.creation_time = hex(int((time.time())))
    f_mobi.write(pdb_hdr.creation_time.replace("0x", '').decode("hex"))
    pdb_hdr.mod_time = pdb_hdr.creation_time
    f_mobi.write(pdb_hdr.mod_time.replace("0x", '').decode("hex"))
    f_mobi.write(str('%08x'%pdb_hdr.bkup_time).decode("hex"))
    f_mobi.write(str('%08x'%pdb_hdr.mod_num).decode("hex"))
    f_mobi.write(str('%08x'%pdb_hdr.app_info).decode("hex"))
    f_mobi.write(str('%08x'%pdb_hdr.sort_info).decode("hex"))
    f_mobi.write(pdb_hdr.type)
    f_mobi.write(pdb_hdr.creator)
    f_mobi.write(str('%08x'%pdb_hdr.unique_id_seed).decode("hex"))
    f_mobi.write(str('%08x'%pdb_hdr.next_record_list).decode("hex"))
    f_mobi.write(str('%04x'%pdb_hdr.num_records).decode("hex"))
    record_unique_id = 0
    for i in pdb_hdr.records_list:
        record_unique_id_hex = str('%02x'%record_unique_id).decode("hex") 
        f_mobi.write("\x00\x00" + str('%04x'%i).decode("hex") + "\x00\x00\x00" + record_unique_id_hex)
        record_unique_id = record_unique_id + 2
        if record_unique_id == 14:
            record_unique_id = 16
    f_mobi.write(str('%04x'%zero_padding).decode("hex"))
            
            
################## PalmDOC Header ##################
    # Compression #
    palm_compression = 0x0001
    f_mobi.write(str('%04x'%palm_compression).decode("hex"))
    # Unused #
    f_mobi.write(str('%04x'%zero_unused).decode("hex"))
    # Text length #
    palm_txt_len = 75 + len(ip_data)
    f_mobi.write(str('%08x'%palm_txt_len).decode("hex"))
    # Record count #
    palm_record_count = 1
    f_mobi.write(str('%04x'%palm_record_count).decode("hex"))
    # Record size #
    palm_record_size = 4096
    f_mobi.write(str('%04x'%palm_record_size).decode("hex"))
    # Current position #
    palm_current_pos = 0
    f_mobi.write(str('%08x'%palm_current_pos).decode("hex"))


################## MOBI Header ##################
    mobi_hdr = Mobi
    # Identifier #
    f_mobi.write(mobi_hdr.id)
    # Header length #
    mobi_hdr.hdr_len = 0x108
    f_mobi.write(str('%08x'%mobi_hdr.hdr_len).decode("hex"))
    # Mobi type #
    f_mobi.write(str('%08x'%mobi_hdr.mobi_type).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.text_encoding).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.unique_id).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.file_ver).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.ortographic_idx).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.inflection_idx).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.index_names).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.index_keys).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.extra_idx_0).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.extra_idx_1).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.extra_idx_2).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.extra_idx_3).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.extra_idx_4).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.extra_idx_5).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.first_non_book_idx).decode("hex"))
    mobi_hdr.full_name_offset = 0x1E4
    f_mobi.write(str('%08x'%mobi_hdr.full_name_offset).decode("hex"))
    mobi_hdr.full_name_len = 11
    f_mobi.write(str('%08x'%mobi_hdr.full_name_len).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.locale).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.input_language).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.output_language).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.min_ver).decode("hex"))
    mobi_hdr.first_img_idx = 3
    f_mobi.write(str('%08x'%mobi_hdr.first_img_idx).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.huffman_rec_offset).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.huffman_record_count).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.huffman_table_offset).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.huffman_table_len).decode("hex"))
    mobi_hdr.exth_flags = 0x850
    f_mobi.write(str('%08x'%mobi_hdr.exth_flags).decode("hex"))
    for i in range(32):
        f_mobi.write("\x00")
    f_mobi.write("\xFF\xFF\xFF\xFF")
    f_mobi.write(str('%08x'%mobi_hdr.drm_offset).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.drm_count).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.drm_size).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.drm_flags).decode("hex"))
    for i in range(8):
        f_mobi.write("\x00")
    f_mobi.write(str('%04x'%mobi_hdr.first_content_rec_num).decode("hex"))
    f_mobi.write(str('%04x'%mobi_hdr.last_content_rec_num).decode("hex"))
    f_mobi.write("\x00\x00\x00\x01")
    f_mobi.write(str('%08x'%mobi_hdr.fcis_rec_num).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.fcis_rec_count).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.flis_rec_num).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.flis_rec_count).decode("hex"))
    for i in range(8):
        f_mobi.write("\x00")
    f_mobi.write("\x00\x00\x00\x05")
    f_mobi.write(str('%08x'%mobi_hdr.first_comp_data_sec_count).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.num_of_comp_data_sec).decode("hex"))
    f_mobi.write("\xFF\xFF\xFF\xFF")
    f_mobi.write(str('%08x'%mobi_hdr.extra_rec_data_flags).decode("hex"))
    f_mobi.write(str('%08x'%mobi_hdr.indx_rec_offset).decode("hex"))
    for i in range(20):
        f_mobi.write("\xFF")
    for i in range(4):
        f_mobi.write("\x00")
    for i in range(4):
        f_mobi.write("\xFF")
    for i in range(4):
        f_mobi.write("\x00")
        
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
#     f_mobi.write(book_header+ip_data+book_footer)
  
    f_mobi.write("\x00\x00")
  
################## FLIS ##################
    flis_hdr = FLIS
    # Identifier #
    f_mobi.write(flis_hdr.id)
    # Header length #
    f_mobi.write(str('%08x'%flis_hdr.fixed_val_1).decode("hex"))
    f_mobi.write(str('%04x'%flis_hdr.fixed_val_2).decode("hex"))
    f_mobi.write(str('%04x'%flis_hdr.fixed_val_3).decode("hex"))
    f_mobi.write(str('%08x'%flis_hdr.fixed_val_4).decode("hex"))
    f_mobi.write(str('%08x'%flis_hdr.fixed_val_5).decode("hex"))
    f_mobi.write(str('%04x'%flis_hdr.fixed_val_6).decode("hex"))
    f_mobi.write(str('%04x'%flis_hdr.fixed_val_7).decode("hex"))
    f_mobi.write(str('%08x'%flis_hdr.fixed_val_8).decode("hex"))
    f_mobi.write(str('%08x'%flis_hdr.fixed_val_9).decode("hex"))
    f_mobi.write(str('%08x'%flis_hdr.fixed_val_10).decode("hex"))

  
################## FCIS ##################
    fcis_hdr = FCIS
    # Identifier #
    f_mobi.write(fcis_hdr.id)
    # Header length #
    f_mobi.write(str('%08x'%fcis_hdr.fixed_val_1).decode("hex"))
    f_mobi.write(str('%08x'%fcis_hdr.fixed_val_2).decode("hex"))
    f_mobi.write(str('%08x'%fcis_hdr.fixed_val_3).decode("hex"))
    f_mobi.write(str('%08x'%fcis_hdr.fixed_val_4).decode("hex"))
    fcis_hdr.text_len = palm_txt_len
    f_mobi.write(str('%08x'%fcis_hdr.text_len).decode("hex"))
    f_mobi.write(str('%08x'%fcis_hdr.fixed_val_5).decode("hex"))
    f_mobi.write(str('%08x'%fcis_hdr.fixed_val_6).decode("hex"))
    f_mobi.write(str('%08x'%fcis_hdr.fixed_val_7).decode("hex"))
    f_mobi.write(str('%04x'%fcis_hdr.fixed_val_8).decode("hex"))
    f_mobi.write(str('%04x'%fcis_hdr.fixed_val_9).decode("hex"))
    f_mobi.write(str('%08x'%fcis_hdr.fixed_val_10).decode("hex"))
  
################## EOF ##################
    f_mobi.write("\xE9\x8E\x0D\x0A")
  
    
    f_mobi.close()

if __name__ == "__main__":
  main()
