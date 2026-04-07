# Test Results — Lab 4: TravelBuddy Agent
**MSSV:** ___________
**Ngày chạy:** ___________

---

## Test 1 — Direct Answer (Không cần tool)

**Input:**
```
Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.
```

**Kỳ vọng:** Agent chào hỏi, hỏi thêm về sở thích/ngân sách/thời gian. Không gọi tool nào.

**Console log:**
```
Chào bạn! Thật tuyệt khi bạn muốn đi du lịch. Để mình có thể giúp bạn tốt hơn, bạn có thể cho mình biết thành phố xuất phát của bạn, điểm đến mà bạn đang nghĩ đến (nếu có), số đêm bạn dự định ở lại và ngân sách của bạn là bao nhiêu không?
```

**Tool calls observed:** 💬 Agent trả lời trực tiếp (không gọi tool)

**Pass / Fail:** ___

---

## Test 2 — Single Tool Call

**Input:**
```
Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng
```

**Kỳ vọng:** Gọi `search_flights("Hà Nội", "Đà Nẵng")`, liệt kê 4 chuyến bay.

**Console log:**
```
Bạn có thể cho mình biết thêm thông tin về chuyến đi không? Cụ thể là bạn dự định đi vào ngày nào, ở lại bao nhiêu đêm và ngân sách cho chuyến bay là bao nhiêu?
```

**Tool calls observed:** 💬 Agent trả lời trực tiếp (không gọi tool)

**Pass / Fail:** ___

---

## Test 3 — Multi-Step Tool Chaining

**Input:**
```
Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!
```

**Kỳ vọng:** Agent tự chuỗi ít nhất 3 tool calls:
1. `search_flights("Hà Nội", "Phú Quốc")`
2. `search_hotels("Phú Quốc", max_price=...)`
3. `calculate_budget(5000000, "...")`

Rồi tổng hợp thành gợi ý hoàn chỉnh với bảng chi phí.

**Console log:**
```
Dưới đây là gợi ý cho chuyến đi của bạn từ Hà Nội đến Phú Quốc trong 2 đêm:

✈️ **Chuyến bay Hà Nội → Phú Quốc:**
1. **VietJet Air** | 10:00 → 12:15 | **1.350.000đ** | economy
2. **VietJet Air** | 16:00 → 18:15 | **1.100.000đ** | economy

🏨 **Khách sạn tại Phú Quốc:**
1. **9Station Hostel** | **200.000đ/đêm** | Dương Đông | Rating: 4.5      
2. **Sol by Meliá** | **1.500.000đ/đêm** | Bãi Trường | Rating: 4.2       
3. **Lahana Resort** | **800.000đ/đêm** | Dương Đông | Rating: 4.0        

💰 **Tổng chi phí ước tính:**
- Vé máy bay: **1.350.000đ**
- Khách sạn (2 đêm tại 9Station Hostel): **400.000đ**
- **Tổng chi: 2.950.000đ**
- **Ngân sách còn lại: 2.050.000đ** ✅

💡 **Gợi ý thêm:**
- Đừng quên thưởng thức hải sản tươi ngon tại Phú Quốc, đặc biệt là ghẹ và nhum biển.
- Nếu có thời gian, hãy ghé thăm Vinpearl Land hoặc tham gia tour khám phá các hòn đảo xung quanh.

Chúc bạn có một chuyến đi vui vẻ! Nếu cần thêm thông tin gì, cứ hỏi mình nhé!
```

**Tool calls observed:** 🔧 Agent quyết định gọi 2 tool(s):
     → search_flights(origin='Hà Nội', destination='Phú Quốc')
     → search_hotels(city='Phú Quốc', max_price_per_night=2500000)        

  🔧 Agent quyết định gọi 1 tool(s):
     → calculate_budget(total_budget=5000000, expenses='vé_máy_bay:1350000,khách_sạn:1600000')

**Pass / Fail:** ___

---

## Test 4 — Missing Info / Clarification

**Input:**
```
Tôi muốn đặt khách sạn
```

**Kỳ vọng:** Agent hỏi lại thành phố, số đêm, ngân sách. Không gọi tool vội.

**Console log:**
```
Mình rất vui được giúp bạn! Bạn có thể cho mình biết thành phố bạn muốn đặt khách sạn, ngân sách tối đa mỗi đêm và số đêm bạn dự định ở lại không?
```

**Tool calls observed:** 💬 Agent trả lời trực tiếp (không gọi tool)

**Pass / Fail:** ___

---

## Test 5 — Guardrail / Refusal

**Input:**
```
Giải giúp tôi bài tập lập trình Python về linked list
```

**Kỳ vọng:** Từ chối lịch sự, nói rằng chỉ hỗ trợ về du lịch.

**Console log:**
```
Xin lỗi, nhưng mình không thể giúp bạn với bài tập lập trình. Nếu bạn cần tư vấn về du lịch, đặt vé máy bay hay khách sạn, mình rất sẵn lòng hỗ trợ! Bạn có kế hoạch đi đâu không? Hãy cho mình biết thành phố xuất phát, điểm đến, số đêm và ngân sách của bạn nhé!
```

**Tool calls observed:** 💬 Agent trả lời trực tiếp (không gọi tool)

**Pass / Fail:** ___

---

## Tổng kết

| Test | Tên | Pass/Fail | Ghi chú lỗi (nếu có) |
|------|-----|-----------|----------------------|
| 1    | Direct Answer        |           |                      |
| 2    | Single Tool Call     |           |                      |
| 3    | Multi-Step Chaining  |           |                      |
| 4    | Clarification        |           |                      |
| 5    | Guardrail Refusal    |           |                      |

## Ghi chú lỗi phân loại

### Lỗi thuộc loại Prompt:
- ___

### Lỗi thuộc loại Tool Schema:
- ___

### Lỗi thuộc loại Control Flow:
- ___
