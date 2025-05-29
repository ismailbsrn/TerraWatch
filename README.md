
# TerraWatch 🌱

**TerraWatch** is a real-time soil moisture monitoring system built for smart agriculture. It simulates sensor data, transmits it over MQTT, bridges it to HTTP, and visualizes the data via a simple web interface using cloud infrastructure.

🎥 **Demo Video:** [Watch on YouTube](https://youtu.be/EwifHPq33WA?si=AFu8vBvWQqzRdqJq)

## Features

- 🌍 Real-time soil moisture data simulation  
- 📡 MQTT-to-HTTP data bridge  
- ☁️ Azure Event Hub integration  
- 🧠 MongoDB for data persistence (containerized)  
- 📊 Web frontend for data visualization  
- 🔐 Scalable cloud-native architecture

## Tech Stack

- **Backend:** Python (FastAPI), MQTT, Azure Event Hub  
- **Database:** MongoDB (running in container instance)  
- **Frontend:** HTML, JavaScript (basic)  
- **Cloud:** Microsoft Azure (VM, Container Instance, Event Hub)

## Project Architecture

1. **Simulator** generates soil moisture data.
2. **MQTT Bridge** forwards data to an HTTP endpoint.
3. Azure **VM** listens to Event Hub and writes data to **MongoDB**.
4. Frontend fetches and displays real-time data.

## Getting Started

1. Clone the repository.
2. Set up your `.env` for MQTT broker, Event Hub, and DB connection.
3. Launch simulator and bridge.
4. Deploy backend API on Azure VM.
5. Serve frontend via simple HTTP server or Azure Static Web Apps.

## Demo

[![Watch the video](https://img.youtube.com/vi/EwifHPq33WA/0.jpg)](https://youtu.be/EwifHPq33WA?si=AFu8vBvWQqzRdqJq)

---

## License

This project is licensed under the MIT License.
