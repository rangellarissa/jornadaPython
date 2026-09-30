
new_list = []
names = ["L", "A", "T"]
names.append("M")
print(names)
print(names[0])

message1 = {
    "user": "IA",
    "text": "Bora aprender Python"
}

message2 = {
    "user": "L",
    "text": "Bora sim"
}

message_list = [message1, message2]
new_message = {
    "role": "user",
    "content": "vamos começar!"
}
message_list.append(new_message)
print(message_list)