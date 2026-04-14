## HOW TO Connect webhook with line using Cloude Cloudflare Tunnel แบบไม่ทางการ
tester101 เขียนลวกๆ
เนื่องจากที่ทำจะเชื่อมกับ Line แนะนำให้ไปเปิด account ก่อน
แล้วก็จะได้ข้อมูลที่ต้องใส่ตามที่ไฟล์ example.env

ใส่ข้อมูลลงไป แล้วเปลี่ยนชื่อไฟล์เป็น .env 

ติดตั้ง Cloudflare Tunnel 
```
brew install cloudflared
```

ถ้าไม่ได้แนะนำโหลด Homebrew ก่อน ตามลิ้งค์ที่แนบไป ดูเอาเองนะ จุ้บๆ
https://brew.sh/

เปิด server ก่อน 
```
python receive_request.py
```

ดูว่า server รันที่ไหน อย่างตัวอย่างจะรันที่ 5001 สามารถขอ ลิ้งค์ จาก Cloudflare ได้ตาม port ที่เปิด

```
cloudflared tunnel --url http://localhost:5001
```

แล้วจะได้ 
```
https://random_name.trycloudflare.com
```

เอา https มะกี้ ไปใส่ที่ messaging API ของ Line Developer 
## จบแล้ว 
