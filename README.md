# Echo-Guardian: Autonomous First-Responder AI System

## Overview
Echo-Guardian is a high-performance, AI-powered visual and audio first-responder system designed to secure disaster zones autonomously. Engineered for critical situations such as structural fires, collapses, or hazardous material spills, the system acts as an immediate set of eyes and ears on the ground.

By processing raw drone footage or security camera feeds through a custom computer vision pipeline, Echo-Guardian detects threats, trapped personnel, and vehicles in real-time. Upon positive detection, the backend dynamically generates a situational text script and utilizes advanced text-to-speech engines to broadcast localized, authoritative evacuation warnings.

**Author:** Puttala Jeevan Kumar

---

## Table of Contents
1. [System Architecture](#system-architecture)
2. [Core Features](#core-features)
3. [Technology Stack](#technology-stack)
4. [Installation & Setup](#installation--setup)
5. [Environment Variables](#environment-variables)
6. [API Documentation](#api-documentation)
7. [Technical Documentation (Modules)](#technical-documentation-modules)
8. [Future Roadmap](#future-roadmap)

---

## System Architecture
Echo-Guardian operates on a decoupled client-server architecture. 
* **Backend:** A Python FastAPI server handles asynchronous media uploads, manages the YOLOv8 neural network inference, and routes audio generation requests. It encodes all output media (annotated images and audio buffers) into Base64 strings.
* **Frontend:** A lightweight, vanilla JavaScript dashboard that decodes the Base64 payloads, renders the visual bounding boxes, and plays the audio warnings natively in the browser.

---

## Core Features
* **Real-Time Visual Threat Detection:** Utilizes Ultralytics YOLOv8 to scan image bytes and video frames for dynamic objects (people, vehicles, hazards).
* **Dynamic Audio Generation:** Integrates the ElevenLabs API to generate realistic, context-aware emergency broadcast audio based on the specific objects detected in the frame.
* **Unbreakable API Shield:** Features a resilient fallback architecture. If external APIs (like ElevenLabs) experience downtime or rate limits, the system automatically intercepts the failure and falls back to the browser's native SpeechSynthesis API to guarantee audio delivery.
* **CORS & Base64 Pipeline:** Fully configured CORS middleware allows seamless cross-origin requests, while Base64 encoding bypasses the need for temporary static file storage on the server.

---

## Technology Stack
* **Backend Framework:** Python 3.10+, FastAPI, Uvicorn
* **Computer Vision:** Ultralytics (YOLOv8), OpenCV, PyTorch (CUDA 12.1 enabled)
* **Audio Generation:** ElevenLabs API
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (ES6)
* **Environment:** Windows Subsystem for Linux (WSL) - Ubuntu

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/Jeevang1-epic/Echo-Guardian.git](https://github.com/Jeevang1-epic/Echo-Guardian.git)
cd Echo-Guardian
