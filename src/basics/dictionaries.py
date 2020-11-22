#used to store key value pairs

monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec": "December"
}

print(monthConversions["Jan"])
print(monthConversions.get("Jan","Not a valid Key"))