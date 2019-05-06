format = "%Y-%m-%d %H:%M:%S"
format2 = "%Y-%m-%d %H:%M"


waktu = datetime.datetime.strptime(object.write_date,format)
waktu = timezone('UTC').localize(waktu)
waktu = waktu.astimezone(timezone('Asia/Jakarta'))
now = datetime.datetime.now(timezone('Asia/Jakarta'))

delay = now - waktu
microseconds = delay.seconds*1000000 + delay.microseconds

groupA = str(object.partner_id.phone)

Tgl = datetime.datetime.strptime(object.create_date,format)
Tgl = timezone('UTC').localize(Tgl)
Tgl = Tgl.astimezone(timezone('Asia/Jakarta'))
Tgl = Tgl.strftime(format2)


isi = "Yth. *" +str(object.partner_id.display_name) + ',*\n\n'\
    + "Terimakasih atas kerjasama yang telah terjalin." '\n'\
    + "Kami menerima pesanan : " + '\n\n'\
    + "Nomor : *#" + str(object.name) + '*\n'\
    + "Total harga : *" + "Rp " + str(object.amount_total) + '*\n'\
    + "Tanggal pesanan : *" +str(Tgl) + " WIB"  + '*\n\n'\
    + "Informasi detail telah kami kirim melalui email *" + str(object.partner_id.email) + "*\n\n"\
    + "Apabila memerlukan informasi lebih lanjut, silahkan hubungi admin di nomor *0811-2223-401*"

wa = env['whatsapp.personal'].send_message_personal_wablas_log(groupA, isi)
action = wa

#str(object.display_name) 

#+ "Nama Product : *" +str(object.product_id.display_name) + '*\n'\
 #+ "Detail Pesanan :" '\n'\
    #+ "_http://belimanis.com/en_US/web/login#min=4&limit=80&view_type=list&model=purchase.order"+ str(object.id) + "&action=425_"

#+ "Anda Memesan Dari : *" +str(object.partner_id.display_name) + '*\n'\
#"*YTH Pelanggan :,*\n\n"\
#customerID = str(object.partner_id.phone)
#customer
#customerID = str(object.partner_id.phone)

#FYI :
#Function Wablas Personal (realtime) :
#send_message_personal_wablas(groupA, isi)

#Function Wablas Personal Log (disimpan di log dulu) :
#send_message_personal_log(groupA, isi)

#note : groupA = no hp tujuan
         # isi = isi mesaage





#groupID = '1528083915'
#+ "_http://belimanis.com/en_US/web/login#min=4&limit=80&view_type=list&model=purchase.order"+str(object.id) + "&action=425_"
