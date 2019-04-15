from KeyValueStore_Server.KeyValueStore_Provider import KeyValueStore_Provider as kvs
config={
    "Protocol":"http",
    "Host":"root:DJNHOFHDAHVQCJPQ@portal-ssl604-47.bmix-dal-yp-52e0cb81-b862-46a1-91a4-b5c0f148e0e7.467726176.composedb.com",
    #169.48.64.90",
    "Port":18579
}
etcdProvider = kvs.EtcdProvider(config)
etcdProvider.SetKey('/nodes')
result= etcdProvider.GetKey('/nodes/mydir1','file2')
for x in result:
    print(x.value)
#print(result)
#etcdProvider.CreateDirectory('/nodes/mydir1/abc/cd')
etcdProvider.SetKey("",'/nodes/mydir1/abc/file1', 1)
etcdProvider.SetKey('','/nodes/mydir1/abc/cd/file2', 6)
etcdProvider.Watch('/nodes/mydir/n1')
etcdProvider.SetKey('','/nodes/mydir/n1', 6)
result= etcdProvider.GetKey('/nodes/mydir','n1')
print(result)
