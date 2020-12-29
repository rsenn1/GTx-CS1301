
#Print the time at which the run will end

start_hour = 3
start_minute = 48
length = 172

end_time = (start_hour * 60 + start_minute + length) 
end_hour = str(end_time // 60)
end_min = str(end_time % 60)

print(end_hour + ":" + end_min)
