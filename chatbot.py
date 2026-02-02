def ai_chatbot(question, indicators):
    rsi = indicators.get("rsi", None)
    trend = indicators.get("trend", "Neutral")

    response = f"""
### 🤖 AI Trading Assistant (Educational)

**Your Question:** {question}

**Current Market Summary:**
- Trend: {trend}
- RSI: {rsi}

**Explanation:**
- RSI above 70 → Overbought
- RSI below 30 → Oversold
- Moving averages help identify trend direction
- Use multiple indicators together

⚠️ *This is NOT financial advice. Always do your own research.*
    """
    return response
