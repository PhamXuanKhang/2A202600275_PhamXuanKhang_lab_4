from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

from tools import search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# 1. Đọc System Prompt
# ============================================================
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# ============================================================
# 2. Khai báo State
# ============================================================
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# ============================================================
# 3. Khởi tạo LLM và Tools
# ============================================================
tools_list = [search_flights, search_hotels, calculate_budget]
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm_with_tools = llm.bind_tools(tools_list)

# ============================================================
# 4. Agent Node
# ============================================================
def agent_node(state: AgentState):
    messages = state["messages"]

    # Đảm bảo system prompt luôn ở đầu conversation
    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + list(messages)

    response = llm_with_tools.invoke(messages)

    # === LOGGING ===
    if response.tool_calls:
        print(f"\n  🔧 Agent quyết định gọi {len(response.tool_calls)} tool(s):")
        for tc in response.tool_calls:
            args_str = ", ".join(f"{k}={repr(v)}" for k, v in tc["args"].items())
            print(f"     → {tc['name']}({args_str})")
    else:
        print("\n  💬 Agent trả lời trực tiếp (không gọi tool)")

    return {"messages": [response]}

# ============================================================
# 5. Xây dựng Graph
# ============================================================
builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools_list))

# Edges: START → agent → (tool_calls?) → tools → agent → ... → END
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile()

# ============================================================
# 6. Chat Loop
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("  TravelBuddy — Trợ lý Du lịch Thông minh 🧳")
    print("  Gõ 'quit' / 'exit' / 'q' để thoát")
    print("=" * 60)

    while True:
        try:
            user_input = input("\nBạn: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nTạm biệt!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "q"):
            print("TravelBuddy: Tạm biệt! Chúc bạn có chuyến đi vui vẻ! ✈️")
            break


        print("\nTravelBuddy đang suy nghĩ...", end="", flush=True)

        result = graph.invoke({"messages": [("human", user_input)]})

        
        final_message = result["messages"][-1]
        print(f"\r\nTravelBuddy: {final_message.content}")
        print("-" * 60)
