from speedtest import Speedtest

st = Speedtest()

print("Download Speed:", st.download())
print("Upload Speed:", st.upload())
