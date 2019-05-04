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

Alamat = str(object.partner_shipping_id.street)
if(object.partner_shipping_id.street2 != False) : 
    Alamat = Alamat + "\n" + str(object.partner_shipping_id.street2)
    
if(object.partner_shipping_id.city != False) :
    Alamat = Alamat + "\n" + str(object.partner_shipping_id.city) + ", "
    
if(object.partner_shipping_id.state_id.display_name != False) :
    Alamat = Alamat + str(object.partner_shipping_id.state_id.display_name) + " " + str(object.partner_shipping_id.zip)
    
if(object.partner_shipping_id.country_id.display_name != False) :
    Alamat = Alamat + "\n" + str(object.partner_shipping_id.country_id.display_name)
    
isi = "Yth. *" + str(object.partner_id.display_name) + "*, ( *" + str(object.partner_id.phone) + "* )\n\n"\
    + "Terimakasih telah melakukan pemesanan." + "\n"\
    + "Pesanan Anda telah kami terima dengan kode tracking *#" + str(object.display_name) + ".*\n\n"\
    + "Tanggal pemesanan : " + str(Tgl) + " WIB" + "\n"\
    + "Metode Pengiriman : *" + str(object.carrier_id.display_name) + "* (Estimasi: " + object.currency_id.symbol + " " + str(object.delivery_price) + ")" + "\n"\
    + "Metode Pembayaran : *" + str(object.payment_acquirer_id.display_name) + "*\n\n"\
    + "   Harga : " + object.currency_id.symbol + " " + str(object.amount_untaxed) + "\n"\
    + "   Pajak  : " + object.currency_id.symbol + "   " + str(object.amount_tax) + "\n"\
    + "   ----------------------------- *""+" + "*\n"\
    + "   Total :   " + object.currency_id.symbol + " *" + str(object.amount_total) + "*\n\n"\
    + "Alamat Pengiriman: \n" + str(Alamat) + "\n\n"\
    + "Status : " + str(object.state) + "\n"\
    + "Update Terakhir : " + str(now.strftime("%Y-%m-%d %H:%M" + " WIB")) + "\n"\
    + "Di update oleh : " + str(object.partner_id.create_uid.display_name) + "\n\n"\
    + "Informasi detail telah kami kirim melalui email ke *" + str(object.partner_id.email) + "*\n\n"\
    + "Apabila memerlukan informasi lebih lanjut, silahkan hubungi admin di nomor *0811-2223-401*."
    
if (str(object.state) == "sale"):
    wa = env['whatsapp.personal'].send_message_personal_wablas_log(groupA, isi)
    action = wa
