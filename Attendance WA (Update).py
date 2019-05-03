format = "%Y-%m-%d %H:%M:%S"
format2 = "%d-%m-%Y %H:%M"

waktu = datetime.datetime.strptime(object.write_date,"%Y-%m-%d %H:%M:%S")
now = datetime.datetime.now()
#time1 = datetime.datetime.strftime(object.write_time,"%H:%M")
#time2 = datetime.datetime.strftime(object.write_time,"%H:%M")

delay = now - waktu
microseconds = delay.seconds*1000000 + delay.microseconds

a = waktu.strftime("%H:%M")
b = now.strftime("%H:%M")


groupA = '628156814955'
groupID = '1528083915'
 

#a = waktu.strftime("%M:%S")
#b = now.strftime("%M:%S")
#c = JamKeluar
#d = JamMasuk

#time2 = datetime.strptime(d,"%H%M")


JamMasuk = datetime.datetime.strptime(object.check_in,format)
JamMasuk = timezone('UTC').localize(JamMasuk)
JamMasuk = JamMasuk.astimezone(timezone('Asia/Jakarta'))
JamMasuk = JamMasuk.strftime(format2)
#JamKeluar = datetime.datetime.strptime(object.check_out,format)
#JamKeluar = timezone('UTC').localize(JamKeluar)
#JamKeluar = JamKeluar.astimezone(timezone('Asia/Jakarta'))
#JamKeluar = JamKeluar.strftime(format2)

#TotalJam = JamKeluar - JamMasuk
#TotalKerja = datetime.datetime.strptime(object.check_out,format)-JamMasuk


if object.check_out == False :
    pesan = "Anda Telah Check-in hari ini"
    Keluar = ""
    Judul = "*#I#ATTENDANCE IN#*"
    HasilJam = ""
    
else: #checkout
    pesan = "Terimakasih atas kerjasamanya.\nAnda Telah Check-out ..."
    JamKeluar = datetime.datetime.strptime(object.check_out,format)
    JamKeluar= timezone('UTC').localize(JamKeluar)
    JamKeluar = JamKeluar.astimezone(timezone('Asia/Jakarta'))
    JamKeluar = JamKeluar.strftime(format2)
    JamMasuk = JamMasuk.strftime(format2)
    TotalJam = JamKeluar - JamMasuk
    Keluar = '_Jam Keluar: ' + str(JamKeluar) + ' WIB_\n'
    Judul = "*#ATTENDANCE OUT#*"
    HasilJam = '_Total Jam Kerja : ' +  str(TotalJam) + '_\n' \
    #c = JamKeluar
    #d = JamMasuk
    #time1 = datetime.strftime(c,"%H%M") # convert string to time
    #time2 = datetime.strftime(d,"%H%M") 
    #diff = time1 -time2
    #diff.total_seconds()/3600
    #diff.total = "_Total Jam Kerja : ...._" + '\n' \
    #TotalKerja = b-a
    


isi = Judul + '\n\n' \
    + '*[' + object.employee_id.name + ']* ' + '\n\n' \
    + '_Jam Masuk: ' + str(JamMasuk) + ' WIB' +'_\n' \
    + Keluar + '\n' \
    + HasilJam + '\n' \


wa = env['whatsapp.group'].send_message_wablas_log(groupA, groupID, isi)
action = wa

#time.sleep(500000/1000000)

#if microseconds < 800000 :
