def add_time(start, duration, weekday = ""):

# haftanın başlangıç günü verileni küçük harfe çevirerek çalışacak.
# eğer diğer güne geçerse kaç gün geçtiğine göre bildirimde bulunacak
  
  cur_h_m, cur_h_type = start.split()
  cur_h, cur_m = cur_h_m.split(":")
  
  dur_h, dur_m = duration.split(":")
  
  #cur_h_type
  #cur_h
  #cur_m
  #dur_h
  #dur_m
  
  cur_h_i = int(cur_h) 
  cur_m_i = int(cur_m)
  dur_h_i = int(dur_h)
  dur_m_i = int(dur_m)
  
  day_count = 0
      
  for i in range(dur_m_i):
    cur_m_i += 1
    dur_m_i -= 1
    if cur_m_i == 60:
      cur_m_i = 0
      cur_h_i += 1
      if cur_h_i == 13:
        cur_h_i = 1
      if cur_h_i == 12:
        if cur_h_type == "AM":
          cur_h_type = "PM"
        else:
          cur_h_type = "AM"
          day_count += 1
        
  
  for i in range(dur_h_i):
    cur_h_i += 1
    dur_h_i -= 1
    if cur_h_i == 13:
        cur_h_i = 1
    if cur_h_i == 12:
      if cur_h_type == "AM":
        cur_h_type = "PM"
      else:
        cur_h_type = "AM"
        day_count += 1
        
  new_day_name = ""
  days_dict = {"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
  if weekday != "": 
    day_num = days_dict[weekday.lower()]
    new_day_num = day_num + day_count
    new_day_num = new_day_num % 7
    if new_day_num == 0:
        new_day_num = 7
    for k,v in days_dict.items():
      if v == new_day_num:
        new_day_name = k 
    if day_count == 0:
      new_time = "{}:{} {}, {}".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type,new_day_name.title())
    elif day_count == 1:
      new_time = "{}:{} {}, {} (next day)".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type,new_day_name.title())
    else:
      new_time = "{}:{} {}, {} ({} days later)".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type,new_day_name.title(),day_count)
  else:
    if day_count == 0:
      new_time = "{}:{} {}".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type)
    elif day_count == 1:
      new_time = "{}:{} {} (next day)".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type,)
    else:
      new_time = "{}:{} {} ({} days later)".format(cur_h_i,str(cur_m_i).zfill(2),cur_h_type, day_count)
  
  return new_time

  
# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)