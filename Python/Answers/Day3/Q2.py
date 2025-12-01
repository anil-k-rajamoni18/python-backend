logs = {
  "level": "INFO",
  "entries": [
    {"id": 1, "messages": ["start", "processing", "done"]},
    {"id": 2, "messages": ["start", "error", "retry", "done"]},
  ]
}

#messageslist=logs["entries"][0]["messages"]+logs["entries"][1]["messages"]
allMessages=[message for entry in logs["entries"] for message in entry["messages"]]
print(allMessages)

#errorCount=logs["entries"][0]["messages"].count("done")+logs["entries"][1]["messages"].count("done")
errorCount=sum(entry["messages"].count("error") for entry in logs["entries"])
print(errorCount)

"""
for entry in logs["entries"]:
    for message in entry["messages"]:
        if message=="error":
            print(entry)
"""
entries=[entry for entry in logs["entries"] if "error" in entry["messages"]]
print(entries)



