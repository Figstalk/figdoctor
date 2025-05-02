from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# โมเดลรับข้อมูลจากผู้ใช้
class DiagnosisRequest(BaseModel):
    symptom: str

# หน้าหลัก
@app.get("/")
def read_root():
    return {"message": "ยินดีต้อนรับสู่ระบบหมอฟิกส์!"}

# Endpoint สำหรับวินิจฉัยอาการ
@app.post("/diagnose")
def diagnose(request: DiagnosisRequest):
    symptom = request.symptom.lower()

    # ตัวอย่างการวินิจฉัยง่าย ๆ
    if "จุดดำ" in symptom or "ใบมีจุด" in symptom:
        return {"diagnosis": "อาจเกิดจากเชื้อรา แนะนำให้ตัดใบที่เป็นและลดความชื้น"}
    elif "ใบเหลือง" in symptom:
        return {"diagnosis": "อาจขาดไนโตรเจนหรือรากมีปัญหา ลองตรวจดินหรือเสริมปุ๋ยอินทรีย์"}
    else:
        return {"diagnosis": "ไม่สามารถวินิจฉัยได้แน่ชัด โปรดแนบรูปภาพหรือปรึกษาผู้เชี่ยวชาญ"}