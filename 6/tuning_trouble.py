with open("6/input.txt", "r", encoding="utf8") as reader:
    data = reader.readline().strip()


def get_message_index(marker_length):
    for i in range(len(data) - marker_length):
        if len(set(data[i : i + marker_length])) == marker_length:
            return i + marker_length


print(get_message_index(4))
print(get_message_index(14))
