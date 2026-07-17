# 🌍 AI Trip Planner

An agentic AI travel planning assistant that generates personalized trip itineraries using **LangGraph**, **Groq LLMs**, and real-time tools for weather, currency conversion, place search, and cost calculations.

**Live Demo:** [aitripplanner-18360.streamlit.app](https://aitripplanner-18360.streamlit.app/)

---

## ✨ Features

- **Conversational trip planning** — just tell it where you want to go and for how long
- **Agentic tool use** powered by LangGraph, including:
  - 🌦️ **Weather Tool** — current and forecasted weather for the destination
  - 💱 **Currency Conversion Tool** — real-time currency conversion for budgeting
  - 📍 **Place Search Tool** — points of interest, attractions, and recommendations
  - 🧮 **Calculator Tool** — trip cost breakdowns and estimates
- **LLM-powered reasoning** via Groq for fast inference
- **Simple Streamlit UI** — no separate backend required, runs as a single deployable app

---

## 🏗️ Architecture

```
User Input (Streamlit UI)
        │
        ▼
   GraphBuilder (LangGraph StateGraph)
        │
        ├── Agent Node  → Groq LLM (bound with tools)
        │
        └── Tools Node  → Weather | Currency | Places | Calculator
        │
        ▼
   Final AI-generated Travel Plan
```

The app was originally built with a FastAPI backend + Streamlit frontend split, but has been consolidated into a single Streamlit app (`app.py`) that invokes the LangGraph agent directly — no separate backend server needed for deployment.

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Agent Orchestration | LangGraph |
| LLM Provider | Groq |
| Tooling | LangChain custom tools |
| Language | Python 3.13 |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.13+
- API keys for: Groq, and any tool-specific services (weather, maps/places, etc.)

### Installation

```bash
git clone https://github.com/Keerthivardhan1507/AI_TRIP_PLANNER.git
cd AI_TRIP_PLANNER
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_maps_api_key
OPENWEATHER_API_KEY=your_weather_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### Run locally

```bash
streamlit run app.py
```

---

## ☁️ Deployment

This app is deployed on **Streamlit Community Cloud**. API keys are configured via the app's **Secrets** manager (Settings → Secrets) rather than a committed `.env` file.

---

## 📌 Usage

1. Open the app
2. Enter a prompt like:
   > *"Plan a trip to Goa for 5 days"*
3. The agent will generate a day-by-day itinerary including places to visit, estimated costs, and weather considerations

---

## 🔮 Future Improvements

- [ ] **Improve cost/price accuracy** — current price estimates from the LLM/tools can run higher than real-world costs; plan to integrate more reliable pricing APIs (flights, hotels, local transport) for realistic budgeting
- [ ] Add multi-city / multi-leg trip support
- [ ] Add user preference memory (budget tier, travel style, dietary needs)
- [ ] Export itinerary as PDF/downloadable document
- [ ] Add map visualization of the generated itinerary
- [ ] Support for multiple LLM providers (OpenAI, Anthropic, etc.)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a PR or raise an issue.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Keerthivardhan**
[GitHub](https://github.com/Keerthivardhan1507)

---

*This travel plan generator uses AI and should be used as a starting point for trip planning — please verify prices, operating hours, and travel requirements independently before your trip.*