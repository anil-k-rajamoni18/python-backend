tx_ids = ["TX1001", "TX1002", "TX1001", "TX1005", "TX1002", "TX1007"]
uniqueIds=set(tx_ids)
print(uniqueIds)    
duplicates=set()
unique=[]
for tx_id in tx_ids:
    if tx_ids.count(tx_id)>1:
        duplicates.add(tx_id)
    else:
        unique.append(tx_id)
print(f"duplicate ids:{list(duplicates)}")
print(f"unique ids:{unique}")