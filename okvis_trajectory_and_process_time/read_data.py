with open('/home/cc/output/okvis_process_time/OKVIS_perimage_process_time_V203.txt') as reader, open('/home/cc/output/okvis_process_time/OKVIS_process_time_V203.txt', 'w') as writer:
    for index, line in enumerate(reader):
        if index % 2 == 0:
            writer.write(line)
