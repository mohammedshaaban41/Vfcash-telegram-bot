import re

def parse_vfcash(message):

    result = {}

    # نوع العملية
    if "تم تحويل" in message:
        result["type"] = "📤 تحويل صادر"
        result["icon"] = "🔴"

        m = re.search(r"تم تحويل\s+([\d.,]+)\s+جنيه", message)
        if m:
            result["amount"] = m.group(1)

        m = re.search(r"لرقم\s+(\d+)", message)
        if m:
            result["phone"] = m.group(1)

    elif "تم استلام" in message:
        result["type"] = "📥 تحويل وارد"
        result["icon"] = "🟢"

        m = re.search(r"تم استلام\s+([\d.,]+)\s+جنيه", message)
        if m:
            result["amount"] = m.group(1)

        m = re.search(r"من\s+(\d+)", message)
        if m:
            result["phone"] = m.group(1)

    # الرصيد
    m = re.search(r"الحالي\s+([\d.,]+)", message)
    if m:
        result["balance"] = m.group(1)

    # التاريخ والوقت
    m = re.search(r"تاريخ العملية\s+(\d+:\d+)\s+(\d{2}-\d{2}-\d{2})", message)
    if m:
        result["time"] = m.group(1)
        result["date"] = m.group(2)

    # رقم العملية
    m = re.search(r"رقم العملية\s+(\d+)", message)
    if m:
        result["operation"] = m.group(1)

    return result
