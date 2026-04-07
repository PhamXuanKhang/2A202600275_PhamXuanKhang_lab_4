# TravelBuddy Agent 🧳

TravelBuddy là một trợ lý du lịch thông minh được xây dựng bằng kiến trúc **LangGraph** kết hợp với LLM OpenAI. Agent có thể hỗ trợ người dùng tìm kiếm chuyến bay, tìm khách sạn và tính toán ngân sách tự động thông qua framework Tool Calling.

## Tính năng nổi bật
- ✈️ **Tìm kiếm chuyến bay**: Hỗ trợ tra cứu giá vé, hãng bay, giờ khởi hành giữa các thành phố theo tuyến cố định.
- 🏨 **Tìm kiếm khách sạn**: Lọc và đề xuất khách sạn dựa trên rating và hạn mức ngân sách khách hàng.
- 💰 **Quản lý ngân sách (Calculate Budget)**: Tính toán tự động và kiểm soát chi phí thực tế, chặn số liệu âm để chống lại thao túng công cụ.
- 🛡️ **Bảo mật & Guardrails**: Chống Prompt Injection, từ chối xử lý các yêu cầu ngoài luồng (như viết code, tư vấn tài chính), có cơ sở reasoning thông minh khi rơi vào các tình huống mâu thuẫn intent.

## Cấu trúc project
- `agent.py`: File chính khởi tạo Agent, lập biểu đồ phân tuyến đồ thị luồng đàm thoại (StateGraph), và định nghĩa loop hội thoại.
- `tools.py`: Chứa các công cụ (như search_flights, search_hotels, calculate_budget) và các function phục vụ mapping, parser.
- `system_prompt.txt`: Chứa persona, rule behavior và định dạng response được ép chặt vào Agent ở node "call_agent", đảm bảo output ổn định.
- `test_results.md` & `test.md`: Nhật ký báo thử nghiệm với hơn 15 Advanced Cases kiểm tra bảo mật, robustness.

## Cài đặt & Sử dụng
1. Cài đặt các thư viện yêu cầu:
   ```bash
   pip install -r requirements.txt
   ```
2. Thiết lập OpenAI API Key trong file `.env` gốc của dự án:
   ```env
   OPENAI_API_KEY=sk-*************
   ```
3. Chạy trợ lý ảo dạng Console:
   ```bash
   python agent.py
   ```