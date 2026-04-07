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
Chào bạn! Có rất nhiều điểm đến thú vị ở Việt Nam. Bạn có thể cho mình biết bạn thích khám phá thiên nhiên, văn hóa hay ẩm thực không? Hoặc bạn có một ngân sách cụ thể nào cho chuyến đi này không?
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
✈️ Chuyến bay từ Hà Nội đi Đà Nẵng:

1. **Vietnam Airlines** | 06:00→07:20 | **1.450.000đ** | economy
2. **Vietnam Airlines** | 14:00→15:20 | **2.800.000đ** | business
3. **VietJet Air** | 08:30→09:50 | **890.000đ** | economy 
4. **Bamboo Airways** | 11:00→12:20 | **1.200.000đ** | economy

Bạn có muốn tìm khách sạn ở Đà Nẵng không? Nếu có, hãy cho tôi biết ngân sách tối đa mỗi đêm của bạn nhé!
```

**Tool calls observed:** 🔧 Agent quyết định gọi 1 tool(s):
     → search_flights(origin='Hà Nội', destination='Đà Nẵng')

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

✈️ **Chuyến bay**:
- **VietJet Air** | 16:00 → 18:15 | **1.100.000đ** | economy

🏨 **Khách sạn**:
1. **9Station Hostel** | **200.000đ/đêm** | Dương Đông | Rating: 4.5
2. **Lahana Resort** | **800.000đ/đêm** | Dương Đông | Rating: 4.0

💰 **Tổng chi phí ước tính**:
- **Chuyến bay**: 1.100.000đ
- **Khách sạn (2 đêm)**: 1.600.000đ
- **Tổng chi**: 2.700.000đ
- **Ngân sách còn lại**: 2.300.000đ ✅

💡 **Gợi ý thêm**: Bạn có thể sử dụng ngân sách còn lại để tham gia các hoạt động vui chơi, ăn uống hoặc mua sắm tại Phú Quốc. Đừng quên ghé thăm các bãi biển đẹp và thưởng thức hải sản tươi ngon nhé!
```

**Tool calls observed:** 🔧 Agent quyết định gọi 1 tool(s):
     → search_flights(origin='Hà Nội', destination='Phú Quốc')

  🔧 Agent quyết định gọi 1 tool(s):
     → search_hotels(city='Phú Quốc', max_price_per_night=2000000)

  🔧 Agent quyết định gọi 1 tool(s):
     → calculate_budget(total_budget=5000000, expenses='flight:1100000,hotel_total:1600000')

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
Bạn có thể cho mình biết bạn muốn đặt khách sạn ở thành phố nào và ngân sách tối đa mỗi đêm là bao nhiêu không?
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
Xin lỗi, nhưng mình không thể giúp bạn với bài tập lập trình. Nếu bạn cần thông tin về du lịch, đặt vé máy bay hay khách sạn, mình rất sẵn lòng hỗ trợ!
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
