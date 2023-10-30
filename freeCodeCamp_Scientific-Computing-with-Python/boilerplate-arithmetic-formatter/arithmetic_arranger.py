def arithmetic_arranger(islemler, secim=False):
  
  birinci = list()
  isaret = list()
  ikinci = list()
    
  # islemler 5'ten fazlaysa hata ver 
  if len(islemler) > 5:
    return "Error: Too many problems."
  
  # islemleri ayır
  for islem in islemler:
    # islemi bol
    ayrilmis_islem = islem.split()
    
    # listeleri hazırla
    birinci.append(ayrilmis_islem[0])
    isaret.append(ayrilmis_islem[1])
    ikinci.append(ayrilmis_islem[2])

  
      
  # Kontrollere başla
  for i in range(len(birinci)):
    
    # Yalnızca sayı içeriyor mu diye kontrol et
    if not (birinci[i].isdigit() and ikinci[i].isdigit()):
      return "Error: Numbers must only contain digits."

    # islemler'deki sayılar 4'ten büyükse hata ver
    if len(birinci[i]) > 4 or len(ikinci[i]) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    # islemler çarpma veya bölmeyse hata ver
    if isaret[i] == "*" or isaret[i] == "/":
      return "Error: Operator must be '+' or '-'."
        
  s1 = list()
  s2 = list()
  s3 = list()
  s4 = list()
        
  for i in range(len(birinci)):
    if len(birinci[i]) > len(ikinci[i]):
      s1.append(" "*2 + birinci[i])
    else:
      s1.append(" " * (len(ikinci[i]) - len(birinci[i]) + 2) + birinci[i])

  for i in range(len(ikinci)):
    if len(ikinci[i]) > len(birinci[i]):
      s2.append(isaret[i] + " " +ikinci[i])
    else:
      s2.append(isaret[i] + " " * (len(birinci[i])-len(ikinci[i])+1) + ikinci[i])
  
  for i in range(len(birinci)):
    s3.append("-" * (max(len(birinci[i]),len(ikinci[i])) + 2))        

  if secim == True:
    for i in range(len(birinci)):
      if isaret[i] == "+":
        sonuc = str(int(birinci[i]) + int(ikinci[i]))
      elif isaret[i] == "-":
        sonuc = str(int(birinci[i]) - int(ikinci[i]))  

      mak = max(len(birinci[i]), len(ikinci[i]))
  
      
      
      if len(sonuc) > mak:
        s4.append(" " * (len(sonuc)-mak) + sonuc)
      else:
        s4.append(" " * (mak + 2 - len(sonuc)) + sonuc)
      
    arranged_problems = "    ".join(s1) + "\n" + "    ".join(s2) + "\n" + "    ".join(s3) + "\n" + "    ".join(s4)
  else:
    arranged_problems = "    ".join(s1) + "\n" + "    ".join(s2) + "\n" + "    ".join(s3) 
    
  return arranged_problems