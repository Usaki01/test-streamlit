import streamlit as st

st.set_page_config(page_title="Cervical Cancer Asserment", page_icon=":memo:")

st.title("Assessment Demo")
st.sidebar.header("แบบประเมินมะเร็งปากมดลูก")
st.sidebar.write("คำอธิบายแบบประเมิน")
st.subheader("ข้อมูลทั่วไป")
age = st.number_input("กรอกอายุของท่าน", min_value= 0, max_value=100, value=0, placeholder="โปรดใส่อายุของท่าน...")
st.write('อายุของท่านคือ ', age, 'ปี')
st.write("---------------------------------------------------")

st.subheader("ข้อมูลสุขภาพ")
use = st.radio(
    "เคยปวดท้องประจำเดือนหรือไม่",
    ["ไม่เคย", "เป็นบางครั้ง", "ทุกครั้ง"],
    index=None,
)

st.write("ความถี่ในการปวดท้องประจำเดือน", use)
st.write("---------------------------------------------------")

if st.button('ยืนยัน', type="primary"):
    if age == 0 or use == None:
        st.write("โปรดกรอกข้อมูลของท่าน")
    elif age > 30 and use == "ทุกครั้ง":
        st.markdown("## ท่านมีความเสี่ยงสูงที่จะเป็นมะเร็งปากมดลูก")
        st.write("อย่างไรก็ตามแบบประเมินนี้เป็นเพียงเครื่องมือในการประเมินความเสี่ยงเบื้องต้น ควรเข้ารับการคัดกรองมะเร็งปากมดลูกที่เป็นวิธีมาตรฐาน เพื่อความแม่นยำ และเข้าสู่ระบบ การรักษาได้อย่างทันท่วงที")
        st.image('271748222_5093640660668828_4892199078576618570_n.jpg',
          caption = 'อ้างอิง: https://www.facebook.com/CGHphaholyothin/photos/a.565950873437852/5093640667335494/?type=3')   
        st.write("การตรวจคัดกรองมะเร็งปากมดลูกได้ถูกบรรจุเป็นสิทธิ ประโยชน์กองทุนหลักประกันสุขภาพแห่งชาติ สำหรับหญิงไทยอายุ 30-59 ปี ทุกคน ทุกสิทธิการรักษา")
        st.write(''' - ติดต่อหน่วยบริการหรือสถานพยาบาลในระบบสปสช.
                \n - จองคิวผ่านแอปเป๋าตัง
                \n - ขอรับชุดตรวจคัดกรองมะเร็งปากมดลูกที่หน่วยบริการ ที่เข้าร่วม เช่น ร้านยา คลินิกการพยาบาล ฯลฯ
                \n **ติดต่อเพิ่มเติม สายด่วน สปสช. 1330**''')
    else:
        st.markdown("## ท่านมีความเสี่ยงต่ำที่จะเป็นมะเร็งปากมดลูก")
        st.write("อย่างไรก็ตาม อย่าลืมสังเกตอาการ และหลีกเลี่ยงปัจจัยเสี่ยงที่อาจทำให้เกิดเป็นมะเร็งปากมดลูกได้ และควรเข้าตรวจคัดกรองมะเร็งปากมดลูกที่สภานพยาบาลหากท่านอยู่ในกลุ่มดังนี้")
        st.write(''' - สตรีทุกคนที่มีอายุตั้งแต่ 21 ปีขึ้นไป หรือ 3 ปีหลังจากมีเพศสัมพันธ์ครั้งแรก ควรเริ่มทำการตรวจแปปสเมียร์ หลังจากนั้นทำการตรวจทุก 1-2 ปี
          \n - สตรีที่มีอายุตั้งแต่ 30 ปีขึ้นไป ควรตรวจแปปสเมียร์ทุกปี หากผลตรวจเป็นปกติติดต่อกัน 3 ปี สามารถตรวจแปปสเมียร์ทุก 3 ปีได้ 
          \n **ยกเว้นกลุ่มที่มีความเสี่ยงของมะเร็งปากมดลูก เช่น มีการติดเชื้อ HIV ติดเชื้อ HPV (Human Papillomavirus) มีโรคเกี่ยวกับภูมิคุ้มกันต่ำ หรือมีมารดาที่ใช้ยา diethylstilbestrol ขณะตั้งครรภ์ ต้องทำการตรวจแปปสเมียร์ทุกปี** ''')
        st.image('271748222_5093640660668828_4892199078576618570_n.jpg',
          caption = 'อ้างอิง: https://www.facebook.com/CGHphaholyothin/photos/a.565950873437852/5093640667335494/?type=3')   
st.write("---------------------------------------------------")
