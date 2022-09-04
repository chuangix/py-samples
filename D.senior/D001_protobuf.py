import proto.addressbook_pb2 as addressbook_pb2

person = addressbook_pb2.Person()
person.name = "123"
person.email = 123
phone = person.phones.add()
phone.number = "2345"
phone.type = person.PhoneType.HOME

deserialized = addressbook_pb2.Person()
serialized = person.SerializeToString()
deserialized.ParseFromString(serialized)
print(serialized)
print(deserialized)
